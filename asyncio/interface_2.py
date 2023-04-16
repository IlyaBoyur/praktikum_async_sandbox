import asyncio
import time


async def greeting(name: str):
    print(f"{time.ctime()} Привет, {name}...")
    await asyncio.sleep(1.6)
    print(f"{time.ctime()} Пока, {name}...")
    event_loop = asyncio.get_event_loop()
    event_loop.stop()


def blocking_sleep():
    time.sleep(0.7)
    print(f"{time.ctime()} Вызов блокирующего метода в треде...")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(greeting("гость"))
    loop.run_in_executor(None, blocking_sleep)
    loop.run_forever()
    pending_tasks = asyncio.all_tasks(loop)
    group_tasks = asyncio.gather(*pending_tasks, return_exceptions=True)
    loop.run_until_complete(group_tasks)
    loop.close()
