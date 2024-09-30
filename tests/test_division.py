import src.division

def test_division():
    assert src.division.perform_operation(10, 5) == 2
    assert src.division.perform_operation(1, 1) == 1
    assert src.division.perform_operation(100, 2) == 50
