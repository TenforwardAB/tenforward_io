from bs4 import BeautifulSoup
from collections import OrderedDict
from django import forms
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from crum import get_current_request
from wagtail.core import blocks
from wagtail.core.blocks import BaseStreamBlock
from wagtail.core.models import Site
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from django.utils.functional import cached_property
from .templatetags.streams_tags import custom_bleach

try:
    # Imports the register_feature decorator from the 'features' module.
    from features.registry import register_feature, registry
except ImportError:
    # If features isn't installed, @register_feature becomes a noop, and the registry is empty.
    # noinspection PyUnusedLocal
    def register_feature(**kwargs):
        return lambda klass: klass
    registry = {'default': set(), 'special': set()}

from .utils import BACKGROUND_COLORS, FOREGROUND_COLORS, get_block_tuple, BlockTupleMixin

SVG_ICONS = [
        'alarm', 'calendar', 'chat', 'chat_multi', 'clock', 'cloud-computing', 'cup', 'devices', 'dial',
        'finger_tap', 'fingerprint', 'flag', 'google-play', 'library', 'link', 'music', 'payment-method',
        'pictures', 'rocket', 'settings', 'shirt', 'smartphones'
    ]

BTN_COLOR = [
    'primary', 'secondary', 'green', 'green-light', 'black', 'orange', 'orange-light', 'red', 'grey',
    'grey-light', 'yellow', 'lime'
]

# =======
# Globals
# =======
wh_height_helptext = (
    'If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column "'
    'layout), set the image to be this many pixels tall.'
)

wh_width_helptext = (
    'If "Fixed Dimensions" is checked, or if this block is placed outside a layout element (e.g. outside a N-Column '
    'layout), set the image to be this many pixels wide.'
)


class FeatureCustomizedStreamBlock(blocks.StreamBlock):
    """
    Identical to StreamBlock, except that we override the constructor to make it save self._base_blocks and
    self._dependencies, instead of self.base_blocks and self.dependencies. This lets us replace them with @properties.
    """

    def __init__(self, local_blocks=None, **kwargs):
        self._constructor_kwargs = kwargs

        # Note, this is calling BaseStreamBlock's super __init__, not FeatureCustomizedStreamBlock's. We don't want
        # BaseStreamBlock.__init__() to run, because it tries to assign to self.child_blocks, which it can't do because
        # we've overriden it with an @property. But we DO want Block.__init__() to run.
        super(BaseStreamBlock, self).__init__(**kwargs)

        # create a local (shallow) copy of base_blocks so that it can be supplemented by local_blocks
        self._child_blocks = self.base_blocks.copy()
        if local_blocks:
            for name, block in local_blocks:
                block.set_name(name)
                self._child_blocks[name] = block

        self._dependencies = self._child_blocks.values()

    @property
    def child_blocks(self):
        request = get_current_request()
        # Protect against crashing in case this ever runs outside of a request cycle.
        if request is None:
            return self._child_blocks

        # Protect against crashing of the site has no features (like the initial site built by Wagtail migration)
        # noinspection PyUnresolvedReferences
        try:
            features = request.site.features
            return OrderedDict([
                item for item in self._child_blocks.items() if features.feature_is_enabled(item[0])
            ])
        except Exception as e:  # Site.features.RelatedObjectDoesNotExist:
            return self._child_blocks

    @property
    def dependencies(self):
        request = get_current_request()
        print(dir(request))
        # Protect against crashing in case this ever runs outside of a request cycle.
        if request is None:
            return self._child_blocks

        # Protect against crashing of the site has no features (like the initial site built by Wagtail migration)
        # noinspection PyUnresolvedReferences
        try:
            features = request.site.features
            return [block for block in self._dependencies if features.feature_is_enabled(block.name)]
        except Exception as e:  # Site.features.RelatedObjectDoesNotExist:
            print(e)
            return self._child_blocks


class TagFilterImageChooserBlock(ImageChooserBlock):
    def __init__(self, tag, **kwargs):
        self.tag = tag
        super(ImageChooserBlock, self).__init__(**kwargs)

    @cached_property
    def field(self):
        # Filter the choice field to include only images with
        # the tag >>>tag<<<

        return forms.ModelChoiceField(
            queryset=self.target_model.objects.filter(tags__name=self.tag),
            widget=self.widget,
            required=self._required,
            validators=self._validators,
            help_text=self._help_text
        )


# ====================
# Component Sub-blocks
# ====================
class IntegerChoiceBlock(blocks.ChoiceBlock):
    """
    A ChoiceBlock for intergers only. Using this instead of ChoiceBlock ensures that the value retrieved from the
    field is an integer instead of a string.
    """

    def to_python(self, value):
        return int(value)

    def get_prep_value(self, value):
        return int(value)

    def value_from_form(self, value):
        return int(value)


class LinkBlock(blocks.StructBlock):
    """
    Allows a user to optionally link the containing block to a Page, a Document, or a relative or absolute URL.

    NOTE: Due to limitations in CSS, callers of LinkBlock() must not specify a label in the construction arguments.
    See the comment in the Meta class for why.

    NOTE: Within a template, checking for the existence of `self.link` will always return True because the LinkBlock
    object is not falsey, even if it has no contents. To retrieve the value of a LinkBlock, use the {% link_url %}
    template tag from jetstream_tags. ex:
        {% load jetstream_tags %}
        {% link_url self.link as url %}
        {% if url %}
            <a href={{ url }}></a>
        {% endif %}
    """
    page = blocks.PageChooserBlock(
        required=False,
        help_text="Link to the chosen page. If a Page is selected, it will take precedence over both."
    )
    document = DocumentChooserBlock(
        required=False,
        help_text="Link to the chosen document. If a document is selected, it will take precedence over a URL."
    )
    url = blocks.CharBlock(
        required=False,
        help_text="Link to the given URL. This can be a relative URL to a location your own site (e.g. /example-page) "
                  "or an absolute URL to a page on another site (e.g. http://www.caltech.edu). Note: absolute URLs "
                  "must include the http:// otherwise they will not work."
    )

    class Meta:
        label = 'Link'
        form_classname = 'link-block'


