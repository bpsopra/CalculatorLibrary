"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_division(self):
        assert 2 == calculator.divide(4, 2)
