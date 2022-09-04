import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch

class SatMachine(nn.Module):
    def __init__(self):
        super().__init__()
        self.N_BANDS = 12
        self.machine = nn.Sequential(
                nn.Conv3d(1, 8, (1, 7, 7)),
                nn.ReLU(),
                nn.MaxPool3d((1, 4, 4)),
                nn.Conv3d(8, 16, (1, 7, 7)),
                nn.ReLU(),
                nn.MaxPool3d((1, 4, 4)),
                nn.Conv3d(16, 32, (4, 1, 1)),
                nn.ReLU(),
                nn.MaxPool3d((3, 1, 1)),
                nn.Flatten(),
                nn.Linear(384, 128),
                nn.ReLU(),
                nn.Linear(128, 1),
                nn.Sigmoid()
        )

    def forward(self, x):
        x = self.machine(x)
        return x

