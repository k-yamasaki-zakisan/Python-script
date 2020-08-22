import asyncio
import time
import functools


def delayed_print(mes, sec):
    time.sleep(sec)
    print(mes)


async def call_1(mes, sec):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, delayed_print, mes, sec)


async def call_2(mes, sec):
    loop = asyncio.get_event_loop()
    func = functools.partial(delayed_print, mes, sec)
    await loop.run_in_executor(None, func)


async def call_3(message, seconds):
    loop = asyncio.get_event_loop()
    func = functools.partial(delayed_print, mes=message, sec=seconds)
    await loop.run_in_executor(None, func)


def main():
    loop = asyncio.get_event_loop()
    gather = asyncio.gather(
        call_1('333', 3),
        call_2('222', 2),
        call_1('111', 1)
    )
    loop.run_until_complete(gather)


if __name__ == '__main__':
    main()