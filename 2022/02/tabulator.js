playPoints = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

matchPoints = {
  'WIN': 6,
  'DRAW': 3,
  'LOSS': 0
}

matchUps = {
  'A': { // Rock
    'X': matchPoints['DRAW'], // Rock
    'Y': matchPoints['WIN'],  // Paper
    'Z': matchPoints['LOSS']  // Scissors
  },
  'B': { // Paper
    'X': matchPoints['LOSS'], // Rock
    'Y': matchPoints['DRAW'], // Paper
    'Z': matchPoints['WIN']   // Scissors
  },
  'C': { // Scissors
    'X': matchPoints['WIN'],  // Rock
    'Y': matchPoints['LOSS'], // Paper
    'Z': matchPoints['DRAW']  // Scissors
  }
}

inputs = process.argv[2].split(' ');
l = inputs[0]
r = inputs[1]

score = playPoints[r] + matchUps[l][r]

console.log(score)