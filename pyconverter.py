#!/usr/bin/env python3.6
import imageio
import os
import rawpy
import sys

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'


source_dir = sys.argv[1]
out_dir = os.path.join(source_dir, 'out')
source_ext = sys.argv[2]
dest_ext = sys.argv[3]


def convert(source_filename: str):
    print(f'Processing {source_filename}... ', end='')
    dest_filename = os.path.join(out_dir, source_filename.replace(source_ext, dest_ext))
    with rawpy.imread(os.path.join(source_dir, source_filename)) as raw:
        rgb = raw.postprocess()
    imageio.imsave(dest_filename, rgb)
    print('done')


os.makedirs(out_dir, exist_ok=True)
filename_gen = (filename for filename in os.listdir(source_dir) if filename.endswith(source_ext))
for source_filename in filename_gen:
    convert(source_filename)
