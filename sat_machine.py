import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch

class SatMachine(nn.Module):
    def __init__(self):
        super().__init__()
        self.N_BANDS = 9
        self.machine = nn.Sequential(
                nn.Conv3d(1, 8, (1, 4, 4)),
                nn.ReLU(),
                nn.MaxPool3d((1, 2, 2)),
                nn.Conv3d(8, 16, (3, 1, 1)),
                nn.ReLU(),
                nn.MaxPool3d((3, 1, 1)),
                nn.Flatten(),
                nn.Linear(1152, 128),
                nn.ReLU(),
                nn.Linear(128, 3)
        )

        self.fc = nn.Sequential(
            nn.Linear(4,2),
            nn.ReLU(),
            nn.Linear(2,1),
            nn.Sigmoid()
        )

    def forward(self, x, elevation):
        x = self.machine(x)
        x = torch.cat((x, elevation), dim=1)
        x = self.fc(x)
        return x

