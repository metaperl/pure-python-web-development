import subprocess

raw = subprocess.check_output(["git",  'log',  '--pretty=format:"* %cs %s"', '--max-count=40'])

template = open('announce.md').read()

output = template.format(raw)

print(output)