# Tasks

## [ ] Opening book pre Crazyhouse
- Stiahnuť subset Lichess Crazyhouse PGN (database.lichess.org)
- Skonvertovať na polyglot `.bin` formát (cez PyChess alebo pgn-extract + polyglot)
- Použiť v cutechess-cli: `-openings file=crazyhouse.bin`

## [ ] Testovací framework (engine vs engine)
- Nainštalovať `cutechess-cli`
- Dve binárky: `stockfish_base` vs `stockfish_modified`
- Openingová kniha (rôzne začiatky hier)
- Skript na vyhodnotenie výsledkov (win/loss/draw)
- 500 hier = detekcia ~10 Elo zlepšenia pri 95% istote
- Zvážiť SPRT namiesto fixného počtu hier
