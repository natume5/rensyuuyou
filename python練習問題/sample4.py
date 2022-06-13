#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


parser = argparse.ArgumentParser(description='サンプルスクリプトです。')


parser.add_argument('arg1', type=int, help='hogeを指定してください。')
parser.add_argument('arg2', type=str, help='fooを指定してください。')
parser.add_argument("--opt1", default=10, help="fugaを指定してください。")
parser.add_argument("--opt2", help="hugaを指定してください。任意です。")

args = parser.parse_args()

print(args.arg1)
print(args.arg2)
print(args.opt1)
print(args.opt2)

