import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch

class HsiMachine(nn.Module):
    def __init__(self):
        super().__init__()
        self.N_BANDS = 242
        self.machine = nn.ModuleList([nn.Sequential(
            nn.Conv2d(1, 8, (4, 4)),
            nn.ReLU(),
            nn.MaxPool2d((2, 2)),
            nn.Conv2d(8, 16, (4, 4)),
            nn.ReLU(),
            nn.MaxPool2d((2, 2)),
            nn.Flatten(),
            nn.Linear(400, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        ) for i in range(self.N_BANDS)])

        self.fc = nn.Sequential(
            nn.Linear(self.N_BANDS, 12),
            nn.ReLU(),
            nn.Linear(12,1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = [self.machine[i](x[:,i]) for i in range(self.N_BANDS)]
        x = torch.stack(x, dim=1)
        x = x.squeeze(dim=2)
        x = self.fc(x)
        return x

