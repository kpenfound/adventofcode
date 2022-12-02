import anyio
import dagger

async def main():
  top = [0, 0, 0]
  args = ['expr', '0']
  async with dagger.Connection() as client:
    base = client.container().from_('alpine')
    with open('input.txt', 'r') as _file:
      for line in _file:
        if line.rstrip() == "":
          elf = base.with_exec(args)
          total = int(await elf.stdout())
          if total > top[0]:
            top[0] = total
            top.sort()
          args = ['expr', '0']
        else:
          args.append('+')
          args.append(line.rstrip())
    elf = base.with_exec(args)
    total = int(await elf.stdout())
    if total > top[0]:
      top[0] = total
  print('answer is', sum(top))

if __name__ == "__main__":
  anyio.run(main)