import pykka, time, sys
from mopidy import core
from screen  import lines
from lcd_class import Lcd


class moplcdFrontend(pykka.ThreadingActor, core.CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                self.core = core
                self.lines = lines()
                
        def on_start(self):

#        def mute_changed(self, mute):
#                self.lines.write("mute")
                
        def track_playback_paused(self, tl_track, time_position):
                self.lines.track(False, "Pause")
                self.lines.time()
        
        def track_playback_resumed(self, tl_track, time_position):
                self.lines.track(True, "Play")
                self.lines.time()
