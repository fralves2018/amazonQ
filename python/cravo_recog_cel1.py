# This script sets up data loading and transformation pipelines for an image classification task

from pathlib import Path
import torch
from torchvision import datasets, transforms
from torch.utils.data import random_split, DataLoader

# Directory containing the image dataset
DATA_DIR = Path(r"C:\ReconhecimentoFloresIa\dataset")  # adjust if path changed

# ---------- transforms ----------
# Data augmentation transforms for training:
# - Random cropping to 224x224 pixels while maintaining 80-100% of original area
# - Random horizontal flips
# - Random rotation up to 25 degrees
# - Random color jittering of brightness, contrast, saturation and hue
# - Convert to tensor
transform_train = transforms.Compose([
    transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(25),
    transforms.ColorJitter(brightness=0.2, contrast=0.2,
                           saturation=0.3, hue=0.05),
    transforms.ToTensor()
])

# Validation transforms:
# - Resize images to 224x224 pixels
# - Convert to tensor
transform_val = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# ---------- datasets ----------
# Create dataset objects for training and validation
# Both use ImageFolder which assumes data is organized in class subdirectories
full_ds_trainaug = datasets.ImageFolder(root=DATA_DIR, transform=transform_train)
full_ds_val      = datasets.ImageFolder(root=DATA_DIR, transform=transform_val)

# Print total number of images in the dataset
print("Total imagens (com novas fotos):", len(full_ds_trainaug))
