from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import DataLoader
import os


class CustomImageFolder(ImageFolder):
    def __init__(self, root: str, transform):
        super(CustomImageFolder, self).__init__(root, transform)

    def __getitem__(self, index: int):
        path, target = self.samples[index]
        sample = self.loader(path)
        if self.transform is not None:
            sample = self.transform(sample)

        return path, sample, target


class LoadData:
    def __init__(self, train_path=None, val_path=None, test_path=None, test_video_path=None, batch_size=10):
        self.train_path = train_path
        self.val_path = val_path
        self.test_path = test_path
        self.test_video_path = test_video_path
        self.batch_size = batch_size

    def train_loader(self):
        transform = transforms.Compose([
            transforms.Resize([224, 224]),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        image_folder = ImageFolder(self.train_path, transform)
        train_data = DataLoader(
            image_folder, batch_size=self.batch_size, shuffle=True)

        return train_data

    def val_loader(self):
        transform = transforms.Compose([
            transforms.Resize([224, 224]),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        image_folder = ImageFolder(self.val_path, transform)
        val_data = DataLoader(
            image_folder, batch_size=self.batch_size, shuffle=True)

        return val_data

    def test_loader(self):
        transform = transforms.Compose([
            transforms.Resize([224, 224]),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        image_folder = CustomImageFolder(self.test_path, transform)
        test_data = DataLoader(
            image_folder, batch_size=self.batch_size, shuffle=True)

        return test_data

    def test_video_loader(self):
        video_files = sorted(os.listdir(self.test_video_path))
        transform = transforms.Compose([
            transforms.Resize([224, 224]),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        
        return self.test_video_path, video_files, transform
