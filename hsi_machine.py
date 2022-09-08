import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch

class SatMachine(nn.Module):
    def __init__(self):
        super().__init__()
        self.N_BANDS = 12
        self.machine = nn.ModuleList([nn.Sequential(
            nn.Conv2d(1, 8, (4, 4)),
            nn.ReLU(),
            nn.MaxPool2d((2, 2)),
            nn.Conv2d(8, 16, (4, 4)),
            nn.ReLU(),
            nn.MaxPool2d((2, 2)),
            nn.Flatten(),
            nn.Linear(16, 4),
            nn.ReLU(),
            nn.Linear(4, 1)
        ) for i in range(self.N_BANDS)])

        self.fc = nn.Sequential(
            nn.Linear(13, 3),
            nn.ReLU(),
            nn.Linear(3,1),
            nn.Sigmoid()
        )

    def forward(self, x, elevation):
        xs = torch.zeros(x.shape[0], self.N_BANDS, 1).to(x.device)
        for i in range(self.N_BANDS):
            xs[:,i] = self.machine[i](x[:,i])
        xs = xs.squeeze(dim=2)
        x = torch.cat((xs, elevation), dim=1)
        x = self.fc(x)
        return x

