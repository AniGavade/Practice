import time

start = time.perf_counter()  # It can return floating time value in seconds.(in fractions of seconds)


def do_something():
    print("sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping")


do_something()
finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds(s)")
