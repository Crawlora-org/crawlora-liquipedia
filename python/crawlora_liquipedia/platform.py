"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class LiquipediaClient(CrawloraClient):
    """Synchronous Liquipedia API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-liquipedia-python/0.2.0')
        super().__init__(*args, **kwargs)

    def all_pages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-all-pages', params, response_type=response_type, timeout=timeout, headers=headers)

    def backlinks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-backlinks', params, response_type=response_type, timeout=timeout, headers=headers)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def category_members(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-category-members', params, response_type=response_type, timeout=timeout, headers=headers)

    def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    def links(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-links', params, response_type=response_type, timeout=timeout, headers=headers)

    def page(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-page', params, response_type=response_type, timeout=timeout, headers=headers)

    def prefix_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-prefix-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def recent_changes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-recent-changes', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def tags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-tags', params, response_type=response_type, timeout=timeout, headers=headers)

    def wikis(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('liquipedia-wikis', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncLiquipediaClient(AsyncCrawloraClient):
    """Asynchronous Liquipedia API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-liquipedia-python/0.2.0')
        super().__init__(*args, **kwargs)

    async def all_pages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-all-pages', params, response_type=response_type, timeout=timeout, headers=headers)

    async def backlinks(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-backlinks', params, response_type=response_type, timeout=timeout, headers=headers)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def category_members(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-category-members', params, response_type=response_type, timeout=timeout, headers=headers)

    async def enums(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-enums', params, response_type=response_type, timeout=timeout, headers=headers)

    async def links(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-links', params, response_type=response_type, timeout=timeout, headers=headers)

    async def page(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-page', params, response_type=response_type, timeout=timeout, headers=headers)

    async def prefix_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-prefix-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def recent_changes(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-recent-changes', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-tags', params, response_type=response_type, timeout=timeout, headers=headers)

    async def wikis(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('liquipedia-wikis', params, response_type=response_type, timeout=timeout, headers=headers)
