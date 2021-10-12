#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# This is the Celcius to Farenheit converter
# This program uses defined functions


def calculate_farenheit():
    # calculate fahrenheit from celsius input

    # input
    celsius_string = input("Enter a temperature (°C): ")

    try:
        # convert string to integer
        celsius_integer = int(celsius_string)
        # process
        fahrenheit = (9 / 5) * celsius_integer + 32
        # output
        print("{0}°C is equal to {1}°F.".format(celsius_integer, fahrenheit))
    except Exception:
        print("{0} is an invalid input.".format(celsius_string))
    print("\nDone.")


def main():
    # this function just calls other functions

    # call function
    calculate_farenheit()


if __name__ == "__main__":
    main()
