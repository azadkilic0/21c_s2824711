from .SquareGenerator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to the start.")
        return [x ** 3 for x in range(start, end + 1)]