class DimensionsOptionsBlock(blocks.StructBlock):
    """
    Allows the user to specify arbitrary dimensions for a block that has certain interactions with
    the various column layouts.
    """
    use = blocks.BooleanBlock(
        default=False,
        required=False,
        label='Use Fixed Dimensions',
        help_text="Normally, the image will expand its height to satisfy the suggested height on its parent block. "
                  "Checking this box will make it conform to the specified height and width, instead."
    )
    height = blocks.IntegerBlock(
        default=200,
        label="Height (pixels)",
        help_text=wh_height_helptext
    )
    width = blocks.IntegerBlock(
        default=200,
        label="Width (pixels)",
        help_text=wh_width_helptext
    )

    @property
    def media(self):
        return forms.Media(
            js=['streams/js/admin/dimensions-options.js']
        )

    def js_initializer(self):
        return "fixed_dimensions"

    class Meta:
        form_classname = 'dimensions-options struct-block'
        # Don't display a label for this block. Our override of wagtailadmin/block_forms/struct.html obeys this flag.
        no_label = True


class BackgroundOptionsBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(
        required=False,
        help_text="This image, if supplied, will appear as a background for this block"
    )
    background_color = blocks.ChoiceBlock(
        choices=BACKGROUND_COLORS,
        blank=False,
        required=False,
        default=BACKGROUND_COLORS[0],
        help_text="Set the background color of this block.  If a Background Image is also supplied, the Background "
                  "Image will be displayed instead of this color"
    )

    class Meta:
        form_classname = 'color-options struct-block'
        # Don't display a label for this block. Our override of wagtailadmin/block_forms/struct.html obeys this flag.
        no_label = True


class ActionButtonBlock(blocks.StructBlock):
    STYLES = (
        ('btn-primary', 'Primary'),
        ('btn-light', 'Default'),
        ('btn-link', 'Info'),
    )

    text = blocks.TextBlock()
    link = LinkBlock()
    style = blocks.ChoiceBlock(
        choices=[(style[0], style[1]) for style in STYLES],
        default=STYLES[0][0]
    )

    class Meta:
        label = 'Action Button'
        template = 'streams/blocks/action_button_block.html'
        form_classname = 'action-button-block struct-block'
        icon = 'form'


class ActionButtonBarBlock(blocks.StructBlock):
    CHOICES = (
        ('center-block', 'Center'),
        ('left-align-block', 'Align Left'),
        ('right-align-block', 'Align Right')
    )

    alignment = blocks.ChoiceBlock(
        choices=[(choice[0], choice[1]) for choice in CHOICES],
        default=CHOICES[0][0],
    )
    actions = blocks.ListBlock(
        ActionButtonBlock(),
        default=[]
    )

    class Meta:
        label = 'Action Button Bar'
        template = 'streams/blocks/action_button_bar_block.html'
        form_classname = 'action-button-bar struct-block'
        icon = 'form'


class ColorOptionsBlock(blocks.StructBlock):
    background_image = ImageChooserBlock(
        required=False,
        help_text="This image, if supplied, will appear as a background for this block"
    )
    background_color = blocks.ChoiceBlock(
        choices=BACKGROUND_COLORS,
        blank=False,
        required=False,
        default=BACKGROUND_COLORS[0],
        help_text="Set the background color of this block.  If a Background Image is also supplied, the Background "
                  "Image will be displayed instead of this color"
    )
    text_color = blocks.ChoiceBlock(
        choices=FOREGROUND_COLORS,
        blank=False,
        required=False,
        default=FOREGROUND_COLORS[0],
        help_text="Set the color for the text in this block. This is here so you can make your text visible on both "
                  "light and dark backgrounds."
    )

    class Meta:
        form_classname = 'color-options struct-block'
        # Don't display a label for this block. Our override of wagtailadmin/block_forms/struct.html obeys this flag.
        no_label = True


class RelatedLinksNodeBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)
    link = LinkBlock()

    class Meta:
        template = 'streams/blocks/related_link.html'


