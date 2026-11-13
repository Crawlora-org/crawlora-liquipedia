# crawlora-liquipedia — Liquipedia API client for Python

Python client for Crawlora's hosted Liquipedia API. It exposes 12 API endpoints covering wiki discovery, pages, search, categories, recent changes, links, and backlinks. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-python-homepage); the package does not run a browser or scrape
Liquipedia locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Liquipedia or its owners.

## Install

```sh
python -m pip install crawlora-liquipedia
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_liquipedia import LiquipediaClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with LiquipediaClient(api_key=api_key) as client:
    result_1 = client.wikis()
    print(result_1)
    result_2 = client.search(wiki='counterstrike', q='Major', srlimit='5')
    print(result_2)
```

The package also exports `Client` as an alias for `LiquipediaClient`. Operation
methods are available directly in snake_case and through the `liquipedia`
group. The async package client is `AsyncLiquipediaClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_liquipedia import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.wikis()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/examples/python.py) for a complete usage example.

## Supported Liquipedia API endpoints

This package exposes every route below through direct snake_case methods and the `liquipedia` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/liquipedia/all-pages` | `liquipedia-all-pages` | Enumerate pages on a Liquipedia wiki |
| `GET` | `/liquipedia/backlinks` | `liquipedia-backlinks` | List Liquipedia pages linking to a page |
| `GET` | `/liquipedia/categories` | `liquipedia-categories` | Enumerate categories on a Liquipedia wiki |
| `GET` | `/liquipedia/category-members` | `liquipedia-category-members` | List Liquipedia category members |
| `GET` | `/liquipedia/enums` | `liquipedia-enums` | Discover Liquipedia MediaWiki filters |
| `GET` | `/liquipedia/links` | `liquipedia-links` | List links from Liquipedia pages |
| `GET` | `/liquipedia/page` | `liquipedia-page` | Get a Liquipedia page |
| `GET` | `/liquipedia/prefix-search` | `liquipedia-prefix-search` | Suggest matching page titles on a Liquipedia wiki |
| `GET` | `/liquipedia/recent-changes` | `liquipedia-recent-changes` | List recent changes on a Liquipedia wiki |
| `GET` | `/liquipedia/search` | `liquipedia-search` | Search a Liquipedia wiki |
| `GET` | `/liquipedia/tags` | `liquipedia-tags` | List change tags on a Liquipedia wiki |
| `GET` | `/liquipedia/wikis` | `liquipedia-wikis` | Discover Liquipedia wikis |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
