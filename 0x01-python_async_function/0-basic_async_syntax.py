#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds (included).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
