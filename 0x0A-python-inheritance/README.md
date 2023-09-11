# this repo about inheritance in python

```the folder contain 15 files:```



- [README.md](README.md): this file
- [0-lookup.py](0-lookup.py): a function that returns the list of available attributes and methods of an object
- [1-my_list.py](1-my_list.py): a class `MyList` that inherits from `list`
- [2-is_same_class.py](2-is_same_class.py): a function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`
- [3-is_kind_of_class.py](3-is_kind_of_class.py): a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`
- [4-inherits_from.py](4-inherits_from.py): a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`
- [5-base_geometry.py](5-base_geometry.py): an empty class `BaseGeometry`
- [6-base_geometry.py](6-base_geometry.py): a class `BaseGeometry` (based on `5-base_geometry.py`)
- [7-base_geometry.py](7-base_geometry.py): a class `BaseGeometry` (based on `6-base_geometry.py`)
- [8-rectangle.py](8-rectangle.py): a class `Rectangle` that inherits from `BaseGeometry` (based on `7-base_geometry.py`)
- [9-rectangle.py](9-rectangle.py): a class `Rectangle` that inherits from `BaseGeometry` (based on `8-rectangle.py`)
- [10-square.py](10-square.py): a class `Square` that inherits from `Rectangle` (based on `9-rectangle.py`)
- [11-square.py](11-square.py): a class `Square` that inherits from `Rectangle` (based on `10-square.py`)

## and some advanced tasks:

- [100-my_int.py](100-my_int.py): a class `MyInt` that inherits from `int`
- [101-add_attribute.py](101-add_attribute.py): a function that adds a new attribute to an object if it’s possible


## a small brief about inheritance in python:

Inheritance allows us to define a class that inherits all the methods and properties from another class.

1- Parent class is the class being inherited from, also called base class.

2- Child class is the class that inherits from another class, also called derived class.

3- when you add the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function.

4- The `super()` function will make the child class inherit all the methods and properties from its parent.

5- By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

6- If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

7- Multiple Inheritance: a class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.

8- Multilevel Inheritance: we can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.

---

## Author
* **Abdullah-Faik** - [abdullah-faik](www.github.com/abdullah-faik)