# ======================================================================================================
# ====================================== MEDIA BLOCKS ==================================================
# ======================================================================================================
@register_feature(feature_type='default')
class ImagePanelBlock(blocks.StructBlock, BlockTupleMixin):
    STYLES = (
        ('link', 'Image Link', 'streams/blocks/image_panel_block-link.html', []),
        ('captioned', 'Image w/ Caption', 'streams/blocks/image_panel_block-caption.html', []),
        ('rollover', 'Image Link w/ Rollover Text', 'streams/blocks/image_panel_block-rollover.html', []),
        ('separate_text', 'Image Card (Equal Heights)', 'streams/blocks/image_panel_block-card.html', ['equal']),
        ('separate_text_natural', 'Image Card (Natural Heights)', 'streams/blocks/image_panel_block-card.html', ['natural']),  # noqa
        ('image_listing_left', 'Listing (Image Left)', 'streams/blocks/image_panel_block-listing.html', ['left']),
        ('image_listing_right', 'Listing (Image Right)', 'streams/blocks/image_panel_block-listing.html', ['right']),
    )

    image = ImageChooserBlock()
    style = blocks.ChoiceBlock(choices=[(style[0], style[1]) for style in STYLES], default='link')
    title = blocks.CharBlock(required=False)
    desc = blocks.CharBlock(
        required=False,
        label='Body'
    )
    display_caption = blocks.BooleanBlock(
        label='Display Caption',
        help_text='Check this box to display the caption and photo credit below this image.',
        required=False,
        default=False
    )
    link = LinkBlock()
    fixed_dimensions = DimensionsOptionsBlock()

    class Meta:
        label = 'Image Panel'
        form_classname = 'image-panel struct-block'
        icon = 'image'

    def render(self, value, context=None):
        """
        We override this method to allow a template to be chosen dynamically based on the value of the "style" field.
        """
        style_to_template_map = {style[0]: (style[2], style[3]) for style in self.STYLES}
        try:
            (template, extra_classes) = style_to_template_map[value['style']]
        except KeyError:
            # If this block somehow doesn't have a known style, fall back to the basic_render() method.
            return self.render_basic(value, context=context)

        new_context = self.get_context(value, parent_context=context if context is None else dict(context))
        new_context['extra_classes'] = " ".join(extra_classes)
        return mark_safe(render_to_string(template, new_context))

    @property
    def media(self):
        return forms.Media(
            js=['streams/js/admin/image-panel.js']
        )

    def js_initializer(self):
        return 'image_panel'


@register_feature(feature_type='default')
class HeroImageBlock(blocks.StructBlock, BlockTupleMixin):

    style = blocks.ChoiceBlock(
        choices=[
            ('regular-width', 'Regular Width'),
            ('full-width', 'Full Width')
        ],
        default='regular-width',
        label='Overall style',
        help_text=('Regular Width fills the normal page area. '
                   'Full Width fills the entire width of the browser. Shorter images will be tiled.')
    )
    text_style = blocks.ChoiceBlock(
        choices=[
            ('bare-serif', 'Bare text w/ serif font'),
            ('bare-sans-serif', 'Bare text w/ sans-serif font'),
            ('white-translucent-serif', 'White translucent background behind serif text'),
            ('white-translucent-sans-serif', 'White translucent background behind sans-serif text'),
        ],
        default='white-translucent-serif',
        label='Text style'
    )
    image = ImageChooserBlock()
    title = blocks.CharBlock(required=False)
    desc = blocks.RichTextBlock(
        required=False,
        label='Text'
    )
    height = blocks.IntegerBlock(
        default=500,
        label='Height (pixels)'
    )
    position = blocks.ChoiceBlock(
        choices=[
            ('position-top-left', 'Top Left'),
            ('position-top-middle', 'Top Middle'),
            ('position-top-right', 'Top Right'),
            ('position-left', 'Left'),
            ('position-middle', 'Middle'),
            ('position-right', 'Right'),
            ('position-bottom-left', 'Bottom Left'),
            ('position-bottom-middle', 'Bottom Middle'),
            ('position-bottom-right', 'Bottom Right'),
        ],
        default='position-middle',
        label='Text Position'
    )
    actions = ActionButtonBarBlock(
        label='Action Buttons',
        required=False
    )

    class Meta:
        label = 'Hero Image'
        template = 'streams/blocks/hero_image_block.html'
        form_classname = 'hero-image struct-block'
        icon = 'image'


@register_feature(feature_type='default')
class HeroImageCarouselBlock(blocks.StructBlock, BlockTupleMixin):

    slides = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('title', blocks.CharBlock(required=False)),
            ('text', blocks.TextBlock(required=False)),
            ('link', LinkBlock()),
        ])
    )
    height = blocks.IntegerBlock(
        default=300,
        label="Hero Image Height (pixels)",
    )
    width = blocks.IntegerBlock(
        default=1000,
        label="Hero Image Width (pixels)",
    )
    cycle_timeout = blocks.IntegerBlock(
        default=10000,
        help_text="The time between automatic image cycles (in milliseonds). Set to 0 to disable automatic cycling."
    )

    class Meta:
        template = 'streams/blocks/hero_image_carousel_block.html'
        form_classname = 'image-carousel struct-block'
        label = 'Hero Image Slider'
        icon = 'image'


@register_feature(feature_type='default')
class ImageCarouselBlock(blocks.StructBlock, BlockTupleMixin):

    header = blocks.TextBlock(required=False)
    slides = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock()),
            ('text', blocks.CharBlock(required=False)),
            ('link', LinkBlock()),
        ])
    )
    cycle_timeout = blocks.IntegerBlock(
        default=5000,
        help_text="The time between automatic image cycles (in milliseonds). Set to 0 to disable automatic cycling."
    )

    class Meta:
        template = 'streams/blocks/image_carousel_block.html'
        label = 'Image Carousel'
        icon = 'image'


