# PEP8 -> Python's Indentation and Styling Guide
Naming Conventions
What is PEP8?
- Python Enhancement Proposal (PEP8)
- Guido Van Rosen
- Make the code consistent and easy to work with across large codebases
- PEP8 -> 4 indentation spaces instead of tabs
- Code is Consistent in Pep8 -> Collaboration is a lot easier
- Pep8 is a style guide for Python
- Pep8 makes it easier for others to maintain

There are 8 rules of PEP8:

## Rule 1
- Indentation: Python requires indentation to structure code
- 4 spaces for indentation level
- VSCode -> Settings -> Insert Spaces

## Rule 2
- Length: 79 characters
- Settings -> editor -> rulers

## Rule 3
- Spacing: 2 Blank lines between functions
- 1 Blanl line between methods in a class

## Rule 4
- Imports:
- Standard Libary Imports (alphabetical order)
- Third-Party Imports ( Third-Party Imports)
- Local Imports (Local Imports)
- VS Code Extension: ISort

Summary:
- Indentation (4 Spaces)
- Line Limit (79 chars)
- Blank Lines
- Organised Imports

Naming Conventions and Whitespace Usage.
- In Python, variables use lower case and underscores
- variable_a, def this_is_a_function()
- SnakeCase -> Some coders use PascalCase, CamelCase
- Whitespace around Operators (add space around operators)
- Avoid adding unnecessary spaces inside paranthesis or brackets
- result = (a+b)*(c-d)
- Black Formatter -> Extension

- Naming Conventions: Consistent naming conventions help others instantly understand your code. A good name
- communicates the purpose of a variable, function, or class without needing extra explanation
- Rules
    - Variables and Functions
    - Use snake_case: lowercase letters with underscores seperating words.
    - Example: my_variable, calculate_sum()
    - Classes
    - Use CapWords (PascalCase): Each word starts with a capital latter, no
    - underscores.
    - Example: MyClass, UserAccount
    - Constants
    - Use ALL_CAPS: All letters uppercase with underscores separating words.
    - Example: MAX_LIMIT, TAX

## Documentation and Comments
- Inline Comments: Explain Why rather whan WHAT
- Keep them short 
- value = 5 # Initialize base value
- Docstrings
- Purpose, Parameters, Return Value
- They make functions easier to understand
- Google Style, Numpy Style
- Good Documentation - Explain why code is there, this good documentation 
- makes code easier to read and understand

# Code Organisation and Modularity
- Keeping functions short
- Single Responsibility principle
- Grouping Related Functions
- SRP: Single Responsibility Principle -> Pythonic
- Each Function should do one thing really well
- Split one function to read data and one function to shorten data
- Break up large functions into smaller ones (over 20 lines -> break it down)
- Keep all of these in a module
- Main Functions at the top, Helper Functions below
- Encapsulating methods can be useful for complex projects
- Bundle Data -> makes it more organised and modular
- Encapsulate this all in a grocery list clause
- All grocery list functionality in one place

Key TakeAways:
- SRP (Function does one thing)
- Keeping Functions Short
- Grouping Related Functions
- Top Down Approach
- Encapsulating Data and Methods
- Make code easier to maintain and scale
- Error-Handling Techniques

# Best Practices for Error Handling Techniques
- Predict and manage potential errors
- Approach 1: Look before you leap
- Approach 2: Easier to ask for forgiveness than permission
- LBYL : Check conditions before attempting an operation
- EAFP : Skips pre-checking then use try-except: 
- EAFP used when errors are unpredictable, LBYL is for predictable errors

# Multi-Line Text -> Comments
- Triple Quotes: ''' ''''

# Git is good for tracking and using version control
- Must be familiar with Git
- Git branches will work and can be used as a bug fix
- Keeps everything organised
- Writing and using everything in a team process is a collaborative process
- Be open to suggestions
- Document decisions (Why these choices were made? Helps you build on work)
- Code Style
- Version Control
- Writing and Reviewing

# Day 6
- Pep8 
- Indentation
- Line Length
- Organising Modules
- naming conventions
- whitespaces
- docstrings
- comments
- multi-line formatting
- using type hints
- avoid global variables and use constants

# Code Review - How professionals use review
- Crucial part of development
- Preparing for review
- Clean code principles
- code and consistent to read
- small focused commits
- make it easier to check what each change is doing
- fixed typo like login function
- submitting too much code will make people not want to review it
- Write a clear concise description
- Widly accepted for writing pull requests in professional developments
- Summary: The purpose of the PR and how useful it is
- Testing: Explains how the changes were tested
- Checklist: Optional Section