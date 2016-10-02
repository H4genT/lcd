import pykka, time, sys, logging
from mopidy.core import CoreListener
#from screen  import lines

logger = logging.getLogger('moplcd')

class moplcdFrontend(pykka.ThreadingActor, CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                self.core = core
                self.config = config
                self.lines = lines()
                print("Actor Init")
                
        def on_start(self):
                logger.debug('moplcd started')
                #self.lines.startstop(True)
                print("Actor Start")
        
        def on_stop(self):
                logger.debug('moplcd stopped')
                #self.lines.startstop(False)
                print("Actor Stop")

#        def mute_changed(self, mute):
#                self.lines.write("mute")
                
        def track_playback_paused(self, tl_track, time_position):
                #self.lines.track(False, "Pause")
                #self.lines.time()
                print("Actor Paused")
        
        def track_playback_resumed(self, tl_track, time_position):
                #self.lines.track(True, "Play")
                #self.lines.time()
                print("Actor Resumed")
                
        def on_event(self, event, **kwargs):
                print("Actor Event")
                return CoreListener.on_event(self, event, **kwargs)
