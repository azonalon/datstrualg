import re
import sys
file = open(sys.argv[0], 'r')

for line in file:
    re.sub(r'$ *def *([^][]]) *:')
