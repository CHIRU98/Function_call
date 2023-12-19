#from qdrant_client import models, QdrantClient
#from sentence_transformers import SentenceTransformer

#encoder = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    
  {
    "name": "change Label Value",
    "api_name": "changeLabelCaption",
    "description": "The 'Change Label Caption' function is employed to alter the descriptive label or text presented to the user. This function allows for the modification of the content intended to provide information, guidance, or context within the user interface based on the user's input or specific requirements.",
    "parameters": [
      {
        "name": "caption",
        "description": "The caption the user wants to change for the label."
      }
    ]
  },
  {
    "name": "change Label Caption Name",
    "api_name": "changeLabelCaptionName",
    "description": "The 'Change Label Caption Name' function is used to modify the caption name provided by the user.",
    "parameters": [
      {
        "name": "name",
        "description": "This is for the name provided by the user for the caption name."
      }
    ]
  },
  {
    "name": "change Label Layout",
    "api_name": "changeLabelLayout",
    "description": "This function enables users to modify the layout of the label, providing the flexibility to reposition, resize, or apply other adjustments to the spatial arrangement of the label within the user interface. By utilizing this feature, users can tailor the label's placement and dimensions to suit specific design preferences and enhance the overall visual organization of the interface",
    "parameters": [
      {
        "name": "height",
        "description": "Specify the height for the label layout."
      },
      {
        "name": "width",
        "description": "Specify the width for the label layout."
      }
    ]
  },
  {
    "name": "change Label Validation",
    "api_name": "changeLabelValidation",
    "description": "This function allows you to customize and adjust validation settings associated with the label. Use this function to modify various validation configurations, ensuring flexibility and control over the label's behavior.",
    "parameters": [
      {
        "name": "isRequired",
        "description": "Set to true if label requires validation; otherwise, set to false."
      },
      {
        "name": "animation",
        "description": "Define animation settings for the label."
      }
    ]
  },
  {
    "name": "change Label Behaviour",
    "api_name": "changeLabelBehaviour",
    "description": "Alters the behavior of the label with this function.",
    "parameters": [
      {
        "name": "show",
        "description": "Set to true to display the label; set to false to hide it."
      }
    ]
  },
  {
    "name": "change Label ClassName",
    "api_name": "changeLabelClassName",
    "description": "Use this function to update or alter the class name linked to the label. By employing this feature, you can modify the identifier that determines the styling and behavior associated with the label, facilitating seamless adjustments and customization within the user interface.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new class name for the label."
      }
    ]
  },
  {
  "name": "change Label Text",
  "api_name": "changeLabelText",
  "description": "This function allows users to tailor and refine the text style employed in the label. By using this feature, individuals can make adjustments to the font, size, color, and other stylistic attributes of the text within the label, providing a means to achieve a customized and visually appealing presentation that aligns with their design preferences or the overall aesthetics of the user interface.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the label text."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the label text."
    },
    {
      "name": "color",
      "description": "Define the color of the label text."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the label text."
    },
    {
      "name": "textAlign",
      "description": "Specify the text alignment (e.g., left, center, right) for the label text."
    },
    {
      "name": "whiteSpace",
      "description": "Set the white-space property (e.g., normal, nowrap) for the label text."
    }
  ]
},
{
  "name": "change Label Background",
  "api_name": "changeLabelBackground",
  "description": "This function facilitates the customization of the background style associated with the label. Users can utilize this feature to modify the visual appearance and design of the label, tailoring it to suit specific aesthetic preferences or to better align with the overall visual theme of the user interface.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the label."
    },
    {
      "name": "image",
      "description": "Set the background image for the label."
    },
    {
      "name": "repeat",
      "description": "Define the repetition pattern (e.g., repeat, no-repeat) for the background image."
    },
    {
      "name": "position",
      "description": "Specify the background image position (e.g., top, center, bottom) for the label."
    },
    {
      "name": "size",
      "description": "Set the size of the background image for the label."
    },
    {
      "name": "attachment",
      "description": "Define the attachment behavior (e.g., scroll, fixed) for the background image."
    }
  ]
},
{
  "name": "change Label Border",
  "api_name": "changeLabelBorder",
  "description": "This function empowers users to fine-tune the border style of the label. By utilizing this feature, individuals can make precise adjustments to the visual characteristics of the label's border, including aspects such as color, thickness, and border type. This allows for a customized and polished appearance, ensuring the label seamlessly integrates with the overall design aesthetics of the user interface.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the border color for the label."
    },
    {
      "name": "style",
      "description": "Define the border style (e.g., solid, dashed) for the label."
    },
    {
      "name": "borderWidth",
      "description": "Set the border width for the label."
    }
  ]
},
{
  "name": "change Label Display Style",
  "api_name": "changeLabelDisplayStyle",
  "description": "This versatile function empowers you to make adjustments to the display style of the label. Easily modify padding and margin settings to achieve the desired visual appearance. Use this function to customize the spacing and positioning of the label, enhancing the overall design and layout of your application.",
  "parameters": [
    {
      "name": "padding",
      "description": "Specify the padding for the label."
    },
    {
      "name": "margin",
      "description": "Specify the margin for the label."
    }
  ]
},
{
  "name": "change Label Mouse Events",
  "api_name": "changeLabelMouseEvents",
  "description": "Modify mouse events for the label using this function.",
  "parameters": [
    {
      "name": "onClick",
      "description": "Specify the action to be taken on a mouse click event."
    },
    {
      "name": "onDoubleClick",
      "description": "Specify the action to be taken on a double-click event."
    },
    {
      "name": "onMouseEnter",
      "description": "Specify the action to be taken on a mouse enter event."
    },
    {
      "name": "onMouseLeave",
      "description": "Specify the action to be taken on a mouse leave event."
    }
  ]
},
{
  "name": "change Label Touch Events",
  "api_name": "changeLabelTouchEvents",
  "description": "Modify touch events for the label using this function.",
  "parameters": [
    {
      "name": "onTap",
      "description": "Specify the action to be taken on a tap event."
    },
    {
      "name": "onDoubleTap",
      "description": "Specify the action to be taken on a double-tap event."
    }
  ]
},
{
  "name": "change Label Device Sizes",
  "api_name": "changeLabelDeviceSizes",
  "description": "Specify different styles for various device sizes using this function.",
  "parameters": [
    {
      "name": "all",
      "description": "Style settings for all device sizes."
    },
    {
      "name": "mobile",
      "description": "Style settings for mobile devices."
    },
    {
      "name": "tabletPortrait",
      "description": "Style settings for tablet devices in portrait mode."
    },
    {
      "name": "tabletLandscape",
      "description": "Style settings for tablet devices in landscape mode."
    },
    {
      "name": "largeScreen",
      "description": "Style settings for large screens."
    }
  ]
},
{
  "name": "change Anchor Caption",
  "api_name": "changeAnchorCaption",
  "description": "Empower your application's user interface with this function, designed to effortlessly modify the caption of an anchor. Enhance the textual content associated with the anchor by using this versatile function. Whether you need to update, customize, or completely change the caption, this function provides the flexibility you need to seamlessly manage anchor text, improving the overall user experience.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the anchor."
    }
  ]
},
{
  "name": "change Anchor Name",
  "api_name": "changeAnchorName",
  "description": "Change the name associated with the anchor.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the anchor."
    }
  ]
},
{
  "name": "change Anchor Badge Value",
  "api_name": "changeAnchorBadgeValue",
  "description": "Set the badge value for the anchor.",
  "parameters": [
    {
      "name": "value",
      "description": "The new badge value for the anchor."
    }
  ]
},
{
  "name": "change Anchor Accessibility",
  "api_name": "changeAnchorAccessibility",
  "description": "Modify accessibility settings for the anchor.",
  "parameters": [
    {
      "name": "hint",
      "description": "Provide a hint for accessibility."
    },
    {
      "name": "tabIndex",
      "description": "Set the tab index for the anchor."
    },
    {
      "name": "shortcutKey",
      "description": "Specify a shortcut key for the anchor."
    }
  ]
},
{
  "name": "change Anchor Layout",
  "api_name": "changeAnchorLayout",
  "description": "Transform the visual presentation of your anchor with this function, offering precise control over its layout. Use this powerful tool to adjust the positioning, size, and alignment of the anchor within your application's layout. Whether you're fine-tuning the spacing, resizing, or ensuring pixel-perfect alignment, this function provides the flexibility needed to achieve an optimal and visually appealing layout for your anchors, enhancing the overall design of your user interface.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the anchor."
    },
    {
      "name": "height",
      "description": "Set the height for the anchor."
    }
  ]
},
{
  "name": "change Anchor Behavior",
  "api_name": "changeAnchorBehavior",
  "description": "Modify the behavior of the anchor.",
  "parameters": [
    {
      "name": "target",
      "description": "Specify the target for the anchor."
    },
    {
      "name": "show",
      "description": "Set to true to display the anchor; set to false to hide it."
    },
    {
      "name": "animation",
      "description": "Specify animation settings for the anchor."
    },
    {
      "name": "encodeURL",
      "description": "Specify whether to encode the URL for the anchor."
    }
  ]
},
{
  "name": "change Anchor Graphics",
  "api_name": "changeAnchorGraphics",
  "description": "Modify graphic settings for the anchor.",
  "parameters": [
    {
      "name": "iconClass",
      "description": "Set the icon class for the anchor."
    },
    {
      "name": "iconUrl",
      "description": "Set the icon URL for the anchor."
    },
    {
      "name": "iconWidth",
      "description": "Set the icon width for the anchor."
    },
    {
      "name": "iconHeight",
      "description": "Set the icon height for the anchor."
    },
    {
      "name": "iconMargin",
      "description": "Set the margin for the icon within the anchor."
    },
    {
      "name": "iconPosition",
      "description": "Set the position of the icon within the anchor."
    }
  ]
},
{
  "name": "change Anchor ClassName",
  "api_name": "changeAnchorClassName",
  "description": "Change the class name associated with the anchor.",
  "parameters": [
    {
      "name": "name",
      "description": "The new class name for the anchor."
    }
  ]
},
{
  "name": "change Anchor Text",
  "api_name": "changeAnchorText",
  "description": "Elevate the visual appeal of your anchor text with this dynamic function, designed to modify the text style seamlessly. Tailor the appearance of your anchor by adjusting font properties, such as size, color, weight, and more. Whether you're aiming for a bold and vibrant look or a subtle and elegant style, this function provides the flexibility to effortlessly customize the text style of your anchors, enhancing the overall aesthetics of your user interface.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the anchor text."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the anchor text."
    },
    {
      "name": "color",
      "description": "Define the color of the anchor text."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the anchor text."
    },
    {
      "name": "textAlign",
      "description": "Specify the text alignment (e.g., left, center, right) for the anchor text."
    },
    {
      "name": "whiteSpace",
      "description": "Set the white-space property (e.g., normal, nowrap) for the anchor text."
    }
  ]
},
{
  "name": "change Anchor Background",
  "api_name": "changeAnchorBackground",
  "description": "Transform the visual impact of your anchor by using this versatile function to adjust its background style. With this powerful tool, you can customize background properties such as color, gradient, transparency, and more. Whether you aim for a vibrant and eye-catching design or a subtle and cohesive background, this function provides the flexibility to seamlessly tailor the background style of your anchors, enhancing the overall aesthetics of your user interface.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the anchor."
    },
    {
      "name": "repeat",
      "description": "Define the repetition pattern (e.g., repeat, no-repeat) for the anchor background."
    },
    {
      "name": "position",
      "description": "Specify the background position (e.g., top, center, bottom) for the anchor."
    },
    {
      "name": "size",
      "description": "Set the size of the background for the anchor."
    },
    {
      "name": "attachment",
      "description": "Define the attachment behavior (e.g., scroll, fixed) for the anchor background."
    }
  ]
},
{
  "name": "change Anchor Border",
  "api_name": "changeAnchorBorder",
  "description": "Adjust the border style of the anchor.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the border color for the anchor."
    },
    {
      "name": "style",
      "description": "Define the border style (e.g., solid, dashed) for the anchor."
    },
    {
      "name": "borderWidth",
      "description": "Set the border width for the anchor."
    }
  ]
},
{
  "name": "change Button Caption",
  "api_name": "changeButtonCaption",
  "description": "Modify the caption of the button using this function.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the button."
    }
  ]
},
{
  "name": "change Button Name",
  "api_name": "changeButtonName",
  "description": "Change the name associated with the button.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the button."
    }
  ]
},
{
  "name": "change Button Type",
  "api_name": "changeButtonType",
  "description": "Change the type of the button.",
  "parameters": [
    {
      "name": "type",
      "description": "The new type for the button."
    }
  ]
},
{
  "name": "change Button Badge Value",
  "api_name": "changeButtonBadgeValue",
  "description": "Set the badge value for the button.",
  "parameters": [
    {
      "name": "value",
      "description": "The new badge value for the button."
    }
  ]
},
{
  "name": "change Button Layout",
  "api_name": "changeButtonLayout",
  "description": "Refine the visual presentation of your button effortlessly using this function, granting you precise control over its layout. Utilize this powerful tool to adjust the positioning, size, and alignment of the button within your application's layout. Whether you're fine-tuning spacing, resizing, or ensuring pixel-perfect alignment, this function offers the flexibility needed to achieve an optimal and visually appealing layout for your buttons, enhancing the overall design and user experience.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the button."
    },
    {
      "name": "height",
      "description": "Set the height for the button."
    }
  ]
},
{
  "name": "change Button Behavior",
  "api_name": "changeButtonBehavior",
  "description": "Modify the behavior of the button.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the button; set to false to hide it."
    },
    {
      "name": "disabled",
      "description": "Set to true to disable the button; set to false to enable it."
    },
    {
      "name": "animation",
      "description": "Specify animation settings for the button."
    }
  ]
},
{
  "name": "change Button Class",
  "api_name": "changeButtonClass",
  "description": "Change the class name associated with the button.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the button."
    }
  ]
},
{
  "name": "change Button Text",
  "api_name": "changeButtonText",
  "description": "Modify the text style of the button.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the button text."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the button text."
    },
    {
      "name": "color",
      "description": "Define the color of the button text."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the button text."
    },
    {
      "name": "textAlign",
      "description": "Specify the text alignment (e.g., left, center, right) for the button text."
    }
  ]
},
{
  "name": "change Button Background",
  "api_name": "changeButtonBackground",
  "description": "Transform the visual impact of your button by leveraging this versatile function to adjust its background style. With this powerful tool, customize background properties such as color, gradient, transparency, and more. Whether you're aiming for a vibrant and attention-grabbing design or a subtle and cohesive background, this function provides the flexibility to seamlessly tailor the background style of your buttons, enhancing the overall aesthetics of your user interface.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the button."
    },
    {
      "name": "repeat",
      "description": "Define the repetition pattern (e.g., repeat, no-repeat) for the button background."
    },
    {
      "name": "position",
      "description": "Specify the background position (e.g., top, center, bottom) for the button."
    },
    {
      "name": "size",
      "description": "Set the size of the background for the button."
    },
        {
      "name": "attachment",
      "description": "Define the attachment behavior (e.g., scroll, fixed) for the button background."
    }
  ]
},
{
  "name": "change Button Border",
  "api_name": "changeButtonBorder",
  "description": "Refine the visual appeal of your button with this versatile function designed to adjust its border style. Utilize this powerful tool to customize border properties such as color, thickness, radius, and more. Whether you're aiming for a sleek and modern design or a classic and sophisticated look, this function provides the flexibility to seamlessly tailor the border style of your buttons, enhancing the overall aesthetics and visual coherence of your user interface.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the border color for the button."
    },
    {
      "name": "style",
      "description": "Define the border style (e.g., solid, dashed) for the button."
    },
    {
      "name": "borderWidth",
      "description": "Set the border width for the button."
    }
  ]
},
{
  "name": "change Button Display",
  "api_name": "changeButtonDisplay",
  "description": "Transform the visual presentation of your button effortlessly using this versatile function, offering precise control over its display style. Customize the padding and margin properties to achieve the desired spacing and positioning within your application's layout. Whether you're adjusting the spacing for a compact layout or ensuring generous margins for a more spacious design, this function provides the flexibility to seamlessly modify the display style of your buttons, enhancing the overall aesthetics and user experience.",
  "parameters": [
    {
      "name": "padding",
      "description": "Specify the padding for the button."
    },
    {
      "name": "margin",
      "description": "Specify the margin for the button."
    }
  ]
},
{
  "name": "change Button On Focus",
  "api_name": "changeButtonOnFocus",
  "description": "Specify the action to be taken when the button is focused.",
  "parameters": [
    {
      "name": "text",
      "description": "The action or text to be associated with the button's focus event."
    }
  ]
},
{
  "name": "change Button On Blur",
  "api_name": "changeButtonOnBlur",
  "description": "Specify the action to be taken when the button loses focus.",
  "parameters": [
    {
      "name": "text",
      "description": "The action or text to be associated with the button's blur event."
    }
  ]
},
{
  "name": "change Button Mouse Events",
  "api_name": "changeButtonMouseEvents",
  "description": "Modify mouse events for the button.",
  "parameters": [
    {
      "name": "onClick",
      "description": "Specify the action to be taken on a mouse click event."
    },
    {
      "name": "onDoubleClick",
      "description": "Specify the action to be taken on a double-click event."
    },
    {
      "name": "onMouseEnter",
      "description": "Specify the action to be taken on a mouse enter event."
    },
    {
      "name": "onMouseLeave",
      "description": "Specify the action to be taken on a mouse leave event."
    }
  ]
},
{
  "name": "change Button Touch Events",
  "api_name": "changeButtonTouchEvents",
  "description": "Modify touch events for the button.",
  "parameters": [
    {
      "name": "onTap",
      "description": "Specify the action to be taken on a tap event."
    },
    {
      "name": "onDoubleTap",
      "description": "Specify the action to be taken on a double-tap event."
    }
  ]
},
{
  "name": "change Button Keyboard Events",
  "api_name": "changeButtonKeyboardEvents",
  "description": "Modify keyboard events for the button.",
  "parameters": [
    {
      "name": "onKeyDown",
      "description": "Specify the action to be taken on a key down event."
    },
    {
      "name": "onKeyPress",
      "description": "Specify the action to be taken on a key press event."
    },
    {
      "name": "onKeyUp",
      "description": "Specify the action to be taken on a key up event."
    }
  ]
},
{
  "name": "change Icon Caption",
  "api_name": "changeIconCaption",
  "description": "Modify the caption of the icon using this function.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the icon."
    }
  ]
},
{
  "name": "change Icon Name",
  "api_name": "changeIconName",
  "description": "Change the name associated with the icon.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the icon."
    }
  ]
},
{
  "name": "change Icon Behavior",
  "api_name": "changeIconBehavior",
  "description": "Modify the behavior of the icon.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the icon; set to false to hide it."
    },
    {
      "name": "animation",
      "description": "Specify animation settings for the icon."
    }
  ]
},
{
  "name": "change Icon Class",
  "api_name": "changeIconClass",
  "description": "Change the class name associated with the icon.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the icon."
    }
  ]
},
{
  "name": "change Icon Text Style",
  "api_name": "changeIconTextStyle",
  "description": "Modify the text style of the icon.",
  "parameters": [
    {
      "name": "color",
      "description": "Define the color of the icon text."
    }
  ]
},
{
  "name": "change Icon Display Style",
  "api_name": "changeIconDisplayStyle",
  "description": "Modify the display style (opacity) of the icon.",
  "parameters": [
    {
      "name": "opacity",
      "description": "Set the opacity for the icon."
    }
  ]
},
{
  "name": "change Icon Device Sizes",
  "api_name": "changeIconDeviceSizes",
  "description": "Specify different styles for various device sizes using this function.",
  "parameters": [
    {
      "name": "all",
      "description": "Style settings for all device sizes."
    },
    {
      "name": "mobile",
      "description": "Style settings for mobile devices."
    },
    {
      "name": "tabletPortrait",
      "description": "Style settings for tablet devices in portrait mode."
    },
    {
      "name": "tabletLandscape",
      "description": "Style settings for tablet devices in landscape mode."
    },
    {
      "name": "largeScreen",
      "description": "Style settings for large screens."
    }
  ]
},
{
  "name": "change Picture Name",
  "api_name": "changePictureName",
  "description": "Change the name associated with the picture.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the picture."
    }
  ]
},
{
  "name": "change Picture Tab Index",
  "api_name": "changePictureTabIndex",
  "description": "Set the tab index for the picture.",
  "parameters": [
    {
      "name": "value",
      "description": "The tab index value for the picture."
    }
  ]
},
{
  "name": "change Picture Aspect",
  "api_name": "changePictureAspect",
  "description": "Set the aspect ratio for the picture.",
  "parameters": [
    {
      "name": "aspect",
      "description": "Specify the aspect ratio for the picture (Both, H, V)."
    }
  ]
},
{
  "name": "change Picture Shape",
  "api_name": "changePictureShape",
  "description": "Set the shape of the picture.",
  "parameters": [
    {
      "name": "shape",
      "description": "Specify the shape of the picture (rounded, circle, thumbnail)."
    }
  ]
},
{
  "name": "change Picture Layout",
  "api_name": "changePictureLayout",
  "description": "Adjust the layout of the picture.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the picture."
    },
    {
      "name": "height",
      "description": "Set the height for the picture."
    }
  ]
},
{
  "name": "change Picture Behavior",
  "api_name": "changePictureBehavior",
  "description": "Modify the behavior of the picture.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the picture; set to false to hide it."
    }
  ]
},
{
  "name": "change Picture ClassName",
  "api_name": "changePictureClassName",
  "description": "Change the class name associated with the picture.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the picture."
    }
  ]
},
{
  "name": "change Picture Background",
  "api_name": "changePictureBackground",
  "description": "Elevate the visual impact of your picture by using this versatile function to seamlessly modify its background style. With this powerful tool, customize background properties such as color, gradient, transparency, and more. Whether you're aiming for a vibrant and attention-grabbing design or a subtle and cohesive background, this function provides the flexibility to effortlessly tailor the background style of your pictures, enhancing the overall aesthetics and visual appeal.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the picture."
    },
    {
      "name": "position",
      "description": "Specify the background position for the picture."
    },
    {
      "name": "size",
      "description": "Set the size of the background for the picture."
    }
  ]
},
{
  "name": "change Picture Border",
  "api_name": "changePictureBorder",
  "description": "Refine the visual presentation of your picture with this versatile function designed to adjust its border style. Utilize this powerful tool to customize border properties such as color, thickness, radius, and more. Whether you're aiming for a sleek and modern frame or a classic and sophisticated border, this function provides the flexibility to seamlessly tailor the border style of your pictures, enhancing the overall aesthetics and visual coherence of your images.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the border color for the picture."
    },
    {
      "name": "style",
      "description": "Define the border style (e.g., solid, dashed) for the picture."
    },
    {
      "name": "borderWidth",
      "description": "Set the border width for the picture."
    }
  ]
},
{
  "name": "change Picture Display Style",
  "api_name": "changePictureDisplayStyle",
  "description": "Transform the visual presentation of your picture effortlessly using this versatile function, offering precise control over its display style. Customize the padding and margin properties to achieve the desired spacing and positioning within your application's layout. Whether you're adjusting the spacing for a compact layout or ensuring generous margins for a more spacious design, this function provides the flexibility to seamlessly modify the display style of your pictures, enhancing the overall aesthetics and visual appeal of your images.",
  "parameters": [
    {
      "name": "padding",
      "description": "Specify the padding for the picture."
    },
    {
      "name": "margin",
      "description": "Specify the margin for the picture."
    }
  ]
},
{
  "name": "change Picture Mouse Events",
  "api_name": "changePictureMouseEvents",
  "description": "Modify mouse events for the picture.",
  "parameters": [
    {
      "name": "onClick",
      "description": "Specify the action to be taken on a mouse click event."
    },
    {
      "name": "onDoubleClick",
      "description": "Specify the action to be taken on a double-click event."
    },
    {
      "name": "onMouseEnter",
      "description": "Specify the action to be taken on a mouse enter event."
    },
    {
      "name": "onMouseLeave",
      "description": "Specify the action to be taken on a mouse leave event."
    }
  ]
},
{
  "name": "change Picture Touch Events",
  "api_name": "changePictureTouchEvents",
  "description": "Modify touch events for the picture.",
  "parameters": [
    {
      "name": "onTap",
      "description": "Specify the action to be taken on a tap event."
    }
  ]
},
{
  "name": "change Picture Device Sizes",
  "api_name": "changePictureDeviceSizes",
  "description": "Specify different styles for various device sizes using this function.",
  "parameters": [
    {
      "name": "all",
      "description": "Style settings for all device sizes."
    },
    {
      "name": "mobile",
      "description": "Style settings for mobile devices."
    },
    {
      "name": "tabletPortrait",
      "description": "Style settings for tablet devices in portrait mode."
    },
    {
      "name": "tabletLandscape",
      "description": "Style settings for tablet devices in landscape mode."
    },
    {
      "name": "largeScreen",
      "description": "Style settings for large screens."
    }
  ]
},
{
  "name": "change Tree ClassName",
  "api_name": "changeTreeClassName",
  "description": "Change the class name associated with the tree.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the tree."
    }
  ]
},
{
  "name": "change Tree Text Style",
  "api_name": "changeTreeTextStyle",
  "description": "Modify the text style of the tree.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the tree text."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the tree text."
    },
    {
      "name": "color",
      "description": "Define the color of the tree text."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the tree text."
    }
  ]
},
{
  "name": "change Tree Background Style",
  "api_name": "changeTreeBackgroundStyle",
  "description": "Modify the background style of the tree.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the tree."
    },
    {
      "name": "position",
      "description": "Specify the background position for the tree."
    },
    {
      "name": "size",
      "description": "Set the size of the background for the tree."
    }
  ]
},
{
  "name": "change Tree Border Style",
  "api_name": "changeTreeBorderStyle",
  "description": "Modify the border style of the tree.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the border color for the tree."
    },
    {
      "name": "style",
      "description": "Define the border style (e.g., solid, dashed) for the tree."
    },
    {
      "name": "borderWidth",
      "description": "Set the border width for the tree."
    }
  ]
},
{
  "name": "change Tree Display Style",
  "api_name": "changeTreeDisplayStyle",
  "description": "Modify the display style (padding) of the tree.",
  "parameters": [
    {
      "name": "padding",
      "description": "Specify the padding for the tree."
    }
  ]
},
{
  "name": "change Tree Name",
  "api_name": "changeTreeName",
  "description": "Change the name associated with the tree.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the tree."
    }
  ]
},
{
  "name": "change Tree Layout",
  "api_name": "changeTreeLayout",
  "description": "Adjust the layout of the tree.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the tree."
    },
    {
      "name": "height",
      "description": "Set the height for the tree."
    }
  ]
},
{
  "name": "change Tree Behavior",
  "api_name": "changeTreeBehavior",
  "description": "Modify the behavior of the tree.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the tree; set to false to hide it."
    }
  ]
},
{
  "name": "change Tree Format",
  "api_name": "changeTreeFormat",
  "description": "Specify the horizontal alignment for the tree.",
  "parameters": [
    {
      "name": "horizontalAlign",
      "description": "Specify the horizontal alignment for the tree (e.g., left, center, right)."
    }
  ]
},
{
  "name": "change Tree Callback Events",
  "api_name": "changeTreeCallbackEvents",
  "description": "Specify callback events for the tree.",
  "parameters": [
    {
      "name": "onExpand",
      "description": "Specify the action to be taken on an expand event."
    },
    {
      "name": "onCollapse",
      "description": "Specify the action to be taken on a collapse event."
    },
    {
      "name": "onSelect",
      "description": "Specify the action to be taken on a select event."
    }
  ]
},
{
  "name": "change Text Name",
  "api_name": "changeTextName",
  "description": "Change the name associated with the text.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the text."
    }
  ]
},
{
  "name": "change Text Layout",
  "api_name": "changeTextLayout",
  "description": "Adjust the layout of the text.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the text."
    },
    {
      "name": "height",
      "description": "Set the height for the text."
    }
  ]
},
{
  "name": "change Text Validation",
  "api_name": "changeTextValidation",
  "description": "Specify validation settings for the text.",
  "parameters": [
    {
      "name": "required",
      "description": "Set to true to make the text required for validation."
    }
  ]
},
{
  "name": "change Text Behavior",
  "api_name": "changeTextBehavior",
  "description": "Modify the behavior of the text.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the text; set to false to hide it."
    }
  ]
},
{
  "name": "change Text Caption",
  "api_name": "changeTextCaption",
  "description": "Specify the position of the text caption.",
  "parameters": [
    {
      "name": "position",
      "description": "Specify the position for the text caption (e.g., top, bottom, left, right)."
    }
  ]
},
{
  "name": "change Text Format",
  "api_name": "changeTextFormat",
  "description": "Specify the horizontal alignment for the text.",
  "parameters": [
    {
      "name": "horizontalAlign",
      "description": "Specify the horizontal alignment for the text (e.g., left, center, right)."
    }
  ]
},
{
  "name": "change Text ClassName",
  "api_name": "changeTextClassName",
  "description": "Change the class name associated with the text.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the text."
    }
  ]
},
{
  "name": "change Text Style",
  "api_name": "changeTextStyle",
  "description": "Modify the text style of the text.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the text."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the text."
    },
    {
      "name": "color",
      "description": "Define the color of the text."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the text."
    }
  ]
},
{
  "name": "change Text Background",
  "api_name": "changeTextBackground",
  "description": "Enhance the visual impact of your text by using this versatile function to seamlessly modify its background style. With this powerful tool, you can customize background properties such as color, gradient, transparency, and more. Whether you're aiming for a vibrant and attention-grabbing design or a subtle and cohesive background, this function provides the flexibility to effortlessly tailor the background style of your text, elevating the overall aesthetics and readability.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the text."
    },
    {
      "name": "position",
      "description": "Specify the background position for the text."
    },
    {
      "name": "size",
      "description": "Set the size of the background for the text."
    }
  ]
},
{
  "name": "change Text Display Style",
  "api_name": "changeTextDisplayStyle",
  "description": "Transform the visual presentation of your text effortlessly using this versatile function, offering precise control over its display style. Customize the padding and margin properties to achieve the desired spacing and positioning within your application's layout. Whether you're adjusting the spacing for a compact layout or ensuring generous margins for a more spacious design, this function provides the flexibility to seamlessly modify the display style of your text, enhancing the overall aesthetics and readability.",
  "parameters": [
    {
      "name": "padding",
      "description": "Specify the padding for the text."
    },
    {
      "name": "margin",
      "description": "Specify the margin for the text."
    }
  ]
},
{
  "name": "change Number Name",
  "api_name": "changeNumberName",
  "description": "Change the name associated with the number input.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the number input."
    }
  ]
},
{
  "name": "change Number Placeholder",
  "api_name": "changeNumberPlaceholder",
  "description": "Set the placeholder text for the number input.",
  "parameters": [
    {
      "name": "placeholder",
      "description": "The placeholder text for the number input."
    }
  ]
},
{
  "name": "change Number Layout",
  "api_name": "changeNumberLayout",
  "description": "Adjust the layout of the number input.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the number input."
    },
    {
      "name": "height",
      "description": "Set the height for the number input."
    }
  ]
},
{
  "name": "change Text Area Name",
  "api_name": "changeTextAreaName",
  "description": "Change the name associated with the text area.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the text area."
    }
  ]
},
{
  "name": "change Text Area Placeholder",
  "api_name": "changeTextAreaPlaceholder",
  "description": "Set the placeholder text for the text area.",
  "parameters": [
    {
      "name": "placeholder",
      "description": "The placeholder text for the text area."
    }
  ]
},
{
  "name": "change Text Area Layout",
  "api_name": "changeTextAreaLayout",
  "description":"Refine the visual arrangement of your text area effortlessly using this versatile function, providing precise control over its layout. Utilize this powerful tool to adjust the positioning, size, and alignment of the text area within your application's layout. Whether you're fine-tuning the spacing for a compact design or ensuring ample room for a more spacious layout, this function offers the flexibility needed to seamlessly adjust the layout of your text area, enhancing the overall aesthetics and readability.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the text area."
    },
    {
      "name": "height",
      "description": "Set the height for the text area."
    }
  ]
},
{
  "name": "change Text Area Behavior",
  "api_name": "changeTextAreaBehavior",
  "description": "Modify the behavior of the text area.",
  "parameters": [
    {
      "name": "autoFocus",
      "description": "Set to true to automatically focus on the text area."
    },
    {
      "name": "readOnly",
      "description": "Set to true to make the text area read-only."
    },
    {
      "name": "show",
      "description": "Set to true to display the text area; set to false to hide it."
    },
    {
      "name": "disabled",
      "description": "Set to true to disable the text area."
    },
    {
      "name": "autoTrim",
      "description": "Set to true to automatically trim the value of the text area."
    },
    {
      "name": "updateValueOn",
      "description": "Specify when to update the value of the text area (e.g., blur, input, change)."
    },
    {
      "name": "updateDelay",
      "description": "Specify the delay (in milliseconds) before updating the value of the text area."
    }
  ]
},
{
  "name": "change Text Area ClassName",
  "api_name": "changeTextAreaClassName",
  "description": "Change the class name associated with the text area.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the text area."
    }
  ]
},
{
  "name": "change Text Area Text",
  "api_name": "changeTextAreaText",
  "description": "Elevate the visual appeal of your text area with this versatile function designed to seamlessly modify its text style. Utilize this powerful tool to customize text properties such as font size, color, weight, and more. Whether you're aiming for a bold and modern look or a subtle and classic style, this function provides the flexibility to effortlessly tailor the text style of your text area, enhancing the overall aesthetics and readability of your content.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the text area."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the text area."
    },
    {
      "name": "color",
      "description": "Define the color of the text area."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the text area."
    },
    {
      "name": "textAlign",
      "description": "Specify the text alignment for the text area (e.g., left, center, right)."
    }
  ]
},
{
  "name": "change Text Area Background",
  "api_name": "changeTextAreaBackground",
  "description": "Transform the visual presence of your text area by using this versatile function to seamlessly modify its background style. With this powerful tool, customize background properties such as color, gradient, transparency, and more. Whether you're aiming for a vibrant and attention-grabbing design or a subtle and cohesive background, this function provides the flexibility to effortlessly tailor the background style of your text area, elevating the overall aesthetics and readability of your content.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the text area."
    }
  ]
},
{
  "name": "change Select Name",
  "api_name": "changeSelectName",
  "description": "Change the name associated with the select input.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the select input."
    }
  ]
},
{
  "name": "change Select Placeholder",
  "api_name": "changeSelectPlaceholder",
  "description": "Set the placeholder text for the select input.",
  "parameters": [
    {
      "name": "placeholder",
      "description": "The placeholder text for the select input."
    }
  ]
},
{
  "name": "change Select Layout",
  "api_name": "changeSelectLayout",
  "description": "Adjust the layout of the select input.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the select input."
    },
    {
      "name": "height",
      "description": "Set the height for the select input."
    }
  ]
},
{
  "name": "change Select ClassName",
  "api_name": "changeSelectClassName",
  "description": "Change the class name associated with the select input.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the select input."
    }
  ]
},
{
  "name": "change Select Text Style",
  "api_name": "changeSelectTextStyle",
  "description": "Modify the text style of the select input.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the select input."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the select input."
    },
    {
      "name": "color",
      "description": "Define the color of the select input."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the select input."
    },
    {
      "name": "textAlign",
      "description": "Specify the text alignment for the select input (e.g., left, center, right)."
    }
  ]
},
{
  "name": "change Select Background Style",
  "api_name": "changeSelectBackgroundStyle",
  "description": "Modify the background style of the select input.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the select input."
    }
  ]
},
{
  "name": "change Select Display Style",
  "api_name": "changeSelectDisplayStyle",
  "description": "Modify the display style (margin) of the select input.",
  "parameters": [
    {
      "name": "margin",
      "description": "Specify the margin for the select input."
    }
  ]
},
{
  "name": "change Radioset Name",
  "api_name": "changeRadiosetName",
  "description": "Change the name associated with the radioset.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the radioset."
    }
  ]
},
{
  "name": "change Radioset Layout",
  "api_name": "changeRadiosetLayout",
  "description": "Adjust the layout of the radioset.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the radioset."
    },
    {
      "name": "height",
      "description": "Set the height for the radioset."
    }
  ]
},
{
  "name": "change Radioset Caption",
  "api_name": "changeRadiosetCaption",
  "description": "Specify the position of the radioset caption.",
  "parameters": [
    {
      "name": "position",
      "description": "Specify the position for the radioset caption (e.g., top, bottom, left, right)."
    }
  ]
},
{
  "name": "change Radioset Format",
  "api_name": "changeRadiosetFormat",
  "description": "Specify the horizontal alignment for the radioset.",
  "parameters": [
    {
      "name": "horizontalAlign",
      "description": "Specify the horizontal alignment for the radioset (e.g., left, center, right)."
    }
  ]
},
{
  "name": "change Radioset ClassName",
  "api_name": "changeRadiosetClassName",
  "description": "Change the class name associated with the radioset.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the radioset."
    }
  ]
},
{
  "name": "change Radioset Text Style",
  "api_name": "changeRadiosetTextStyle",
  "description": "Modify the text style of the radioset.",
  "parameters": [
    {
      "name": "size",
      "description": "Specify the font size for the radioset."
    },
    {
      "name": "fontFamily",
      "description": "Set the font family for the radioset."
    },
    {
      "name": "color",
      "description": "Define the color of the radioset."
    },
    {
      "name": "fontStyle",
      "description": "Set the font style (e.g., normal, italic) for the radioset."
    }
  ]
},
{
  "name": "change Radioset Background Style",
  "api_name": "changeRadiosetBackgroundStyle",
  "description": "Modify the background style of the radioset.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the radioset."
    }
  ]
},
{
  "name": "change Radioset Display Style",
  "api_name": "changeRadiosetDisplayStyle",
  "description": "Modify the display style (padding and margin) of the radioset.",
  "parameters": [
    {
      "name": "padding",
      "description": "Specify the padding for the radioset."
    },
    {
      "name": "margin",
      "description": "Specify the margin for the radioset."
    }
  ]
},
{
  "name": "change Checkbox Caption",
  "api_name": "changeCheckBoxCaption",
  "description": "Change the caption associated with the checkbox.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the checkbox."
    }
  ]
},
{
  "name": "change Checkbox Name",
  "api_name": "changeCheckBoxName",
  "description": "Change the name associated with the checkbox.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the checkbox."
    }
  ]
},
{
  "name": "change Checkbox Layout",
  "api_name": "changeCheckBoxLayout",
  "description": "Adjust the layout of the checkbox.",
  "parameters": [
    {
      "name": "width",
      "description": "Set the width for the checkbox."
    },
    {
      "name": "height",
      "description": "Set the height for the checkbox."
    }
  ]
},
{
  "name": "change Checkbox ClassName",
  "api_name": "changeCheckBoxClassName",
  "description": "Change the class name associated with the checkbox.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the checkbox."
    }
  ]
},
{
  "name": "change Checkbox Display Style",
  "api_name": "changeCheckBoxDisplayStyle",
  "description": "Modify the display style (margin) of the checkbox.",
  "parameters": [
    {
      "name": "margin",
      "description": "Specify the margin for the checkbox."
    }
  ]
},
 {
    "name": "changeCheckBoxCaption",
    "api_name": "changeCheckBoxCaption",
    "description": "Modify the displayed caption or label associated with a checkbox. This function allows you to update the text that appears alongside a checkbox, enhancing user interface customization.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the name of the target checkbox for which the caption should be changed."
      }
    ]
  },
  {
    "name": "changeCheckBoxName",
    "api_name": "changeCheckBoxName",
    "description": "Alter the identifier or name attribute of a checkbox. This function provides the capability to redefine the unique identifier associated with a checkbox, facilitating better code organization and interaction.",
    "parameters": [
      {
        "name": "name",
        "description": "Provide the new identifier or name for the checkbox, ensuring clarity and coherence in your application structure."
      }
    ]
  },
  {
    "name": "changeCheckBoxLayout",
    "api_name": "changeCheckBoxLayout",
    "description": "Adjust the size, both width and height, of a checkbox within your user interface. This function enables fine-tuning of the checkbox dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "Specify the new width for the checkbox, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "Specify the new height for the checkbox, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "changeCheckBoxClassName",
    "api_name": "changeCheckBoxClassName",
    "description": "Modify the CSS class name associated with a checkbox. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the checkbox.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the checkbox, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "changeCheckBoxBackgroundStyle",
    "api_name": "changeCheckBoxBackgroundStyle",
    "description": "Adjust the background style, including color, of a checkbox. This function provides the capability to modify the visual appearance of the checkbox background, enhancing the overall design.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new color for the checkbox background, allowing for a customized and visually appealing appearance."
      }
    ]
  },
  {
    "name": "changeCheckBoxDisplayStyle",
    "api_name": "changeCheckBoxDisplayStyle",
    "description": "Modify the display style, including margin, of a checkbox. This function enables customization of the checkbox's display properties, providing control over its spacing and layout within the user interface.",
    "parameters": [
      {
        "name": "Margin",
        "description": "Specify the new margin for the checkbox, influencing its spacing and placement within the layout. This allows for precise control over the checkbox's display."
      }
    ]
  },
  {
    "name": "changeVideoName",
    "api_name": "changeVideoName",
    "description": "Modify the name attribute of a video element. This function allows you to update the identifier or name associated with a video, facilitating better organization in your application.",
    "parameters": [
      {
        "name": "name",
        "description": "Provide the new name for the video element, enhancing clarity and coherence in your code structure."
      }
    ]
  },
  {
    "name": "changeVideoLayout",
    "api_name": "changeVideoLayout",
    "description": "Adjust the size (width and height) of a video element. This function enables fine-tuning of the video dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "Specify the new width for the video element, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "Specify the new height for the video element, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "changeVideoBehavior",
    "api_name": "changeVideoBehavior",
    "description": "Modify various behavioral aspects of a video element. This function allows you to control the appearance and functionality of the video by toggling options such as show, enable controls, enable autoplay, loop, and mute.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the video element."
      },
      {
        "name": "Enable Controls",
        "description": "Enable or disable user controls for the video."
      },
      {
        "name": "Enable Autoplay",
        "description": "Enable or disable autoplay functionality for the video."
      },
      {
        "name": "Loop",
        "description": "Toggle looping behavior for the video."
      },
      {
        "name": "Mute",
        "description": "Toggle mute functionality for the video."
      }
    ]
  },
  {
    "name": "changeVideoClassName",
    "api_name": "changeVideoClassName",
    "description": "Modify the CSS class name associated with a video element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the video.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the video element, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "changeVideoText",
    "api_name": "changeVideoText",
    "description": "Modify the color of the text associated with a video element. This function allows you to customize the text color, improving the overall visual appearance of the video element.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new color for the text associated with the video element."
      }
    ]
  },
  {
    "name": "changeVideoBackground",
    "api_name": "changeVideoBackground",
    "description": "Modify various background properties of a video element. This function enables customization of the background color, repeat pattern, position, and size, enhancing the visual presentation of the video element.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new background color for the video element."
      },
      {
        "name": "Repeat",
        "description": "Specify the repeat pattern for the video background."
      },
      {
        "name": "Position",
        "description": "Specify the position of the video background within the element."
      },
      {
        "name": "Size",
        "description": "Specify the size of the video background, influencing its dimensions."
      }
    ]
  },
  {
    "name": "changeVideoBorder",
    "api_name": "changeVideoBorder",
    "description": "Modify various border properties of a video element. This function enables customization of the border color, style, and width, enhancing the visual presentation of the video element.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new border color for the video element."
      },
      {
        "name": "Style",
        "description": "Specify the new border style for the video element."
      },
      {
        "name": "Border Width",
        "description": "Specify the new border width for the video element."
      }
    ]
  },
  {
    "name": "changeVideoDisplay",
    "api_name": "changeVideoDisplay",
    "description": "Modify various display properties of a video element. This function enables customization of padding and overflow, influencing the spacing and overflow behavior of the video element.",
    "parameters": [
      {
        "name": "Padding",
        "description": "Specify the new padding for the video element, influencing its spacing within the layout."
      },
      {
        "name": "Overflow",
        "description": "Specify the overflow behavior for the video element, controlling how content overflows its box."
      }
    ]
  },
  {
    "name": "change Audio Name",
    "api_name": "changeAudioName",
    "description": "Modify the name attribute of an audio element. This function allows you to update the identifier or name associated with an audio element, facilitating better organization in your application.",
    "parameters": [
      {
        "name": "name",
        "description": "Provide the new name for the audio element, enhancing clarity and coherence in your code structure."
      }
    ]
  },
  {
    "name": "change Audio Layout",
    "api_name": "changeAudioLayout",
    "description": "Adjust the size (width and height) of an audio element. This function enables fine-tuning of the audio dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "Specify the new width for the audio element, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "Specify the new height for the audio element, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Audio Behavior",
    "api_name": "changeAudioBehavior",
    "description": "Modify various behavioral aspects of an audio element. This function allows you to control the appearance and functionality of the audio by toggling options such as show, enable controls, enable autoplay, loop, and mute.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the audio element."
      },
      {
        "name": "Enable Controls",
        "description": "Enable or disable user controls for the audio."
      },
      {
        "name": "Enable Autoplay",
        "description": "Enable or disable autoplay functionality for the audio."
      },
      {
        "name": "Loop",
        "description": "Toggle looping behavior for the audio."
      },
      {
        "name": "Mute",
        "description": "Toggle mute functionality for the audio."
      }
    ]
  },
  {
    "name": "change Audio ClassName",
    "api_name": "changeAudioClassName",
    "description": "Modify the CSS class name associated with an audio element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the audio.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the audio element, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Iframe Name",
    "api_name": "changeIframeName",
    "description": "Modify the name attribute of an iframe element. This function allows you to update the identifier or name associated with an iframe, facilitating better organization in your application.",
    "parameters": [
      {
        "name": "name",
        "description": "Provide the new name for the iframe element, enhancing clarity and coherence in your code structure."
      }
    ]
  },
  {
    "name": "change Iframe Layout",
    "api_name": "changeIframeLayout",
    "description": "Adjust the size (width and height) of an iframe element. This function enables fine-tuning of the iframe dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "Specify the new width for the iframe element, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "Specify the new height for the iframe element, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Iframe Behavior",
    "api_name": "changeIframeBehavior",
    "description": "Modify various behavioral aspects of an iframe element. This function allows you to control the appearance and functionality of the iframe by toggling options such as show and encoding the URL.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the iframe element."
      },
      {
        "name": "Encode URL",
        "description": "Toggle URL encoding for the iframe source, ensuring proper rendering and security."
      }
    ]
  },
  {
    "name": "change Iframe ClassName",
    "api_name": "changeIframeClassName",
    "description": "Modify the CSS class name associated with an iframe element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the iframe.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the iframe element, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Message Caption",
    "api_name": "changeMessageCaption",
    "description": "Modify the caption associated with a message. This function allows you to update the displayed text for a message, enhancing user communication.",
    "parameters": [
      {
        "name": "caption",
        "description": "The new caption text for the message."
      }
    ]
  },
  {
    "name": "change Message Name",
    "api_name": "changeMessageName",
    "description": "Modify the name attribute of a message. This function enables you to update the identifier or name associated with a message for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the message."
      }
    ]
  },
  {
    "name": "change Message Type",
    "api_name": "changeMessageType",
    "description": "Modify the type of a message. This function allows you to update the type or category of a message, facilitating better classification.",
    "parameters": [
      {
        "name": "type",
        "description": "The new type or category for the message."
      }
    ]
  },
  {
    "name": "change Message Layout",
    "api_name": "changeMessageLayout",
    "description": "Adjust the size (width and height) of a message. This function enables fine-tuning of the message dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the message, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the message, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Message Behavior",
    "api_name": "changeMessageBehavior",
    "description": "Modify various behavioral aspects of a message. This function allows you to control the appearance and functionality of the message by toggling options such as show, hide, close, and animation.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the message."
      },
      {
        "name": "Hide",
        "description": "Hide the message from view."
      },
      {
        "name": "Close",
        "description": "Enable or disable the close button for the message."
      },
      {
        "name": "Animation",
        "description": "Toggle animation effects for the message."
      }
    ]
  },
  {
    "name": "change Message ClassName",
    "api_name": "changeMessageClassName",
    "description": "Modify the CSS class name associated with a message. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the message.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the message, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Spinner Caption",
    "api_name": "changeSpinnerCaption",
    "description": "Modify the caption associated with a spinner. This function allows you to update the displayed text for a spinner, enhancing user communication.",
    "parameters": [
      {
        "name": "caption",
        "description": "The new caption text for the spinner."
      }
    ]
  },
  {
    "name": "change Spinner Name",
    "api_name": "changeSpinnerName",
    "description": "Modify the name attribute of a spinner. This function enables you to update the identifier or name associated with a spinner for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the spinner."
      }
    ]
  },
  {
    "name": "change Spinner Type",
    "api_name": "changeSpinnerType",
    "description": "Modify the type of a spinner. This function allows you to update the type or category of a spinner, facilitating better classification.",
    "parameters": [
      {
        "name": "type",
        "description": "The new type or category for the spinner."
      }
    ]
  },
  {
    "name": "change Spinner Picture",
    "api_name": "changeSpinnerPicture",
    "description": "Adjust the height of the picture associated with a spinner. This function enables fine-tuning of the picture dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "height",
        "description": "The new height for the spinner picture, influencing its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Spinner Behavior",
    "api_name": "changeSpinnerBehavior",
    "description": "Modify various behavioral aspects of a spinner. This function allows you to control the appearance and functionality of the spinner by toggling options such as show and animation.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the spinner."
      },
      {
        "name": "Animation",
        "description": "Toggle animation effects for the spinner."
      }
    ]
  },
  {
    "name": "change Spinner Graphics",
    "api_name": "changeSpinnerGraphics",
    "description": "Modify various graphics properties of a spinner. This function enables customization of the icon class and icon size, enhancing the visual presentation of the spinner.",
    "parameters": [
      {
        "name": "Icon Class",
        "description": "Specify the new icon class for the spinner, allowing for seamless integration with your styling preferences."
      },
      {
        "name": "Icon Size",
        "description": "Specify the new icon size for the spinner graphics, influencing its dimensions."
      }
    ]
  },
  {
    "name": "change Spinner Class Name",
    "api_name": "changeSpinnerClassName",
    "description": "Modify the CSS class name associated with a spinner. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the spinner.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the spinner, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Spinner Text Style",
    "api_name": "changeSpinnerTextStyle",
    "description": "Modify various text style properties of a spinner. This function enables customization of the size, font family, color, and font style of the spinner text.",
    "parameters": [
      {
        "name": "Size",
        "description": "Specify the new size for the spinner text."
      },
      {
        "name": "Font Family",
        "description": "Specify the new font family for the spinner text."
      },
      {
        "name": "Color",
        "description": "Specify the new color for the spinner text."
      },
      {
        "name": "Font Style",
        "description": "Specify the new font style for the spinner text."
      }
    ]
  },
  {
    "name": "change Spinner Background Style",
    "api_name": "changeSpinnerBackgroundStyle",
    "description": "Modify various background style properties of a spinner. This function enables customization of the background color, repeat pattern, position, and size, enhancing the visual presentation of the spinner.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new background color for the spinner."
      },
      {
        "name": "Repeat",
        "description": "Specify the repeat pattern for the spinner background."
      },
      {
        "name": "Position",
        "description": "Specify the position of the spinner background within the element."
      },
      {
        "name": "Size",
        "description": "Specify the size of the spinner background, influencing its dimensions."
      }
    ]
  },
  {
    "name": "change Search Name",
    "api_name": "changeSearchName",
    "description": "Modify the name attribute of a search element. This function enables you to update the identifier or name associated with a search element for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the search element."
      }
    ]
  },
  {
    "name": "change Search Type",
    "api_name": "changeSearchType",
    "description": "Modify the type of a search element. This function allows you to update the type or category of a search element, facilitating better classification.",
    "parameters": [
      {
        "name": "type",
        "description": "The new type or category for the search element."
      }
    ]
  },
  {
    "name": "change Search Placeholder",
    "api_name": "changeSearchPlaceholder",
    "description": "Modify the placeholder text of a search element. This function enables you to update the temporary text displayed inside the search input, providing additional context or instructions.",
    "parameters": [
      {
        "name": "placeholder",
        "description": "The new placeholder text for the search element."
      }
    ]
  },
  {
    "name": "change Search Layout",
    "api_name": "changeSearchLayout",
    "description": "Adjust the size (width and height) of a search element. This function enables fine-tuning of the search element dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the search element, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the search element, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Search Display Format",
    "api_name": "changeSearchDisplayFormat",
    "description": "Modify the display format limit of search results. This function allows you to specify the limit for displaying search results, enhancing control over the presentation.",
    "parameters": [
      {
        "name": "limit",
        "description": "Specify the limit for displaying search results."
      }
    ]
  },
  {
    "name": "change Search Validation",
    "api_name": "changeSearchValidation",
    "description": "Modify the validation value of a search element. This function allows you to set validation criteria for the search input, ensuring input conformity.",
    "parameters": [
      {
        "name": "value",
        "description": "Specify the validation value for the search element."
      }
    ]
  },
  {
    "name": "change Search Behavior",
    "api_name": "changeSearchBehavior",
    "description": "Modify various behavioral aspects of a search element. This function allows you to control the appearance and functionality of the search element by toggling options such as read-only, show, disabled, show clear, search on, delay time (ms), and min chars.",
    "parameters": [
      {
        "name": "Read Only",
        "description": "Toggle read-only mode for the search element."
      },
      {
        "name": "Show",
        "description": "Toggle the visibility of the search element."
      },
      {
        "name": "Disabled",
        "description": "Disable user interaction with the search element."
      },
      {
        "name": "Show Clear",
        "description": "Toggle the visibility of the clear button for the search element."
      },
      {
        "name": "Search On",
        "description": "Toggle the search functionality for the search element."
      },
      {
        "name": "Delay Time (ms)",
        "description": "Specify the delay time for triggering search events in milliseconds."
      },
      {
        "name": "Min Chars",
        "description": "Specify the minimum number of characters required for triggering search events."
      }
    ]
  },
  {
    "name": "change Search Graphics",
    "api_name": "changeSearchGraphics",
    "description": "Adjust the picture width of a search element. This function enables fine-tuning of the graphics dimensions associated with the search element.",
    "parameters": [
      {
        "name": "Picture Width",
        "description": "Specify the new picture width for the search graphics, influencing its dimensions."
      }
    ]
  },
  {
    "name": "change Search Class Name",
    "api_name": "changeSearchClassName",
    "description": "Modify the CSS class name associated with a search element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the search element.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the search element, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Search Text Style",
    "api_name": "changeSearchTextStyle",
    "description": "Modify various text style properties of a search element. This function enables customization of the size, font family, color, and font style of the search text.",
    "parameters": [
      {
        "name": "Size",
        "description": "Specify the new size for the search text."
      },
      {
        "name": "Font Family",
        "description": "Specify the new font family for the search text."
      },
      {
        "name": "Color",
        "description": "Specify the new color for the search text."
      },
      {
        "name": "Font Style",
        "description": "Specify the new font style for the search text."
      }
    ]
  },
  {
    "name": "change Search Background Style",
    "api_name": "changeSearchBackgroundStyle",
    "description": "Modify various background style properties of a search element. This function enables customization of the background color, repeat pattern, position, and size, enhancing the visual presentation of the search element.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new background color for the search element."
      },
      {
        "name": "Repeat",
        "description": "Specify the repeat pattern for the search background."
      },
      {
        "name": "Position",
        "description": "Specify the position of the search background within the element."
      },
      {
        "name": "Size",
        "description": "Specify the size of the search background, influencing its dimensions."
      }
    ]
  },
  {
    "name": "change Progress Bar Name",
    "api_name": "changeProgressBarName",
    "description": "Modify the name attribute of a progress bar element. This function enables you to update the identifier or name associated with a progress bar for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the progress bar."
      }
    ]
  },
  {
    "name": "change Progress Bar Type",
    "api_name": "changeProgressBarType",
    "description": "Modify the type of a progress bar element. This function allows you to update the type or category of a progress bar, facilitating better classification.",
    "parameters": [
      {
        "name": "type",
        "description": "The new type or category for the progress bar."
      }
    ]
  },
  {
    "name": "change Progress Bar Layout",
    "api_name": "changeProgressBarLayout",
    "description": "Adjust the size (width and height) of a progress bar element. This function enables fine-tuning of the progress bar dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the progress bar, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the progress bar, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Progress Bar Default Value",
    "api_name": "changeProgressBarDefaultValue",
    "description": "Modify the default value of a progress bar element. This function allows you to set the initial value for the progress bar, influencing its starting position.",
    "parameters": [
      {
        "name": "value",
        "description": "Specify the new default value for the progress bar."
      }
    ]
  },
  {
    "name": "change Progress Bar Validation",
    "api_name": "changeProgressBarValidation",
    "description": "Modify the validation criteria of a progress bar element. This function allows you to set minimum and maximum values for the progress bar, ensuring proper bounds.",
    "parameters": [
      {
        "name": "Minimum Value",
        "description": "Specify the new minimum value for the progress bar."
      },
      {
        "name": "Maximum Value",
        "description": "Specify the new maximum value for the progress bar."
      }
    ]
  },
  {
    "name": "change Progress Bar Behavior",
    "api_name": "changeProgressBarBehavior",
    "description": "Modify various behavioral aspects of a progress bar element. This function allows you to control the appearance and functionality of the progress bar by toggling options such as show, display format, and caption placement.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the progress bar."
      },
      {
        "name": "Display Format",
        "description": "Specify the display format for the progress bar value."
      },
      {
        "name": "Caption Placement",
        "description": "Specify the placement of the caption associated with the progress bar."
      }
    ]
  },
  {
    "name": "change Progress Bar Class Name",
    "api_name": "changeProgressBarClassName",
    "description": "Modify the CSS class name associated with a progress bar element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the progress bar.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the progress bar, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Progress Bar Display Style",
    "api_name": "changeProgressBarDisplayStyle",
    "description": "Modify the display style, including margin, of a progress bar element. This function enables customization of the progress bar's display properties, providing control over its spacing and layout within the user interface.",
    "parameters": [
      {
        "name": "Margin",
        "description": "Specify the new margin for the progress bar, influencing its spacing and placement within the layout. This allows for precise control over the progress bar's display."
      }
    ]
  },
  {
    "name": "change Progress Circle Title",
    "api_name": "changeProgressCircleTitle",
    "description": "Modify the title associated with a progress circle. This function allows you to update the displayed title text for a progress circle, enhancing user communication.",
    "parameters": [
      {
        "name": "title",
        "description": "The new title text for the progress circle."
      }
    ]
  },
  {
    "name": "change Progress Circle Subtitle",
    "api_name": "changeProgressCircleSubtitle",
    "description": "Modify the subtitle associated with a progress circle. This function allows you to update the displayed subtitle text for a progress circle, providing additional context or information.",
    "parameters": [
      {
        "name": "Subtitle",
        "description": "The new subtitle text for the progress circle."
      }
    ]
  },
  {
    "name": "change Progress Circle Name",
    "api_name": "changeProgressCircleName",
    "description": "Modify the name attribute of a progress circle element. This function enables you to update the identifier or name associated with a progress circle for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the progress circle."
      }
    ]
  },
  {
    "name": "change Progress Circle Type",
    "api_name": "changeProgressCircleType",
    "description": "Modify the type of a progress circle element. This function allows you to update the type or category of a progress circle, facilitating better classification.",
    "parameters": [
      {
        "name": "type",
        "description": "The new type or category for the progress circle."
      }
    ]
  },
  {
    "name": "change Progress Circle Layout",
    "api_name": "changeProgressCircleLayout",
    "description": "Adjust the size (width and height) of a progress circle element. This function enables fine-tuning of the progress circle dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the progress circle, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the progress circle, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Progress Circle Default Value",
    "api_name": "changeProgressCircleDefaultValue",
    "description": "Modify the default value of a progress circle element. This function allows you to set the initial value for the progress circle, influencing its starting position.",
    "parameters": [
      {
        "name": "Value",
        "description": "Specify the new default value for the progress circle."
      }
    ]
  },
  {
    "name": "change Progress Circle Validation",
    "api_name": "changeProgressCircleValidation",
    "description": "Modify the validation criteria of a progress circle element. This function allows you to set minimum and maximum values for the progress circle, ensuring proper bounds.",
    "parameters": [
      {
        "name": "Minimum Value",
        "description": "Specify the new minimum value for the progress circle."
      },
      {
        "name": "Maximum Value",
        "description": "Specify the new maximum value for the progress circle."
      }
    ]
  },
  {
    "name": "change Progress Circle Behavior",
    "api_name": "changeProgressCircleBehavior",
    "description": "Modify various behavioral aspects of a progress circle element. This function allows you to control the appearance and functionality of the progress circle by toggling options such as show, display format, and caption placement.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the progress circle."
      },
      {
        "name": "Display Format",
        "description": "Specify the display format for the progress circle value."
      },
      {
        "name": "Caption Placement",
        "description": "Specify the placement of the caption associated with the progress circle."
      }
    ]
  },
  {
    "name": "change Progress Circle Class Name",
    "api_name": "changeProgressCircleClassName",
    "description": "Modify the CSS class name associated with a progress circle element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the progress circle.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the progress circle, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Progress Circle Display Style",
    "api_name": "changeProgressCircleDisplayStyle",
    "description": "Modify the display style, including margin, of a progress circle element. This function enables customization of the progress circle's display properties, providing control over its spacing and layout within the user interface.",
    "parameters": [
      {
        "name": "Margin",
        "description": "Specify the new margin for the progress circle, influencing its spacing and placement within the layout. This allows for precise control over the progress circle's display."
      }
    ]
  },
  {
    "name": "change Chips Name",
    "api_name": "changeChipsName",
    "description": "Modify the name attribute of a chips element. This function enables you to update the identifier or name associated with chips for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the chips."
      }
    ]
  },
  {
    "name": "change Chips Placeholder",
    "api_name": "changeChipsPlaceholder",
    "description": "Modify the placeholder text of a chips element. This function enables you to update the temporary text displayed inside the chips input, providing additional context or instructions.",
    "parameters": [
      {
        "name": "placeholder",
        "description": "The new placeholder text for the chips input."
      }
    ]
  },
  {
    "name": "change Chips Layout",
    "api_name": "changeChipsLayout",
    "description": "Adjust the size (width and height) of a chips element. This function enables fine-tuning of the chips dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the chips, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the chips, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Chips Input Width",
    "api_name": "changeChipsInputWidth",
    "description": "Modify the width of the input area within a chips element. This function enables customization of the input area width, providing control over the space allocated for user input.",
    "parameters": [
      {
        "name": "Input Width",
        "description": "Specify the new width for the input area within the chips, influencing its dimensions."
      }
    ]
  },
  {
    "name": "change Chips Behavior",
    "api_name": "changeChipsBehavior",
    "description": "Modify various behavioral aspects of a chips element. This function allows you to control the appearance and functionality of the chips by toggling options such as auto-focus, read-only, max size, input position, allow only select, enable reorder, show, disabled, delay time (ms), and min chars.",
    "parameters": [
      {
        "name": "Auto Focus",
        "description": "Toggle auto-focus for the chips, automatically bringing it into focus upon page load."
      },
      {
        "name": "Read Only",
        "description": "Toggle read-only mode for the chips, preventing user interaction."
      },
      {
        "name": "Max Size",
        "description": "Specify the maximum size of the chips, limiting the number of selected items."
      },
      {
        "name": "Input Position",
        "description": "Specify the position of the input area within the chips."
      },
      {
        "name": "Allow Only Select",
        "description": "Toggle the option to allow only selected items in the chips."
      },
      {
        "name": "Enable Reorder",
        "description": "Toggle the ability to reorder items within the chips."
      },
      {
        "name": "Show",
        "description": "Toggle the visibility of the chips."
      },
      {
        "name": "Disabled",
        "description": "Disable user interaction with the chips."
      },
      {
        "name": "Delay Time (ms)",
        "description": "Specify the delay time for triggering events in milliseconds."
      },
      {
        "name": "Min Chars",
        "description": "Specify the minimum number of characters required for triggering events."
      }
    ]
  },
  {
    "name": "change Chips Class Name",
    "api_name": "changeChipsClassName",
    "description": "Modify the CSS class name associated with a chips element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the chips.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the chips, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Chips Background Style",
    "api_name": "changeChipsBackgroundStyle",
    "description": "Modify the background color of a chips element. This function enables customization of the chips background color, enhancing the visual presentation of the element.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new background color for the chips."
      }
    ]
  },
  {
    "name": "change Chips Display Style",
    "api_name": "changeChipsDisplayStyle",
    "description": "Modify the display style of a chips element. This function enables customization of the chips' overall style, providing control over its appearance.",
    "parameters": [
      {
        "name": "Style",
        "description": "Specify the new display style for the chips, influencing its visual presentation."
      }
    ]
  },
  {
    "name": "change Currency Name",
    "api_name": "changeCurrencyName",
    "description": "Modify the name attribute of a currency element. This function enables you to update the identifier or name associated with a currency for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the currency."
      }
    ]
  },
  {
    "name": "change Currency Layout",
    "api_name": "changeCurrencyLayout",
    "description": "Adjust the size (width and height) of a currency element. This function enables fine-tuning of the currency dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the currency, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the currency, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Currency Validation",
    "api_name": "changeCurrencyValidation",
    "description": "Modify the validation criteria of a currency element. This function allows you to specify whether the currency input is required, ensuring user input conformity.",
    "parameters": [
      {
        "name": "Required",
        "description": "Toggle the requirement for the currency input, making it mandatory for user interaction."
      }
    ]
  },
  {
    "name": "change Currency Behavior",
    "api_name": "changeCurrencyBehavior",
    "description": "Modify various behavioral aspects of a currency element. This function allows you to control the appearance and functionality of the currency by toggling options such as show.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the currency, influencing its display within the user interface."
      }
    ]
  },
  {
    "name": "change Currency Caption",
    "api_name": "changeCurrencyCaption",
    "description": "Modify the position of the caption associated with a currency element. This function allows you to specify the placement of the caption, providing flexibility in the visual arrangement.",
    "parameters": [
      {
        "name": "Position",
        "description": "Specify the new position for the currency caption, influencing its alignment within the element."
      }
    ]
  },
  {
    "name": "change Currency Format",
    "api_name": "changeCurrencyFormat",
    "description": "Modify the horizontal alignment of a currency element. This function allows you to control the alignment of the currency value within the element.",
    "parameters": [
      {
        "name": "Horizontal Align",
        "description": "Specify the new horizontal alignment for the currency, influencing its positioning within the element."
      }
    ]
  },
  {
    "name": "change Currency Class Name",
    "api_name": "changeCurrencyClassName",
    "description": "Modify the CSS class name associated with a currency element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the currency.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the currency, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Currency Text Style",
    "api_name": "changeCurrencyTextStyle",
    "description": "Modify various text style properties of a currency element. This function enables customization of the size, font family, color, and font style of the currency text.",
    "parameters": [
      {
        "name": "Size",
        "description": "Specify the new size for the currency text."
      },
      {
        "name": "Font Family",
        "description": "Specify the new font family for the currency text."
      },
      {
        "name": "Color",
        "description": "Specify the new color for the currency text."
      },
      {
        "name": "Font Style",
        "description": "Specify the new font style for the currency text."
      }
    ]
  },
  {
    "name": "change Currency Background Style",
    "api_name": "changeCurrencyBackgroundStyle",
    "description": "Modify various background style properties of a currency element. This function enables customization of the background color, repeat pattern, position, and size, enhancing the visual presentation of the currency.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new background color for the currency."
      },
      {
        "name": "Repeat",
        "description": "Specify the repeat pattern for the currency background."
      },
      {
        "name": "Position",
        "description": "Specify the position of the currency background within the element."
      },
      {
        "name": "Size",
        "description": "Specify the size of the currency background, influencing its dimensions."
      }
    ]
  },
  {
    "name": "change Currency Display Style",
    "api_name": "changeCurrencyDisplayStyle",
    "description": "Modify various display style properties of a currency element. This function enables customization of the padding and margin for the currency, influencing its overall appearance and spacing within the layout.",
    "parameters": [
      {
        "name": "Padding",
        "description": "Specify the new padding for the currency, influencing its internal spacing within the element."
      },
      {
        "name": "Margin",
        "description": "Specify the new margin for the currency, influencing its spacing and placement within the layout."
      }
    ]
  },
  {
    "name": "change Currency Placeholder",
    "api_name": "changeCurrencyPlaceholder",
    "description": "Modify the placeholder text of a currency element. This function enables you to update the temporary text displayed inside the currency input, providing additional context or instructions.",
    "parameters": [
      {
        "name": "placeholder",
        "description": "The new placeholder text for the currency input."
      }
    ]
  },
  {
    "name": "change Currency",
    "api_name": "changeCurrency",
    "description": "Modify the currency type associated with a currency element. This function allows you to update the currency type, providing flexibility in displaying different currency symbols.",
    "parameters": [
      {
        "name": "currency",
        "description": "The new currency type for the currency element."
      }
    ]
  },
  {
    "name": "change Switch Name",
    "api_name": "changeSwitchName",
    "description": "Modify the name attribute of a switch element. This function enables you to update the identifier or name associated with a switch for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the switch."
      }
    ]
  },
  {
    "name": "change Switch Layout",
    "api_name": "changeSwitchLayout",
    "description": "Adjust the size (width and height) of a switch element. This function enables fine-tuning of the switch dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the switch, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the switch, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Switch Validation",
    "api_name": "changeSwitchValidation",
    "description": "Modify the validation criteria of a switch element. This function allows you to specify whether the switch input is required, ensuring user input conformity.",
    "parameters": [
      {
        "name": "required",
        "description": "Toggle the requirement for the switch input, making it mandatory for user interaction."
      }
    ]
  },
  {
    "name": "change Switch Behavior",
    "api_name": "changeSwitchBehavior",
    "description": "Modify various behavioral aspects of a switch element. This function allows you to control the appearance and functionality of the switch by toggling options such as show and disabled.",
    "parameters": [
      {
        "name": "Show",
        "description": "Toggle the visibility of the switch."
      },
      {
        "name": "Disabled",
        "description": "Disable user interaction with the switch."
      }
    ]
  },
  {
    "name": "change Switch Graphics",
    "api_name": "changeSwitchGraphics",
    "description": "Modify the graphics associated with a switch element. This function allows you to update the visual representation or graphics associated with the switch.",
    "parameters": [
      {
        "name": "Graphics",
        "description": "Specify the new graphics for the switch, influencing its visual representation."
      }
    ]
  },
  {
    "name": "change Switch Class Name",
    "api_name": "changeSwitchClassName",
    "description": "Modify the CSS class name associated with a switch element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the switch.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the switch, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Switch Display",
    "api_name": "changeSwitchDisplay",
    "description": "Modify the display style, including margin, of a switch element. This function enables customization of the switch's display properties, providing control over its spacing and layout within the user interface.",
    "parameters": [
      {
        "name": "Margin",
        "description": "Specify the new margin for the switch, influencing its spacing and placement within the layout. This allows for precise control over the switch's display."
      }
    ]
  },
  {
    "name": "change Date Name",
    "api_name": "changeDateName",
    "description": "Modify the name attribute of a date element. This function enables you to update the identifier or name associated with a date for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the date."
      }
    ]
  },
  {
    "name": "change Date Placeholder",
    "api_name": "changeDatePlaceholder",
    "description": "Modify the placeholder text of a date element. This function enables you to update the temporary text displayed inside the date input, providing additional context or instructions.",
    "parameters": [
      {
        "name": "placeholder",
        "description": "The new placeholder text for the date input."
      }
    ]
  },
  {
    "name": "change Date Layout",
    "api_name": "changeDateLayout",
    "description": "Adjust the size (width) of a date element. This function enables fine-tuning of the date dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the date, influencing its horizontal dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Layout Name",
    "api_name": "changeLayoutName",
    "description": "Modify the name attribute of a layout element. This function enables you to update the identifier or name associated with a layout for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the layout."
      }
    ]
  },
  {
    "name": "change Layout Dimension",
    "api_name": "changeLayoutDimension",
    "description": "Adjust the size (width and height) of a layout element. This function enables fine-tuning of the layout dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the layout, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the layout, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Layout Class Name",
    "api_name": "changeLayoutClassName",
    "description": "Modify the CSS class name associated with a layout element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the layout.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the layout, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Accordion Name",
    "api_name": "changeAccordianName",
    "description": "Modify the name attribute of an accordion element. This function enables you to update the identifier or name associated with an accordion for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the accordion."
      }
    ]
  },
  {
    "name": "change Accordion Type",
    "api_name": "changeAccordianType",
    "description": "Modify the type of an accordion element. This function allows you to update the type or category of an accordion, facilitating better classification.",
    "parameters": [
      {
        "name": "type",
        "description": "The new type or category for the accordion."
      }
    ]
  },
  {
    "name": "change Accordion Layout",
    "api_name": "changeAccordianLayout",
    "description": "Adjust the height of an accordion element. This function enables fine-tuning of the accordion height, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "height",
        "description": "The new height for the accordion, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Accordion Class Name",
    "api_name": "changeAccordianClassName",
    "description": "Modify the CSS class name associated with an accordion element. This function provides the ability to update the styling by changing the class, enhancing the visual presentation of the accordion.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new CSS class name for the accordion, allowing for seamless integration with your styling preferences."
      }
    ]
  },
  {
    "name": "change Accordion Pane Text",
    "api_name": "changeAccordianPaneText",
    "description": "Modify the color of the text within accordion panes. This function allows you to update the color of text displayed within accordion panes, enhancing the visual presentation.",
    "parameters": [
      {
        "name": "color",
        "description": "Specify the new color for the text within accordion panes."
      }
    ]
  },
  {
    "name": "change Accordion Background",
    "api_name": "changeAccordianBackground",
    "description": "Modify the background color of an accordion element. This function enables customization of the accordion background color, enhancing the visual presentation of the element.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new background color for the accordion."
      }
    ]
  },
  {
    "name": "change Accordion Display",
    "api_name": "changeAccordianDisplay",
    "description": "Modify the padding of an accordion element. This function enables customization of the accordion's display properties, providing control over its spacing within the user interface.",
    "parameters": [
      {
        "name": "Padding",
        "description": "Specify the new padding for the accordion, influencing its spacing within the layout."
      }
    ]
  },
  {
    "name": "change Tab Name",
    "api_name": "changeTabName",
    "description": "Modify the name attribute of a tab element. This function enables you to update the identifier or name associated with a tab for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the tab."
      }
    ]
  },
  {
    "name": "change Tab Type",
    "api_name": "changeTabType",
    "description": "Modify the type of a tab element. This function allows you to update the type or category of a tab, facilitating better classification.",
    "parameters": [
      {
        "name": "type",
        "description": "The new type or category for the tab."
      }
    ]
  },
  {
    "name": "change Tab Layout",
    "api_name": "changeTabLayout",
    "description": "Adjust the size (height) and position of tabs within a tab container. This function enables fine-tuning of the tab dimensions and position, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Height",
        "description": "The new height for the tab, influencing its vertical dimensions within the tab container."
      },
      {
        "name": "Tabs Position",
        "description": "Specify the position of the tabs within the tab container."
      }
    ]
  },
  {
    "name": "change Tab Format",
    "api_name": "changeTabFormat",
    "description": "Modify the horizontal alignment and order of tabs within a tab container. This function allows you to control the alignment and order of tabs, influencing their positioning within the container.",
    "parameters": [
      {
        "name": "Horizontal Align",
        "description": "Specify the new horizontal alignment for the tabs within the tab container."
      },
      {
        "name": "Tab Order",
        "description": "Specify the new order for the tabs within the tab container."
      }
    ]
  },
  {
    "name": "change Wizard Name",
    "api_name": "changeWizardName",
    "description": "Modify the name attribute of a wizard element. This function enables you to update the identifier or name associated with a wizard for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the wizard."
      }
    ]
  },
  {
    "name": "change Wizard Caption for Steps",
    "api_name": "changeWizardCaptionforSteps",
    "description": "Modify the captions for various steps in a wizard. This function allows you to update the captions for next, previous, done, and cancel steps within the wizard, providing clear instructions to users.",
    "parameters": [
      {
        "name": "Next",
        "description": "Specify the new caption for the 'Next' step within the wizard."
      },
      {
        "name": "Previous",
        "description": "Specify the new caption for the 'Previous' step within the wizard."
      },
      {
        "name": "Done",
        "description": "Specify the new caption for the 'Done' step within the wizard."
      },
      {
        "name": "Cancel",
        "description": "Specify the new caption for the 'Cancel' step within the wizard."
      }
    ]
  },
  {
    "name": "change Wizard Layout",
    "api_name": "changeWizardLayout",
    "description": "Adjust the size (width and height), step style, actions alignment, and default step of a wizard element. This function enables fine-tuning of the wizard dimensions, step appearance, alignment of actions, and setting the default step.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the wizard, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the wizard, determining its vertical dimensions within the layout."
      },
      {
        "name": "Step Style",
        "description": "Specify the new style for the wizard steps, influencing their appearance."
      },
      {
        "name": "Actions Alignment",
        "description": "Specify the new alignment for the actions within the wizard."
      },
      {
        "name": "Default Step",
        "description": "Specify the default step for the wizard, determining the initial step displayed."
      }
    ]
  },
  {
    "name": "change Container Name",
    "api_name": "changecontainerName",
    "description": "Modify the name attribute of a container element. This function enables you to update the identifier or name associated with a container for better organization.",
    "parameters": [
      {
        "name": "name",
        "description": "The new identifier or name for the container."
      }
    ]
  },
  {
    "name": "change Container Layout",
    "api_name": "changecontainerLayout",
    "description": "Adjust the size (width and height) of a container element. This function enables fine-tuning of the container dimensions, allowing for a more customized and visually appealing layout.",
    "parameters": [
      {
        "name": "Width",
        "description": "The new width for the container, influencing its horizontal dimensions within the layout."
      },
      {
        "name": "Height",
        "description": "The new height for the container, determining its vertical dimensions within the layout."
      }
    ]
  },
  {
    "name": "change Container Text Style",
    "api_name": "changecontainerTextStyle",
    "description": "Modify various text style properties of a container element. This function enables customization of the size, font family, color, and font style of the text within the container.",
    "parameters": [
      {
        "name": "Size",
        "description": "Specify the new size for the text within the container."
      },
      {
        "name": "Font Family",
        "description": "Specify the new font family for the text within the container."
      },
      {
        "name": "Color",
        "description": "Specify the new color for the text within the container."
      },
      {
        "name": "Font Style",
        "description": "Specify the new font style for the text within the container."
      }
    ]
  },
  {
    "name": "change Container Background Style",
    "api_name": "changecontainerBackgroundstyle",
    "description": "Modify various background style properties of a container element. This function enables customization of the background color, repeat pattern, position, size, and image, enhancing the visual presentation of the container.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new background color for the container."
      },
      {
        "name": "Repeat",
        "description": "Specify the repeat pattern for the container background."
      },
      {
        "name": "Position",
        "description": "Specify the position of the container background within the element."
      },
      {
        "name": "Size",
        "description": "Specify the size of the container background, influencing its dimensions."
      },
      {
        "name": "Image",
        "description": "Specify the image for the container background, enhancing its visual appeal."
      }
    ]
  },
  {
    "name": "change Container Border Style",
    "api_name": "changecontainerBorderstyle",
    "description": "Modify various border style properties of a container element. This function enables customization of the border color, style, and width, enhancing the visual presentation of the container.",
    "parameters": [
      {
        "name": "Color",
        "description": "Specify the new border color for the container."
      },
      {
        "name": "Style",
        "description": "Specify the new border style for the container."
      },
      {
        "name": "Border Width",
        "description": "Specify the new border width for the container, influencing its thickness."
      }
    ]
  },
  {
    "name": "change Container Display Style",
    "api_name": "changecontainerDisplayStyle",
    "description": "Modify various display style properties of a container element. This function enables customization of the padding, margin, and opacity for the container, influencing its overall appearance and spacing within the layout.",
    "parameters": [
      {
        "name": "Padding",
        "description": "Specify the new padding for the container, influencing its internal spacing within the element."
      },
      {
        "name": "Margin",
        "description": "Specify the new margin for the container, influencing its spacing and placement within the layout."
      },
      {
        "name": "Opacity",
        "description": "Specify the new opacity for the container, influencing its transparency."
      }
    ]
  }
]

#qdrant = QdrantClient(host="localhost", port=6333)

#qdrant.recreate_collection(
#    collection_name="FunctionCalling",
#    vectors_config=models.VectorParams(
#        size=encoder.get_sentence_embedding_dimension(),  
#        distance=models.Distance.DOT,
#    ),
#)


#qdrant.upload_records(
#        collection_name="FunctionCalling",
#    records=[
#        models.Record(
#            id=idx, vector=encoder.encode( doc["description"]).tolist(), payload=doc
#        )
#        for idx, doc in enumerate(documents)
#    ],
#)


#hits = qdrant.search(
#    collection_name="functioncalling",
#    query_vector=encoder.encode("change the button color to the Green").tolist(),
#    limit=20,
#)
#for hit in hits:
#    print(hit.payload["api_name"])
