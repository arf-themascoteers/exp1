import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torch
from torchvision.models import resnet50, ResNet50_Weights


class HsiMachine(nn.Module):
    def __init__(self):
        super().__init__()
        self.N_BANDS = 242
        self.resnets = nn.ModuleList([resnet50() for i in range(self.N_BANDS)])

        for a_resnet in self.resnets:
            number_input = a_resnet.fc.in_features
            a_resnet.fc = nn.Sequential(
                nn.Linear(number_input, 256),
                nn.BatchNorm1d(256),
                nn.ReLU(),
                nn.Linear(256, 1),
            )
            weights_data = a_resnet.conv1.weight.data[:, 0]
            weights_data = weights_data.reshape(weights_data.shape[0], 1, weights_data.shape[1], weights_data.shape[2])
            a_resnet.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
            a_resnet.conv1.weight.data = weights_data

            for param in a_resnet.layer1.parameters():
                param.requires_grad = False

            for param in a_resnet.layer2.parameters():
                param.requires_grad = False

            for param in a_resnet.layer3.parameters():
                param.requires_grad = False

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

