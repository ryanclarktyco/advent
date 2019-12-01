#!/usr/bin/env python

from sys import argv

filename = argv[1]

txt = open(filename)

parens = txt.read()

floor = 0
position = 0
for c in parens:
    position = position + 1
    if c == '(':
        floor = floor + 1
    elif c == ')':
        floor = floor - 1
    if floor < 0:
        break

print position
