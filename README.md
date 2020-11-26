<h1 align=center>Pyscryptic</h1>

## Why, and, A Bit of history

I Once have a friend who is lazy AF either lazy to learn programming and/or lazy to read. long story short, circumstances forced him to do his thing which need source code written by me, and no other way (the project is somewhat connected and relevant with mine).
so i wrote this to obfuscate thing and making it a little bit harder for him to read, yet still runnable.

I also take this project as a code golfing, and metaprogramming learning project. so the source code also obfuscated or at least minified.

## Installation

> TODO: Add To PyPI
> ```bash
> python3 -m pip install pyscryptic
> ```

## Usage

```bash
python3 -m pyscryptic YOUR_SCRIPT.py
```

example:

```bash
python3 -m pyscryptic main.py
```

this will create obfuscated `main.py` file with new name of `obf_main.py`.
in theory both should run like the original.

```bash
python3 obf_main.py
```
