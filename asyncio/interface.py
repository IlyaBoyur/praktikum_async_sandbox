import time
import asyncio

async def greeting(name: str):
    print(f'{time.ctime()} Привет, {name}...')
    await asyncio.sleep(1.6)
    print(f'{time.ctime()} Пока, {name}...')
    event_loop = asyncio.get_event_loop()
    event_loop.stop()  # Необходимо явно вызвать stop для остановки цикла событий

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(greeting('гость'))
    loop.create_task(greeting('пользователь'))
    loop.create_task(greeting('администратор'))
    try:
        loop.run_forever()
    finally:
        loop.close()



    loop_2 = asyncio.get_event_loop()
    print(f"ID for loop - {id(loop)}")
    print(f"ID for loop_2 - {id(loop_2)}")
    print(f"loop is equal to loop_2 - {loop is loop_2}")
