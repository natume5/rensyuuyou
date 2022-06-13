#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='1.01')

args = parser.parse_args()

print(args.version)