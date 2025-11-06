from fundamentals.classes import Dog
from fundamentals.code_challenge import make_sandwich
from fundamentals.functions import calculate_circle_diameter, convert_temperature

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()

print(calculate_circle_diameter(7))
print(calculate_circle_diameter(2.5))

temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(100, 'C')
converted_c = convert_temperature(212, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")

# code_challenge.py
print(make_sandwich("wheat", "turkey", "cheddar", True))
print(make_sandwich("rye", "ham"))