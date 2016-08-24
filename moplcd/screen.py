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
                self.lcd.line2(time.strftime("%c"))
                self.lcd.line3("Screen initialisiert")
                self.lcd.line4("ist das Codewort")
                
        def clear(self):
                self.lcd.line2(time.strftime(""))
                self.lcd.line3("")
                self.lcd.line4("")
                
        def write(self, word):
                self.lcd.line2(time.strftime("%c"))
                self.lcd.line3(word)
                self.lcd.line4("ist das Codewort")
