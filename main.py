import asyncio
import time
from datetime import datetime

from config import (
    BOT_NAME,
    CHECK_INTERVAL_SECONDS,
    LANG,
    ENABLE_NO_SIGNAL_ALERT
)

from engine import run_engine
from telegram_control import (
    start_bot,
    send_signal_message,
    send_no_signal_message
)
from utils import log_info, log_error


async def main_loop():
    log_info(f"{BOT_NAME} Engine Started")

    while True:
        try:
            signals = run_engine()

            if signals:
                for signal in signals:
                    await send_signal_message(signal)
            else:
                if ENABLE_NO_SIGNAL_ALERT:
                    await send_no_signal_message()

        except Exception as e:
            log_error(f"Engine Error: {e}")

        await asyncio.sleep(CHECK_INTERVAL_SECONDS)


async def main():
    log_info(f"{BOT_NAME} Initializing...")
    await start_bot()
    await main_loop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log_info("Bot stopped manually")
