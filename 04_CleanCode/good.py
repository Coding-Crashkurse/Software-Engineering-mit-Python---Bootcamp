def calculate(a: int, b: int, operation: str) -> float:
    """
    Führt eine arithmetische Operation mit zwei Zahlen durch.

    Args:
        a (int): Die erste Zahl.
        b (int): Die zweite Zahl.
        operation (str): Die arithmetische Operation, die durchgeführt werden soll:
                         "add" für Addition,
                         "multiply" für Multiplikation,
                         "divide" für Division.

    Returns:
        float: Das Ergebnis der Operation.

    Raises:
        ValueError: Wenn die Operation ungültig ist.
    """
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed.")
    else:
        raise ValueError(f"Invalid operation: {operation}")

try:
    result = calculate(4, 2, "add")
    print(result)
except ValueError as e:
    print(e)
