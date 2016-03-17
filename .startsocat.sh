#!/bin/bash

sudo socat -d -d -d -d -lf /tmp/socat pty,link=/dev/ttyS0,raw,echo=0,user=lilli,group=staff pty,link=/dev/ttyS1,raw,echo=0,user=lilli,group=staff