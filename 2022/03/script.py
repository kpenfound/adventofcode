import anyio
import dagger
import sys

async def main():
  sum = 0
  group = []
  async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
    tabulator = client.host().directory('.').file('tabulator.js')
    base = (
      client
      .container()
      .from_('node:16')
      .with_mounted_file('/src/tabulator.js', tabulator)
      .with_workdir('/src')
    )
    with open('input.txt', 'r') as _file:
      for line in _file:
        group.append(line.rstrip())
        if len(group) == 3:
          round = base.with_exec(['node', 'tabulator.js', group[0], group[1], group[2]])
          sum += int(await round.stdout())
          group = []
  print('answer is', sum)

if __name__ == "__main__":
  anyio.run(main)