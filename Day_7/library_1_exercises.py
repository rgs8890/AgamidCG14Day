import math
import requests

#area = math.pi * math.radius ** 2
# Exercise 1
def area(radius: float) -> float:

    return math.pi * (radius ** 2)

def fetch_data(url: str) -> str:
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code}"
    
result: str = fetch_data("Https://api.github.com")
print(result)

def factorial(n:int) -> int:
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial(5))

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(10))