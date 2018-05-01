#! /usr/bin/env python

import asciimage
import argparse
import sys
import os

parser = argparse.ArgumentParser(
    description="Convert an image into ASCII art")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-l", help="Local file path")
group.add_argument("-u", help="Remote image url")

parser.add_argument(
    "-g", help="Show the image in grayscale", action='store_true')
parser.add_argument(
    "-s", help="To HTML", action="store_true")

args = parser.parse_args()

options = asciimage.Options(args)

image = None
if args.l:
    image = asciimage.get_from_file(args.l)
else:
    image = asciimage.get_from_url(args.u)

y, x = os.popen('stty size', 'r').read().split()
output = asciimage.to_ascii(image, asciimage.Screen((x, y)), options)

writer = asciimage.FileWriter(options.to_html())
writer.write(output)
