from .SquareGenerator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        """Overrides SquareGenerator to generate squares with additional error checking.

        Parameters:
            start (int): The starting number of the range.
            end (int): The ending number of the range.

        Returns:
            list: A list of squares from start to end of the given range.

        Raises:
            ValueError: If the start of the range is not less than the end.
        """
        if start >= end:
            raise ValueError("Start of range must be less than the end.")
        return [x ** 2 for x in range(start, end + 1)]
