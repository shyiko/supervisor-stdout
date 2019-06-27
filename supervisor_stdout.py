from __future__ import print_function
import sys

def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def main():
    while 1:
        write_stdout('READY\n') # transition from ACKNOWLEDGED to READY
        line = sys.stdin.readline() # read header line from stdin
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len'])) # read the event payload
        write_stdout('RESULT %s\n%s'%(len(data), data)) # transition from READY to ACKNOWLEDGED

def event_handler(event, response):
    line, data = response.split('\n', 1)
    headers = dict([ x.split(':') for x in line.split() ])
    lines = data.strip().split('\n')
    prefix = '%s: '%(headers['processname'])
    print('\n'.join([ prefix + l for l in lines]),
        file=sys.stdout if headers['channel'] == 'stdout' else sys.stderr)

if __name__ == '__main__':
    main()
