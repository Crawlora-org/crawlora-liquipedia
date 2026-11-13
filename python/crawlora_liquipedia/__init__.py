"""Typed Liquipedia client for the Crawlora hosted API."""

from .platform import LiquipediaClient, AsyncLiquipediaClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = LiquipediaClient
AsyncClient = AsyncLiquipediaClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Liquipedia'
PLATFORM = 'liquipedia'
CONTRACT_REVISION = 'sha256:158c4854176f104cc7b6851de936ca85b4f0ff757b4bcd2ca75ea6cd4fef0918'

__all__ = [
    "LiquipediaClient", "AsyncLiquipediaClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
