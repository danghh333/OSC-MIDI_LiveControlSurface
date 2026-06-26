from __future__ import absolute_import, unicode_literals
from .Custom_Script import Custom_Script

"""
class Custom_Script(ControlSurface):

    def __init__(self, c_instance):
        super(Custom_Script, self).__init__(c_instance)
        self.show_message('Custom_Script loaded!')
        self.log_message('Custom_Script: hello from the embedded interpreter')
"""

def create_instance(c_instance):
    return Custom_Script(c_instance)