# Percent-Change-To-Offset-Percent-Change-In-An-Asset

This project calculates the offset percentage needed to return to the initial value after a given percentage change in an asset. It handles both gains and losses and provides a clear message describing the offset needed.

## Features

- Calculate the offset percentage for both gains and losses.
- Handle edge cases such as 100% loss.
- Command-line interface for user input.
- Unit tests to ensure correctness.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/percent-change-offset.git
    cd percent-change-offset
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to calculate the offset percentage:
```sh
python main.py
```
