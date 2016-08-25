import pykka, time
from mopidy import core
from screen  import lines
from lcd_class import Lcd


class moplcdFrontend(pykka.ThreadingActor, core.CoreListener):
        def __init__(self, config, core):
                super(moplcdFrontend, self).__init__()
                self.core = core
                stderr = sys.stderr.write;
                self.lcd = Lcd()
                # Try to trap any exit errors and cleanup GPIO
                def exit_fn():
                        if not traceback.format_exc().startswith('None'):
                                s=traceback.format_exc()
                # Register
                #atexit.register(exit_fn)
                def interrupt():
                        return False
                boardrevision = 2
                self.lcd.init(boardrevision)
                self.lcd.setWidth(20)

#        def mute_changed(self, mute):
#                self.lines.write("mute")
                
        def track_playback_paused(self, tl_track, time_position):
                self.lcd.line3("Paused -" tl_track)
                ShowTime()
        
        def track_playback_resumed(self, tl_track, time_position):
                self.lcd.line3(tl_track)
                ShowTime()
                
        def ShowTime(self):
                self.lcd.line1(time.strftime(" %d.%m.%Y - %H:%M"))
