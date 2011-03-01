# -*- coding: utf-8 -*-
#Copyright (c) 2010, Walter Bender

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

from gettext import gettext as _

#
# Sprite layers
#

HIDE_LAYER = 100
CANVAS_LAYER = 500
OVERLAY_LAYER = 525
TURTLE_LAYER = 550
BLOCK_LAYER = 600
CATEGORY_LAYER = 700
TAB_LAYER = 710
STATUS_LAYER = 900
TOP_LAYER = 1000

#
# Block-palette categories
#

PALETTE_NAMES = []
PALETTES = []
COLORS = []

# Special-case some block colors
BOX_COLORS = {'red': ["#FF0000", "#A00000"],
              'orange': ["#FFD000", "#AA8000"],
              'yellow': ["#FFFF00", "#A0A000"],
              'blue': ["#0000FF", "#000080"],
              'cyan': ["#00FFFF", "#00A0A0"],
              'green': ["#00FF00", "#008000"],
              'purple': ["#FF00FF", "#A000A0"],
              'white': ["#FFFFFF", "#A0A0A0"],
              'black': ["#000000", "#000000"]}

#
# Misc. parameters
#
PALETTE_HEIGHT = 120
PALETTE_WIDTH = 175
SELECTOR_WIDTH = 55
ICON_SIZE = 55
GRADIENT_COLOR = "#FFFFFF"
STANDARD_STROKE_WIDTH = 1.0
BLOCK_SCALE = 2.0
PALETTE_SCALE = 1.5
DEFAULT_TURTLE = 'Yertle'
DEFAULT_TURTLE_COLORS = ['#008000', '#00A000']
HORIZONTAL_PALETTE = 0
VERTICAL_PALETTE = 1
BLACK = -9999
WHITE = -9998
HIT_HIDE = 248
HIT_SHOW = 240
HIT_RED = "#F80000"
HIT_GREEN = "#00F000"
HIDE_WHITE = "#F8F8F8"
SHOW_WHITE = "#F0F0F0"
DEFAULT_SCALE = 33
XO1 = 'xo1'
XO15 = 'xo1.5'
UNKNOWN = 'unknown'

#
# Block-style definitions
#
# TODO: define depreciated blocks
BASIC_STYLE_HEAD = []
BASIC_STYLE_HEAD_1ARG = []
BASIC_STYLE_TAIL = []
BASIC_STYLE = []
BASIC_STYLE_EXTENDED_VERTICAL = []
INVISIBLE = []
BASIC_STYLE_EXTENDED = []
BASIC_STYLE_1ARG = ['settextsize', 'settextcolor', 'nop']
BASIC_STYLE_VAR_ARG = []
BULLET_STYLE = ['templatelist', 'list']
BASIC_STYLE_2ARG = []
BOX_STYLE = ['textsize']
BOX_STYLE_MEDIA = []
NUMBER_STYLE = ['myfunc']
NUMBER_STYLE_VAR_ARG = []
NUMBER_STYLE_BLOCK = []
NUMBER_STYLE_PORCH = []
NUMBER_STYLE_1ARG = []
NUMBER_STYLE_1STRARG = []
COMPARE_STYLE = []
COMPARE_PORCH_STYLE = []
BOOLEAN_STYLE = []
NOT_STYLE = []
FLOW_STYLE = []
FLOW_STYLE_TAIL = []
FLOW_STYLE_1ARG = []
FLOW_STYLE_BOOLEAN = []
FLOW_STYLE_WHILE = []
FLOW_STYLE_ELSE = []
COLLAPSIBLE_TOP = []
COLLAPSIBLE_TOP_NO_ARM = []
COLLAPSIBLE_TOP_NO_LABEL = []
COLLAPSIBLE_TOP_NO_ARM_NO_LABEL = []
COLLAPSIBLE_BOTTOM = []

# Depreciated block styles
PORTFOLIO_STYLE_2x2 = []
PORTFOLIO_STYLE_1x1 = []
PORTFOLIO_STYLE_2x1 = []
PORTFOLIO_STYLE_1x2 = []

