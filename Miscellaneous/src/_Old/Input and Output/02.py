from sarge import capture_stdout

from sarge import run
p = capture_stdout('ls')
print p.stdout.text.upper()
