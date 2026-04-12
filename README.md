# Shor's Algorithm

A quantum algorithm that factors integers exponentially faster 
than any known classical algorithm, threatening the foundation 
of modern RSA encryption.

## Why It Matters

RSA encryption — which secures most internet communications — 
relies on the fact that factoring large numbers is computationally 
hard. A classical computer would take longer than the age of the 
universe to factor a 2048-bit RSA key. Shor's algorithm makes 
this tractable on quantum hardware, making current encryption 
potentially breakable.

## How It Works

Shor's algorithm has two parts:

1. **Classical part** — reduces the factoring problem into 
   finding the period of the function f(x) = a^x mod N
2. **Quantum part** — uses superposition to evaluate f(x) 
   for all values of x simultaneously, then applies the 
   Quantum Fourier Transform to extract the period

Once the period r is found, the factors are calculated using:
- factor1 = gcd(a^(r/2) + 1, N)
- factor2 = gcd(a^(r/2) - 1, N)

## This Implementation

Demonstrates Shor's algorithm on N=15 with a=7:
- Quantum circuit finds period r=4
- Classical extraction calculates factors: **3 and 5**
- Verified: 3 × 5 = 15 ✓

## Installation

pip install qiskit qiskit-aer numpy

## Requirements
- Python 3.8+
- Qiskit 2.0+
- Qiskit-Aer 0.17+
- NumPy