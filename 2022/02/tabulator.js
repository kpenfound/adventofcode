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

pt2 = {
  'A': { // Rock
    'X': 'Z', // Lose
    'Y': 'X',  // Draw
    'Z': 'Y'  // Win
  },
  'B': { // Paper
    'X': 'X', // Lose
    'Y': 'Y',  // Draw
    'Z': 'Z'  // Win
  },
  'C': { // Scissors
    'X': 'Y', // Lose
    'Y': 'Z',  // Draw
    'Z': 'X'  // Win
  }
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
// pt 2
r = pt2[l][r]

score = playPoints[r] + matchUps[l][r]

console.log(score)