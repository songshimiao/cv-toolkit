import sys

import numpy as np


def calculate(values: np.ndarray) -> float:
    total = float(np.sum(values))
    mean = float(np.mean(values))
    result = total + mean
    return result


def main() -> None:
    values = np.array([10, 20, 30], dtype=float)

    print("Python:", sys.executable)
    print("NumPy:", np.__version__)

    answer = calculate(values)
    print("Result:", answer)


if __name__ == "__main__":
    main()
