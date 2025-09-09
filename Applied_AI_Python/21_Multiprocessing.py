import multiprocessing
import time


def square_numbers():
    for i in range(6):
        time.sleep(2)
        print(f"Number: {i*i}")


def cube_letters():
    for letter in range(6):
        time.sleep(2.1)
        print(f"Letter: {letter**3}")


if __name__ == "__main__":
    # Create processes (not threads!)
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_letters)

    t = time.time()

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"Finished in: {finished_time:.2f} seconds")
