from __future__ import absolute_import, print_function, unicode_literals
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement
from _Framework.SessionComponent import SessionComponent
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE

CHANNEL = 0
TRACK_STOP = (65, 66, 67, 68, 69, 70, 71, 72)
NUM_TRACKS = 8
NUM_SCENES = 8

class Custom_Script(ControlSurface):
    def __init__(self, c_instance):
        super(Custom_Script, self).__init__(c_instance)
        with self.component_guard():
            # Clip grid
            matrix = ButtonMatrixElement()
            for row in range(NUM_SCENES):
                matrix.add_row([
                    ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL,
                                  row * NUM_TRACKS + col)
                    for col in range(NUM_TRACKS)
                ])
            session = SessionComponent(NUM_TRACKS, NUM_SCENES)
            session.set_clip_launch_buttons(matrix)

            # Track stop
            stop_buttons = tuple(
                ButtonElement(True, MIDI_NOTE_TYPE, CHANNEL, note)
                for note in TRACK_STOP
            )
            session.set_stop_track_clip_buttons(stop_buttons)

        self.show_message('Custom_Script loaded')
        self.log_message('Custom_Script: setup complete')

def create_instance(c_instance):
    return Custom_Script(c_instance)