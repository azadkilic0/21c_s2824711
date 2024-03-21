from .SquareGenerator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        """Overrides the abstract method from SquareGenerator to generate cubes instead of squares.

        Parameters:
            start (int): The starting number of the range.
            end (int): The ending number of the range.

        Returns:
            list: A list of cubes from start to end.

        Raises:
            ValueError: If start is not less than end, indicating the range is invalid.
        """
        if start >= end:
            raise ValueError("Start of range must be less than the end.")
        return [x ** 3 for x in range(start, end + 1)]
