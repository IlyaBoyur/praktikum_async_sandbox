import asyncio
import random


async def delay():
    rand_delay = random.uniform(0.3, 1.9)
    print(f"Generated rand {rand_delay}...")
    await asyncio.sleep(rand_delay)
    print(f"Coro finished {rand_delay}...")
    return rand_delay


async def main():
    tasks = [asyncio.Task(delay()) for i in range(5)]
    print("Started...")
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED
    )
    for task in done:
        print(task.result())


if __name__ == "__main__":
    asyncio.run(main())
