def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    return a / b


def is_even(number: int) -> bool:
    return number % 2 == 0


from typing import List, Tuple

CityTemperature = Tuple[str, float]
TemperatureList = List[CityTemperature]


def print_temperatures(temperatures: TemperatureList) -> None:
    for city, temp in temperatures:
        print(f"In {city}, the temperature is {temp}°C")


temperatures = [("Berlin", 20.5), ("Paris", 25.3), ("London", 18.2)]
print_temperatures(temperatures)


from typing import Dict, List


def mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


def get_value(mapping: Dict[str, int], key: str) -> int:
    return mapping[key]


from typing import Optional


def find_first_even(numbers: List[int]) -> Optional[int]:
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


from typing import Callable


def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
