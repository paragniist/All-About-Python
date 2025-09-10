from concurrent.futures import ProcessPoolExecutor
import time


def square_numbers(number):
    time.sleep(1)
    return f"Square: {number * number}"


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square_numbers, numbers))
        # Collect results safely

    for result in results:
        print(result)
