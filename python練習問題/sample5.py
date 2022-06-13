#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--opt1', action='store_const', const=100)
parser.add_argument('--opt2', action='store_true')
parser.add_argument('--opt3', action='store_false')
args = parser.parse_args()

print(args.opt1)
print(args.opt2)
print(args.opt3)