@register_feature(feature_type='default')
class ImageGalleryBlock(blocks.StructBlock, BlockTupleMixin):
    """
    Renders an Image Gallery in a variety of styles.
    """
    STYLES = (
        ('gallery', 'Image Gallery', 'streams/blocks/image_gallery_block-gallery.html', []),
        ('slider', 'Image Slider w/ Thumbnail Picker', 'streams/blocks/image_gallery_block-slider.html', []),
    )
    # Only factors of 12 are allowed, because we use a 12-column layout.
    COLUMN_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (6, 6)]

    style = blocks.ChoiceBlock(choices=[(style[0], style[1]) for style in STYLES], default='normal')
    columns = IntegerChoiceBlock(choices=COLUMN_CHOICES, default=3)
    height = blocks.IntegerBlock(
        default=300,
        label='Height (pixels)',
        help_text="Images' widths will be scaled with the number of columns. This field determines their height."
    )
    images = blocks.ListBlock(
        ImageChooserBlock(label='Image')
    )

    class Meta:
        label = 'Image Gallery'
        form_classname = 'image-gallery struct-block'
        icon = 'image'

    def render(self, value, context=None):
        """
        We override this method to allow a template to be chosen dynamically based on the value of the "style" field.
        """
        style_to_template_map = {style[0]: (style[2], style[3]) for style in self.STYLES}
        try:
            (template, extra_classes) = style_to_template_map[value['style']]
        except KeyError:
            # If this block somehow doesn't have a known style, fall back to the basic_render() method.
            return self.render_basic(value, context=context)

        new_context = self.get_context(value, parent_context=context if context is None else dict(context))
        new_context['extra_classes'] = " ".join(extra_classes)
        new_context['bootstrap_column_width'] = int(12 / value['columns'])
        return mark_safe(render_to_string(template, new_context))

    @property
    def media(self):
        # We need to pull in StructBlock's own js code, in addition to ours.
        return super().media + forms.Media(
            js=['streams/js/admin/image-gallery.js']
        )

    def js_initializer(self):
        # Until this gets documented properly, see the following link for an explanation of what's going on here:
        # https://stackoverflow.com/a/47743729/464318
        parent_initialiser = super().js_initializer()
        return "ImageGallery(%s)" % parent_initialiser


@register_feature(feature_type='default')
class SpacerBlock(blocks.StructBlock, BlockTupleMixin):

    height = IntegerChoiceBlock(
        choices=[
            (12, 12),
            (20, 20),
            (25, 25),
            (30, 30),
            (40, 40),
            (50, 50),
            (75, 75),
            (100, 100),
            (125, 125),
            (150, 150),
            (175, 175),
            (200, 200),
            (225, 225),
            (250, 250)
        ],
        blank=False,
        default=25,
        label="Height (pixels)",
        help_text="Add empty vertical space whose height is this many pixels.")

    class Meta:
        label = 'Spacer'
        template = 'streams/blocks/spacer_block.html'
        form_classname = 'spacer struct-block'
        icon = 'arrows-up-down'


@register_feature(feature_type='default')
class RelatedLinksBlock(blocks.StructBlock, BlockTupleMixin):
    title = blocks.CharBlock(
        required=False,
        label='Title',
    )
    links = blocks.ListBlock(
        RelatedLinksNodeBlock(label='Link'),
        label='Links'
    )
    color = ColorOptionsBlock()
    fixed_dimensions = DimensionsOptionsBlock()

    class Meta:
        label = 'Related Links'
        template = 'streams/blocks/related_links_block.html'
        form_classname = 'related-links struct-block'
        icon = 'list-ul'


@register_feature(feature_type='default')
class VideoBlock(blocks.StructBlock, BlockTupleMixin):

    video = EmbedBlock(
        label="Video Embed URL",
        help_text="Paste the video URL from YouTube or Vimeo. e.g. https://www.youtube.com/watch?v=l3Pz_xQZVDg "
                  "or https://vimeo.com/207076450."
    )
    title = blocks.CharBlock(required=False)

    fixed_dimensions = DimensionsOptionsBlock()

    class Meta:
        label = 'Video w/ Title'
        template = 'streams/blocks/video_block.html'
        form_classname = 'video-block struct-block'
        icon = 'media'


@register_feature(feature_type='default')
class SectionTitleBlock(blocks.StructBlock, BlockTupleMixin):
    STYLES = {
        'section_divider': 'streams/blocks/section_title-section_divider.html',
        'block_header': 'streams/blocks/section_title-block_header.html'
    }

    text = blocks.CharBlock(required=True)
    style = blocks.ChoiceBlock(
        choices=[
            ('section_divider', 'Section Divider'),
            ('block_header', 'Block Header'),
        ],
        requried=True,
        blank=False,
        default='section_divider'
    )

    def render(self, value, context=None):
        """
        Uses the appropriate template to render this block, based on the 'style' value.
        """
        try:
            template = self.STYLES[value['style']]
        except KeyError:
            # If this block somehow doesn't have a known style, fall back to the basic_render() method.
            return self.render_basic(value, context=context)

        new_context = self.get_context(value, parent_context=context if context is None else dict(context))
        return mark_safe(render_to_string(template, new_context))

    class Meta:
        form_classname = 'section-title struct-block'
        label = 'Section Title'
        icon = 'form'


@register_feature(feature_type='default')
class MenuListingBlock(blocks.StructBlock, BlockTupleMixin):

    title = blocks.CharBlock(
        required=False,
        help_text="If supplied, display this at the top of the menu listing"
    )
    show = blocks.ChoiceBlock(
        choices=[
            ('siblings', 'Page Siblings'),
            ('children', 'Page Children')
        ],
        blank=False,
        default='siblings',
        help_text='"Page Siblings" lists all pages at the same level of the site page hierarchy as this page; '
                  '"Page Children" lists all pages that are directly below this page in the page hierarchy.'
    )
    color = ColorOptionsBlock()
    fixed_dimensions = DimensionsOptionsBlock()

    class Meta:
        template = 'streams/blocks/menu_listing_block.html'
        form_classname = 'menu-listing struct-block'
        label = 'Menu Section'
        icon = 'list-ul'


