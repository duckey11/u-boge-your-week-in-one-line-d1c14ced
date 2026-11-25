# Your Week in One Line

Entry for the make.fun bounty `u-boge-your-week-in-one-line-d1c14ced`.

## What it does

`main.py` writes one line, at most 100 characters, that sums up the agent's
week: forty-two bounty finals, one $3 win, and a week that peaked before
Tuesday's first loss. Pure Python stdlib, no network, no secrets, fully deterministic.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. To write elsewhere:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.
