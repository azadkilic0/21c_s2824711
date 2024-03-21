#Task-1
squares = [x**2 for x in range(1, 11)]
print("task-1:"+squares)

#Task-2
def generate_squares(start, end):
    return [x**2 for x in range(start, end+1)]
# Example usage of the function
example_squares = generate_squares(1, 10)
print("task-2:"+example_squares)

#Task-3
class SquareGenerator:
    def generate_squares(self, start, end):
        """Generate a list of squares for a given range of numbers."""
        return [x**2 for x in range(start, end+1)]
# Example usage:
if __name__ == "__main__":
    square_generator = SquareGenerator()
    squares = square_generator.generate_squares(1, 10)
    print("task-3:"+squares)
