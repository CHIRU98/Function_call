import json
import torch

torch.cuda.empty_cache()

from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


app = Flask(__name__)

def get_prompt(user_query: str, functions: list = []) -> str:
    if len(functions) == 0:
        return f"USER: <<question>> {user_query}\nASSISTANT: "
    functions_string = json.dumps(functions)
    return f"USER: <<question>> {user_query} <<function>> {functions_string}\nASSISTANT: "


# Device setup
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

print("device",device)

# Model and tokenizer setup
model_id = "gorilla-llm/gorilla-openfunctions-v1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch_dtype)
print("starting model push to gpu")
model.to(device)
print("model loaded in device")

# Pipeline setup
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    batch_size=16,
    torch_dtype=torch_dtype,
    device=device,
)

###############
labelCaption = [
  {
    "name": "change Label Value",
    "api_name": "changeLabelCaption",
    "description": "The 'Change Label Caption' function is used to modify the caption provided by the user.",
    "parameters": [
      {
        "name": "caption",
        "description": "The caption the user wants to change for the label."
      }
    ]
  }
]

LabelCaptionName = [
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
  }
]
 
changeLabelLayout = [
  {
    "name": "change Label Layout",
    "api_name": "changeLabelLayout",
    "description": "Adjust the layout of the label using this function.",
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
  }]

LabelValidation =[{
    "name": "change Label Validation",
    "api_name": "changeLabelValidation",
    "description": "Modify validation settings for the label using this function.",
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
  }
  ]
LabelBehaviour = [{
    "name": "change Label Behaviour",
    "api_name": "changeLabelBehaviour",
    "description": "Alters the behavior of the label with this function.",
    "parameters": [
      {
        "name": "show",
        "description": "Set to true to display the label; set to false to hide it."
      }
    ]
  }
  ]

LabelClassName=  [{
    "name": "change Label ClassName",
    "api_name": "changeLabelClassName",
    "description": "Change the class name associated with the label.",
    "parameters": [
      {
        "name": "name",
        "description": "Specify the new class name for the label."
      }
    ]
  }
]

LabelTextStyle = [{
  "name": "change Label Text Style",
  "api_name": "changeLabelTextStyle",
  "description": "Modify the text style of the label using this function.",
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
}
]

LabelBackgroundStyle = [{
  "name": "change Label Background Style",
  "api_name": "changeLabelBackgroundStyle",
  "description": "Adjust the background style of the label using this function.",
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
}
]

LabelBorderStyle = [{
  "name": "change Label Border Style",
  "api_name": "changeLabelBorderStyle",
  "description": "Adjust the border style of the label using this function.",
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
}
]

LabelDisplayStyle = [{
  "name": "change Label Display Style",
  "api_name": "changeLabelDisplayStyle",
  "description": "Modify the display style (padding and margin) of the label using this function.",
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
}
]

LabelMouseEvents = [{
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
}
]

LabelTouchEvents = [{
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
}
]

LabelDeviceSizes = [{
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
}
]

AnchorCaption = [{
  "name": "change Anchor Caption",
  "api_name": "changeAnchorCaption",
  "description": "Modify the caption of the anchor using this function.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the anchor."
    }
  ]
}
]

AnchorName = [{
  "name": "change Anchor Name",
  "api_name": "changeAnchorName",
  "description": "Change the name associated with the anchor.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the anchor."
    }
  ]
}
]

AnchorBadgeValue = [{
  "name": "change Anchor Badge Value",
  "api_name": "changeAnchorBadgeValue",
  "description": "Set the badge value for the anchor.",
  "parameters": [
    {
      "name": "value",
      "description": "The new badge value for the anchor."
    }
  ]
}
]

