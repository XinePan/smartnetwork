"""
Django user settings for smartnetwork project of APP Home.

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#sidebar
SIDEBAR = {
    'index':[
        {'id':'Home','endpoint':'Home131','text':'Home131','type':3},
           ]
}
#section_nav
SECTION_NAV = {
    'index':[
        {'id':'Home','endpoint':'Home','text':'Home','type':3},
           ]
}

# carousel
CAROUSEL ={
  "id":"Tester",
  "version":"1.0.0",
    "pagination":4,
  "carousel_item":[
    {'active':True,'img':'128x128.png','head':'First Slider','text':'hello world','link':'https://www.sohu.com','link_text':'https://www.sohu.com','type':2},
    {'img':'CloudCampus-stack.png','head':'Second Slider','text':'hello world','link':'#','link_text':'sdf'},
    {'img':'128x128.png','head':'First Slider','text':'hello world','link':'https://www.sohu.com','link_text':'搜狐','type':2},
    {'img':'CloudCampus-stack.png','head':'Second Slider','text':'hello world','link':'#','link_text':'sdf'},
{'img':'CloudCampus-stack.png','head':'Second Slider','text':'hello world','link':'#','link_text':'sdf'},
    {'img':'128x128.png','head':'First Slider','text':'hello world','link':'https://www.sohu.com','link_text':'搜狐','type':2},
    {'img':'CloudCampus-stack.png','head':'Second Slider','text':'hello world','link':'#','link_text':'sdf'},
{'img':'CloudCampus-stack.png','head':'Second Slider','text':'hello world','link':'#','link_text':'sdf'},
{'img':'CloudCampus-stack.png','head':'Second Slider','text':'hello world','link':'#','link_text':'sdf'},
]
}