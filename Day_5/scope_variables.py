# Scope prefers to where a variable is accessible
# Global and Local Scope
# SCOPE: Refers to where a variable is accessible
# A variable in global scope can be accessed anywhere in the program
# A varaible in local scope is limited to the function or the block parts defined

def chocolate():
    message = "I love chocoloate!"

    print(message)

chocolate()
# NameError -> message lives inside the function -> it is within the scope
# When a variable is defined outside of the scope it is a global variable

# Variables which do not change are called constants
# This value does not always stay the same
# The lifetime of a variable refers to how long it exists

# Variables in local scope only exist for the duration of the function where they are defined. The variable no longer exists.
# Scope defines where a variable is accessible. Lifetime defines how long a variable exists when it is located in the program.

