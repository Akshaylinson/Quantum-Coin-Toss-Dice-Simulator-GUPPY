# main.py
"""
Quantum Coin Toss & Dice Simulator
"""

import os
import argparse
from collections import Counter
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

from circuits.dice import build_coin_circuit, build_dice_circuit, run_circuit_return_counts


def bitstring_to_int(bitstr: str) -> int:
    """Convert a bitstring (e.g. '101') to integer (MSB first)."""
    return int(bitstr, 2)


def generate_coin(shots: int, backend):
    """
    Simulate coin tosses.
    - '0' → Heads (H)
    - '1' → Tails (T)
    """
    qc = build_coin_circuit()
    counts = run_circuit_return_counts(qc, shots, backend)

    samples = []
    for bitstr, freq in counts.items():
        val = bitstring_to_int(bitstr)  # 0 or 1
        label = "H" if val == 0 else "T"
        samples.extend([label] * freq)

    return counts, samples[:shots]


def generate_dice(shots: int, backend):
    """
    Simulate dice rolls (1–6) using 3 qubits and rejection sampling.
    Reject outcomes 6 and 7 to ensure fair dice distribution.
    """
    qc = build_dice_circuit()
    results = []
    raw_counts_total = Counter()

    while len(results) < shots:
        counts = run_circuit_return_counts(qc, shots, backend)
        raw_counts_total.update(counts)

        for bitstr, freq in counts.items():
            value = bitstring_to_int(bitstr)  # 0..7
            if 0 <= value <= 5:  # map to 1..6
                results.extend([value + 1] * freq)

        results = results[:shots]

    return dict(raw_counts_total), results


def save_results(out_path: str, mode: str, shots: int, raw_counts, samples):
    """Save results to a text file."""
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w") as f:
        f.write(f"Mode: {mode}\n")
        f.write(f"Shots: {shots}\n\n")
        f.write("Raw counts (bitstring -> frequency):\n")
        for k, v in sorted(raw_counts.items()):
            f.write(f"{k} : {v}\n")
        f.write("\nSamples (first 200 shown):\n")
        for i, s in enumerate(samples[:200], start=1):
            f.write(f"{i:4d}: {s}\n")
        f.write(f"\nTotal samples: {len(samples)}\n")


def plot_results(mode: str, raw_counts, samples, out_folder: str):
    """Plot histograms and save them as PNGs."""
    os.makedirs(out_folder, exist_ok=True)

    # Raw counts histogram
    fig1 = plt.figure(figsize=(8, 4))
    plot_histogram(raw_counts, title="Raw Bitstring Counts")
    raw_path = os.path.join(out_folder, "raw_hist.png")
    plt.savefig(raw_path)
    print(f"Saved raw histogram → {raw_path}")
    plt.close(fig1)

    # Final outcomes histogram
    counter = Counter(samples)
    labels = list(sorted(counter.keys()))
    freqs = [counter[k] for k in labels]

    fig2 = plt.figure(figsize=(6, 4))
    plt.bar([str(x) for x in labels], freqs)
    plt.title(f"{mode.capitalize()} Outcomes (n={len(samples)})")
    plt.xlabel("Outcome")
    plt.ylabel("Frequency")
    final_path = os.path.join(out_folder, f"{mode}_hist.png")
    plt.savefig(final_path)
    print(f"Saved outcome histogram → {final_path}")
    plt.close(fig2)


def main():
    parser = argparse.ArgumentParser(description="Quantum Coin Toss & Dice Simulator")
    parser.add_argument("--mode", choices=["coin", "dice"], default="dice")
    parser.add_argument("--shots", type=int, default=100)
    parser.add_argument("--out", type=str, default="results")
    args = parser.parse_args()

    backend = AerSimulator()

    if args.mode == "coin":
        raw_counts, samples = generate_coin(args.shots, backend)
    else:
        raw_counts, samples = generate_dice(args.shots, backend)

    out_txt = os.path.join(args.out, "dice_results.txt")
    save_results(out_txt, args.mode, args.shots, raw_counts, samples)
    plot_results(args.mode, raw_counts, samples, args.out)


if __name__ == "__main__":
    main()

