from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        """Abstract method to generate a sequence of squares from start to end.
        Must be implemented by subclasses.

        Parameters:
            start (int): The starting number of the range.
            end (int): The ending number of the range.

        Returns:
            list: A list of squares from start to end.
        """
        pass
