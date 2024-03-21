import math


#Task-1
squares = [x**2 for x in range(1, 11)]
print( "Task 1 :",squares)

#Task-2
def generate_squares(start, end):
    return [x**2 for x in range(start, end+1)]
# Example usage of the function
example_squares = generate_squares(1, 10)
print("Task 2 :",example_squares)

#Task-3
class SquareGenerator:
    def generate_squares(self, start, end):
        """Generate a list of squares for a given range of numbers."""
        return [x**2 for x in range(start, end+1)]
# Example usage:
if __name__ == "__main__":
    square_generator = SquareGenerator()
    squares = square_generator.generate_squares(1, 10)
    print("Task 3 :",squares)

#Task-4
square_roots = [math.sqrt(number) for number in squares]
print("Task 4 :",square_roots)

#Task-5
class SquareGenerator:
    def generate_squares(self, start, end):
        """Generate a list of squares for a given range of numbers.

        Raises:
            ValueError: If end < start, indicating the range is invalid.
        """
        if end < start:
            raise ValueError("End of range must be greater than or equal to the start.")
        return [x ** 2 for x in range(start, end + 1)]
# Example usage:
if __name__ == "__main__":
    square_generator = SquareGenerator()
    try:
        squares = square_generator.generate_squares(1, 10)
        print("Task 5 :")
        print(squares)
        squares_invalid = square_generator.generate_squares(10, 1)  # This should raise an exception
    except ValueError as error:
        print(f"Error: {error}")

#Task-6
from Lab_3 import SquareGenerator
if __name__ == "__main__":
    square_generator = SquareGenerator()
    try:
        squares = square_generator.generate_squares(1, 10)
        print ("Task 6 :")
        print(squares)
        # This line is expected to raise an exception due to invalid range
        squares_invalid = square_generator.generate_squares(10, 1)
    except ValueError as error:
        print(f"Error: {error}")

#Task-7


