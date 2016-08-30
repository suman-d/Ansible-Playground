#!/usr/bin/env python
import time
import socket

with open("after.txt", "w") as a:
        now = round(time.time(), 5)
        with open("before.txt", "r") as b:
                boot_time = now - round(float(b.readlines()[0].strip()), 5)
                print "Boot time for the VM ", socket.gethostname(), " is ", boot_time
                a.write(str(boot_time) + "\n")


~
~
