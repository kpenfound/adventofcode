scores = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' // plus 1

input = process.argv[2]
c1 = input.substring(0, input.length / 2)
c2 = input.substring(input.length / 2, input.length)

for (var i = 0; i < c1.length; i++) {
  if (c2.indexOf(c1.charAt(i)) != -1) {
    console.log(scores.indexOf(c1.charAt(i)) + 1)
    break
  }
}