@register_feature(feature_type='default')
class FancyRichTextBlock(blocks.StructBlock, BlockTupleMixin):

    text = blocks.RichTextBlock(
        required=True,
        label="Body"
    )
    color = ColorOptionsBlock()
    fixed_dimensions = DimensionsOptionsBlock()

    class Meta:
        template = 'streams/blocks/fancy_rich_text_block.html'
        form_classname = 'fancy-richtext struct-block'
        label = 'Rich Text'
        icon = 'doc-full'


@register_feature(feature_type='default')
class CalloutBlock(blocks.StructBlock, BlockTupleMixin):
    """
    CalloutBlock is for those Divisions-style grid blocks that have a solid background color, a title, and a blurb.
    They should not be able to be placed at the top level; they only belong inside a column layout.
    """

    title = blocks.CharBlock(
        required=True,
        max_length=100
    )
    body = blocks.RichTextBlock(
        required=True
    )
    color = ColorOptionsBlock()
    fixed_dimensions = DimensionsOptionsBlock()

    class Meta:
        template = 'streams/blocks/callout_block.html'
        form_classname = 'callout struct-block'
        label = 'Callout'
        icon = 'doc-full'


class IFrameBlock(blocks.CharBlock, BlockTupleMixin):
    """
    We need a custom field as a place to add a validation. Orignally we just used a CharBlock directly,
    but then you could put anything in here - including script tags.
    """
    class Meta:
        help_text = (
            "Paste the iFrame from your provider here. e.g.  "
            '<iframe height="300px" frameborder="0" style="padding: 25px 10px;"'
            ' src="https://user.wufoo.com/embed/z1qnwrlw1iefzsu/">'
            '  <a href="https://user.wufoo.com/forms/z1qnwrlw1iefzsu/">Fill out my Wufoo form! </a>'
            '</iframe>'
        )
        label = 'iFrame'
        template = 'streams/blocks/iframe_block.html'
        form_classname = 'iframe-block struct-block'
        icon = 'media'

    def clean(self, value):
        """
        Parse the iframe data submitted and then rebuild the tag using only the allowed attributes.
        For browsers that do not support iframes, we allow a subset of tags inside the iframe contents.
        """
        soup = BeautifulSoup(value, "lxml")
        iframe = soup.find('iframe')
        if not iframe:
            raise ValidationError(_("The embed string needs to look like '<iframe ...></iframe>'"))

        contents = ' '.join(str(item) for item in iframe.contents) if iframe.contents else ''
        contents = custom_bleach(contents, "a,b,i,em,strong,br,sup,sub")
        # I am allowing the standards compliant tags listed on
        # https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe
        # plus 'frameborder' - in case someone actually wants a border around their embed
        allowed_tags = ['allowfullscreen', 'height', 'width', 'name', 'referrerpolicy', 'sandbox', 'src',
                        'title', 'width', 'frameborder']
        tag = "<iframe"
        for attr in iframe.attrs.keys():
            if attr in allowed_tags:
                tag += ' {0}="{1}"'.format(attr, iframe.attrs[attr])
        tag += ' scrolling="auto">{0}</iframe>'.format(contents)

        return tag


@register_feature(feature_type='special')
class IFrameEmbedBlock(blocks.StructBlock, BlockTupleMixin):
    """
    Offer users the ability to use iframes.
    BECAUSE this is a 'special feature' we can restrict which sites are allowed to use them.
    """
    html = IFrameBlock()

    fixed_dimensions = DimensionsOptionsBlock()

    class Meta:
        label = 'iFrame'
        template = 'streams/blocks/iframe_block.html'
        form_classname = 'iframe-block struct-block'
        icon = 'media'


###############################################################################
########################### LAYOUT BLOCK TYPES ################################
###############################################################################
# These go at the end because they need to include all of the content blocks defined above.
COLUMN_PERMITTED_BLOCKS = [
    get_block_tuple(FancyRichTextBlock()),
    get_block_tuple(CalloutBlock()),
    get_block_tuple(ImageCarouselBlock()),
    get_block_tuple(ImageGalleryBlock()),
    get_block_tuple(RelatedLinksBlock()),
    get_block_tuple(ImagePanelBlock()),
    get_block_tuple(VideoBlock()),
    get_block_tuple(IFrameEmbedBlock()),
    get_block_tuple(SectionTitleBlock()),
    get_block_tuple(MenuListingBlock()),
    get_block_tuple(SpacerBlock()),
]

# Choices for col-md-## class used by bootstrap for grids
BS_COL_CHOICES = [(x, x) for x in range(1, 12)]
col_helptext = "Column width is represented as units out of twelve. EX. 6 / 12 units will take up half the container."
fixed_height_helptext = (
    "Blocks that contain images that are placed in one of the columns here will set themselves to this height unless "
    "specifically overridden on the block."
)


