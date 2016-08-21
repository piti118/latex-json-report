from os import path
import subprocess

def compile(driver_file, cwd):
    # compile
    out = subprocess.run(['xelatex', driver_file],
                         cwd=cwd,
                         stdout=subprocess.PIPE)

    base = path.splitext(driver_file)[0]

    if out.returncode == 0:
        return path.join(cwd, base+'.pdf')
    else:
        raise Exception('Fail to compile: ' + out.stdout.decode('utf-8'))
