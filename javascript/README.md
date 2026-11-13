# @crawlora-org/liquipedia — Liquipedia API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Liquipedia API.
It exposes 12 API endpoints for wiki discovery, pages, search, categories, recent changes, links, and backlinks through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-javascript-homepage). It does not run a browser or scrape Liquipedia locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Liquipedia or its owners.

## Install

```sh
npm install @crawlora-org/liquipedia
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { LiquipediaClient } from "@crawlora-org/liquipedia";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new LiquipediaClient({ apiKey });
const result1 = await client.wikis({});
console.log(result1);
const result2 = await client.search({ wiki: "counterstrike", q: "Major", srlimit: "5" });
console.log(result2);
```

The client also exports `Client` as an alias for `LiquipediaClient`. Operation
methods are available directly in camelCase and through the `liquipedia`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Liquipedia API endpoints

This package exposes each route below as a direct method and through the `liquipedia` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md) for complete input details.

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

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
