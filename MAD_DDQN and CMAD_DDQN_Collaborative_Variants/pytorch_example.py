import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch as T


class Model(nn.Module):
    def __init__(self, lr, num_classes, input_dims):
        super(Model, self).__init__()
        
        self.fc1 = nn.Linear(*input_dims, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, num_classes)

        self.optimizer = optim.Adam(self.parameters(), lr=lr)
        #self.parameters() tell adam which tensors to update
        self.loss = nn.CrossEntropyLoss()
        self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.to(self.device)

    def forward(self, input_data):
        layer1 = F.sigmoid(self.fc1(input_data))
        layer2 = F.sigmoid(self.fc2(layer1))
        layer3 = self.fc3(layer2) # Crossentropy loss will handle activation

        return layer3
    
    def learn(self, input_data, labels):
        self.optimizer.zero_grad()

        input_data = T.tensor(input_data).to(self.device) #Convert inputs to tensors
        labels = T.tensor(labels).to(self.device)

        predictions = self.forward(self, input_data)
        costs = self.loss(predictions, labels)

        costs.backward()
        self.optimizer.step() # Updates parameters using gradients