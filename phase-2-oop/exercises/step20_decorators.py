def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- Starting ---")
        func(*args, **kwargs)
        print("--- Done ---")
    return wrapper

@greet_decorator
def process_data():
    print(f"Processing data...")

@greet_decorator
def say_hello(name):
    print(f"Hello, {name}")

process_data()
say_hello("Noman")
