from mopidy import core
import pykka
from screen  import lines

class moplcdFrontend(pykka.ThreadingActor, core.CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                self.core = core
                lines = lines()
                lines.write("Actor initialisiert")

        def mute_changed(self, mute):
                lines.write("mute")

        def playback_state_changed(old_state, new_state):
                lines.write("new_state")
