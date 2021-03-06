from collections import deque


# The generator thing
def countdown(n):
    while n > 0:
        # Pass execution to another task
        yield n
        n -= 1


tasks = deque()
tasks.extend([countdown(10), countdown(5), countdown(20)])


def run():
    while tasks:
        # The event loop
        task = tasks.popleft()
        try:
            x = next(task)
            print(x)
            tasks.append(task)
        except StopIteration:
            print("End of task")


if __name__ == "__main__":
    run()
