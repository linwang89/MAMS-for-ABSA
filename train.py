import yaml
import os
from train.train import train

config = yaml.load(open('config.yml'))
mode = config['mode']
os.environ["CUDA_VISIBLE_DEVICES"] = str(config['aspect_' + mode + '_model'][config['aspect_' + mode + '_model']['type']]['gpu'])
train(config)