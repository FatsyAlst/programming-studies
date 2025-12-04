# ========================================
# PYTHON MODULES - Overview & Guide
# ========================================
#
# Official Python Module Index: https://docs.python.org/3/py-modindex.html
#
# What are Modules?
# -----------------
# Modules are Python files (.py) that contain functions, classes, and variables
# that you can import and use in your own code. They help organize and reuse code.
#
# Types of Modules:
# 1. Built-in modules (come with Python)
# 2. Third-party modules (installed via pip)
# 3. Your own custom modules (files you create)

# ========================================
# HOW TO IMPORT MODULES
# ========================================

# Method 1: Import entire module
import math
# Usage: math.sqrt(16) → 4.0

# Method 2: Import specific function/class
from math import sqrt, pi
# Usage: sqrt(16) → 4.0, pi → 3.14159...

# Method 3: Import with alias (shorter name)
import datetime as dt
# Usage: dt.datetime.now()

# Method 4: Import everything (NOT RECOMMENDED - can cause conflicts)
from math import *
# Usage: sqrt(16), but clutters namespace


# ========================================
# COMMONLY USED BUILT-IN MODULES
# ========================================

# --- Math & Numbers ---
import math           # Mathematical functions (sqrt, sin, cos, etc.)
import random         # Random number generation
import statistics     # Statistical functions (mean, median, etc.)

# --- Date & Time ---
import datetime       # Date and time manipulation
import time           # Time-related functions (sleep, time measurements)

# --- File & OS Operations ---
import os             # Operating system interface (file paths, directories)
import sys            # System-specific parameters and functions
import pathlib        # Object-oriented filesystem paths

# --- Data Processing ---
import json           # JSON encoding and decoding
import csv            # CSV file reading and writing
import re             # Regular expressions (pattern matching)

# --- Internet & Web ---
import urllib         # URL handling
import requests       # HTTP library (requires: pip install requests)

# --- Other Useful Modules ---
import collections    # Specialized container datatypes (Counter, defaultdict)
import itertools      # Functions for efficient looping
import functools      # Higher-order functions (decorators, etc.)


# ========================================
# EXAMPLES
# ========================================

# Example 1: Using math module
import math

radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Circle area: {area:.2f}")  # 78.54

# Example 2: Using random module
import random

numbers = [1, 2, 3, 4, 5]
print(random.choice(numbers))      # Random number from list
print(random.randint(1, 10))       # Random integer between 1-10
random.shuffle(numbers)            # Shuffle list in-place

# Example 3: Using datetime module
from datetime import datetime, timedelta

now = datetime.now()
print(f"Current time: {now}")
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# Example 4: Using os module
import os

print(f"Current directory: {os.getcwd()}")
print(f"List files: {os.listdir('.')}")

# Example 5: Using json module
import json

data = {"name": "Felipe", "age": 20, "skills": ["Python", "Git"]}
json_string = json.dumps(data, indent=2)  # Convert to JSON
print(json_string)

# Convert back to Python object
parsed_data = json.loads(json_string)
print(parsed_data["name"])  # Felipe


# ========================================
# CREATING YOUR OWN MODULE
# ========================================

# Step 1: Create a file called my_utils.py
# """
# def greet(name):
#     return f"Hello, {name}!"
# 
# def square(x):
#     return x ** 2
# """

# Step 2: Import and use it in another file
# from my_utils import greet, square
# print(greet("Felipe"))  # Hello, Felipe!
# print(square(5))        # 25


# ========================================
# BEST PRACTICES
# ========================================

# ✅ DO:
# - Import at the top of your file
# - Use specific imports (from module import function)
# - Use aliases for long module names
# - Organize imports: standard library → third-party → your modules

# ❌ DON'T:
# - Use wildcard imports (from module import *)
# - Import inside functions (unless necessary)
# - Create circular imports (module A imports B, B imports A)

# ========================================
# USEFUL RESOURCES
# ========================================

# Official Python Module Index: https://docs.python.org/3/py-modindex.html
# Popular third-party modules: https://pypi.org/
# Python Package Installer (pip): https://pip.pypa.io/

