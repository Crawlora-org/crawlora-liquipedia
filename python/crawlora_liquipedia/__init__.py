"""Typed Liquipedia client for the Crawlora hosted API."""

from .platform import LiquipediaClient, AsyncLiquipediaClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = LiquipediaClient
AsyncClient = AsyncLiquipediaClient
__version__ = '0.3.0'
DISPLAY_NAME = 'Liquipedia'
PLATFORM = 'liquipedia'
CONTRACT_REVISION = 'sha256:fb7e59b76f3ad34121322924359d88530fde7dff2df2189e1a35c59f2da3af81'

__all__ = [
    "LiquipediaClient", "AsyncLiquipediaClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
