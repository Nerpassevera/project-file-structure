import src.multiplication

def test_multiplication():
    # Assert
    assert src.multiplication.perform_operation(1, 1) == 1
    assert src.multiplication.perform_operation(10, 20) == 200
    assert src.multiplication.perform_operation(55, 11) == 605