BLOCK_STYLES = {'basic-style-head': BASIC_STYLE_HEAD,
                'basic-style-head-1arg': BASIC_STYLE_HEAD_1ARG,
                'basic-style-tail': BASIC_STYLE_TAIL,
                'basic-style': BASIC_STYLE,
                'basic-style-extended-vertical': BASIC_STYLE_EXTENDED_VERTICAL,
                'invisible': INVISIBLE,
                'basic-style-extended': BASIC_STYLE_EXTENDED,
                'basic-style-1arg': BASIC_STYLE_1ARG,
                'basic-style-var-arg': BASIC_STYLE_VAR_ARG,
                'bullet-style': BULLET_STYLE,
                'basic-style-2arg': BASIC_STYLE_2ARG,
                'box-style': BOX_STYLE,
                'box-style-media': BOX_STYLE_MEDIA,
                'number-style': NUMBER_STYLE,
                'number-style-var-arg': NUMBER_STYLE_VAR_ARG,
                'number-style-block': NUMBER_STYLE_BLOCK,
                'number-style-porch': NUMBER_STYLE_PORCH,
                'number-style-1arg': NUMBER_STYLE_1ARG,
                'number-style-1strarg': NUMBER_STYLE_1STRARG,
                'compare-style': COMPARE_STYLE,
                'compare-porch-style': COMPARE_PORCH_STYLE,
                'boolean-style': BOOLEAN_STYLE,
                'not-style': NOT_STYLE,
                'flow-style': FLOW_STYLE,
                'flow-style-tail': FLOW_STYLE_TAIL,
                'flow-style-1arg': FLOW_STYLE_1ARG,
                'flow-style-boolean': FLOW_STYLE_BOOLEAN,
                'flow-style-while': FLOW_STYLE_WHILE,
                'flow-style-else': FLOW_STYLE_ELSE,
                'collapsible-top': COLLAPSIBLE_TOP,
                'collapsible-top-no-arm': COLLAPSIBLE_TOP_NO_ARM,
                'collapsible-top-no-label': COLLAPSIBLE_TOP_NO_LABEL,
                'collapsible-top-no-arm-no-label':
                    COLLAPSIBLE_TOP_NO_ARM_NO_LABEL,
                'collapsible-bottom': COLLAPSIBLE_BOTTOM,
                'portfolio-style-2x2': PORTFOLIO_STYLE_2x2,
                'portfolio-style-1x1': PORTFOLIO_STYLE_1x1,
                'portfolio-style-2x1': PORTFOLIO_STYLE_2x1,
                'portfolio-style-1x2': PORTFOLIO_STYLE_1x2}

#
# Blocks that are expandable
#
EXPANDABLE_STYLE = ['boolean-style', 'compare-porch-style', 'compare-style',
                    'number-style-porch', 'number-style', 'basic-style-2arg']

EXPANDABLE = ['vspace', 'hspace', 'identity2']

EXPANDABLE_BLOCKS = []

EXPANDABLE_ARGS = ['templatelist', 'list', 'myfunc1arg', 'myfunc2arg',
                   'myfunc3arg', 'userdefined', 'userdefined2args',
                   'userdefined3args']
#
# Blocks that are 'collapsible'
#
COLLAPSIBLE = ['sandwichbottom', 'sandwichcollapsed']

#
# Depreciated block styles that need dock adjustments
#
OLD_DOCK = ['and', 'or', 'plus', 'minus', 'division', 'product', 'remainder']

#
# Blocks that contain media
#
CONTENT_BLOCKS = ['number', 'string', 'description', 'audio', 'video',
                  'journal']

#
# These blocks get a special skin
#
BLOCKS_WITH_SKIN = ['journal', 'audio', 'description', 'nop', 'userdefined',
                    'video', 'userdefined2args', 'userdefined3args']

PYTHON_SKIN = ['nop', 'userdefined', 'userdefined2args', 'userdefined3args']

#
# These blocks hold constants
#
CONSTANTS = {'leftpos': None, 'toppos': None, 'rightpos': None,
             'bottompos': None, 'width': None, 'height': None, 'red': 0,
             'orange': 10, 'yellow': 20, 'green': 40, 'cyan': 50, 'blue': 70,
             'purple': 90, 'titlex': None, 'titley': None, 'leftx': None,
             'topy': None, 'rightx': None, 'bottomy': None}

