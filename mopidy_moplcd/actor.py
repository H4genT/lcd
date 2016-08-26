import pykka, time, sys, logging
from mopidy import core
from screen  import lines
from lcd_class import Lcd

logger = logging.getLogger('moplcd')

class moplcdFrontend(pykka.ThreadingActor, core.CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                self.core = core
                self.lines = lines()
                
        def on_start(self):
                self.lines.startstop(True)
        
        def on_stop(self):
                self.lines.startstop(False)

#        def mute_changed(self, mute):
#                self.lines.write("mute")
                
        def track_playback_paused(self, tl_track, time_position):
                self.lines.track(False, "Pause")
                self.lines.time()
        
        def track_playback_resumed(self, tl_track, time_position):
                self.lines.track(True, "Play")
                self.lines.time()
