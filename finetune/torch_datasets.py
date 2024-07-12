import os
import pandas as pd
from PIL import Image
import torch
from torch.utils.data import Dataset


class CustomDataset(Dataset):
    def __init__(self, base_path, csv_path, transform=None):
        self.data = pd.read_csv(csv_path)
        self.base_path = base_path
        self.transform = transform
        self.label_map = {'malignant': 1, "benign": 0}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        image = Image.open(os.path.join(self.base_path, row['filename']))
        y = torch.tensor(self.label_map[row['label']])

        if self.transform:
            image = self.transform(image)

        return image, y
