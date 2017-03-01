#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import os, sys

import logging
import csv #perhaps sqlite might be more stable??

#abstraction layer import for hardware
import hardware.comm as hw

log = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s: %(message)s', level=logging.DEBUG)


class ControlThemAll(object):
    def __init__(self):
        print("blub")

    def mainloop(self):
        log.info("logger might be useful")
        i2c_handle = hw.I2CStuff()
        timestamp = i2c_handle.rtc()
        log.info("retrieved timestamp is {}".format(timestamp))



if __name__ == "__main__":
    control_instance = ControlThemAll()
    control_instance.mainloop()