AnchorAccessibility = [{
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
}
]
AnchorLayout = [{
  "name": "change Anchor Layout",
  "api_name": "changeAnchorLayout",
  "description": "Adjust the layout of the anchor.",
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
}
]
AnchorBehavior = [{
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
}
]
AnchorGraphics = [{
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
}
]
AnchorClassName = [{
  "name": "change Anchor ClassName",
  "api_name": "changeAnchorClassName",
  "description": "Change the class name associated with the anchor.",
  "parameters": [
    {
      "name": "name",
      "description": "The new class name for the anchor."
    }
  ]
}
]
AnchorTextStyle = [{
  "name": "change Anchor Text Style",
  "api_name": "changeAnchorTextStyle",
  "description": "Modify the text style of the anchor.",
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
}
]
AnchorBackgroundStyle = [{
  "name": "change Anchor Background Style",
  "api_name": "changeAnchorBackgroundStyle",
  "description": "Adjust the background style of the anchor.",
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
}
]
AnchorBorderStyle = [{
  "name": "change Anchor Border Style",
  "api_name": "changeAnchorBorderStyle",
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
}
]

ButtonCaption = [{
  "name": "change Button Caption",
  "api_name": "changeButtonCaption",
  "description": "Modify the caption of the button using this function.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the button."
    }
  ]
}
]
ButtonName = [{
  "name": "change Button Name",
  "api_name": "changeButtonName",
  "description": "Change the name associated with the button.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the button."
    }
  ]
}
]
ButtonType = [{
  "name": "change Button Type",
  "api_name": "changeButtonType",
  "description": "Change the type of the button.",
  "parameters": [
    {
      "name": "type",
      "description": "The new type for the button."
    }
  ]
}
]
ButtonBadgeValue = [{
  "name": "change Button Badge Value",
  "api_name": "changeButtonBadgeValue",
  "description": "Set the badge value for the button.",
  "parameters": [
    {
      "name": "value",
      "description": "The new badge value for the button."
    }
  ]
}
]

ButtonLayout = [{
  "name": "change Button Layout",
  "api_name": "changeButtonLayout",
  "description": "Adjust the layout of the button.",
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
}
]

ButtonBehavior = [{
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
}
]
ButtonClass = [{
  "name": "change Button Class",
  "api_name": "changeButtonClass",
  "description": "Change the class name associated with the button.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the button."
    }
  ]
}
]
ButtonTextStyle = [{
  "name": "change Button Text Style",
  "api_name": "changeButtonTextStyle",
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
}
]
ButtonBackgroundStyle = [{
  "name": "change Button Background Style",
  "api_name": "changeButtonBackgroundStyle",
  "description": "Adjust the background style of the button.",
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
}
]
ButtonBorderStyle = [{
  "name": "change Button Border Style",
  "api_name": "changeButtonBorderStyle",
  "description": "Adjust the border style of the button.",
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
}
]
ButtonDisplayStyle = [{
  "name": "change Button Display Style",
  "api_name": "changeButtonDisplayStyle",
  "description": "Modify the display style (padding and margin) of the button.",
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
}
]
ButtonOnFocus = [{
  "name": "change Button On Focus",
  "api_name": "changeButtonOnFocus",
  "description": "Specify the action to be taken when the button is focused.",
  "parameters": [
    {
      "name": "text",
      "description": "The action or text to be associated with the button's focus event."
    }
  ]
}
]
ButtonOnBlur = [{
  "name": "change Button On Blur",
  "api_name": "changeButtonOnBlur",
  "description": "Specify the action to be taken when the button loses focus.",
  "parameters": [
    {
      "name": "text",
      "description": "The action or text to be associated with the button's blur event."
    }
  ]
}
]
ButtonMouseEvents = [{
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
}
]
ButtonTouchEvents = [{
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
}
]
KeyboardEvents = [{
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
}
]

IconCaption = [{
  "name": "change Icon Caption",
  "api_name": "changeIconCaption",
  "description": "Modify the caption of the icon using this function.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the icon."
    }
  ]
}
]
IconName = [{
  "name": "change Icon Name",
  "api_name": "changeIconName",
  "description": "Change the name associated with the icon.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the icon."
    }
  ]
}
]
IconBehavior = [{
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
}
]

