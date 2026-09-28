# Password Generator

A tiny Python script that generates a random 12-character password and prints it to the terminal.

## Features

- Mixes lowercase letters, uppercase letters, numbers, and symbols
- No dependencies, just the Python standard library
- Runs in one command

## Requirements

- Python 3.6+

## Usage

```bash
python password_generator.py
```

Example output:

```
aT7$kQ2&mZp9
```

## How it works

The script joins four character sets (lowercase, uppercase, symbols, digits) into one pool, then uses `random.sample()` to pick 12 characters from it and joins them into a string.

## Customizing

- **Length:** change `k=12` to whatever you want (max is 70, the size of the pool).
- **Symbols:** edit the `symbols` string to add or remove characters.

## Limitations

- `random.sample()` picks without replacement, so a character never appears twice in the same password.
- The `random` module isn't cryptographically secure. This is fine for learning or throwaway passwords, but don't use it for anything important.

## License

MIT
