# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
#Function to determine fibonacci sequence
def generate_fibonacci(n):
    """Generates and prints the first N terms of the Fibonacci sequence."""
    # Requirement: N must be a positive integer
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    a, b = 0, 1
    terms = []

    # Iterative loop to generate sequence
    for _ in range(n):
        terms.append(str(a))
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(terms))


def is_fibonacci_number(num):
    """Determines whether a given non-negative integer belongs to the Fibonacci sequence."""
    if num < 0:
        print(f"{num} is NOT a Fibonacci number.")
        return

    a, b = 0, 1

    # Keep generating terms until we reach or exceed the target number
    while a < num:
        a, b = b, a + b

    if a == num:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


def main():
    # PART A
    print("--- PART A: Generate Sequence ---")
    try:
        terms_input = int(input("How many terms? "))
        generate_fibonacci(terms_input)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

    print()  # Spacer line

    # PART B 
    print("--- PART B: Check Sequence Membership ---")
    try:
        check_input = int(input("Enter a number to check: "))
        is_fibonacci_number(check_input)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()