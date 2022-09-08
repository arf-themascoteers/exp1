import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch
from torchvision.models import resnet50, ResNet50_Weights


class HsiMachine(nn.Module):
    def __init__(self):
        super().__init__()
        self.N_BANDS = 5
        self.LENGTH = 32
        self.VECTOR_LENGTH = 3
        self.band_net = nn.ModuleList([nn.Sequential(
            nn.Linear(self.LENGTH* self.LENGTH, 64),
            nn.ReLU(),
            nn.Linear(64, self.VECTOR_LENGTH),
        ) for i in range(self.N_BANDS)])

        self.fc = nn.Sequential(
            nn.Linear(self.N_BANDS * self.VECTOR_LENGTH, 16),
            nn.ReLU(),
            nn.Linear(16,1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = x.reshape(x.shape[0], self.N_BANDS, -1)
        x = [self.band_net[i](x[:,i]) for i in range(self.N_BANDS)]
        x = torch.stack(x, dim=1)
        x = x.squeeze(dim=2)
        x = self.fc(x)
        return x

