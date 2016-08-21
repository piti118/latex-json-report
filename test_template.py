from os import path
from importlib import import_module
import os
import shutil
import sys
import argparse


def main(module_name):
    # module_name = 'templates.ultimate_sample_template'

    module = import_module(module_name)

    t = module.template()
    tmpdir = path.join(path.dirname(__file__), 'tmp')
    print('Working on '+tmpdir)
    shutil.rmtree(tmpdir)
    os.makedirs(tmpdir)
    t.compile(t.sample_data(), tmpdir, pipe=False)

    print('see output at '+tmpdir+'/driver.pdf')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
        "Test template.\n" +
        'Ex: python test_template.py templates.basic_template',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('module', metavar='module', type=str, nargs=1,
        help='template module name(ex: templates.basic_template)')
    args = parser.parse_args()
    main(args.module[0])
