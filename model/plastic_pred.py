import torch 
import torch.nn as nn 
from PIL import Image
from torchvision import transforms

class CNNModel(nn.Module):
    def __init__(self, num_classes=9, dropout_prob=0.5):
        super(CNNModel, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Dropout(p=dropout_prob),  
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Dropout(p=dropout_prob),  
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        self.fc_input_size = self._get_fc_input_size()
        self.classifier = nn.Sequential(
            nn.Linear(self.fc_input_size, 128),
            nn.ReLU(),
            nn.Dropout(p=dropout_prob),  # Dropout layer before the final fully connected layer
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

    def _get_fc_input_size(self):
        with torch.no_grad():
            dummy_input = torch.zeros(1, 3, 255, 255)
            features = self.features(dummy_input)
            fc_input_size = features.view(1, -1).size(1)
        return fc_input_size

class PlasticPredict:
    def __init__(self, img):
        self.img  = img 
    def pred(self):
        #"cuda" if torch.cuda.is_available() else 
 
        loaded_model = CNNModel()

 
        state_dict = torch.load('./model/micro_plastic.pth', map_location=torch.device('cpu'))
 
        loaded_model.load_state_dict(state_dict)
        
        input_tensor = self.img
 
        input_batch = input_tensor.unsqueeze(0)
        with torch.no_grad():
            output = loaded_model(input_batch)
            _, predicted = torch.max(output, 1)
        return predicted.item()
    

if __name__=="__main__":
    print()