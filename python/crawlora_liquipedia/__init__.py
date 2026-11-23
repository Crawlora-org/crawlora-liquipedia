"""Typed Liquipedia client for the Crawlora hosted API."""

from .platform import LiquipediaClient, AsyncLiquipediaClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = LiquipediaClient
AsyncClient = AsyncLiquipediaClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Liquipedia'
PLATFORM = 'liquipedia'
CONTRACT_REVISION = 'sha256:082e401eac4261443369b03e0bc06d47982d8179b660b8a889ac62ac4a802b58'

__all__ = [
    "LiquipediaClient", "AsyncLiquipediaClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
