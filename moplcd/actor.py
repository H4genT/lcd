import pykka, time, sys, logging
from mopidy.core import CoreListener
from screen  import lines

logger = logging.getLogger('moplcd')

class moplcdFrontend(pykka.ThreadingActor, CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                logger.info("moplcd initialising")
                self.core = core
                self.config = config
                self.lines = lines()
                
        def track_playback_started(tl_track):
                logger.info("track playback startet")
                self.lines.track(True, tl_track)

        def on_start(self): 
                self.lines.startstop(True)
        
        def on_stop(self):
                
                #abc        
                
                
        def mute_changed(self, mute):
                #self.lines.write("mute")
                
        def track_playback_paused(self, tl_track, time_position):
                
                #self.lines.track(False, "Pause")
                #self.lines.time()
        
        def track_playback_resumed(self, tl_track, time_position):
                
                #self.lines.track(True, "Play")
                #self.lines.time()
'''
