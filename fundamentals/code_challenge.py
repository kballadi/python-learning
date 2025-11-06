def make_sandwich(bread_type, filling, cheese=None, toasted=False):
    """
    This function makes a sandwich with user-specified ingredients.
    
    Args:
        bread_type (str): The type of bread for the sandwich.
        filling (str): The main filling of the sandwich.
        cheese (str, optional): The type of cheese to add. Defaults to None.
        toasted (bool, optional): Whether the sandwich should be toasted. Defaults to False.    
    """
    if toasted and cheese is not None:
        return (f"Making a toasted {bread_type} sandwich with {filling} and {cheese} cheese.")
    else:
        return (f"Making a {bread_type} sandwich with {filling}")