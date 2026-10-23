import torch

def mse(pred, target):
    return ((pred - target) ** 2).mean().item()