# %% [markdown]
# # ❓ Python Quiz: Object-Oriented Programming in Manufacturing
# 
# Test your knowledge of Python classes by answering these questions related to manufacturing, machines, and inventory management.

# %%
# BEGIN MULTIPLE CHOICE
## points: 1
## title: Select the Best Answer
## question number: 1

# %% [markdown]
# ## machine-instance
# ### **How do you correctly create an instance of a class named `Machine`?**
# 
# #### OPTIONS
# `machine1 = Machine()`  
# `machine1 = new Machine`  
# `machine1 = Machine.create()`  
# `class machine1 = Machine`  
# 
# #### SOLUTION
# `machine1 = Machine()`

# %% [markdown]
# ## factory-production-count
# ### **What will the following code output?**
# ```python
# class Factory:
#     production_count = 100
# 
# factory1 = Factory()
# factory2 = Factory()
# factory1.production_count = 150
# print(factory2.production_count)
# ```
# 
# #### OPTIONS
# 100  
# 150  
# Error  
# None  
# 
# #### SOLUTION
# 100

# %% [markdown]
# ## inventory-method
# ### **Which method in a class is automatically called when a new instance is created?**
# 
# #### OPTIONS
# `__init__`  
# `__new__`  
# `create_instance`  
# `initialize`  
# 
# #### SOLUTION
# `__init__`

# %% [markdown]
# ## machine-status
# ### **What will be the output of the following code?**
# ```python
# class Machine:
#     def __init__(self):
#         self.status = "idle"
# 
# m1 = Machine()
# m1.status = "running"
# print(m1.status)
# ```
# 
# #### OPTIONS
# idle  
# running  
# Error  
# None  
# 
# #### SOLUTION
# running

# %%
# END MULTIPLE CHOICE

# %%
# BEGIN SELECT MANY
## points: 2
## title: Select All That Apply
## question number: 2
## grade: parts

# %% [markdown]
# ## class-attributes
# ### **Which of the following are true about class attributes in Python?**
# 
# #### OPTIONS
# Class attributes are shared across all instances.  
# Class attributes can be modified at the instance level.  
# Class attributes must always be integers.  
# A class attribute can be accessed using both the class name and an instance.  
# 
# #### SOLUTION
# Class attributes are shared across all instances.  
# Class attributes can be modified at the instance level.  
# A class attribute can be accessed using both the class name and an instance.

# %% [markdown]
# ## object-oriented-benefits
# ### **What are benefits of using object-oriented programming (OOP) in a manufacturing system?**
# 
# #### OPTIONS
# Code reusability through inheritance.  
# More structured and modular code.  
# Slower performance due to extra complexity.  
# Easier to model real-world systems like machines and inventory.  
# 
# #### SOLUTION
# Code reusability through inheritance.  
# More structured and modular code.  
# Easier to model real-world systems like machines and inventory.

# %% [markdown]
# ## class-methods
# ### **Which of the following statements about instance methods are true?**
# 
# #### OPTIONS
# Instance methods can access both instance attributes and class attributes.  
# An instance method must always have `self` as its first parameter.  
# Instance methods can only modify class attributes.  
# An instance method can call other methods of the same class.  
# 
# #### SOLUTION
# Instance methods can access both instance attributes and class attributes.  
# An instance method must always have `self` as its first parameter.  
# An instance method can call other methods of the same class.

# %% [markdown]
# ## factory-maintenance
# ### **Which of the following are good practices for designing a `Machine` class in a factory system?**
# 
# #### OPTIONS
# Define an `__init__` method to initialize machine attributes.  
# Use class attributes to store unique machine IDs.  
# Implement methods like `start_machine()` and `stop_machine()`.  
# Store all machine attributes in global variables instead of the class.  
# 
# #### SOLUTION
# Define an `__init__` method to initialize machine attributes.  
# Implement methods like `start_machine()` and `stop_machine()`.

# %%
# END SELECT MANY

# %%
# BEGIN TF
## points: 1
## title: True or False
## question number: 3

# %% [markdown]
# ## instance-vs-class
# ### **Instance variables belong to the class and are shared among all instances.**
# 
# #### SOLUTION
# False

# %% [markdown]
# ## class-inheritance
# ### **A subclass automatically inherits all methods and attributes from its parent class.**
# 
# #### SOLUTION
# True

# %% [markdown]
# ## self-keyword
# ### **The `self` keyword refers to the instance of the class within a method.**
# 
# #### SOLUTION
# True

# %% [markdown]
# ## encapsulation
# ### **Encapsulation is the practice of restricting direct access to certain attributes and methods of a class.**
# 
# #### SOLUTION
# True

# %%
# END TF

# %%
# BEGIN QUESTION
name: Free-Response Define a Machine Class

# %% [markdown]
# ## Define a `Machine` Class
# 
# Write a Python class named `Machine` that:
# - Has an `__init__` method that initializes `machine_id` and `status` (`"idle"` by default).
# - Includes a method `start_machine()` that changes `status` to `"running"`.
# - Includes a method `stop_machine()` that changes `status` to `"stopped"`.
# 
# ### Example:
# ```python
# m1 = Machine(101)
# print(m1.status)  # Output: idle
# m1.start_machine()
# print(m1.status)  # Output: running
# m1.stop_machine()
# print(m1.status)  # Output: stopped
# ```

# %%
# BEGIN SOLUTION

class Machine:
    def __init__(self, machine_id, status="idle"):
        self.machine_id = machine_id
        self.status = status

    def start_machine(self):
        self.status = "running"

    def stop_machine(self):
        self.status = "stopped"

# Example usage
m1 = Machine(101)
print(m1.status)  # Should print idle
m1.start_machine()
print(m1.status)  # Should print running
m1.stop_machine()
print(m1.status)  # Should print stopped

# %%
# END SOLUTION

# %%
# BEGIN QUESTION
name: Free-Response Modify an Inventory Class

# %% [markdown]
# ## Modify an Inventory Class
# 
# Given the `Inventory` class below, modify it to:
# - Add an `add_stock(quantity)` method that increases the `stock` attribute.
# - Add a `remove_stock(quantity)` method that decreases `stock` but ensures it doesn’t go below zero.
# - Implement a `__str__()` method that returns `"Product: <name>, Stock: <stock>"`.
# 
# ### Example:
# ```python
# item = Inventory("Gears", 50)
# item.add_stock(20)
# print(item)  # Output: Product: Gears, Stock: 70
# item.remove_stock(80)
# print(item)  # Output: Product: Gears, Stock: 0
# ```

# %%
# BEGIN SOLUTION

class Inventory:
    def __init__(self, name, stock=0):
        self.name = name
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def remove_stock(self, quantity):
        self.stock = max(0, self.stock - quantity)

    def __str__(self):
        return f"Product: {self.name}, Stock: {self.stock}"

# Example usage
item = Inventory("Gears", 50)
item.add_stock(20)
print(item)
item.remove_stock(80)
print(item)

# %%
# END SOLUTION