#
# Block-name dictionary used for labels
#
BLOCK_NAMES = {
    'list': ['list'],
    'myfunc': [_('Python'), 'f(x)', 'x'],
    'nop': [_(' ')],
    'settextsize': [_('set text size')],
    'textsize': [_('text size')]}

#
# Logo primitives
#
# TODO: check hats (nop1, 2, 3), setxy
PRIMITIVES = {
    'list': 'bulletlist',
    'myfunc': 'myfunction',
    'nop': 'userdefined',
    'settextsize': 'settextsize',
    'textsize': 'textsize'}

#
# block default values
#

DEFAULTS = {
    'myfunc': ['x', 100],
    'nop': [100]}

#
# Blocks that can interchange strings and numbers for their arguments
#
STRING_OR_NUMBER_ARGS = ['plus2', 'equal2', 'less2', 'greater2', 'box',
                         'template1x1', 'template1x2', 'template2x1', 'list',
                         'template2x2', 'template1x1a', 'templatelist', 'nop',
                         'print', 'stack', 'hat', 'addturtle', 'myfunc',
                         'myfunc1arg', 'myfunc2arg', 'myfunc3arg', 'comment',
                         'sandwichtop', 'sandwichtop_no_arm', 'userdefined',
                         'userdefined2args', 'userdefined3args', 'storein']

CONTENT_ARGS = ['show', 'showaligned', 'push', 'storein', 'storeinbox1',
                'storeinbox2']

PREFIX_DICTIONARY = {'journal': '#smedia_', 'description': '#sdescr_',
                     'audio': '#saudio_', 'video': '#svideo_'}

#
# Status blocks
#

MEDIA_SHAPES = ['audiooff', 'audioon', 'audiosmall',
                'videooff', 'videoon', 'videosmall',
                'cameraoff', 'camerasmall',
                'journaloff', 'journalon', 'journalsmall',
                'descriptionoff', 'descriptionon', 'descriptionsmall',
                'pythonoff', 'pythonon', 'pythonsmall',
                'list', '1x1', '1x1a', '2x1', '1x2', '2x2']

OVERLAY_SHAPES = ['Cartesian', 'Cartesian_labeled', 'polar']

STATUS_SHAPES = ['status', 'info', 'nostack', 'dupstack', 'noinput',
                 'emptyheap', 'emptybox', 'nomedia', 'nocode', 'overflowerror',
                 'negroot', 'syntaxerror', 'nofile', 'nojournal', 'zerodivide',
                 'notanumber', 'incompatible']

#
# Emulate Sugar toolbar when running from outside of Sugar
#
TOOLBAR_SHAPES = ['hideshowoff', 'eraseron', 'run-fastoff',
                  'run-slowoff', 'debugoff', 'stopiton']

#
# Legacy names
#
OLD_NAMES = {'product': 'product2', 'storeinbox': 'storein', 'minus': 'minus2',
             'division': 'division2', 'plus': 'plus2', 'and': 'and2',
             'or': 'or2', 'less': 'less2', 'greater': 'greater2',
             'equal': 'equal2', 'remainder': 'remainder2',
             'identity': 'identity2', 'division': 'division2',
             'audiooff': 'audio', 'endfill': 'stopfill',
             'descriptionoff': 'description', 'template3': 'templatelist',
             'template1': 'template1x1', 'template2': 'template2x1',
             'template6': 'template1x2', 'template7': 'template2x2',
             'template4': 'template1x1a', 'hres': 'width', 'vres': 'height',
             'sandwichtop2': 'sandwichtop', 'image': 'show'}

#
# Define the relative size and postion of media objects
#                    (w, h, x, y, dx, dy)
#
TITLEXY = (0.9375, 0.875)

#
# Relative placement of portfolio objects (used by depreciated blocks)
#
TEMPLATES = {'t1x1': (0.5, 0.5, 0.0625, 0.125, 1.05, 0),
             't2z1': (0.5, 0.5, 0.0625, 0.125, 1.05, 1.05),
             't1x2': (0.45, 0.45, 0.0625, 0.125, 1.05, 1.05),
             't2x2': (0.45, 0.45, 0.0625, 0.125, 1.05, 1.05),
             't1x1a': (0.9, 0.9, 0.0625, 0.125, 0, 0),
             'bullet': (1, 1, 0.0625, 0.125, 0, 0.1),
             'insertimage': (0.333, 0.333)}

