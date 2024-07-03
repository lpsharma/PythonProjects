import torch
from torchvision import datasets, transforms
from models.model import SimpleCNN
from config import Config
from utils.utils import load_checkpoint

def infer():
    config = Config()

    # Load the model
    model = SimpleCNN(num_classes=config.num_classes).to(config.device)
    checkpoint = load_checkpoint(f'{config.weights_path}/model_epoch_{config.num_epochs}.pth')
    model.load_state_dict(checkpoint['state_dict'])
    model.eval()

    # Data loader
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ])
    test_dataset = datasets.CIFAR10(root=config.data_path, train=False, download=True, transform=transform)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=config.batch_size, shuffle=False, num_workers=config.num_workers)

    # Inference loop
    with torch.no_grad():
        correct = 0
        total = 0
        for data, targets in test_loader:
            data = data.to(config.device)
            targets = targets.to(config.device)

            outputs = model(data)
            _, predicted = torch.max(outputs.data, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()

        print(f'Accuracy of the model on the test images: {100 * correct / total}%')

if __name__ == '__main__':
    infer()
