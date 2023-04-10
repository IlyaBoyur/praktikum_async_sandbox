import asyncio


async def main():
    my_future = asyncio.Future()
    print(asyncio.isfuture(my_future))
    print(my_future.done())  # Результат ещё не получен, поэтому Future счиатется невыполненной
    print(my_future.cancelled())
    print(my_future._state)
    my_future.set_result('Результат')
    print(my_future.done())  # Теперь Future завершена
    print(my_future.result())


asyncio.run(main()) 