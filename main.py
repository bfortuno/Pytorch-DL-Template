"""
Main entry point for the PyTorch training template.

This script checks for GPU availability and prints a test tensor.
"""

import torch

if torch.cuda.is_available():
    print(f"Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("Using CPU")

x = torch.tensor([1.0, 2.0, 3.0])
print("Tensor:", x)
