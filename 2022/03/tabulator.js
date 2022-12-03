scores = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' // plus 1

input = process.argv.slice(2)

for (var i = 0; i < input[0].length; i++) {
  if (input[1].indexOf(input[0].charAt(i)) != -1) {
    if (input[2].indexOf(input[0].charAt(i)) != -1) {
      console.log(scores.indexOf(input[0].charAt(i)) + 1)
      break
    }
  }
}
