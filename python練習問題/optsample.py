#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse

def init(lang):
	return lang.split(',')

parser = argparse.ArgumentParser()
parser.add_argument('--langs', type=init)

args = parser.parse_args()

print(args.langs)
