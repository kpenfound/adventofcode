input = process.argv[2]

groups = input.split(',')
g1 = groups[0].split('-')
ls = parseInt(g1[0])
le = parseInt(g1[1])

g2 = groups[1].split('-')
rs = parseInt(g2[0])
re = parseInt(g2[1])

overlap = 0
if (ls >= rs && le <= re) {
  overlap = 1
} else if (rs >= ls && re <= le) {
  overlap = 1
} else if (le >= rs && ls <= rs) {
  overlap = 1
} else if (re >= ls && rs <= ls) {
  overlap = 1
} else {
  overlap = 0
}

console.log(overlap)