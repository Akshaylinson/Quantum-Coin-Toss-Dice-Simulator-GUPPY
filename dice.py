# circuits/dice.py
"""
Quantum Coin Toss & Dice Simulator - Circuits
"""

from qiskit import QuantumCircuit
from qiskit.compiler import transpile


def build_coin_circuit():
    """
    1-qubit coin toss circuit:
    Apply Hadamard to create superposition, then measure.
    """
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    return qc


def build_dice_circuit():
    """
    3-qubit dice circuit:
    Apply Hadamard on each qubit, then measure all.
    Produces values 0–7; we'll reject 6 and 7 in main.py.
    """
    qc = QuantumCircuit(3, 3)
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc


def run_circuit_return_counts(qc, shots, backend):
    """
    Run a circuit on the provided backend and return counts (bitstring -> freq).
    """
    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=shots)
    result = job.result()
    return result.get_counts()

