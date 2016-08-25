import sys
import socket
import os
import time
import atexit
import traceback
import RPi.GPIO as GPIO
from lcd_class import Lcd

class lines:
        def __init__(self):
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
                self.lcd.line1("    Pi Music Box")
                self.lcd.line2("")
                self.lcd.line3("Gestartet")
                self.lcd.line4("")
                
        def time(self):
                self.lcd.line2(time.strftime(" %d.%m.%Y - %H:%M"))
                
        def track(self, state, track):
                if state:
                        self.lcd.line3(track)
                else:
                        self.lcd.line3("Paused - " + track)
                
                
