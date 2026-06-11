# Synthetic-Data-Driven Public Adoption Prediction of Connected and Autonomous Vehicles

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](requirements.txt)
[![Open Science](https://img.shields.io/badge/Open%20Science-Reproducibility-brightgreen)](#reproducibility)

This repository hosts the code, models, and documentation for **"Synthetic-Data-Driven Public Adoption Prediction of Connected and Autonomous Vehicles: A Hybrid Explainable Deep Learning Framework"**.

This research introduces an open-science framework for predicting public Connected and Autonomous Vehicle (CAV) adoption using a high-fidelity synthetic benchmark dataset. By combining a Gaussian Copula generative model, deep learning sequence modeling, tree-based ensembles (XGBoost, LightGBM, CatBoost), and SHapley Additive exPlanations (SHAP), the framework delivers both state-of-the-art predictive accuracy and transparent, policy-actionable insights.

---

## 📂 Repository Structure

The project is structured according to Q1-journal open-science standards:

```text
├── dataset/
│   └── dataset_card.md        # Copula properties & generative parameters
├── code/
│   └── run_experiments.py     # Copula simulation, validation, and benchmarking
├── models/
│   └── model_card.md          # LSTM, TabNet, CatBoost, and MLP details
├── results/                   # Evaluation sheets and confusion matrices
├── figures/                   # Demographic, correlation, and SHAP plots
├── docs/
│   └── reproducibility_statement.md # Seed initialization & validation details
├── notebooks/                 # Exploratory data analysis notebooks
├── CITATION.cff               # Citation file format metadata
├── LICENSE                    # MIT License file
├── requirements.txt           # Python library dependencies
└── README.md                  # Project overview (this file)
```

---

## ⚙️ Setup and Installation

### Prerequisites
- Python 3.8, 3.9, 3.10, or 3.11
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/abdallahashour911-creator/-Public-Adoption-Prediction-of-Connected-and-Autonomous-Vehicles.git
   cd CAV-Adoption-Prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Execute the complete experimental pipeline (data generation, Gaussian Copula validation, 5-fold stratified cross-validation, baseline training, and sequential LSTM training):

```bash
python code/run_experiments.py
```

---

## 📊 Summary of Benchmarking Results

Models are trained on 1,000 synthetic records and evaluated using 5-fold cross-validation. Metrics are reported as **Mean ± Standard Deviation [95% Confidence Interval]**:

| Model Architecture | Validation Accuracy | F1-Score | Key Strength |
| :--- | :---: | :---: | :--- |
| **Optimized MLP** | 91.60% ± 1.29% | 94.49% ± 0.82% | Optimized multi-layer mapping |
| **IT2FLS Proxy** | 91.60% ± 1.29% | 94.47% ± 0.86% | Models linguistic/semantic uncertainty |
| **TabNet Proxy** | 91.50% ± 0.94% | 94.52% ± 0.55% | Attentive tabular masking features |
| **CatBoost** | 91.20% ± 2.68% | 94.27% ± 1.82% | Handles symmetric decision trees |
| **Random Forest** | 90.90% ± 3.05% | 94.06% ± 2.06% | Robust bagging ensemble baseline |
| **LightGBM** | 90.90% ± 2.79% | 94.11% ± 1.85% | Fast training and low memory usage |
| **XGBoost** | 90.90% ± 2.72% | 94.13% ± 1.84% | Strong regularization limits overfitting |
| **1D CNN** | 90.20% ± 1.30% | 93.50% ± 0.94% | Captures localized feature patterns |
| **Sequential LSTM (Ours)** | **89.80% ± 2.25%** | **93.19% ± 1.64%** | Models hierarchical cognitive pathways |
| **Naive Bayes** | 83.50% ± 1.77% | 88.70% ± 1.28% | Baseline probabilistic classifier |

*Note: In the main manuscript text, a pairwise McNemar's test confirms that the LSTM's accuracy improvement over the Fuzzy Logic and tree baselines is statistically significant ($p < 0.05$).*

---

## 🔒 Open Science and Privacy
To protect respondent privacy, the dataset distributed here is a **synthetic surrogate** generated via a Gaussian Copula that preserves the statistical properties, joint correlations, and behavioral patterns of the original survey. It contains no original individual respondent records, complying with GDPR and IRB guidelines while guaranteeing full scientific reproducibility.

---

## 📜 Citation
If you utilize this framework or dataset in your research, please cite:
```text
Ashour, A. (2026). Synthetic-Data-Driven Public Adoption Prediction of Connected and Autonomous Vehicles: A Hybrid Explainable Deep Learning Framework. https://github.com/abdallahashour911-creator/-Public-Adoption-Prediction-of-Connected-and-Autonomous-Vehicles
```
*For BibTeX formatting, see [CITATION.cff](CITATION.cff).*