#
# Names for blocks without names for popup help
#
SPECIAL_NAMES = {
    'textsize': _('text size')}

#
# Help messages
#
HELP_STRINGS = {
    'cartesian': _("displays Cartesian coordinates"),
    'clean': _("clears the screen and reset the turtle"),
    'debugoff': _("Debug"),
    'eraseron': _("Clean"),
    'myfunc': _("a programmable block: used to add advanced math equations, e.g., sin(x)"),
    'next': _('displays next palette'),
    'nop': _("runs code found in the tamyblock.py module found in the Journal"),
    'orientation': _("changes the orientation of the palette of blocks"),
    'polar': _("displays polar coordinates"),
    'run-fastoff': _("Run"),
    'run-slowoff': _("Step"),
    'savepix': _("saves a picture to the Sugar Journal"),
    'savesvg': _("saves turtle graphics as an SVG file in the Sugar Journal"),
    'stopiton': _("Stop turtle"),
    'textcolor': _(
        "holds current text color (can be used in place of a number block)"),
    'textsize': _(
        "holds current text size (can be used in place of a number block)")}

#
# 'dead key' Unicode dictionaries
#

DEAD_KEYS = ['grave', 'acute', 'circumflex', 'tilde', 'diaeresis', 'abovering']
DEAD_DICTS = [{'A': 192, 'E': 200, 'I': 204, 'O': 210, 'U': 217, 'a': 224,
               'e': 232, 'i': 236, 'o': 242, 'u': 249},
              {'A': 193, 'E': 201, 'I': 205, 'O': 211, 'U': 218, 'a': 225,
               'e': 233, 'i': 237, 'o': 243, 'u': 250},
              {'A': 194, 'E': 202, 'I': 206, 'O': 212, 'U': 219, 'a': 226,
               'e': 234, 'i': 238, 'o': 244, 'u': 251},
              {'A': 195, 'O': 211, 'N': 209, 'U': 360, 'a': 227, 'o': 245,
               'n': 241, 'u': 361},
              {'A': 196, 'E': 203, 'I': 207, 'O': 211, 'U': 218, 'a': 228,
               'e': 235, 'i': 239, 'o': 245, 'u': 252},
              {'A': 197, 'a': 229}]
NOISE_KEYS = ['Shift_L', 'Shift_R', 'Control_L', 'Caps_Lock', 'Pause',
              'Alt_L', 'Alt_R', 'KP_Enter', 'ISO_Level3_Shift', 'KP_Divide',
              'Escape', 'Return', 'KP_Page_Up', 'Up', 'Down', 'Menu',
              'Left', 'Right', 'KP_Home', 'KP_End', 'KP_Up', 'Super_L',
              'KP_Down', 'KP_Left', 'KP_Right', 'KP_Page_Down', 'Scroll_Lock',
              'Page_Down', 'Page_Up']
WHITE_SPACE = ['space', 'Tab']

CURSOR = '█'
RETURN = '⏎'


