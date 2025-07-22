#!/usr/bin/python

import time
import numpy as np
from multiprocessing import Process, Queue 
from gpiozero import LED
import time

class Laser:
    def __init__(self, q, pin, state=False, verbose=True):
        self.q = q
        self.pin = pin
        self.state = False
        self.led = LED(pin)
        self.verbose = verbose
    
    def toggle(self):
        if self.verbose: print("Called toggle!")
        if self.state:
            self.led.off()
            self.state = False
        else:
            self.led.on()
            self.state = True

    def start(self):
        if self.verbose: print("Called start!")
        self.p = Process(target=self.run, args=((self.q),))
        self.p.start()

    def run(self, queue):
        inp = (0)

        while True:
            
            try:
                inp = queue.get_nowait()
                if self.verbose: print(inp)
                if inp:
                    print("[Button] Pressed for pin: ", self.pin)

                    self.toggle()
                
            except:
                time.sleep(0.01)
                pass

if __name__ == "__main__":

    print("Start laser")
