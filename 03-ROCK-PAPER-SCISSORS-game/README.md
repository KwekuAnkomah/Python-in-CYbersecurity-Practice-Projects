# Rock, Paper, Scissors

A CLI Rock, Paper, Scissors game against the computer, played as a best-of-3 match.

## What it does
- Computer picks randomly from rock, paper, or scissors each round
- Compares choices and tracks wins, losses, and ties across the match
- Validates input and rejects anything that isn't rock, paper, or scissors
- Lets the player quit mid-match by typing "q"
- After a match ends, asks to play again — resets scores and rounds cleanly for a fresh match

## What I learned
- Using `random.choice()` to pick from a list instead of a number range
- Wrapping an existing program in an outer "play again" loop (same two-loop pattern as the guessing game)
- Why loop variables need to be reset inside the outer loop, not just declared once at the top — otherwise leftover values carry into the next round
- Why the order of `elif` checks matters — a more general check can accidentally catch a case meant for a more specific one further down
- Using a dedicated flag (`quit_game`) to break out of both the inner and outer loop cleanly when the player quits mid-match
