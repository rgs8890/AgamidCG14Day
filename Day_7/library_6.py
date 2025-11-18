'''
    Adding Unique ID's
    - uuid library is a built-in Python module that generates
      universally unique identifiers (UUIDs). These IDs are 128
      bit values which are incredibly unlikely to repeat, making them
      perfect for situations where you need unique references
'''
import uuid
unique_id = str(uuid.uuid4())
print(unique_id)
