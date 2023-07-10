#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that takes in two integer arguments (n and max_delay),
    and returns a list of n random float delays between 0 and max_delay."""
    delays = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
