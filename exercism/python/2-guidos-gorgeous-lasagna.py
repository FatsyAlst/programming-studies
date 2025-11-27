"""
Lasagna Cooking Helper

This module provides helper functions for calculating time-related aspects of preparing and baking a lasagna.

Functions included:
- bake_time_remaining(passed_time): Calculates remaining bake time based on expected bake time and elapsed time.
- preparation_time_in_minutes(number_of_layers): Calculates the preparation time for the lasagna based on the number of layers (2 minutes per layer).
- elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): Calculates the total time spent (preparation + baking).

Constants:
- EXPECTED_BAKE_TIME: int - The expected total bake time for the lasagna in minutes.
- PREPARATION_TIME: int - Preparation time per layer in minutes.

Designed for educational use with Python basics (functions, parameters, constants, and docstrings).
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 30


def bake_time_remaining(passed_time):  
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - passed_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time based on the number of layers.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes).

    Multiplies the number of layers by 2.
    """
    return 2 * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate total elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - time spent baking so far.
    :return: int - total minutes elapsed (prep + baking).

    Adds (the double of number of layers) with the baking time so far.
    """
    return 2 * number_of_layers + elapsed_bake_time
