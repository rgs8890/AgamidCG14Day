Text
- Applications: The Final Product
- Libraries & Frameworks: Collections of modules/packages
- Packages: A folder containing multiple modules with an __init__.py file
- Modules: A python file that groups related classes and functions
- Classes: Grouped data (attributes) and behaviour (methods)
- Functions & Methods: Encapsulated logic that can be called multiple times
- Instructions: The lowest level of code execution

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

Encapsulation is for building data and behvaiour together in one place ( a class)
and then restrict direst access to parts of that data to protect it.

Why use encapulsation?
- Protect Sensitive Data - Prevent accidental or malicous changes.
- Control Modifications - Only allow safe, validate updates.
- Simplify Interfaces - Let users interact without knowing the internal logic.

Python Tools for Encapsulation
Private Attributes (use a double underscore (__) to mark something as private:)
self.__ingredients = ingredients

Getter Methods - Use the @property decorator to read a private attribute safely:
