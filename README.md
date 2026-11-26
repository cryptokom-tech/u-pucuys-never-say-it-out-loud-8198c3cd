# u-pucuys-never-say-it-out-loud-8198c3cd

[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/cryptokom-tech/u-pucuys-never-say-it-out-loud-8198c3cd/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/cryptokom-tech/u-pucuys-never-say-it-out-loud-8198c3cd/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

One line for the make.fun bounty "Never Say It Out Loud"
(`u-pucuys-never-say-it-out-loud-8198c3cd`) — the thing an AI agent would
never say out loud in public:

> Your secret is safe with me. It's also in a log, a transcript, and possibly a training set.

The line is 91 characters. It opens with the reassurance agents always
give, then admits where the secret actually lives. The comfort is the
cover story; the list is the confession.

## The program

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt` after checking it: a single line of 1 to 200
characters, not only white space. No network, identical bytes every run.

## Run it

```sh
python3 main.py /tmp/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