#
# Macros (groups of blocks)
#
MACROS = {
    'until':
              [[0, 'forever', 0, 0, [None, 2, 1]],
               [1, 'vspace', 0, 0, [0, None]],
               [2, 'ifelse', 0, 0, [0, None, 3, None, None]],
               [3, 'vspace', 0, 0, [2, 4]],
               [4, 'stopstack', 0, 0, [3, None]]],
    'while':
              [[0, 'forever', 0, 0, [None, 2, 1]],
               [1, 'vspace', 0, 0, [0, None]],
               [2, 'ifelse', 0, 0, [0, None, 3, 4, None]],
               [3, 'vspace', 0, 0, [2, None]],
               [4, 'stopstack', 0, 0, [2, None]]],
    'kbinput':
              [[0, 'forever', 0, 0, [None, 1, None]],
               [1, 'kbinput', 0, 0, [0, 2]],
               [2, 'vspace', 0, 0, [1, 3]],
               [3, 'if', 0, 0, [2, 4, 7, 8]],
               [4, 'greater2', 0, 0, [3, 5, 6, None]],
               [5, 'keyboard', 0, 0, [4, None]],
               [6, ['number', '0'], 0, 0, [4, None]],
               [7, 'stopstack', 0, 0, [3, None]],
               [8, 'vspace', 0, 0, [3, 9]],
               [9, 'wait', 0, 0, [8, 10, None]],
               [10, ['number', '1'], 0, 0, [9, None]]],
    'picturelist':
              [[0, 'sandwichtop_no_label', 0, 0, [None, 1]],
               [1, 'penup', 0, 0, [0, 2]],
               [2, 'setxy2', 0, 0, [1, 3, 4, 5]],
               [3, 'titlex', 0, 0, [2, None]],
               [4, 'titley', 0, 0, [2, None]],
               [5, 'pendown', 0, 0, [2, 6]],
               [6, 'setscale', 0, 0, [5, 7, 8]],
               [7, ['number', '100'], 0, 0, [6, None]],
               [8, 'show', 0, 0, [6, 9, 10]],
               [9, ['string', _('Title')], 0, 0, [8, None]],
               [10, 'penup', 0, 0, [8, 11]],
               [11, 'setxy2', 0, 0, [10, 12, 13, 14]],
               [12, 'leftx', 0, 0, [11, None]],
               [13, 'topy', 0, 0, [11, None]],
               [14, 'pendown', 0, 0, [11, 15]],
               [15, 'setscale', 0, 0, [14, 16, 17]],
               [16, ['number', '67'], 0, 0, [15, None]],
               [17, 'list', 0, 0, [15, 18, 19, 20]],
               [18, ['string', '∙ '], 0, 0, [17, None]],
               [19, ['string', '∙ '], 0, 0, [17, None]],
               [20, 'sandwichbottom', 0, 0, [17, None]]],
    'picture1x1a':
              [[0, 'sandwichtop_no_label', 0, 0, [None, 1]],
               [1, 'penup', 0, 0, [0, 2]],
               [2, 'setxy2', 0, 0, [1, 3, 4, 5]],
               [3, 'titlex', 0, 0, [2, None]],
               [4, 'titley', 0, 0, [2, None]],
               [5, 'pendown', 0, 0, [2, 6]],
               [6, 'setscale', 0, 0, [5, 7, 8]],
               [7, ['number', '100'], 0, 0, [6, None]],
               [8, 'show', 0, 0, [6, 9, 10]],
               [9, ['string', _('Title')], 0, 0, [8, None]],
               [10, 'penup', 0, 0, [8, 11]],
               [11, 'setxy2', 0, 0, [10, 12, 13, 14]],
               [12, 'leftx', 0, 0, [11, None]],
               [13, 'topy', 0, 0, [11, None]],
               [14, 'pendown', 0, 0, [11, 15]],
               [15, 'setscale', 0, 0, [14, 16, 17]],
               [16, ['number', '90'], 0, 0, [15, None]],
               [17, 'showaligned', 0, 0, [15, 18, 19]],
               [18, 'journal', 0, 0, [17, None]],
               [19, 'sandwichbottom', 0, 0, [17, None]]],
    'picture2x2':
              [[0, 'sandwichtop_no_label', 0, 0, [None, 1]],
               [1, 'penup', 0, 0, [0, 2]],
               [2, 'setxy2', 0, 0, [1, 3, 4, 5]],
               [3, 'titlex', 0, 0, [2, None]],
               [4, 'titley', 0, 0, [2, None]],
               [5, 'pendown', 0, 0, [2, 6]],
               [6, 'setscale', 0, 0, [5, 7, 8]],
               [7, ['number', '100'], 0, 0, [6, None]],
               [8, 'show', 0, 0, [6, 9, 10]],
               [9, ['string', _('Title')], 0, 0, [8, None]],
               [10, 'setscale', 0, 0, [8, 11, 12]],
               [11, ['number', '35'], 0, 0, [10, None]],
               [12, 'penup', 0, 0, [10, 13]],
               [13, 'setxy2', 0, 0, [12, 14, 15, 16]],
               [14, 'leftx', 0, 0, [13, None]],
               [15, 'topy', 0, 0, [13, None]],
               [16, 'pendown', 0, 0, [13, 17]],
               [17, 'showaligned', 0, 0, [16, 18, 19]],
               [18, 'journal', 0, 0, [17, None]],
               [19, 'penup', 0, 0, [17, 20]],
               [20, 'setxy2', 0, 0, [19, 21, 22, 23]],
               [21, 'rightx', 0, 0, [20, None]],
               [22, 'topy', 0, 0, [20, None]],
               [23, 'pendown', 0, 0, [20, 24]],
               [24, 'showaligned', 0, 0, [23, 25, 26]],
               [25, 'journal', 0, 0, [24, None]],
               [26, 'penup', 0, 0, [24, 27]],
               [27, 'setxy2', 0, 0, [26, 28, 29, 30]],
               [28, 'leftx', 0, 0, [27, None]],
               [29, 'bottomy', 0, 0, [27, None]],
               [30, 'pendown', 0, 0, [27, 31]],
               [31, 'showaligned', 0, 0, [30, 32, 33]],
               [32, 'journal', 0, 0, [31, None]],
               [33, 'penup', 0, 0, [31, 34]],
               [34, 'setxy2', 0, 0, [33, 35, 36, 37]],
               [35, 'rightx', 0, 0, [34, None]],
               [36, 'bottomy', 0, 0, [34, None]],
               [37, 'pendown', 0, 0, [34, 38]],
               [38, 'showaligned', 0, 0, [37, 39, 40]],
               [39, 'journal', 0, 0, [38, None]],
               [40, 'sandwichbottom', 0, 0, [38, None]]],
    'picture1x2':
              [[0, 'sandwichtop_no_label', 0, 0, [None, 1]],
               [1, 'penup', 0, 0, [0, 2]],
               [2, 'setxy2', 0, 0, [1, 3, 4, 5]],
               [3, 'titlex', 0, 0, [2, None]],
               [4, 'titley', 0, 0, [2, None]],
               [5, 'pendown', 0, 0, [2, 6]],
               [6, 'setscale', 0, 0, [5, 7, 8]],
               [7, ['number', '100'], 0, 0, [6, None]],
               [8, 'show', 0, 0, [6, 9, 10]],
               [9, ['string', _('Title')], 0, 0, [8, None]],
               [10, 'setscale', 0, 0, [8, 11, 12]],
               [11, ['number', '35'], 0, 0, [10, None]],
               [12, 'penup', 0, 0, [10, 13]],
               [13, 'setxy2', 0, 0, [12, 14, 15, 16]],
               [14, 'leftx', 0, 0, [13, None]],
               [15, 'topy', 0, 0, [13, None]],
               [16, 'pendown', 0, 0, [13, 17]],
               [17, 'showaligned', 0, 0, [16, 18, 19]],
               [18, 'journal', 0, 0, [17, None]],
               [19, 'penup', 0, 0, [17, 20]],
               [20, 'setxy2', 0, 0, [19, 21, 22, 23]],
               [21, 'rightx', 0, 0, [20, None]],
               [22, 'topy', 0, 0, [20, None]],
               [23, 'pendown', 0, 0, [20, 24]],
               [24, 'showaligned', 0, 0, [23, 25, 26]],
               [25, 'description', 0, 0, [24, None]],
               [26, 'penup', 0, 0, [24, 27]],
               [27, 'setxy2', 0, 0, [26, 28, 29, 30]],
               [28, 'leftx', 0, 0, [27, None]],
               [29, 'bottomy', 0, 0, [27, None]],
               [30, 'pendown', 0, 0, [27, 31]],
               [31, 'showaligned', 0, 0, [30, 32, 33]],
               [32, 'journal', 0, 0, [31, None]],
               [33, 'penup', 0, 0, [31, 34]],
               [34, 'setxy2', 0, 0, [33, 35, 36, 37]],
               [35, 'rightx', 0, 0, [34, None]],
               [36, 'bottomy', 0, 0, [34, None]],
               [37, 'pendown', 0, 0, [34, 38]],
               [38, 'showaligned', 0, 0, [37, 39, 40]],
               [39, 'description', 0, 0, [38, None]],
               [40, 'sandwichbottom', 0, 0, [38, None]]],
    'picture2x1':
              [[0, 'sandwichtop_no_label', 0, 0, [None, 1]],
               [1, 'penup', 0, 0, [0, 2]],
               [2, 'setxy2', 0, 0, [1, 3, 4, 5]],
               [3, 'titlex', 0, 0, [2, None]],
               [4, 'titley', 0, 0, [2, None]],
               [5, 'pendown', 0, 0, [2, 6]],
               [6, 'setscale', 0, 0, [5, 7, 8]],
               [7, ['number', '100'], 0, 0, [6, None]],
               [8, 'show', 0, 0, [6, 9, 10]],
               [9, ['string', _('Title')], 0, 0, [8, None]],
               [10, 'setscale', 0, 0, [8, 11, 12]],
               [11, ['number', '35'], 0, 0, [10, None]],
               [12, 'penup', 0, 0, [10, 13]],
               [13, 'setxy2', 0, 0, [12, 14, 15, 16]],
               [14, 'leftx', 0, 0, [13, None]],
               [15, 'topy', 0, 0, [13, None]],
               [16, 'pendown', 0, 0, [13, 17]],
               [17, 'showaligned', 0, 0, [16, 18, 19]],
               [18, 'journal', 0, 0, [17, None]],
               [19, 'penup', 0, 0, [17, 20]],
               [20, 'setxy2', 0, 0, [19, 21, 22, 23]],
               [21, 'rightx', 0, 0, [20, None]],
               [22, 'topy', 0, 0, [20, None]],
               [23, 'pendown', 0, 0, [20, 24]],
               [24, 'showaligned', 0, 0, [23, 25, 26]],
               [25, 'journal', 0, 0, [24, None]],
               [26, 'penup', 0, 0, [24, 27]],
               [27, 'setxy2', 0, 0, [26, 28, 29, 30]],
               [28, 'leftx', 0, 0, [27, None]],
               [29, 'bottomy', 0, 0, [27, None]],
               [30, 'pendown', 0, 0, [27, 31]],
               [31, 'showaligned', 0, 0, [30, 32, 33]],
               [32, 'description', 0, 0, [31, None]],
               [33, 'penup', 0, 0, [31, 34]],
               [34, 'setxy2', 0, 0, [33, 35, 36, 37]],
               [35, 'rightx', 0, 0, [34, None]],
               [36, 'bottomy', 0, 0, [34, None]],
               [37, 'pendown', 0, 0, [34, 38]],
               [38, 'showaligned', 0, 0, [37, 39, 40]],
               [39, 'description', 0, 0, [38, None]],
               [40, 'sandwichbottom', 0, 0, [38, None]]],
    'picture1x1':
              [[0, 'sandwichtop_no_label', 0, 0, [None, 1]],
               [1, 'penup', 0, 0, [0, 2]],
               [2, 'setxy2', 0, 0, [1, 3, 4, 5]],
               [3, 'titlex', 0, 0, [2, None]],
               [4, 'titley', 0, 0, [2, None]],
               [5, 'pendown', 0, 0, [2, 6]],
               [6, 'setscale', 0, 0, [5, 7, 8]],
               [7, ['number', '100'], 0, 0, [6, None]],
               [8, 'show', 0, 0, [6, 9, 10]],
               [9, ['string', _('Title')], 0, 0, [8, None]],
               [10, 'setscale', 0, 0, [8, 11, 12]],
               [11, ['number', '35'], 0, 0, [10, None]],
               [12, 'penup', 0, 0, [10, 13]],
               [13, 'setxy2', 0, 0, [12, 14, 15, 16]],
               [14, 'leftx', 0, 0, [13, None]],
               [15, 'topy', 0, 0, [13, None]],
               [16, 'pendown', 0, 0, [13, 17]],
               [17, 'showaligned', 0, 0, [16, 18, 19]],
               [18, 'journal', 0, 0, [17, None]],
               [19, 'penup', 0, 0, [17, 20]],
               [20, 'setxy2', 0, 0, [19, 21, 22, 23]],
               [21, 'rightx', 0, 0, [20, None]],
               [22, 'topy', 0, 0, [20, None]],
               [23, 'pendown', 0, 0, [20, 24]],
               [24, 'showaligned', 0, 0, [23, 25, 26]],
               [25, 'description', 0, 0, [24, None]],
               [26, 'sandwichbottom', 0, 0, [24, None]]],
    'reskin':
              [[0, 'skin', 0, 0, [None, 1, None]],
               [1, 'journal', 0, 0, [0, None]]]}
