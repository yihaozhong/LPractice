import multiprocessing
import threading


def my_decorator(func):
    def wrapper():
        print("hi, print before executing the function")
        func()

    return wrapper


@my_decorator
def hello():
    print("hello hello")


hello()


def print_numbers():
    for i in range(1, 100):
        print(i)


def print_letters():
    for letter in range(100):
        print(letter)


# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Both threads have finished.")
counter = 0
# Lock
lock = threading.Lock()


def increment_counter():
    global counter
    with lock:
        temp = counter + 1
        counter = temp


# Create multiple threads
threads = [threading.Thread(target=increment_counter) for _ in range(1000)]

# Start and join threads
for t in threads:
    t.start()

for t in threads:
    t.join()

print(counter)  # Expected: 1000


def square(n):
    return n * n


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool()
    result = pool.map(square, data)
    print(result)  # Outputs: [1, 4, 9, 16, 25]
