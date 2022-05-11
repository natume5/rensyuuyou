"""grepを使って、文字列"Arizona 479, 501, 870. California 209, 213, 650."
にある数字の部分の全てに一致する正規表現を書く。"""

# !/usr/bin/env bash

echo Arizona:
    479, 501, 870. California:
        209, 213, 650. | grep[[:digit:]]
