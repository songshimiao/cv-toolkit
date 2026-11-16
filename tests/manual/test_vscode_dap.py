import sys
from pathlib import Path


def objective(x: float) -> float:
    return (x - 3.0) ** 2 + 1.0

def main() -> None:
    values= [2,4,6,8]
    total = sum(values)
    mean = total / len(values)

    result = total+mean
    score = objective(mean)

    print("Python:", sys.executable)
    print("Project:", Path.cwd())
    print("Result:", result)
    print("Score:", score)


if __name__ == "__main__":
    main()

