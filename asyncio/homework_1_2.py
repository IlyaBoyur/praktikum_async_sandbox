import asyncio
import signal
from datetime import datetime


def time_callback():
    print(datetime.now().ctime())


def signal_handler(signal: int):
    SIGNAL_JOB_MAP = {
        signal.SIGINT: lambda: print("SIGTERM called. Finishing"),
        signal.SIGTERM: lambda: print("SIGINT called. Finishing"),
    }
    SIGNAL_JOB_MAP[signal]()
    loop = asyncio.get_event_loop()
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, signal_handler, signal.SIGINT)
    loop.add_signal_handler(signal.SIGTERM, signal_handler, signal.SIGTERM)
    loop.call_later(3, time_callback)
    loop.run_forever()
