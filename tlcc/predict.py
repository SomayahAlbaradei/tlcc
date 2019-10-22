#!/usr/bin/env python
import os
import cv2
import argh
import torch

from torchvision import transforms

from model.model import TLCC


def load_model():
    model_ = TLCC()
    dir_ = os.path.dirname(os.path.abspath(__file__))
    checkpoint = torch.load(dir_ + '/../model/TLCC.tar',
                            map_location=torch.device('cpu'))
    # noinspection PyUnresolvedReferences
    model_.load_state_dict(checkpoint['state_dict'])
    return model_

def enhance(image, clip_limit=2):
    # convert image to LAB color model
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    # split the image into L, A, and B channels
    l_channel, a_channel, b_channel = cv2.split(image_lab)
    # apply CLAHE to lightness channel
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(1000, 1000))
    cl = clahe.apply(l_channel)
    # merge the CLAHE enhanced L channel with the original A and B channel
    merged_channels = cv2.merge((cl, a_channel, b_channel))
    # convert iamge from LAB color model back to RGB color model
    final_image = cv2.cvtColor(merged_channels, cv2.COLOR_LAB2BGR)
    return final_image

model = load_model()

def _colony_count(img_path):
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import cm
    transform=transforms.Compose([
        transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                   std=[0.229, 0.224, 0.225]),
    ])
    img_output = os.path.split(img_path)[-1].split('.')[:-1]
    img = cv2.imread(img_path)
    img = enhance(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
    ret3, th3 = cv2.threshold(img_blur, 0, 250, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    img_color = cv2.cvtColor(th3, cv2.COLOR_GRAY2RGB)
    img_transformed = transform(img_color)  #.cuda()
    output = model(img_transformed.unsqueeze(0))
    image = np.asarray(output.detach().cpu().reshape(
        output.detach().cpu().shape[2], output.detach().cpu().shape[3]))
    outf = "".join(img_output) + '_out.jpg'
    plt.imsave(outf, image, cmap=cm.jet)
    pred_count = int(output.detach().cpu().sum().numpy())
    print("Number of colonies predicted: %d" % pred_count)
    return pred_count, outf

def colony_count(img_path):
    _colony_count(img_path)

if __name__ == '__main__':
    argh.dispatch_commands([
        colony_count
    ])