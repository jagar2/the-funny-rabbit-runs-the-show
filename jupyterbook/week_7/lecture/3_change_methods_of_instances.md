# ☕ **Object-Oriented Programming: Instance Methods with Kopelauac Coffee**

## 🚀 **Learning Objectives**
By the end of this section, you should be able to:
- Create and implement `__init__()` with multiple parameters, including default parameter values. 🏗️
- Describe what information an **instance method** has access to and can modify. 🔄

---

## ☕ **What is a Class?**
A **class** is like the ultimate coffee recipe book. It defines **attributes (flavor, origin, roast level)** and **methods (brew, serve, refill)** that allow each coffee cup to be uniquely crafted but still follow the sacred traditions of caffeine worship. 🔥

## ☕ **What is an Object?**
An **object** is like an actual **cup of coffee** brewed from the class blueprint. Each cup may have different **strengths, roast levels, or add-ons**, but they all come from the same fundamental coffee-making principles.

### **Example Context: Kopelauac Coffee** ☕🐱
Kopelauac coffee is a **rare and legendary** coffee known for its **exotic processing method** and **rich flavor**. Our Python class will help us model and craft the perfect cup.

---

## 🔧 **Creating a Class with Instance Methods**
### **Defining a `CoffeeCup` Class**
```python
class CoffeeCup:
    def __init__(self, origin, roast_level, caffeine_content, size="Medium"):
        """Initialize instance attributes with default values where applicable."""
        self.origin = origin  # Instance Attribute
        self.roast_level = roast_level  # Instance Attribute
        self.caffeine_content = caffeine_content  # Instance Attribute
        self.size = size  # Default Parameter
    
    def describe_coffee(self):
        """Returns a fancy description of the coffee cup."""
        return f"☕ {self.size} cup of {self.roast_level} roast from {self.origin} | {self.caffeine_content}mg caffeine"
    
    def change_size(self, new_size):
        """Modify the coffee cup size."""
        self.size = new_size
        return f"Your coffee is now a {self.size} size! More caffeine, more energy! 🚀"
```
### **Explanation:**
- `__init__()` initializes **instance attributes** (`origin`, `roast_level`, `caffeine_content`) and includes a **default parameter (`size`)**.
- `describe_coffee()` lets us **brag about our premium coffee cup**.
- `change_size()` modifies an instance attribute (`size`), demonstrating that instance methods **can modify object state**.

---

## ☕ **Creating Coffee Cup Instances**
```python
# Brewing some exotic coffee
cup1 = CoffeeCup("Indonesia", "Dark", 150)
cup2 = CoffeeCup("Ethiopia", "Medium", 120, size="Large")
cup3 = CoffeeCup("Hawaii Kona", "Light", 80, size="Small")

# Checking out the coffee specs
print(cup1.describe_coffee())  # ☕ Medium cup of Dark roast from Indonesia | 150mg caffeine
print(cup2.describe_coffee())  # ☕ Large cup of Medium roast from Ethiopia | 120mg caffeine
print(cup3.describe_coffee())  # ☕ Small cup of Light roast from Hawaii Kona | 80mg caffeine
```
### **Key Takeaways:**
- Each **coffee cup (object)** is brewed with **custom roast levels and origins**.
- The `describe_coffee()` method lets us see the full **coffee profile**.

---

## 📌 **Modifying Instance Attributes with Methods**
```python
# Upsizing the coffee cup
print(cup1.change_size("Large"))  # Your coffee is now a Large size! More caffeine, more energy! 🚀
print(cup1.describe_coffee())  # ☕ Large cup of Dark roast from Indonesia | 150mg caffeine
```
### **What Just Happened?**
- `change_size()` updated **the instance attribute (`size`)**.
- Methods can modify an **object's internal state dynamically**.

---

## 🏆 **Key Takeaways**
✅ `__init__()` initializes attributes and allows **default values**.
✅ **Instance methods** can access and modify **instance attributes**.
✅ Methods allow **dynamic updates** to an object’s properties.
✅ **Kopelauac coffee is elite**, just like Python’s OOP model. ☕🚀

☕ **Just like a perfectly brewed cup of coffee, instance methods let us refine and modify our Python objects to suit our ever-changing caffeine needs!**
