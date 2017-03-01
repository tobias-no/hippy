#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import os

#these packages should provide hopefully sufficient methods 
#for communication with hardware via uart and i2c
import smbus
import serial
#import picamera

from time import time, sleep

class I2CStuff(object):
    def __init__(self):
        #initialize specific hardware addresses
        pass

    def rtc(self):
        #talk to rtc module
        #convert answer to date format
        timestamp = 144
        return timestamp


class UARTStuff(object):
    def __init__(self):
        pass


class CamStuff(object):
    def __init__(object):
        pass

    #some additional parameters like shutter speed or iso might be necessary
    def standard_capture(self, path, filename, width=1024, height=768):
        #ensure that camera object is closed in the end to save energy
        #leaving object open requires about 250mA!!!
        with picamera.PiCamera() as cam:
            cam.resolution = (1024, 768)

            #cam.start_preview() #needed??
            #test how much warm-up time is really necessary
            sleep(2) 

            cam.capture(os.path.join(path, filename), resize=(width, height))

        return os.path.join(path, filename)




if __name__ == "__main__":
    #run basic tests for funcionality
    print("abstraction blub as main")

