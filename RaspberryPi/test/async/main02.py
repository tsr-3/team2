import random
import asyncio

def call():
    asyncio.get_event_loop().run_until_complete(main())

async def main():
    array = arr(100000)
    result = {}
    result['sum'] = sum(array)
    result['product'] = product(array)
    print(await asyncio.gather(result['sum'], result['product']))

async def sum(arr):
    result = 0
    cnt = 0
    for val in arr:
        result += val
        cnt += 1
        print('sum: ' + str(result))
        if cnt % 1000 == 0:
            await asyncio.sleep(1)
    return result

async def product(arr):
    result = 1
    cnt = 0
    for val in arr:
        result *= val
        cnt += 1
        print('product: ' + str(result))
        if cnt % 1000 == 0:
            await asyncio.sleep(1)
    return result

def arr(size):
    array = [0] * size
    for cnt in range(size):
        array[cnt] = random.random()
    return array
