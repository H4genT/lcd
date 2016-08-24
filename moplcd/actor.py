from mopidy import core
import pykka
from screen  import lines

class moplcdFrontend(pykka.ThreadingActor, core.CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                self.core = core
                self.lines = lines()
                self.lines.write("Actor initialisiert")

        def mute_changed(self, mute):
                self.lines.write("mute")
                
                
        def track_playback_paused(self, tl_track, time_position):
                self.lines.write("Paused")
        
        def track_playback_resumed(self, tl_track, time_position):
                self.lines.write("Resumed")
                
