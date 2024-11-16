#!/usr/bin/env python3
from theHarvester.restfulHarvest import main
import asyncio

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    main()
