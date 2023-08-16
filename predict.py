import glob
import os 
import random
import numpy as np
import json
from PIL import Image
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torchvision import models, transforms
from tqdm import tqdm
from torchvision.models import VGG16_Weights
import yaml
import argparse



class_index = ["dog", "cat"]


class Predictor():
    def __init__(self, class_index):
        self.clas_index = class_index

    def predict_max(self, output): # [0.9, 0.1]
        max_id = np.argmax(output.detach().numpy())
        predicted_label = self.clas_index[max_id]
        return predicted_label


predictor = Predictor(class_index)

test_transform = transforms.Compose([
                transforms.Resize(size =512, interpolation=transforms.InterpolationMode.BILINEAR),
                transforms.ToTensor(),
                transforms.Normalize(mean= (0.485, 0.456, 0.406) , std=(0.229, 0.224, 0.225))
    ])


def predict(img):
    # prepare network
    #use_pretrained = True
    net = models.vgg16(weights=None)
    net.classifier[6] = nn.Linear(in_features=4096, out_features=2)
    net.eval()

    # prepare model

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    checkpoint = torch.load('best_score.pth', map_location=device)
    net.load_state_dict(checkpoint['model_state_dict'])

    # prepare input img
    img = test_transform(img)
    img = img.unsqueeze_(0) # (chan, height, width) -> (1, chan, height, width)

    # predict 
    output = net(img)
    response = predictor.predict_max(output)

    return response