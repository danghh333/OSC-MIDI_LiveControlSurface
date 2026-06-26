from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.TransportComponent import TransportComponent
from _Framework.ButtonElement import ButtonElement
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE

CHANNEL     = 0
PLAY_NOTE   = 65
STOP_NOTE   = 66

#Grid
NUM_TRACKS = 8
NUM_SCENES = 8



class Custom_Script(ControlSurface):

    def __init__(self, c_instance):
        super(Custom_Script, self).__init__(c_instance)
        with self.component_guard():
            self._create_controls()
            self._create_transport()
            #self._create_session()
            matrix = ButtonMatrixElement()
            for row in range(NUM_SCENES):
                matrix.add_row([
                    ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, row*NUM_TRACKS+col) for col in range(NUM_TRACKS)
                ])
            session = SessionComponent(NUM_TRACKS, NUM_SCENES)
            session.set_clip_launch_buttons(matrix)
                
        self.show_message('Custom_Script loaded')
        self.log_message('Custom_Script: setup complete')

    def _create_controls(self):
        self._play_button = ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, PLAY_NOTE)
        self._stop_button = ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, STOP_NOTE)

    def _create_transport(self):
        transport = TransportComponent()
        transport.set_play_button(self._play_button)
        transport.set_stop_button(self._stop_button)
    '''
    def _create_session(self):
        matrix = ButtonMatrixElement()
        for row in range(NUM_SCENES):
            matrix.add_row()
            for track in range(NUM_TRACKS):
                matrix.add_row(
                    [ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, row * NUM_TRACKS + col)
                    for col in range(NUM_TRACKS)
                ])
        session = SessionComponent(NUM_TRACKS, NUM_SCENES)
        session.set_clip_launch_buttons(self._grid)
    '''


def create_instance(c_instance):
    return Custom_Script(c_instance)