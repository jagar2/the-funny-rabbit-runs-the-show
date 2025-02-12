# 🏎️ **Object-Oriented Programming: Classes & Objects with Sports Cars**

## 🚀 **Learning Objectives**
By the end of this section, you should be able to:
- Build a **class** that defines the DNA of a high-performance sports car. 🏁
- Give life to your virtual garage by creating **class instances** (a.k.a. ridiculously fast cars). 💨

---

## 🏗️ **Understanding Classes & Objects**
### **What is a Class?**
A **class** is like the **blueprint** for a sports car. It defines **attributes (horsepower, speed, brand)** and **methods (accelerate, drift, show off)** that make each car unique but still follow the same high-speed principles.

### **What is an Object?**
An **object** is like an actual **car rolling off the production line**. Each sports car might have a different **engine, spoiler, or turbo boost**, but they all came from the same master plan.

### **Example Context: Sports Cars** 🏎️
Think of a **luxury car factory** 🎨🏭:
- **Class** = The master plan for creating an absolute beast of a car.
- **Objects** = The beautiful speed demons that hit the streets.

---

## 🔧 **Creating a Class with Attributes**
### **Defining a `SportsCar` Class**
```python
class SportsCar:
    # Class Attribute (Shared across all instances)
    category = "Sports Car"
    
    def __init__(self, brand, model, horsepower, top_speed):
        """Initialize instance attributes."""
        self.brand = brand  # Instance Attribute
        self.model = model  # Instance Attribute
        self.horsepower = horsepower  # Instance Attribute
        self.top_speed = top_speed  # Instance Attribute
    
    def display_info(self):
        """Show off the car's stats in a flashy way."""
        return f"🔥 {self.brand} {self.model} | HP: {self.horsepower} | Top Speed: {self.top_speed} km/h 🚀"
```
### **Explanation:**
- `category` is a **class attribute** (all sports cars are in the elite club).
- `__init__()` initializes **instance attributes** (`brand`, `model`, `horsepower`, `top_speed`).
- `display_info()` is a **method** that lets the car flex its stats.

---

## 🚘 **Creating Objects (Class Instances)**
```python
# Assembling some speed demons
car1 = SportsCar("Ferrari", "F8 Tributo", 710, 340)
car2 = SportsCar("Lamborghini", "Huracan", 630, 325)
car3 = SportsCar("McLaren", "720S", 710, 341)

# Checking out the specs
print(car1.display_info())  # 🔥 Ferrari F8 Tributo | HP: 710 | Top Speed: 340 km/h 🚀
print(car2.display_info())  # 🔥 Lamborghini Huracan | HP: 630 | Top Speed: 325 km/h 🚀
print(car3.display_info())  # 🔥 McLaren 720S | HP: 710 | Top Speed: 341 km/h 🚀
```
### **Key Takeaways:**
- Each **instance (object)** is like a different model with unique specs.
- Methods like `display_info()` let us see the raw power of each beast.

---

## 📌 **Class vs Instance Attributes**
```python
print(car1.category)  # Sports Car (all belong to the same elite squad)
print(car2.category)  # Sports Car
```
### **Class Attributes:**
- Defined **outside `__init__()`**.
- Shared across **all instances**.

### **Instance Attributes:**
- Defined **inside `__init__()`**.
- Unique to **each object** (every car has its own horsepower and speed).

---

## 🏁 **Modifying Class and Instance Attributes**
```python
# Modding an individual car
car1.horsepower = 720  # More power, baby!
print(car1.display_info())  # 🔥 Ferrari F8 Tributo | HP: 720 | Top Speed: 340 km/h 🚀

# Changing the category for all sports cars
SportsCar.category = "High-Performance Monster"
print(car2.category)  # High-Performance Monster
```
### **Important Notes:**
- Modifying an **instance attribute** is like **tuning a specific car**.
- Modifying a **class attribute** is like **renaming the whole league of supercars**.

---

## 🏆 **Key Takeaways**
✅ **Classes** define the blueprint of high-speed beasts.
✅ **Instance attributes** make each sports car unique.
✅ **Class attributes** define shared characteristics of all cars.
✅ Objects let us create **customized speed machines** while following the same elite standards.

🏎️ **Just like sports cars dominate the roads, objects in Python help structure code with style and performance!**