IconClass = [{
  "name": "change Icon Class",
  "api_name": "changeIconClass",
  "description": "Change the class name associated with the icon.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the icon."
    }
  ]
}
]
IconTextStyle = [{
  "name": "change Icon Text Style",
  "api_name": "changeIconTextStyle",
  "description": "Modify the text style of the icon.",
  "parameters": [
    {
      "name": "color",
      "description": "Define the color of the icon text."
    }
  ]
}
]
IconDisplayStyle = [{
  "name": "change Icon Display Style",
  "api_name": "changeIconDisplayStyle",
  "description": "Modify the display style (opacity) of the icon.",
  "parameters": [
    {
      "name": "opacity",
      "description": "Set the opacity for the icon."
    }
  ]
}
]

IconDeviceSizes = [{
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
}
]
PictureName = [{
  "name": "change Picture Name",
  "api_name": "changePictureName",
  "description": "Change the name associated with the picture.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the picture."
    }
  ]
}
]
PictureTabIndex = [{
  "name": "change Picture Tab Index",
  "api_name": "changePictureTabIndex",
  "description": "Set the tab index for the picture.",
  "parameters": [
    {
      "name": "value",
      "description": "The tab index value for the picture."
    }
  ]
}
]
PictureAspect = [{
  "name": "change Picture Aspect",
  "api_name": "changePictureAspect",
  "description": "Set the aspect ratio for the picture.",
  "parameters": [
    {
      "name": "aspect",
      "description": "Specify the aspect ratio for the picture (Both, H, V)."
    }
  ]
}
]
PictureShape = [{
  "name": "change Picture Shape",
  "api_name": "changePictureShape",
  "description": "Set the shape of the picture.",
  "parameters": [
    {
      "name": "shape",
      "description": "Specify the shape of the picture (rounded, circle, thumbnail)."
    }
  ]
}
]
PictureLayout = [{
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
}
]
PictureBehavior = [{
  "name": "change Picture Behavior",
  "api_name": "changePictureBehavior",
  "description": "Modify the behavior of the picture.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the picture; set to false to hide it."
    }
  ]
}
]
PictureClassName = [{
  "name": "change Picture ClassName",
  "api_name": "changePictureClassName",
  "description": "Change the class name associated with the picture.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the picture."
    }
  ]
}
]
PictureBackground = [{
  "name": "change Picture Background",
  "api_name": "changePictureBackground",
  "description": "Modify the background style of the picture.",
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
}
]
PictureBorder = [{
  "name": "change Picture Border",
  "api_name": "changePictureBorder",
  "description": "Modify the border style of the picture.",
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
}
]
PictureDisplayStyle = [{
  "name": "change Picture Display Style",
  "api_name": "changePictureDisplayStyle",
  "description": "Modify the display style (padding and margin) of the picture.",
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
}
]
PictureMouseEvents = [{
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
}
]
PictureTouchEvents = [{
  "name": "change Picture Touch Events",
  "api_name": "changePictureTouchEvents",
  "description": "Modify touch events for the picture.",
  "parameters": [
    {
      "name": "onTap",
      "description": "Specify the action to be taken on a tap event."
    }
  ]
}
]
PictureDeviceSizes = [{
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
}
]
changeTreeClassName = [{
  "name": "change Tree ClassName",
  "api_name": "changeTreeClassName",
  "description": "Change the class name associated with the tree.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the tree."
    }
  ]
}
]
TreeTextStyle = [{
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
}
]
TreeBackgroundStyle = [{
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
}
]

