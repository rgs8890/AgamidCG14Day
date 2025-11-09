# Functions are like the recipe cards for the code -> write the steps once, and then reuse them
# Parameters and Return Values -> these will enable you to create flexible and renewable functions
# Scope where the variables are lived and used
# What is a module - 2 Key Modules (Core Modules, Launch Modules)
# How to create and use this in the code
# __init__.py which helps python recognise your module as part of a package
# keep core functiosn and add helper functions if you need to

# A package is a collection of related modules (python files) that you can import and use in your project
# __init__.py intiialises the project, and the code inside the __init__.py file runs when the package is imported

# Modules #
Why do we use Modules?
- Code Reusability -> Modules, like some public static Classes in C# allow you to write code once and use it multiple times, saving time and effort.
- Organised Structure -> Keeping related functions in separate files helps keep all the project clean and easy to understand
- Easier Maintenance -> If you need to make changes, you only need to update the module, which reflects the changes everywhere it is used

if __name__ == "__main__": -> This line is used to control when certain parts of the code should run. This makes sure that the code we want to execute
only executes if the file is being run directly. It prevents code from running if we want to use a python file as a module but still allowing us to execute the code
in this file if needed.

In Python, every scipt has a built-in variable called __name__ which helps us determine how the script is being used. When you import the script as a module into another file; python sets __name__ to the name of file/module, in this case, the value be "example". 

Python sets the variable __name__ to the value '__main__' -> this tells Python that this is the main program being executed.

- __init__.py is a file used to mark a directory as a Python package; allows a group of related modules together; it became optional in Python 3.3+; it's commonly used to 
  initialize packages and manage what gets imported when a package is imported.

Day 5
- Modules
- Functions
- Paramters
- Scope
- Lifetime
- Launch + Core App
- Return Values
- Variable Scope
- Figuring out where variables live
- Creating/ Importing Modules
- Build first 2 modules