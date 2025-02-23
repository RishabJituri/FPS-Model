import torch
from torch import nn 
from torch import functional as F
from torch.utils.data import Dataset

class dataset(Dataset):
    def __init__(self, difficulty: str):
        super.__init__()
        

