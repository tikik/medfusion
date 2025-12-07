# MedFusion: Medical Multimodal VQA for Clinical Assistance

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

## 📋 Overview
MedFusion is a reproducible multimodal Visual Question Answering (VQA) system for clinical decision support, evaluated on the MMMED benchmark.

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/yourusername/medfusion.git
cd medfusion

# Install dependencies
pip install -r requirements.txt

# Download data
python scripts/download_data.py

# Run baseline experiments
python scripts/generate_baselines.py

# Train MedFusion
python scripts/train_medfusion.py --config experiments/configs/medfusion_simple_cnn.yaml