class BaseTwoColumnSubBlock(blocks.StructBlock, BlockTupleMixin):
    """
    Duplicate of BaseTwoColumnBlock without the sub block to avoid recursion.
    """
    left_column_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=6, help_text=col_helptext)

    fixed_height = blocks.IntegerBlock(
        default=350,
        label="Suggested height for contained widgets",
        help_text="Blocks that contain images that are placed in one of the columns here will set themselves to this "
                  "height unless specifically overridden on the block."
    )
    gutter_width = IntegerChoiceBlock(
        choices=[(0, 0), (12, 12), (20, 20), (30, 30), (40, 40)],
        blank=False,
        default=12,
        label="Column Gutter Width (pixels)",
        help_text="This determines how wide the spacing between columns will be, in pixels."
    )
    background = BackgroundOptionsBlock()
    left_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-left',
        label='Left column content',
        required=False
    )
    right_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Right column content',
        required=False
    )

    class Meta:
        template = 'streams/blocks/layout/two_column_block.html'
        form_classname = 'layout-two-column-sub struct-block'
        label = 'Two Columns'

    @classmethod
    def get_block_machine_name(cls):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as BaseTwoColumnBlock.
        """
        return 'two_column_layout'

    def get_block_tuple(self):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as BaseTwoColumnBlock.
        """
        return ('two_column_layout', self)


class BaseTwoColumnBlock(blocks.StructBlock, BlockTupleMixin):
    """
    Base class to be overridden in implementing sub module with boilerplate implementation of column layout.
    """
    STYLES = (
        ('regular-width', 'Regular Width'),
        ('full-width', 'Full Width'),
        ('regular-width padded', 'Regular Width, Padded'),
        ('full-width padded', 'Full Width, Padded')
    )
    style = blocks.ChoiceBlock(choices=[(style[0], style[1]) for style in STYLES], default=STYLES[0][0])
    left_column_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=6, help_text=col_helptext)
    fixed_height = blocks.IntegerBlock(
        default=350,
        label="Suggested height for contained widgets",
        help_text=fixed_height_helptext
    )
    gutter_width = IntegerChoiceBlock(
        choices=[(0, 0), (12, 12), (20, 20), (30, 30), (40, 40)],
        blank=False,
        default=12,
        label="Column Gutter Width (pixels)",
        help_text="This determines how wide the spacing between columns will be, in pixels."
    )
    background = BackgroundOptionsBlock()
    left_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-left',
        label='Left column content',
        required=False
    )

    right_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Right column content',
        required=False
    )

    class Meta:
        template = 'streams/blocks/layout/two_column_block.html'
        form_classname = 'layout-two-column struct-block'
        label = 'Two Columns'

    @classmethod
    def get_block_machine_name(cls):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as BaseTwoColumnSubBlock.
        """
        return 'two_column_layout'

    def get_block_tuple(self):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as BaseTwoColumnSubBlock.
        """
        return ('two_column_layout', self)


class BaseThreeColumnSubBlock(blocks.StructBlock, BlockTupleMixin):
    """
    Duplicate of BaseThreeColumnBlock without the sub block to avoid recursion.
    """
    left_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-left',
        label='Left column content',
        required=False
    )
    middle_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Middle column content',
        required=False
    )
    right_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Right column content',
        required=False
    )

    left_column_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=4, help_text=col_helptext)
    right_column_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=4, help_text=col_helptext)

    fixed_height = blocks.IntegerBlock(
        default=300,
        label="Suggested height for contained widgets",
        help_text=fixed_height_helptext
    )
    gutter_width = IntegerChoiceBlock(
        choices=[(0, 0), (12, 12), (20, 20), (30, 30), (40, 40)],
        blank=False,
        default=12,
        label="Column Gutter Width (pixels)",
        help_text="This determines how wide the spacing between columns will be, in pixels."
    )
    background = BackgroundOptionsBlock()

    class Meta:
        template = 'streams/blocks/layout/three_column_block.html'
        form_classname = 'layout-three-column-sub struct-block'
        label = 'Three Columns'

    @classmethod
    def get_block_machine_name(cls):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as BaseThreeColumnSubBlock.
        """
        return 'three_column_layout'

    def get_block_tuple(self):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as BaseThreeColumnSubBlock.
        """
        return ('three_column_layout', self)


