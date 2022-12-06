# 2022 Advent of Code

For the 2022 AOC, I decided to incorporate [dagger](dagger.io) into each solution. Some of them will be a bit of a stretch to involve it at all, but I'll try to be creative.

## Day 1

[Problem](https://adventofcode.com/2022/day/1)

This problem was a simple tabulation. I used the Dagger Python SDK to evaluate math with `expr` in an alpine container.

## Day 2

[Problem](https://adventofcode.com/2022/day/2)

This time I used the Dagger Python SDK to execute a nodejs script. The python script would read the input file line by line, and then send each line individually to the node script to evalute. The python script would tabulate the results.

## Day 3

[Problem](https://adventofcode.com/2022/day/3)

This required a pretty similar solution to day 2, so I used basically the same pattern. A python script used dagger to execute a node script and compute each individual line of the input.

## Day 4

[Problem](https://adventofcode.com/2022/day/4)

Also similar to the previous 2 days in the solution. A python script used dagger to send each line to a nodejs script. The one thing that tripped me up here was at first forgetting to cast string numbers to ints in javascript. That makes comparisons very different.

## Day 5

[Problem](https://adventofcode.com/2022/day/5)

Bored with continually loading a nodejs script from python, I instead used redis to perform set operations. The python script used the dagger sdk to load the redis image and run commands against a local redis server container. This one was a lot of work to solve a simple problem, but it was a unique solution.

## Day 6

[Problem](https://adventofcode.com/2022/day/6)

Now that I'd used python as the entrypoint for 5 days in a row, I decided to mix it up. This time I'm using a bash script to execute GraphQL queries against the dagger engine using the dagger cli. The queries load and build a rust application which reads the input and outputs the solution.