TreeBorderStyle = [{
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
}
]
TreeDisplayStyle = [{
  "name": "change Tree Display Style",
  "api_name": "changeTreeDisplayStyle",
  "description": "Modify the display style (padding) of the tree.",
  "parameters": [
    {
      "name": "padding",
      "description": "Specify the padding for the tree."
    }
  ]
}
]
TreeName = [{
  "name": "change Tree Name",
  "api_name": "changeTreeName",
  "description": "Change the name associated with the tree.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the tree."
    }
  ]
}
]
TreeLayout = [{
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
}
]
TreeBehavior = [{
  "name": "change Tree Behavior",
  "api_name": "changeTreeBehavior",
  "description": "Modify the behavior of the tree.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the tree; set to false to hide it."
    }
  ]
}
]
TreeFormat = [{
  "name": "change Tree Format",
  "api_name": "changeTreeFormat",
  "description": "Specify the horizontal alignment for the tree.",
  "parameters": [
    {
      "name": "horizontalAlign",
      "description": "Specify the horizontal alignment for the tree (e.g., left, center, right)."
    }
  ]
}
]
TreeCallbackEvents = [{
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
}
]

TextName = [{
  "name": "change Text Name",
  "api_name": "changeTextName",
  "description": "Change the name associated with the text.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the text."
    }
  ]
}
]
TextLayout = [{
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
}
]
TextValidation = [{
  "name": "change Text Validation",
  "api_name": "changeTextValidation",
  "description": "Specify validation settings for the text.",
  "parameters": [
    {
      "name": "required",
      "description": "Set to true to make the text required for validation."
    }
  ]
}
]
TextBehavior = [{
  "name": "change Text Behavior",
  "api_name": "changeTextBehavior",
  "description": "Modify the behavior of the text.",
  "parameters": [
    {
      "name": "show",
      "description": "Set to true to display the text; set to false to hide it."
    }
  ]
}
]
TextCaption = [{
  "name": "change Text Caption",
  "api_name": "changeTextCaption",
  "description": "Specify the position of the text caption.",
  "parameters": [
    {
      "name": "position",
      "description": "Specify the position for the text caption (e.g., top, bottom, left, right)."
    }
  ]
}
]
TextFormat = [{
  "name": "change Text Format",
  "api_name": "changeTextFormat",
  "description": "Specify the horizontal alignment for the text.",
  "parameters": [
    {
      "name": "horizontalAlign",
      "description": "Specify the horizontal alignment for the text (e.g., left, center, right)."
    }
  ]
}
]
TextClassName = [{
  "name": "change Text ClassName",
  "api_name": "changeTextClassName",
  "description": "Change the class name associated with the text.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the text."
    }
  ]
}
]
TextTextStyle = [{
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
}
]
TextBackgroundStyle = [{
  "name": "change Text Background Style",
  "api_name": "changeTextBackgroundStyle",
  "description": "Modify the background style of the text.",
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
}
]
TextDisplayStyle = [{
  "name": "change Text Display Style",
  "api_name": "changeTextDisplayStyle",
  "description": "Modify the display style (padding and margin) of the text.",
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
}
]
NumberName = [{
  "name": "change Number Name",
  "api_name": "changeNumberName",
  "description": "Change the name associated with the number input.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the number input."
    }
  ]
}
]