class BaseThreeColumnBlock(blocks.StructBlock, BlockTupleMixin):
    STYLES = (
        ('regular-width', 'Regular Width'),
        ('full-width', 'Full Width'),
        ('regular-width padded', 'Regular Width, Padded'),
        ('full-width padded', 'Full Width, Padded')
    )

    style = blocks.ChoiceBlock(choices=[(style[0], style[1]) for style in STYLES], default=STYLES[0][0])
    left_column_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=4, help_text=col_helptext)
    right_column_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=4, help_text=col_helptext)
    fixed_height = blocks.IntegerBlock(
        default=300,
        label="Suggested height for contained widgets",
        help_text=fixed_height_helptext
    )
    gutter_width = IntegerChoiceBlock(
        choices=[(0, 0), (12, 12), (20, 20), (30, 30), (40, 40)],
        blank=False,
        default=12,
        label="Column Gutter Width (pixels)",
        help_text="This determines how wide the spacing between columns will be, in pixels."
    )
    background = BackgroundOptionsBlock()
    left_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-left',
        label='Left column content',
        required=False
    )

    middle_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Middle column content',
        required=False
    )

    right_column = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Right column content',
        required=False
    )

    class Meta:
        template = 'streams/blocks/layout/three_column_block.html'
        form_classname = 'layout-three-column struct-block'
        label = 'Three Columns'

    @classmethod
    def get_block_machine_name(cls):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as ThreeColumnSubBlock.
        """
        return 'three_column_layout'

    def get_block_tuple(self):
        """
        Overrides this method from BlockTupleMixin so that we use the same machine name as ThreeColumnSubBlock.
        """
        return ('three_column_layout', self)


class BaseFourColumnBlock(blocks.StructBlock, BlockTupleMixin):
    STYLES = (
        ('regular-width', 'Regular Width'),
        ('full-width', 'Full Width'),
        ('regular-width padded', 'Regular Width, Padded'),
        ('full-width padded', 'Full Width, Padded')
    )

    style = blocks.ChoiceBlock(choices=[(style[0], style[1]) for style in STYLES], default=STYLES[0][0])
    column_one_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=3, help_text=col_helptext)
    column_two_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=3, help_text=col_helptext)
    column_three_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=3, help_text=col_helptext)
    fixed_height = blocks.IntegerBlock(
        default=250,
        label="Suggested height for contained widgets",
        help_text=fixed_height_helptext
    )
    gutter_width = IntegerChoiceBlock(
        choices=[(0, 0), (12, 12), (20, 20), (30, 30), (40, 40)],
        blank=False,
        default=12,
        label="Column Gutter Width (pixels)",
        help_text="This determines how wide the spacing between columns will be, in pixels."
    )
    background = BackgroundOptionsBlock()
    column_one = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        label='Column One Content',
        required=False
    )
    column_two = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        label='Column Two Content',
        required=False
    )
    column_three = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        label='Column Three Content',
        required=False
    )
    column_four = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        label='Column Four Content',
        required=False
    )

    class Meta:
        template = 'streams/blocks/layout/four_column_block.html'
        form_classname = 'layout-four-column struct-block'
        label = 'Four Columns'

    @classmethod
    def get_block_machine_name(cls):
        """
        Overrides this method from BlockTupleMixin so that we use the legacy machine name.
        """
        return 'four_column_layout'

    def get_block_tuple(self):
        """
        Overrides this method from BlockTupleMixin so that we use the legacy machine name.
        """
        return ('four_column_layout', self)


class BaseSidebarLayoutBlock(blocks.StructBlock, BlockTupleMixin):
    text = blocks.RichTextBlock()
    sidebar = FeatureCustomizedStreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Sidebar',
        required=False
    )
    sidebar_width = IntegerChoiceBlock(choices=BS_COL_CHOICES, blank=False, default=4, help_text=col_helptext)
    sidebar_alignment = blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], blank=False, default='left')
    fixed_height = blocks.IntegerBlock(
        default=250,
        label="Suggested height for child widgets",
        help_text=(
            "Child blocks containing images will set themsevles to this height unless specifically overridden on the "
            "block. Set this to 0 to not enforce a height."
        )
    )

    class Meta:
        template = 'streams/blocks/layout/sidebar_layout_block.html'
        form_classname = 'layout-sidebar struct-block'
        label = 'Sidebar Layout'


class TwoColumnBlock(BaseTwoColumnBlock):
    left_column = blocks.StreamBlock(
        COLUMN_PERMITTED_BLOCKS + [
            get_block_tuple(FancyRichTextBlock()),
        ],
        icon='arrow-left',
        label='Left column content'
    )

    right_column = blocks.StreamBlock(
        COLUMN_PERMITTED_BLOCKS + [
            get_block_tuple(ImagePanelBlock()),
        ],
        icon='arrow-right',
        label='Right column content'
    )


class _SliderBlock(blocks.StructBlock):
    BG_CHOICES = [
        'bg-0', 'bg-1', 'bg-2', 'bg-3', 'bg-4', 'bg-5', 'bg-6', 'bg-7', 'bg-8', 'bg-9', 'bg-10', 'bg-11', 'bg-12',
        'bg-13', 'bg-14', 'bg-15', 'bg-16', 'bg-17', 'bg-18', 'bg-19', 'bg-20', 'bg-rounded1', 'bg-rounded2',
        'bg-rounded3', 'bg-rounded4'
    ]
    TEXT_POS = [
        'top', 'left', 'right'
    ]
    bg_type = blocks.ChoiceBlock(choices=[(bg, bg) for bg in BG_CHOICES], required=True,
                                 default=3, help_text="Set Slide BG according to docs")
    text_placement = blocks.ChoiceBlock(choices=[(pos, pos) for pos in TEXT_POS], required=True,
                                        default='top', help_text="Position of text on the slide")
    heading = blocks.CharBlock(required=True, max_length=50)
    text = blocks.CharBlock(required=False, max_length=255)
    image = ImageChooserBlock(required=False, help_text="Image dimension needs to be XXXXX")


class MainSliderBlock(blocks.StructBlock):
    slides = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("slide", _SliderBlock())
            ]
        )
    )

    class Meta:
        template = 'streams/blocks/main_slider_block.html'
        icon = 'placeholder'
        label = 'Image Slider'


class InfoBlock(blocks.StructBlock):
    boxes = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('heading', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=400)),
                ('svg_icon', blocks.ChoiceBlock(choices=[('/img/svg-icons/{}'.format(svgico), svgico) for svgico in SVG_ICONS], blank=True,
                                  help_text="Choose your")),
                ('url', LinkBlock(required=False))
            ]
        )
    )

    class Meta:
        template = 'streams/blocks/info_block1.html'
        icon = 'placeholder'
        label = 'Info Block 1'


class VerticalTabSlider(blocks.StructBlock):
    BG_CHOICES = [
        ('bg-primary-color bg-5', 'blue'),
        ('bg-orange-light bg-6', 'orange'),
        ('bg-red bg-7', 'red')
    ]
    tabs = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('top_mini_heading', blocks.CharBlock(required=False, max_length=40)),
                ('major_heading', blocks.CharBlock(required=True, max_length=40)),
                ('background', blocks.ChoiceBlock(choices=BG_CHOICES, required=True, default='blue')),
                ('image', ImageChooserBlock(
                    required=False,
                    help_text="This image, if supplied, will appear to the left of the text"
                 )),
                ('text', blocks.RichTextBlock(required=True, min_length=300, max_length=400,
                                              help_text="Text length have to be within 300-400 characters to fit image size"))

            ]
        )
    )

    class Meta:
        template = 'streams/blocks/vertical_tab_sliders.html'
        icon = 'placeholder'
        label = 'Vertical Tab Slider'


class VideoWithTextBlock(blocks.StructBlock):
    BG_CHOICES = [
        'bg-0', 'bg-1', 'bg-2', 'bg-3', 'bg-4', 'bg-5', 'bg-6', 'bg-7', 'bg-8', 'bg-9', 'bg-10', 'bg-11', 'bg-12',
        'bg-13', 'bg-14', 'bg-15', 'bg-16', 'bg-17', 'bg-18', 'bg-19', 'bg-20', 'bg-rounded1', 'bg-rounded2',
        'bg-rounded3', 'bg-rounded4'
    ]
    video = blocks.CharBlock(required=True)
    video_thumb = ImageChooserBlock(
                    required=False,
                    help_text="Thumbnail Image for the Video to be displayed, if not choosen default image will appear"
                 )
    heading = blocks.CharBlock(required=True, max_length=50)
    bg_type = blocks.ChoiceBlock(choices=[(bg, bg) for bg in BG_CHOICES], blank=False, default='bg-8')
    text = blocks.RichTextBlock(required=False, min_length=300, max_length=400)

    class Meta:
        template = 'streams/blocks/single_video_w_text.html'
        icon = 'placeholder'
        label = 'Popup Video with Heading and Text'


class ClientBlock(blocks.StructBlock):
    clients = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('logo_image', TagFilterImageChooserBlock(tag='CLIENTLOGO', required=True)),
                ('url', LinkBlock(required=False))
            ]
        )
    )

    class Meta:
        template = 'streams/blocks/clients_block.html'
        icon = 'placeholder'
        label = 'Clients to display on first page (based on image logo CLIENTLOGO (capital)'


class InfoBlock2(blocks.StructBlock):

    mid_image = ImageChooserBlock(required=False)
    button_color = blocks.ChoiceBlock(choices=[(clr, clr) for clr in BTN_COLOR], required=True, default='red')
    url = LinkBlock()
    left_info_top = blocks.StructBlock(
            [
                ('heading', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=100)),
                ('svg_icon',
                 blocks.ChoiceBlock(choices=[('/img/svg-icons/{}'.format(svgico), svgico) for svgico in SVG_ICONS],
                                    blank=True,
                                    help_text="Choose your")),
            ]
        )
    left_info_bottom = blocks.StructBlock(
            [
                ('heading', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=100)),
                ('svg_icon',
                 blocks.ChoiceBlock(choices=[('/img/svg-icons/{}'.format(svgico), svgico) for svgico in SVG_ICONS],
                                    blank=True,
                                    help_text="Choose your")),
            ]
        )
    right_info_top = blocks.StructBlock(
            [
                ('heading', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=100)),
                ('svg_icon',
                 blocks.ChoiceBlock(choices=[('/img/svg-icons/{}'.format(svgico), svgico) for svgico in SVG_ICONS],
                                    blank=True,
                                    help_text="Choose your")),
            ]
        )
    right_info_bottom = blocks.StructBlock(
            [
                ('heading', blocks.CharBlock(required=True, max_length=40)),
                ('text', blocks.TextBlock(required=True, max_length=100)),
                ('svg_icon',
                 blocks.ChoiceBlock(choices=[('/img/svg-icons/{}'.format(svgico), svgico) for svgico in SVG_ICONS],
                                    blank=True,
                                    help_text="Choose your")),
            ]
        )

    class Meta:
        template = 'streams/blocks/info_block2.html'
        icon = 'placeholder'
        label = 'Info Section with Display image in middle and 2 infoboxes on each side (left & right)'


class FaqBlock(blocks.StructBlock):
    faqs = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('heading', blocks.CharBlock(required=True, max_length=40)),
                ('text1', blocks.TextBlock(required=True, min_length=50, max_length=600,
                                              help_text="Text Paragraph1 ")),
                ('text2', blocks.TextBlock(required=False, min_length=30, max_length=600,
                                               help_text="Text Paragraph2")),
                ('text3', blocks.TextBlock(required=False, min_length=30, max_length=600,
                                               help_text="Text Paragraph2")),
                ('svg_icon',
                 blocks.ChoiceBlock(choices=[('/img/svg-icons/{}'.format(svgico), svgico) for svgico in SVG_ICONS],
                                    blank=True,
                                    help_text="Choose your")),
                ('bullets', blocks.ListBlock(
                    blocks.StructBlock(
                        [
                            ('bullet', blocks.CharBlock(required=False, max_length=45))
                        ]
                    )
                )),
                ('video', blocks.CharBlock(required=False)),
                ('video_slug', blocks.CharBlock(required=False, max_length=30))
            ]
        )
    )

    class Meta:
        template = 'streams/blocks/faq_block.html'
        icon = 'placeholder'
        label = 'FAQ block with various info'

