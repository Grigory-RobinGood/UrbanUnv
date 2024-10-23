import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнование")
    number_atlas = 1
    for i in range(1, 6):
        await asyncio.sleep(power / 2)
        number_atlas += 1
        print(f"Силач {name} поднял {i} шар")
    return name


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

    for completed_task in asyncio.as_completed([task1, task2, task3]):
        name = await completed_task  # Получаем результат (имя)
        print(f"Силач {name} закончил соревнование")
        break


asyncio.run(start_tournament())
