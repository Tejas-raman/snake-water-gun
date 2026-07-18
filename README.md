# Snake Water Gun 🐍💧🔫

A terminal-based Python game built from scratch while learning core Python fundamentals.

---

## About

This was my first complete Python project, built during Week 1 of self-studying Python.  
The goal was to apply what I was learning — functions, dictionaries, loops — into something that actually runs.

---

## How to Play

```bash
python snake_water_gun.py
```

Enter `snake`, `water`, or `gun` when prompted.  
The computer picks randomly. First to get bored quits.

**Rules:**
- Snake drinks Water → Snake wins
- Water drowns Gun → Water wins  
- Gun shoots Snake → Gun wins

---

## Features

- Random computer choice using `random.choice()`
- Score tracking across rounds
- Play again prompt after each round
- Final score display when you quit
- Input validation for invalid entries

---

## Concepts Used

| Concept | Where |
|---|---|
| Functions | `game()` returns `"user"`, `"computer"`, or `"tie"` |
| Dictionaries | Map user input (`"snake"`) to internal values (`-1`) |
| Reverse dictionary | Convert computer's value back to readable word |
| Loops | `while True` for replay, counters for score |
| Return values | Function result used to update score outside the function |
| Conditionals | Win/lose/tie logic |
| Random module | `random.choice([-1, 0, 1])` for computer move |

---

## What I Learned

- Return values let functions communicate results to the rest of the program — the function doesn't need to know about the score, it just returns who won
- Input validation has to happen **before** converting input to dictionary values, not after
- Counters need to live **outside** the function so they persist across rounds
- `while True` with `break` is a clean pattern for "keep going until the user says stop"

---

## Known Mistakes Made During Development

Keeping these here because mistakes are part of learning:

- Used `random.choice(-1, 0, 1)` instead of `random.choice([-1, 0, 1])` — forgot it needs a list
- Tried to update score inside the function instead of using a return value
- Ran input validation after dictionary conversion, which broke it for invalid inputs

---

## Development Notes

Written and debugged by me while learning Python.  
Used Claude and ChatGPT for concept explanations (recursion, return values, dictionary syntax, loop structure) — not for writing the code.

---

## Status

✅ Complete — first project, learning purposes.  
Part of my Python self-study journey targeting MS in AI/ML .
