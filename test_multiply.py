"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
