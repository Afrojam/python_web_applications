# asyncio_example.py
# From https://realpython.com/async-io-python/
import argparse
import asyncio

WAITING_TIME = 0.5

def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION]",
        description="Executes the same code sync or async."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument("-a", action="store_true", help="Enable asynchronous execution")

    return parser


async def async_count():
    print("one")
    await asyncio.sleep(WAITING_TIME)  # Go do whatever and return the control to the event loop
    print("Two")
    await asyncio.sleep(WAITING_TIME)  # Go do whatever and return the control to the event loop


async def main():
    await asyncio.gather(async_count(), async_count(),
                         async_count())  #Each call to count() is a loop.
    # asyncio.gather waits on futures and brings the outputs once all the tasks have finished
    # asyncio.wait is similar, but provides low level control on the execution of the tasks (i.e: Output after first
    # task is done).


def sync_count():
    print("One")
    time.sleep(WAITING_TIME)
    print("Two")
    time.sleep(WAITING_TIME)


def sync_main():
    for _ in range(3):
        sync_count()


if __name__ == "__main__":
    parser = init_argparse()
    args = parser.parse_args()
    import time

    s = time.perf_counter()
    if args.a:
        asyncio.run(main()) # Event loop creation on the coroutine main.
    else:
        sync_main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