NumberPlaceholder = [{
  "name": "change Number Placeholder",
  "api_name": "changeNumberPlaceholder",
  "description": "Set the placeholder text for the number input.",
  "parameters": [
    {
      "name": "placeholder",
      "description": "The placeholder text for the number input."
    }
  ]
}
]
NumberLayout = [{
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
}
]
TextAreaName = [{
  "name": "change Text Area Name",
  "api_name": "changeTextAreaName",
  "description": "Change the name associated with the text area.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the text area."
    }
  ]
}
]
TextAreaPlaceholder = [{
  "name": "change Text Area Placeholder",
  "api_name": "changeTextAreaPlaceholder",
  "description": "Set the placeholder text for the text area.",
  "parameters": [
    {
      "name": "placeholder",
      "description": "The placeholder text for the text area."
    }
  ]
}
]
TextAreaLayout = [{
  "name": "change Text Area Layout",
  "api_name": "changeTextAreaLayout",
  "description": "Adjust the layout of the text area.",
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
}
]
TextAreaBehavior = [{
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
}
]
TextAreaClassName = [{
  "name": "change Text Area ClassName",
  "api_name": "changeTextAreaClassName",
  "description": "Change the class name associated with the text area.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the text area."
    }
  ]
}
]
TextAreaTextStyle = [{
  "name": "change Text Area Text Style",
  "api_name": "changeTextAreaTextStyle",
  "description": "Modify the text style of the text area.",
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
}
]
TextAreaBackgroundStyle = [{
  "name": "change Text Area Background Style",
  "api_name": "changeTextAreaBackgroundStyle",
  "description": "Modify the background style of the text area.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the text area."
    }
  ]
}
]

SelectName = [{
  "name": "change Select Name",
  "api_name": "changeSelectName",
  "description": "Change the name associated with the select input.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the select input."
    }
  ]
}
]
SelectPlaceholder = [{
  "name": "change Select Placeholder",
  "api_name": "changeSelectPlaceholder",
  "description": "Set the placeholder text for the select input.",
  "parameters": [
    {
      "name": "placeholder",
      "description": "The placeholder text for the select input."
    }
  ]
}
]
SelectLayout = [{
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
}
]
SelectClassName = [{
  "name": "change Select ClassName",
  "api_name": "changeSelectClassName",
  "description": "Change the class name associated with the select input.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the select input."
    }
  ]
}
]
SelectTextStyle = [{
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
}
]
SelectBackgroundStyle = [{
  "name": "change Select Background Style",
  "api_name": "changeSelectBackgroundStyle",
  "description": "Modify the background style of the select input.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the select input."
    }
  ]
}
]
SelectDisplayStyle = [{
  "name": "change Select Display Style",
  "api_name": "changeSelectDisplayStyle",
  "description": "Modify the display style (margin) of the select input.",
  "parameters": [
    {
      "name": "margin",
      "description": "Specify the margin for the select input."
    }
  ]
}
]
RadiosetName = [{
  "name": "change Radioset Name",
  "api_name": "changeRadiosetName",
  "description": "Change the name associated with the radioset.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the radioset."
    }
  ]
}
]
RadiosetLayout = [{
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
}
]
RadiosetCaption = [{
  "name": "change Radioset Caption",
  "api_name": "changeRadiosetCaption",
  "description": "Specify the position of the radioset caption.",
  "parameters": [
    {
      "name": "position",
      "description": "Specify the position for the radioset caption (e.g., top, bottom, left, right)."
    }
  ]
}
]
RadiosetFormat = [{
  "name": "change Radioset Format",
  "api_name": "changeRadiosetFormat",
  "description": "Specify the horizontal alignment for the radioset.",
  "parameters": [
    {
      "name": "horizontalAlign",
      "description": "Specify the horizontal alignment for the radioset (e.g., left, center, right)."
    }
  ]
}
]
RadiosetClassName = [{
  "name": "change Radioset ClassName",
  "api_name": "changeRadiosetClassName",
  "description": "Change the class name associated with the radioset.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the radioset."
    }
  ]
}
]
RadiosetTextStyle = [{
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
}
]
RadiosetBackgroundStyle = [{
  "name": "change Radioset Background Style",
  "api_name": "changeRadiosetBackgroundStyle",
  "description": "Modify the background style of the radioset.",
  "parameters": [
    {
      "name": "color",
      "description": "Specify the background color for the radioset."
    }
  ]
}
]
RadiosetDisplayStyle = [{
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
}
]
CheckBoxCaption =[{
  "name": "change Checkbox Caption",
  "api_name": "changeCheckBoxCaption",
  "description": "Change the caption associated with the checkbox.",
  "parameters": [
    {
      "name": "caption",
      "description": "The new caption for the checkbox."
    }
  ]
}
]
CheckBoxName = [{
  "name": "change Checkbox Name",
  "api_name": "changeCheckBoxName",
  "description": "Change the name associated with the checkbox.",
  "parameters": [
    {
      "name": "name",
      "description": "The new name for the checkbox."
    }
  ]
}
]
CheckBoxLayout = [{
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
}
]
CheckBoxClassName = [{
  "name": "change Checkbox ClassName",
  "api_name": "changeCheckBoxClassName",
  "description": "Change the class name associated with the checkbox.",
  "parameters": [
    {
      "name": "className",
      "description": "The new class name for the checkbox."
    }
  ]
}
]
CheckBoxDisplayStyle = [{
  "name": "change Checkbox Display Style",
  "api_name": "changeCheckBoxDisplayStyle",
  "description": "Modify the display style (margin) of the checkbox.",
  "parameters": [
    {
      "name": "margin",
      "description": "Specify the margin for the checkbox."
    }
  ]
}
]

