#!/usr/bin/env python3
"""Jednoduchý interaktívny Crazyhouse vs Fairy-Stockfish."""

import subprocess
import sys

ENGINE = "./src/stockfish"
MOVETIME = 2000  # ms na ťah

def send(proc, cmd):
    proc.stdin.write(cmd + "\n")
    proc.stdin.flush()

def read_until(proc, keyword):
    lines = []
    while True:
        line = proc.stdout.readline().strip()
        if line:
            lines.append(line)
            print(f"  [engine] {line}")
        if keyword in line:
            return lines

def extract_bestmove(lines):
    for line in reversed(lines):
        if line.startswith("bestmove"):
            return line.split()[1]
    return None

def print_board(moves):
    print(f"\n  Ťahy: {' '.join(moves) if moves else '(začiatok)'}")
    print()

def main():
    print("=== Fairy-Stockfish Crazyhouse ===")
    print("Ty = Biely, Engine = Čierny")
    print("Zadávaj ťahy vo formáte UCI napr: e2e4, g1f3, P@e5 (drop)")
    print("'quit' = koniec\n")

    proc = subprocess.Popen(
        [ENGINE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    send(proc, "uci")
    read_until(proc, "uciok")
    send(proc, "setoption name UCI_Variant value crazyhouse")
    send(proc, "isready")
    read_until(proc, "readyok")
    print("Engine pripravený!\n")

    moves = []

    while True:
        print_board(moves)
        move = input("Tvoj ťah (Biely): ").strip()
        if move == "quit":
            break
        if not move:
            continue

        moves.append(move)
        pos = "position startpos" + (f" moves {' '.join(moves)}" if moves else "")
        send(proc, pos)
        send(proc, f"go movetime {MOVETIME}")
        lines = read_until(proc, "bestmove")
        engine_move = extract_bestmove(lines)

        if not engine_move or engine_move == "(none)":
            print("Engine nemá ťah — koniec partie.")
            break

        moves.append(engine_move)
        print(f"\n  >>> Engine hrá: {engine_move}\n")

    send(proc, "quit")
    proc.wait()
    print("Koniec partie.")

if __name__ == "__main__":
    main()
