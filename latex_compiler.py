from os import path
import subprocess

def compile(driver_file, cwd, pipe=True):
    # compile
    print('wtf')
    opt = dict(stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    opt = opt if pipe else {}
    out = subprocess.run(['xelatex', '-halt-on-error', driver_file],
                         cwd=cwd)
                        #  stdout=subprocess.PIPE,
                        #  stderr=subprocess.STDOUT)
    base = path.splitext(driver_file)[0]

    if out.returncode == 0:
        return path.join(cwd, base+'.pdf')
    else:
        output = out.stdout.decode('utf-8') if pipe else 'See above'
        raise Exception('Fail to compilation: ' + output)
