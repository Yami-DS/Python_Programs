"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(actual_min):
    """
    Return the remaining bake time.

    :param actual_min: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function calculates the difference between 'EXPECTED_BAKE_TIME'
    and the time the lasagna has already been baking.
    """
    remaining_time = EXPECTED_BAKE_TIME-actual_min
    return remaining_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """
    Return the preparation time for the given number of layers.

    :param number_of_layers: int - the number of layers to be added.
    :return: int - total preparation time (in minutes).
    """
    total_prep_time = number_of_layers * PREPARATION_TIME
    return total_prep_time
    
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return the total elapsed time since the lasagna preparation started.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - time the lasagna has been baking in the oven.
    :return: int - total elapsed time (prep time + bake time).
    """
    total_min = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return total_min

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
