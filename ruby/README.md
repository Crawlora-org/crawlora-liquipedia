# Crawlora Liquipedia API client for Ruby (`crawlora-liquipedia`)

This Ruby gem calls Crawlora's hosted Liquipedia API at `https://api.crawlora.net/api/v1`. It exposes 12 endpoints covering wiki discovery, pages, search, categories, recent changes, links, and backlinks; it does not call or scrape Liquipedia directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-liquipedia"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/liquipedia"

client = Crawlora::Liquipedia::Client.new
result = client.request("liquipedia-search", JSON.parse("{\"wiki\": \"sample\", \"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 12 API operations.

```ruby
client = Crawlora::Liquipedia::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Liquipedia API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-liquipedia) for account setup, the API operation reference, and release history.
