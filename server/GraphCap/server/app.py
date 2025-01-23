# SPDX-License-Identifier: Apache-2.0
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from GraphCap.agents.router import router as agents_router
from GraphCap.config.router import router as server_router
from GraphCap.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    start_time = time.time()
    logger.info("Starting server initialization...")
    initialization_time = time.time() - start_time
    logger.info(f"Server initialization completed in {initialization_time:.2f} seconds")
    yield
    # Shutdown
    logger.info("Shutting down...")


app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routers
api_version = "/api/v1"
app.include_router(prefix=api_version, router=server_router)
app.include_router(prefix=api_version, router=agents_router)
