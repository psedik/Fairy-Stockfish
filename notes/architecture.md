# Architecture Notes

## Variant Dispatch

Fairy-Stockfish uses a **runtime data-driven dispatch** model. Each variant is defined
as a `Variant` struct with boolean flags. Position methods read from this struct:

```cpp
pos.blast_on_capture()        // Atomic chess
pos.walling()                 // Duck chess
pos.must_capture()            // Checkers
pos.captures_to_hand()        // Crazyhouse ← key flag
pos.extinction_single_piece() // Extinction chess
pos.check_counting()          // 3-check
pos.flag_region(...)          // Racing Kings
```

These are inline functions (`return var->someFlag`) — trivially cheap to call.

## Crazyhouse Is Not Isolated

Crazyhouse is one of ~20 variants, defined in `variant.cpp:620` as a combination of flags:
- `capturestohand`, `dropLoop`, `pocketSize`, `dropChecks`, `dropPromoted`

There is no separate compilation path for Crazyhouse. The search, movegen, and evaluate
functions check variant flags at runtime throughout (~35 variant-specific branches in
`search.cpp` alone).

## Would Isolating Crazyhouse Improve Performance?

**Conclusion: No, not meaningfully.**

- Inline flag reads are near-zero cost; branch predictor handles "almost always false"
  branches for other variants with >99.9% accuracy
- If flags were compile-time constants, dead-code elimination could remove ~35 branches
  in search — realistic gain: **2–5%**, not worth the engineering effort

## Where Real Crazyhouse Bottlenecks Are

1. **NNUE evaluation of pockets** — `half_ka_v2_variants` handles pocket pieces
2. **Move generation** — every node must generate drop moves in addition to normal moves
3. **Larger search tree** — more legal moves per position due to drops

## Improvement Opportunities

- Better NNUE model trained specifically on Crazyhouse games
- Tuning search parameters for Crazyhouse (currently tuned for standard chess)
- Crazyhouse-specific eval heuristics (piece value in hand vs. on board)