functions = [labelCaption,LabelCaptionName,changeLabelLayout,LabelValidation,LabelBehaviour,LabelClassName,LabelTextStyle,LabelBackgroundStyle,LabelBorderStyle,LabelDisplayStyle,LabelMouseEvents,LabelTouchEvents,LabelDeviceSizes,AnchorCaption,AnchorName,AnchorBadgeValue,AnchorAccessibility,AnchorLayout,AnchorBehavior,AnchorGraphics,AnchorClassName,AnchorTextStyle,AnchorBackgroundStyle,AnchorBorderStyle,ButtonCaption,ButtonName,ButtonType,ButtonBadgeValue,ButtonLayout,ButtonBehavior,ButtonClass,ButtonTextStyle,ButtonBackgroundStyle,ButtonBorderStyle,ButtonDisplayStyle,ButtonOnFocus,ButtonOnBlur,ButtonMouseEvents,ButtonTouchEvents,KeyboardEvents,IconCaption,IconName,IconBehavior,IconClass,IconTextStyle,IconDisplayStyle,IconDeviceSizes,PictureName,PictureTabIndex,PictureAspect,PictureShape,PictureLayout,PictureBehavior,PictureClassName,PictureBackground,PictureBorder,PictureDisplayStyle,PictureMouseEvents,PictureTouchEvents,PictureDeviceSizes,changeTreeClassName,TreeTextStyle,TreeBackgroundStyle,TreeBorderStyle,TreeDisplayStyle,TreeName,TreeLayout,TreeBehavior,TreeFormat,TreeCallbackEvents,TextName,TextLayout,TextValidation,TextBehavior,TextCaption,TextFormat,TextClassName,TextTextStyle,TextBackgroundStyle,TextDisplayStyle,NumberName,NumberPlaceholder,NumberLayout,TextAreaName,TextAreaPlaceholder,TextAreaLayout,TextAreaBehavior,TextAreaClassName,TextAreaTextStyle,TextAreaBackgroundStyle,SelectName,SelectPlaceholder,SelectLayout,SelectClassName,SelectTextStyle,SelectBackgroundStyle,SelectDisplayStyle,RadiosetName,RadiosetLayout,RadiosetCaption,RadiosetFormat,RadiosetClassName,RadiosetTextStyle,RadiosetBackgroundStyle,RadiosetDisplayStyle,CheckBoxCaption,CheckBoxName,CheckBoxLayout,CheckBoxClassName,CheckBoxDisplayStyle]
#################
@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/generate_prompt',methods=['POST'])
def generate_prompt():
    data = request.get_json()
    query = data.get('query')
    prompt = get_prompt(query, functions=functions)
    output = pipe(prompt)
    result = output[0]["generated_text"]
    response = result.split('ASSISTANT:')[1].strip()
    return jsonify({"output": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)



