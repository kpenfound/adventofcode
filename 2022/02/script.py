import anyio
import dagger
import sys

async def main():
  points = 0
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
        round = base.with_exec(['node', 'tabulator.js', line.rstrip()])
        points += int(await round.stdout())
  print('answer is', points)

if __name__ == "__main__":
  anyio.run(main)