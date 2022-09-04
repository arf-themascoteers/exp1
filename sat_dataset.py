import os

import PIL.Image
import pandas as pd
import torch
from torchvision.io import read_image
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torchvision import transforms
from matplotlib import pyplot as plt
import os
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn import model_selection

class SatDataset(Dataset):
    def __init__(self, is_train=True):
        self.is_train = is_train
        self.img_dir = "data/out/patches"
        self.csv_file_location = "data/out/csv.csv"
        self.work_csv_file_location = "data/out/work.csv"
        self.transforms = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize(64)
        ])
        self.count_bands = len(os.listdir(self.img_dir))
        self.count_patches = len(os.listdir(os.path.join(self.img_dir,"1")))
        self.image_list = []
        self.dem_list = []
        self.soc_list = []
        df = pd.read_csv(self.csv_file_location)
        train, test = model_selection.train_test_split(df, test_size=0.2)
        df = train
        if not self.is_train:
            df = test

        df = self._preprocess(df)
        df.to_csv(self.work_csv_file_location)
        exit(0)
        i = 0
        for patch in range(1,):
            self.image_list.append(image)
            self.age_list.append(age)
            i = i + 1

        self.__scale__()

    def _preprocess(self, df):
        self.__scale__(df)
        return df

    def __scale__(self, df):
        self.__scale_col__(df, "elevation")
        self.__scale_col__(df, "soc")
        return df

    def __scale_col__(self, df, col):
        x = df[[col]].values.astype(float)
        min_max_scaler = MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        df[col] = x_scaled
        return df

    def unscale(self, values):
        values = [[i] for i in values]
        values = self.scaler.inverse_transform(values)
        values = [i[0] for i in values]
        return values

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, idx):
        image_name = self.image_list[idx]
        age = self.age_list[idx]
        age_torch = self.age_torch_list[idx]
        img_path = os.path.join(self.img_dir, age, image_name)
        image = PIL.Image.open(img_path)
        image = self.transforms(image)
        return image, age_torch

if __name__ == "__main__":
    cid = SatDataset()
    dataloader = DataLoader(cid, batch_size=1, shuffle=True)

