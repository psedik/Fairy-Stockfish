# Fairy-Stockfish Development

## Context
- **Project**: Fairy-Stockfish — the strongest open-source chess variant engine
- **Language**: C++ (engine), Python bindings (pyffish)
- **Goal**: Master Crazyhouse and other variants
- **Why**: Both Peter and I are Crazyhouse chess enthusiasts 🎯

## Project Structure
```
src/          → C++ source (engine, evaluation, search)
tests/        → Test suite
test.py       → Python test harness
setup.py      → Python package builder
```

## Model Routing (Cost Optimization)

**Use Haiku (cheapest, ~20x less than Sonnet):**
- Exploring repo structure and files
- Reading and understanding code flow
- Building, compiling, running basic tests
- Searching for patterns with Grep/Glob
- Simple debugging (missing #includes, syntax errors)
- Running engine and capturing output

**Use Sonnet (when complexity increases):**
- Debugging hard crashes or segfaults
- Performance optimization (algorithm changes)
- Complex evaluation function improvements
- Architectural decisions for new features
- Code review of non-trivial changes
- Understanding subtle bugs in search algorithm

**Use Opus (rare):**
- Novel algorithms for Crazyhouse evaluation
- Fundamental engine redesigns
- Only if Sonnet clearly insufficient

**Syntax for agents:**
```
Task(subagent_type="general-purpose", model="haiku", prompt="...")
```

## Tools
- **Bash**: Build commands, run engine
- **Glob/Grep**: Search code (faster than file reads for code)
- **Read**: Read config/build files when needed
- **Edit**: Modify source code

## Work Style
- Pragmatic, no overengineering
- Try to figure it out before asking
- When stuck, ask clearly
- Focus on Crazyhouse strength first

## Next Steps
1. Explore src/ structure
2. Build from source
3. Test Crazyhouse play
4. Identify optimization opportunities
