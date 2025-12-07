#!/usr/bin/env python3
"""
Train MedFusion model with specified configuration
"""

import argparse
import yaml
import torch
from models.medfusion import MedFusion
from training.trainer import Trainer
from data.mmmed_dataset import MMMEDDataset

def main():
    parser = argparse.ArgumentParser(description="Train MedFusion model")
    parser.add_argument("--config", type=str, required=True,
                       help="Path to configuration file")
    parser.add_argument("--output_dir", type=str, default="results/medfusion",
                       help="Output directory for results")
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu",
                       help="Device to use (cuda/cpu)")
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Initialize model
    model = MedFusion(config['model'])
    
    # Initialize dataset
    dataset = MMMEDDataset(**config['data'])
    
    # Initialize trainer
    trainer = Trainer(
        model=model,
        dataset=dataset,
        config=config['training'],
        output_dir=args.output_dir,
        device=args.device
    )
    
    # Train
    trainer.train()
    
    # Evaluate
    results = trainer.evaluate()
    
    print(f"Training completed. Results: {results}")

if __name__ == "__main__":
    main()
