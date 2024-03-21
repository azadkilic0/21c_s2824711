#Task-1
squares = [x**2 for x in range(1, 11)]
print(squares)

#Task-2
def generate_squares(start, end):
    return [x**2 for x in range(start, end+1)]
# Example usage of the function
example_squares = generate_squares(1, 10)
print(example_squares)
