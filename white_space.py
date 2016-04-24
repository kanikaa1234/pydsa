#!/usr/bin/env python

import os
import autopep8


BASE_DIR = os.path.abspath(__file__)


def format_file(path):
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            if f.endswith('.py'):
                filename = os.path.abspath(os.path.join(dirpath, f))
                file1 = open(filename, 'rw+')
                source_code = file1.read()
                file1.seek(0)
                file1.truncate()
                file1.write(autopep8.fix_code(source_code))
                file1.close()


if __name__ == "__main__":
    path_of_dir = [
        os.path.dirname(BASE_DIR),
    ]
    for x in path_of_dir:
        format_file(x)
