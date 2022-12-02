import anyio
import dagger

async def main():
  max = 0
  args = ['expr', '0']
  async with dagger.Connection() as client:
    base = client.container().from_('alpine')
    with open('input.txt', 'r') as _file:
      for line in _file:
        if line == "\n":
          elf = base.with_exec(args)
          total = int(await elf.stdout())
          if total > max:
            max = total
          args = ['expr', '0']
        else:
          args.append('+')
          args.append(line.rstrip())
  print('answer is', max)

if __name__ == "__main__":
  anyio.run(main)