
def calculate_fuel_cost(quantity, price):
    return quantity * price


def test_petrol_cost():
    assert calculate_fuel_cost(10, 100) == 1000


def test_diesel_cost():
    assert calculate_fuel_cost(20, 90) == 1800


def test_zero_quantity():
    assert calculate_fuel_cost(0, 100) == 0
