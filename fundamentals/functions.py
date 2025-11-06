def calculate_circle_diameter(radius: float) -> float:
    """Calculate the diameter of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The diameter of the circle.
    """
    if(radius < 0):
        return -1
    diameter = radius * 2
    return diameter

# Temperature Conversion Functions
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit) -> float:
    """Convert Fahrenheit temperature to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temperature, unit) -> float:
    """Convert temperature between Celsius and Fahrenheit.

    Args:
        temperature (float): The temperature value to convert.
        unit (str): The unit of the input temperature ('C' for Celsius, 'F' for Fahrenheit).

    Returns:
        float: The converted temperature.
    """
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    else:
        raise ValueError("Unit must be 'C' for Celsius or 'F' for Fahrenheit.")