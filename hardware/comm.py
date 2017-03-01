#!/usr/bin/env python
#! -*- coding: utf-8 -*-

#these packages should provide hopefully sufficient methods 
#for communication with hardware via uart and i2c
import smbus
import serial
#import picamera

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



if __name__ == "__main__":
    #run basic tests for funcionality
    print("abstraction blub as main")

