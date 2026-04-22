# 🧬 Error Correction in Reads (Bioinformatics)

> **Rosalind Problem:** Identification and correction of sequencing errors in DNA reads using Hamming Distance and Reverse Complements.

---

## 🌟 Overview
This project implements a robust error-correction pipeline for DNA reads. In DNA sequencing, machines often make small mistakes (point mutations). This algorithm acts as a "biological filter" to separate real genetic information from technical noise.

---

## 🎯 Why This Matters?

### 🧪 Biology:
**Data Integrity:** If we don't correct these errors, we might misdiagnose a genetic disease or fail to identify a virus strain. Structure determines function, and correct data determines the right diagnosis.

### 💻 IT & Algorithms:
- **Hamming Distance:** Precise error detection by finding exactly 1-base differences.
- **Canonical Representation:** Optimizing memory by treating a DNA string and its Reverse Complement as the same entity.
- **Complexity:** Achieving efficient processing using Python `sets` and `dictionaries` for O(N*M) performance.

---

## 🛠️ Technologies & Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=apple-terminal&logoColor=white)

---

## 🚀 Algorithm Steps

1.  **Preprocessing:** Collect all DNA sequences and their reverse complements.
2.  **Frequency Analysis:** Count occurrences. Reads appearing $\ge 2$ times (including reverse complements) are marked as **Correct**.
3.  **Identification:** Reads appearing only once are flagged as **Incorrect**.
4.  **Correction:** Each incorrect read is compared against the `correct_pool`.
5.  **Output:** Map the error to its single-point mutation fix: `Error->Correction`.

---

## 💻 How to Use

### Install
1. Clone the repository:
   ```bash
   git clone [https://github.com/usershokhrukh/rosalind-problems](https://github.com/usershokhrukh/rosalind-problems)