def calculate_offset(percent_change, initial_value=100):
    """
    Calculates the offset percentage needed to return to the initial value.

    Args:
        percent_change: The percentage change as a float (positive for gain, negative for loss).
        initial_value: The initial value (default: 100).

    Returns:
        A tuple containing:
            - The offset percentage as a float (rounded to 2 decimal places).
            - A message describing the offset needed.
    """
    percent_change_decimal = percent_change / 100
    value_after = initial_value * (1 + percent_change_decimal)
    offset_needed = ((initial_value / value_after) - 1) * 100
    sign = -1 if percent_change > 0 else 1
    message = (
        f"You need a {round(sign * offset_needed, 2)}% "
        f"{'loss' if sign == -1 else 'gain'} to offset your "
        f"{abs(percent_change)}% {'gain' if percent_change > 0 else 'loss'}"
    )
    return round(offset_needed, 2), message


def main():
    """
    Gets user input for percent change and displays the calculated offset.
    """
    while True:
        try:
            percent_change = float(input(
                "Enter current percent change (without a % sign) in asset "
                "(put a negative (-) in front if a loss): "
            ))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    offset_needed, message = calculate_offset(percent_change)
    print(f"{offset_needed}%")
    print(message)


if __name__ == "__main__":
    main()
