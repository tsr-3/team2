import asyncio

counter = 0

def call():
    asyncio.get_event_loop().run_until_complete(interrupt())
    asyncio.get_event_loop().run_until_complete(main())

async def interrupt():
    await asyncio.sleep(20)
    asyncio.get_event_loop().stop()

async def main():
    global counter
    while True:
        counter += 1
        await asyncio.sleep(0.3)

# うまく動かん わからん
