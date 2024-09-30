import src.subtraction

def test_subtraction():
    # Assert
    assert src.subtraction.perform_operation(1, 1) == 0
    assert src.subtraction.perform_operation(100, 1) == 99
    assert src.subtraction.perform_operation(99, 55) == 44
