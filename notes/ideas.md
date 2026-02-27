# Čo sa dá robiť — nápady

## 1. Engine vs Engine
Naša buildnutá verzia vs originál (alebo vs seba samého s inými parametrami).
- Nástroj: `cutechess-cli` alebo vlastný Python script
- Cieľ: vidieť ako silný je, porovnať rôzne nastavenia (Skill Level, čas, NNUE vs klasické hodnotenie)
- Výstup: win/loss/draw štatistiky

## 2. GUI — hrať ručne proti engine
Grafické rozhranie kde vidíš šachovnicu a hráš myšou.
- **Nibbler** — GUI pre Leela/Stockfish, podporuje UCI varianty vr. Crazyhouse
- **PyChess** — open source, podporuje Fairy-Stockfish priamo
- **BabaChess / WinBoard** — staršie, ale funkčné
- Stačí nasmerovať GUI na `./src/stockfish`

## 3. Skúmanie zdrojákov
- Ako funguje drop move generácia (`movegen.cpp`)
- Ako je implementovaný pocket (zajaté figúry)
- NNUE architektúra pre varianty (`nnue/features/half_ka_v2_variants.cpp`)
- Kde sú Crazyhouse-špecifické pravidlá (`variant.cpp`, `position.cpp`)

## 4. NNUE sieť pre Crazyhouse
- Aktuálne build nemá žiadnu sieť (`NNUE_EMBEDDING_OFF`, `EvalFile = <empty>`)
- Existujú externé `.nnue` siete trénované na Crazyhouse?
- Lichess/Fairy-Stockfish releases — stiahnuť a načítať

## 5. Tuning / experimentovanie
- Zmeniť `Skill Level` (-20 až 20) — zahrať si aj proti slabšiemu engine
- Multivariantná analýza (`MultiPV`) — nechať engine ukázať top N ťahov
- Zmeniť čas na ťah a sledovať silu

## 6. Vlastné modifikácie
- Tweaknúť hodnotenie figúr pre Crazyhouse (pocket value)
- Experimentovať so search parametrami
