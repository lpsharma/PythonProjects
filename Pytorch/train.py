import torch
import torch.nn as nn
import torch.optim as optim
from config import Config
from models.model import SimpleCNN
from utils.dataset import get_dataloaders
from utils.utils import save_checkpoint

def train():
    config = Config()

    # Data loaders
    train_loader, test_loader = get_dataloaders(config.data_path, config.batch_size, config.num_workers)

    # Model
    model = SimpleCNN(num_classes=config.num_classes).to(config.device)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config.learning_rate)

    # Training loop
    for epoch in range(config.num_epochs):
        model.train()
        for batch_idx, (data, targets) in enumerate(train_loader):
            data = data.to(config.device)
            targets = targets.to(config.device)

            # Forward pass
            outputs = model(data)
            loss = criterion(outputs, targets)

            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if batch_idx % 100 == 0:
                print(f'Epoch [{epoch+1}/{config.num_epochs}], Step [{batch_idx+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

        # Save checkpoint
        checkpoint = {
            'state_dict': model.state_dict(),
            'optimizer': optimizer.state_dict(),
        }
        save_checkpoint(checkpoint, filename=f'{config.weights_path}/model_epoch_{epoch+1}.pth')

if __name__ == '__main__':
    train()
