#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Nov 8, 2023
# This program asks the user for the amount
# of croissants and bagels
# and calculate the total with tax or not.

import constants


def main():
    # get the price of item
    print("This program will calculate the total")
    print("with tax or not based on the amount on food")
    print("the user orders")
    user_croissants_string = input("Enter the number of croissants: ")
    user_bagels_string = input("Enter the number of bagels: ")

    try:
        # Convert user input to integers
        user_croissants_int = int(user_croissants_string)
        user_bagels_int = int(user_bagels_string)

        # Calculate the amount of food
        amount_of_food = user_croissants_int + user_bagels_int

        # Check if the amount of food is within a valid range
        if 0 <= amount_of_food <= 99:
            # Check if the amount of food is greater than or equal to 6
            if amount_of_food >= 6:
                # Calculate subtotal for croissants and bagels
                croissant_subtotal = constants.PRICE_PER_CROISSANT * user_croissants_int
                bagel_subtotal = constants.PRICE_PER_BAGEL * user_bagels_int

                # Calculate total including tax
                total_subtotal = croissant_subtotal + bagel_subtotal
                total_subtotal_tax = total_subtotal * constants.HST
                total_tax = total_subtotal + total_subtotal_tax

                # Display total with tax
                print(f"Your total with tax is: ${total_tax:.2f}")
            else:
                # Calculate subtotal for croissants and bagels
                croissant_subtotal = constants.PRICE_PER_CROISSANT * user_croissants_int
                bagel_subtotal = constants.PRICE_PER_BAGEL * user_bagels_int

                # Calculate total without tax
                total_subtotal = croissant_subtotal + bagel_subtotal

                # Display total without tax
                print(f"Your total without tax is: ${total_subtotal:.2f}")
        else:
            # Display an error message for an invalid amount of food
            print(f"{amount_of_food} is not a valid number of items")

    except ValueError:
        # Handle invalid integer input
        print("Invalid input. Please enter valid integers for croissants and bagels.")


if __name__ == "__main__":
    main()
