import math
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from fractions import Fraction
a = 7
N = 15
def shors_circuit():
    qc = QuantumCircuit(8, 4)
    for i in range(4):
        qc.h(i)
    qc.x(7)
    qc.barrier()
    qc.cx(3, 4)
    qc.cx(3, 5)
    qc.cx(0, 6)
    qc.cx(0, 7)
    qc.barrier()
    qc.h(0)
    qc.cp(-math.pi/2, 0, 1)
    qc.cp(-math.pi/4, 0, 2)
    qc.cp(-math.pi/8, 0, 3)
    qc.h(1)
    qc.cp(-math.pi/2, 1, 2)
    qc.cp(-math.pi/4, 1, 3)
    qc.h(2)
    qc.cp(-math.pi/2, 2, 3)
    qc.h(3)
    qc.swap(0, 3)
    qc.swap(1, 2)
    qc.measure(range(4), range(4))
    return qc
qc = shors_circuit()
print(qc.draw())
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
counts = job.result().get_counts()
print("Raw counts:", counts)
def extract_factors(counts, a, N, n_counting=4):
    measured_phases = []
    for outcome, count in counts.items():
        decimal = int(outcome, 2)
        phase = decimal / (2**n_counting)
        measured_phases.append((phase, count, outcome))
    measured_phases.sort(key=lambda x: x[1], reverse=True)
    print("Top measurement outcomes:")
    for phase, count, outcome in measured_phases[:5]:
        print(f" {outcome} -> decimal {int(outcome,2)} -> phase {phase:.3f} -> count {count}")
    print("\nAttempting to find factors...")
    for phase, count, outcome in measured_phases:
        if phase == 0:
            continue
        frac = Fraction(phase).limit_denominator(N)
        r = frac.denominator
        if r % 2 == 0:
            factor1 = math.gcd(a**(r//2) + 1, N)
            factor2 = math.gcd(a**(r//2) - 1, N)
            if factor1 not in [1, N] and factor2 not in [1, N]:
                print(f"Period r = {r}")
                print(f"Factors of {N}: {factor1} and {factor2}")
                return factor1, factor2
    print("Could not find factors - try running again")
    return None
extract_factors(counts, a=7, N=15)