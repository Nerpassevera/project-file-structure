from src.addition import perform_operation as addition

def perform_operation(multiplier, multiplicand):
    result = 0
    for _ in range(multiplier):
        result = addition(result, multiplicand)
    return result