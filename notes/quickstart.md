# Quickstart

## Kompilácia

```bash
cd src
make build ARCH=x86-64-modern COMP=clang
```

Binárka vznikne na: `src/stockfish`

## Spustenie (interaktívny UCI mód)

```bash
./src/stockfish
```

## Otestovať Crazyhouse

```bash
echo -e "setoption name UCI_Variant value crazyhouse\nisready\nquit" | ./src/stockfish
# Očakávaný výstup: readyok
```

## Rýchly benchmark

```bash
echo -e "setoption name UCI_Variant value crazyhouse\nbench 128 1 10 default depth\nquit" | ./src/stockfish
```

## UCI príkazy (manuálne)

```
setoption name UCI_Variant value crazyhouse
position startpos
go depth 15
```

## Kde čo je

| Čo | Kde |
|---|---|
| Binárka | `src/stockfish` |
| C++ zdroje | `src/*.cpp` |
| NNUE kód | `src/nnue/` |
| Testy | `tests/` |
| Poznámky | `notes/` |
