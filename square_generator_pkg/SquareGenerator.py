class SquareGenerator:
    def generate_squares(self, start, end):
        """Generate a list of squares for a given range of numbers.

        Raises:
            ValueError: If end < start, indicating the range is invalid.
        """
        if end < start:
            raise ValueError("End of range must be greater than or equal to the start.")
        return [x ** 2 for x in range(start, end + 1)]
