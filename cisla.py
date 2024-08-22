#!/usr/bin/env python
# -*- coding: utf-8 -*-
t = open('cisla.txt', 'a')
for i in xrange(1000000000000000, 9999999999999999):
    t.write('{}\n'.format(i))
t.close()
