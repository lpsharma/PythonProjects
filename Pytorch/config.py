import torch

class Config:
    # Data parameters
    batch_size = 64
    num_workers = 4

    # Model parameters
    num_classes = 10
    learning_rate = 0.001
    num_epochs = 20

    # Device configuration
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Paths
    data_path = './data'
    weights_path = './weights'
