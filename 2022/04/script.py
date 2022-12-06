import anyio
import dagger
import sys

async def main():
  async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
    sum = 0
    tabulator = client.host().directory('.').file('tabulator.js')
    outputs = client.directory()
    base = (
      client
      .container()
      .from_('node:16')
      .with_mounted_file('/src/tabulator.js', tabulator)
      .with_workdir('/src')
    )

    with open('input.txt', 'r') as _file:
      for line in _file:
        pair = base.with_exec(['node', 'tabulator.js', line.rstrip()])
        sum += int(await pair.stdout())
        
  print('answer is', sum)

if __name__ == "__main__":
  anyio.run(main)