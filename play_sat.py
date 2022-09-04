import torch
import torch.nn as nn

class Machine(nn.Module):
    def __init__(self):
        super(Machine, self).__init__()
        self.hidden_dim = 8
        self.num_layers = 1

        self.image_lstm = nn.LSTM(125, self.hidden_dim, self.num_layers, batch_first=True)
        self.image_fc = nn.Linear(self.hidden_dim, 1)

    def forward(self, image, moisture, temperature):
        h0_image = torch.zeros(self.num_layers, image.size(0), self.hidden_dim).requires_grad_()
        c0_image = torch.zeros(self.num_layers, image.size(0), self.hidden_dim).requires_grad_()
        out, (hn, cn) = self.image_lstm(image, (h0_image.detach(), c0_image.detach()))
        x = self.image_fc(out[:,-1,:])
        return x