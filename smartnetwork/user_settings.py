"""
Django user settings for smartnetwork project.

"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#nav
NAV = {
    'left':[
        {'id':'Home','endpoint':'Home','text':'Home','type':1}
    ],
     'right':[
         {'id':'Home','endpoint':'Home','text':'游客','type':4,
          'submenu':[
             {'id':'Home1','endpoint':'Home','text':'关注','type':4},
             {'id':'Home2','endpoint':'Home','text':'注册','type':4}
         ]},
     ],
}

