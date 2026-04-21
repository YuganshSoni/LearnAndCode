import math

from config import (
    MINIMUM_ITERATOR_VALUE,
    MINIMUM_UPPER_LIMIT,
    TYPE_ERROR_MESSAGE,
    VALUE_ERROR_MESSAGE,
    POSITIVE_INT_REQUIRED
)


class DivisorEqualityAnalyzer:
    """
    Analyzes integers in an interval to find consecutive numbers 
    with the same number of positive divisors.
    """

    def get_total_divisors(self, number: int) -> int:
        """
        Calculates the count of positive divisors for a given integer.
        """
        if number < 1:
            raise ValueError(POSITIVE_INT_REQUIRED)
        
        count = 0
        limit = math.isqrt(number)
        for i in range(1, limit + 1):
            if number % i == 0:
                count += 2
                if i * i == number:
                    count -= 1
        return count

    def count_consecutive_matches(self, upper_limit: int) -> int:
        """
        Counts how many values of n (1 < n < upper_limit) satisfy:
        count_divisors(n) == count_divisors(n + 1).
        """
        self._validate_input(upper_limit)
        
        match_count = 0
        for n in range(MINIMUM_ITERATOR_VALUE, upper_limit):
            if self._are_divisors_equal(n, n + 1):
                match_count += 1
        
        return match_count

    def _validate_input(self, value: int) -> None:
        """Ensure the input upper limit is a valid integer."""
        if not isinstance(value, int):
            raise TypeError(TYPE_ERROR_MESSAGE)
        if value < MINIMUM_UPPER_LIMIT:
            raise ValueError(VALUE_ERROR_MESSAGE.format(MINIMUM_UPPER_LIMIT, value))

    def _are_divisors_equal(self, first: int, second: int) -> bool:
        """Helper to compare divisor counts of two numbers."""
        return self.get_total_divisors(first) == self.get_total_divisors(second)

    def run_analysis(self, test_cases: list) -> list:
        """Process a list of test cases and return counts."""
        if not isinstance(test_cases, list):
            raise TypeError(f"Expected a list of test cases, received: {type(test_cases).__name__}")
        
        return [self.count_consecutive_matches(k) for k in test_cases]


def main():
    """Entry point for command line execution."""
    try:
        t_str = input("Enter number of test cases: ")
        t = int(t_str)
        analyzer = DivisorEqualityAnalyzer()
        
        cases = []
        for i in range(t):
            k = int(input(f"Limit k for case {i + 1}: "))
            cases.append(k)
        
        results = analyzer.run_analysis(cases)
        for res in results:
            print(res)
    except (ValueError, EOFError):
        pass


if __name__ == "__main__":
    main()
