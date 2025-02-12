# 🚀 **Advanced Python Classes: Doing Cool Things with Simple Code**

## 🏗️ **Why Use Classes?**
Python classes aren’t just for storing data—they can be used for **automating tasks, generating content, and even making Python speak!**

---

## ⏳ **1️⃣ Self-Updating Timer Class**
### **Why it’s cool?**
This class dynamically **tracks elapsed time**, perfect for benchmarking scripts or timing user actions.

### **Using the Timer Class from `time` Module**
```python
import time

class Timer:
    def __init__(self):
        self.start_time = time.time()

    def elapsed(self):
        return f"⏳ {time.time() - self.start_time:.2f} seconds elapsed"
```
### **How to Use:**
```python
# Start the timer
my_timer = Timer()
time.sleep(2)  # Simulating a delay
print(my_timer.elapsed())  # ⏳ 2.00 seconds elapsed
```
---

## 🌐 **2️⃣ Dynamic HTML Page Generator**
### **Why it’s cool?**
You can **generate an HTML page on the fly** with Python, no manual coding required.

### **Using the HTMLPage Class**
```python
class HTMLPage:
    def __init__(self, title):
        self.title = title
        self.body = ""

    def add_paragraph(self, text):
        self.body += f"<p>{text}</p>\n"

    def render(self):
        return f"""<html>
<head><title>{self.title}</title></head>
<body>
{self.body}
</body>
</html>"""
```
### **How to Use:**
```python
page = HTMLPage("My Dynamic Page")
page.add_paragraph("Welcome to my auto-generated webpage!")
page.add_paragraph("This was made with Python!")
print(page.render())  # Outputs HTML code
```
📌 **Use Case:** Automate report generation, dynamic emails, or website content!

---

## 🔊 **3️⃣ Python Class That Talks (Text-to-Speech)**
### **Why it’s cool?**
Turn Python into a **voice assistant** with `pyttsx3`!

### **Using the Speaker Class**
```python
import pyttsx3

class Speaker:
    def __init__(self, voice_rate=150):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', voice_rate)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
```
### **How to Use:**
```python
s = Speaker()
s.say("Hello! I am a Python class that speaks!")
```
📌 **Use Case:** Create an AI narrator, alert system, or an interactive chatbot!

---

## 🤖 **4️⃣ Neural Network for MNIST Using Classes**
### **Why it’s cool?**
This class builds and trains a simple **neural network** using **PyTorch** to classify handwritten digits from the MNIST dataset.

### **Using the NeuralNetwork Class**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

# Define the Neural Network class
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(28*28, 128)
        self.layer2 = nn.Linear(128, 64)
        self.output_layer = nn.Linear(64, 10)
        self.activation = nn.ReLU()
        self.softmax = nn.LogSoftmax(dim=1)
    
    def forward(self, x):
        x = x.view(-1, 28*28)  # Flatten the input
        x = self.activation(self.layer1(x))
        x = self.activation(self.layer2(x))
        x = self.softmax(self.output_layer(x))
        return x

# Load MNIST dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)

# Create the model, define loss function and optimizer
model = NeuralNetwork()
criterion = nn.NLLLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(1):  # One epoch for simplicity
    for images, labels in trainloader:
        optimizer.zero_grad()
        output = model(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

print("✅ Training Complete!")

# Load test dataset
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=10, shuffle=True)

def evaluate_model(model, testloader):
    model.eval()
    images, labels = next(iter(testloader))
    with torch.no_grad():
        outputs = model(images)
        _, preds = torch.max(outputs, 1)
    
    # Visualizing the results
    fig, axes = plt.subplots(1, 10, figsize=(15,3))
    for i in range(10):
        axes[i].imshow(images[i].view(28,28).numpy(), cmap='gray')
        axes[i].set_title(f'Pred: {preds[i].item()}')
        axes[i].axis('off')
    plt.show()

# Evaluate and visualize model predictions
evaluate_model(model, testloader)
```
### **How to Use:**
- Run the script to **train and evaluate a simple neural network** on MNIST.
- The class `NeuralNetwork` defines the **architecture** and **forward propagation**.
- The `trainloader` handles **batch loading of images**.
- The `evaluate_model()` function tests the model and **visualizes predictions**.

📌 **Use Case:** Image classification, AI-powered handwriting recognition, and deep learning projects.

---

## 📌 **Key Takeaways**
✅ **Classes help automate cool tasks** like tracking time, generating content, and AI training.
✅ **Reusing modules** like `torch` and `time` makes Python **more powerful**.
✅ **Modular design** allows easy expansion and reuse in larger projects.

🚀 **Start using these classes in your own Python scripts and build something amazing!**

