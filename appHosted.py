##This code is about the Model hosted by the author on the "http://luigi.millennium.berkeley.edu:8000/v1".

import openai
def get_gorilla_response(prompt, functions):
    openai.api_key = "EMPTY"
    openai.api_base = "http://luigi.millennium.berkeley.edu:8000/v1"
    try:
        completion = openai.ChatCompletion.create(
        model="gorilla-openfunctions-v1",
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
        functions=functions,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(e, prompt)

buttonType = [
    {
        "name": "change_Button_Type",
        "api_name": "changeButtonType",
        "description": " It will get the type of the button from the user provided query and it will not return the color,it returns only the type.For Ex-Primary,Secondary,Danger,etc",
        "parameters":  [
                        {
                            "name": "type", 
                            "description": "It's type of the Button.For ex-Primary,Secondary,Danger,etc"
                        }
                        ]
    }
]

buttonColor = [
    {
        "name": "change_Button_Color",
        "api_name": "changeButtonColor",
        "description": "It will get the color of the button from the user provided query and it will change the color of the Button.For Ex colors are-Green,red,Green,etc",
        "parameters":  [
                        {
                            "name": "Color", 
                            "description": "It's type of the Button and change the Color of the Button.For Ex-Green,Blue."
                        }
                        ]
    }
]
buttonSize = [
    {
        "name": "change_Button_Size",
        "api_name": "changeButtonSize",
        "description": "changeButtonSize will change the button size based on the user provided query.For Ex-small,medium,large,etc",
        "parameters":  [
                        {
                            "name": "size", 
                            "description": "It's size of the Button and change the size of the Button."
                        }
                        ]
    }
]

buttonCaption = [
    {
        "name": "change_Button_Caption",
        "api_name": "chageButtonCaption",
        "description": "chageButtonCaption is change the caption of the button based on the user provided querya and it will returns the button caption.",
        "parameters":  [
                        {
                            "name": "caption", 
                            "description": "It's caption of the Button."
                        }
                        ]
    }
]
buttonBorderColor = [
    {
        "name": "change_Button_Border_Color",
        "api_name": "changeButtonBorderColor",
        "description": "It will change the button border color for the given user query and return the color",
        "parameters":  [
                        {
                            "name": "bordercolor", 
                            "description": "It's border color of the Button."
                        }
                        ]
    }
]

buttonPosition = [
    {
        "name": "change_Button_Position",
        "api_name": "changeButtonPosition",
        "description": "It will change the button position based on the user provided query and returns the position.",
        "parameters":  [
                        {
                            "name": "position", 
                            "description": "It's border color of the Button."
                        }
                        ]
    }
]
buttonSize = [
    {
        "name": "change_Button_Size",
        "api_name": "changeButtonSize",
        "description": "Change the size of the Button",
        "parameters": [
            {
                "name": "size",
                "description": "It's the size of the Button."
            }
        ]
    }
]
buttonClassName = [
    {
        "name": "change_Button_Class_Name",
        "api_name": "changeButtonClassName",
        "description": "Change the class name of the Button.",
        "parameters": [
            {
                "name": "name",
                "description": "Specifies the new class name for the Button. This allows applying custom styles."
            }
        ]
    }
]
buttonTextColor = [
    {
        "name": "change_Button_Text_Color",
        "api_name": "changeButtonTextColor",
        "description": "Change the text color of the Button.",
        "parameters": [
            {
                "name": "color",
                "description": "Specifies the new text color for the Button. Use valid color codes or names."
            }
        ]
    }
]
buttonFont = [
    {
        "name": "change_Button_Font",
        "api_name": "changeButtonFont",
        "description": "Change the font of the Button.",
        "parameters": [
            {
                "name": "type",
                "description": "Specifies the new font type for the Button. Use values like 'Arial', 'Helvetica', 'Times New Roman', etc."
            }
        ]
    }
]
buttonTextAlign = [
    {
        "name": "change_Button_Text_Align",
        "api_name": "changeButtonTextAlign",
        "description": "Change the text alignment of the Button.",
        "parameters": [
            {
                "name": "align",
                "description": "Specifies the new text alignment for the Button. Use values like 'left', 'center', 'right', etc."
            }
        ]
    }
]
labelName = [
    {
        "name": "change_Label_Name",
        "api_name": "changeLabelName",
        "description": "Change the name of the Label",
        "parameters": [
            {
                "name": "name",
                "description": "Specifies the new name for the Label."
            }
        ]
    }
]
labelLayout = [
    {
        "name": "change_Label_Layout",
        "api_name": "changeLabelLayout",
        "description": "Change the layout (height and width) of the Label.",
        "parameters": [
            {
                "name": "height",
                "description": "Specifies the new height for the Label."
            },
            {
                "name": "width",
                "description": "Specifies the new width for the Label."
            }
        ]
    }
]
labelCaptionPosition = [
    {
        "name": "change_Label_Caption_Position",
        "api_name": "changeLabelCaptionPosition",
        "description": "Change the caption position of the Label.",
        "parameters": [
            {
                "name": "position",
                "description": "Specifies the new caption position for the Label. Use values like 'top', 'bottom', 'left', 'right', etc."
            }
        ]
    }
]
labelTextSize = [
    {
        "name": "change_Label_Text_Size",
        "api_name": "changeLabelTextSize",
        "description": "Change the text size of the Label.",
        "parameters": [
            {
                "name": "size",
                "description": "Specifies the new text size for the Label."
            }
        ]
    }
]
labelTextColor = [
    {
        "name": "change_Label_Text_Color",
        "api_name": "changeLabelTextColor",
        "description": "Change the text color of the Label.",
        "parameters": [
            {
                "name": "color",
                "description": "Specifies the new text color for the Label. Use valid color codes or names."
            }
        ]
    }
]
labelBackgroundColor = [
    {
        "name": "change_Label_Background_Color",
        "api_name": "changeLabelBackgroundColor",
        "description": "It will change the background color of the label based on the user provided query and it will returns the color and parameters should be color",
        "parameters": [
            {
                "name": "color",
                "description": "Specifies the new background color for the Label. Use valid color codes or names."
            }
        ]
    }
]
labelPosition = [
    {
        "name": "change_Label_Position",
        "api_name": "changeLabelPosition",
        "description": "Change the position of the Label.",
        "parameters": [
            {
                "name": "position",
                "description": "Specifies the new position for the Label. Use values like 'relative', 'absolute', 'fixed', etc."
            }
        ]
    }
]
buttonName = [
  {
    "name": "change_Button_Name",
    "api_name": "changeButtonName",
    "description": "It will change the name of the button.",
    "parameters": [
      {
        "name": "name",
        "description": "The new name for the button."
      }
    ]
  }
]

buttonBadgeValue = [
  {
    "name": "change_Badge_Value",
    "api_name": "changeBadgeValue",
    "description": "It will change the badge value of the button.",
    "parameters": [
      {
        "name": "value",
        "description": "The new value for the badge."
      }
    ]
  }
]

buttonLayout = [
  {
    "name": "change_Button_Layout",
    "api_name": "changeButtonLayout",
    "description": "It will change the layout of the button.",
    "parameters": [
      {
        "name": "width",
        "description": "The new width for the button."
      },
      {
        "name": "height",
        "description": "The new height for the button."
      }
    ]
  }
]

buttonAnimation=[
  {
    "name": "change_Button_Animation",
    "api_name": "changeButtonAnimation",
    "description": "It will change the animation of the button.",
    "parameters": [
      {
        "name": "animation",
        "description": "The new animation for the button."
      }
    ]
  }
]

buttonClass = [
  {
    "name": "change_Button_Class",
    "api_name": "changeButtonClass",
    "description": "It will change the class of the button.",
    "parameters": [
      {
        "name": "type",
        "description": "The new class type for the button."
      }
    ]
  }
]

buttonFontStyle=[
  {
    "name": "change_Button_Font_Style",
    "api_name": "changeButtonFontStyle",
    "description": "It will change the font style of the button.",
    "parameters": [
      {
        "name": "type",
        "description": "The new font style type for the button."
      }
    ]
  }
]

buttonBackgroundColor = [
  {
    "name": "change_Button_Background_Color",
    "api_name": "changeButtonBackgroundColor",
    "description": "It will change the background color of the button.",
    "parameters": [
      {
        "name": "color",
        "description": "The new background color for the button."
      }
    ]
  }
]
query = "change button color to the Blue"
func = [buttonType,buttonColor,buttonSize,buttonCaption,buttonBorderColor,buttonType,buttonColor,buttonSize,buttonCaption,buttonBorderColor,buttonPosition,buttonSize,buttonClassName,buttonTextColor,buttonFont,buttonTextAlign,labelName,labelLayout,labelCaptionPosition,labelTextSize,labelTextColor,labelBackgroundColor,labelPosition,buttonName,buttonBadgeValue,buttonLayout,buttonAnimation,buttonClass,buttonFontStyle,buttonBackgroundColor]
res = get_gorilla_response(query, functions=func)
print(res)

















