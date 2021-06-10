import random
import asyncio

def call():
    asyncio.get_event_loop().run_until_complete(main())

async def main():
    array = arr(100000)
    res_sum = sum(array)
    res_product = product(array)
    print(await asyncio.gather(res_sum, res_product))

async def sum(arr):
    result = await sum_cell(arr)
    return result

async def product(arr):
    result = await product_cell(arr)
    return result

async def sum_cell(arr):
    sum = 0
    for val in arr:
        sum += val
        print('sum: ' + str(sum))
    return sum

async def product_cell(arr):
    product = 0
    for val in arr:
        product *= val
        print('product: ' + str(product))
    return product

def arr(size):
    array = []
    for i in range(size):
        array.append(random.random())
    return array

if __name__ == '__main__':
    call()
