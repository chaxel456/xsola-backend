# app/middleware/rate_limit.py

import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class RateLimitMiddleware(
    BaseHTTPMiddleware
):

    clients = {}

    LIMIT = 100

    WINDOW = 60

    async def dispatch(
        self,
        request: Request,
        call_next
    ):

        ip = request.client.host

        now = time.time()

        history = self.clients.get(
            ip,
            []
        )

        history = [
            t for t in history
            if now - t < self.WINDOW
        ]

        if len(history) >= self.LIMIT:

            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Too many requests"
                }
            )

        history.append(now)

        self.clients[ip] = history

        return await call_next(request)