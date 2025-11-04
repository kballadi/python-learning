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