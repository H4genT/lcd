from mopidy import core
import pykka
from screen  import lines

class moplcdFrontend(pykka.ThreadingActor, core.CoreListener):
        def __init__(self, config, core):
                super(Output, self).__init__()
                self.core = core
                self.lines = lines()

        def mute_changed(self, mute):
                self.lines.write("mute")

        def playback_state_changed(self, old_state, new_state):
                self.lines.write(new_state)
