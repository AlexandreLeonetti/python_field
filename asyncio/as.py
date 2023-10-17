# this is a small aync io tutorial
import asyncio

async def  main():
    print("A")
    await asyncio.sleep(2)
    print("B")

asyncio.run(main())
