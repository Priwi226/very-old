#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system ("sudo ip link set dev wlan0 down")
os.system ("sudo ip link set dev wlan0 address 35:35:35:35:35:36")
os.system ("sudo ip link set dev wlan0 up")
