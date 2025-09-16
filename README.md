 🎲 Quantum Coin Toss & Dice Simulator (Qiskit + Aer)

A quantum-powered simulator for **coin tosses** and **dice rolls**, built with [Qiskit](https://qiskit.org/) and the Aer simulator.  
This project demonstrates how **quantum superposition** can generate fair randomness, beyond classical pseudo-random number generators.

---

## ✨ Features
- **Coin Toss Simulation** 🪙  
  - 1 qubit in superposition (`H` gate).  
  - `0` → **Heads**, `1` → **Tails**.  
  - Fair distribution emerges over many shots.  

- **Dice Simulation** 🎲  
  - 3 qubits in superposition (`H` gates).  
  - Outcomes mapped to integers 1–6.  
  - Uses *rejection sampling* to discard invalid states (`6` and `7` → binary `110` & `111`).  
  - Approaches uniform distribution as shots increase.  

- **Data Export**  
  - Saves raw bitstring counts and first 200 outcomes to `results/dice_results.txt`.  

- **Visualization**  
  - Histograms of raw quantum bitstring outcomes.  
  - Bar charts of coin/dice results.  

---

## 📂 Project Structure
quantum-dice-guppy/
│── main.py # Entry point (runs coin/dice simulation)
│── circuits/
│ └── dice.py # Quantum circuits for coin toss & dice roll
│── results/
│ └── dice_results.txt # Simulation outputs (auto-generated)
│── README.md # Project documentation
│── requirements.txt # Dependencies

yaml
Copy code

---

## ⚙️ Installation
1. Clone or download this repo.  
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows PowerShell
Install dependencies:

bash
Copy code
pip install -r requirements.txt
requirements.txt

txt
Copy code
qiskit
qiskit-aer
matplotlib
🚀 Usage
Run the simulator from the command line:

Coin Toss
bash
Copy code
python main.py --mode coin --shots 50
Simulates 50 coin tosses.

Saves results in results/dice_results.txt.

Generates histograms in results/raw_hist.png and results/coin_hist.png.

Dice Roll
bash
Copy code
python main.py --mode dice --shots 200
Simulates 200 dice rolls.

Saves results in results/dice_results.txt.

Generates histograms in results/raw_hist.png and results/dice_hist.png.

📊 Example Output
Coin Toss (50 shots)
Raw bitstrings: 0: 27, 1: 23

Outcomes: ~27 Heads, ~23 Tails

Histogram: ~50/50 distribution.

Dice Roll (200 shots)
Outcomes: {1: 36, 2: 32, 3: 34, 4: 31, 5: 35, 6: 32}

Histogram: Nearly uniform distribution.

🎓 Learning Objectives
Understand quantum superposition as a randomness source.

Implement Hadamard-based random number generation.

Apply rejection sampling for mapping qubits to dice outcomes.

Practice Qiskit AerSimulator usage for quantum experiments.

📜 License
This project is released under the Apache 2.0 License.

✨ Built with Qiskit, by Guppy Quantum Projects 🐟

yaml
Copy code
