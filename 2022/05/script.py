import anyio
import dagger
import sys
import time

async def main():
  host = 'host.docker.internal'
  ts = str(int(time.time()))
  async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
    base = client.container().from_('redis').with_env_variable('NOCACHE', ts)
    last_stack = 0

    stacking = True
    with open('input.txt', 'r') as _file:
      for line in _file:
        line = line.rstrip()
        if line.startswith('move'): # moving
          stacking = False
          moves = line.split(' ')
          move = int(moves[1])
          move_from = int(moves[3])
          move_to = int(moves[5])
          q = base.with_env_variable('NOCACHE', time.time_ns())
          for x in range(move):
            q = q.with_exec(['redis-cli', '-h', host, 'LMOVE', stack(ts,move_from), stack(ts,'temp'), 'RIGHT', 'RIGHT'])
          for x in range(move):
            q = q.with_exec(['redis-cli', '-h', host, 'LMOVE', stack(ts,'temp'), stack(ts,move_to), 'RIGHT', 'RIGHT'])
          await q.stdout()
        elif stacking: # stacking parsing
          for i, c in enumerate(line):
            if c.isalpha():
              _stack = int((i - 1) / 4) + 1
              last_stack = max(last_stack, _stack)
              q = base.with_exec(['redis-cli', '-h', host, 'LPUSH', stack(ts,_stack), c])
              await q.stdout()
    for x in range(last_stack):
      q = base.with_exec(['redis-cli', '-h', host, 'LMOVE', stack(ts,x+1), stack(ts,'answer'), 'RIGHT', 'RIGHT'])
      await q.stdout()
    q = base.with_exec(['redis-cli', '-h', host, 'LRANGE', stack(ts,'answer'), '0', '-1'])
    out = await q.stdout()
    print('answer is', out.replace('\n',''))

def stack(key, num):
  return str(key) + '-' + str(num)

if __name__ == "__main__":
  anyio.run(main)