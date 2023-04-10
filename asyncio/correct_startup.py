import asyncio


async def delay(time: int):
    await asyncio.sleep(time)


def startup():
    loop = asyncio.get_event_loop()
    task = loop.create_task(delay(2))
    loop.run_until_complete(task)
    print("Startup finished!")


if __name__ == "__main__":
    startup()
    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    finally:
        loop.close()
