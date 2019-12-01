#!/usr/bin/env python

from sys import argv

filename = argv[1]

txt = open(filename)

parens = txt.read()

floor = 0

for c in parens:
    if c == '(':
        floor = floor + 1
    elif c == ')':
        floor = floor - 1

print floor
