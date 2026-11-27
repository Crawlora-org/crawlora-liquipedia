# Crawlora Liquipedia API client for PHP (`crawlora/liquipedia`)

This PHP package calls Crawlora's hosted Liquipedia API at `https://api.crawlora.net/api/v1`. It exposes 14 endpoints covering wiki discovery, pages, search, categories, recent changes, links, and backlinks. It does not call or scrape Liquipedia directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/liquipedia
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Liquipedia\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("liquipedia-search", ['wiki' => 'sample', 'q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 14 API operations.

## Supported Liquipedia API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/liquipedia/all-pages` | `liquipedia-all-pages` | Enumerate pages on a Liquipedia wiki |
| `GET` | `/liquipedia/backlinks` | `liquipedia-backlinks` | List Liquipedia pages linking to a page |
| `GET` | `/liquipedia/categories` | `liquipedia-categories` | Enumerate categories on a Liquipedia wiki |
| `GET` | `/liquipedia/category-members` | `liquipedia-category-members` | List Liquipedia category members |
| `GET` | `/liquipedia/embeddedin` | `liquipedia-embeddedin` | List Liquipedia pages that transclude a template |
| `GET` | `/liquipedia/enums` | `liquipedia-enums` | Discover Liquipedia MediaWiki filters |
| `GET` | `/liquipedia/links` | `liquipedia-links` | List links from Liquipedia pages |
| `GET` | `/liquipedia/page` | `liquipedia-page` | Get a Liquipedia page |
| `GET` | `/liquipedia/prefix-search` | `liquipedia-prefix-search` | Suggest matching page titles on a Liquipedia wiki |
| `GET` | `/liquipedia/recent-changes` | `liquipedia-recent-changes` | List recent changes on a Liquipedia wiki |
| `GET` | `/liquipedia/search` | `liquipedia-search` | Search a Liquipedia wiki |
| `GET` | `/liquipedia/tags` | `liquipedia-tags` | List change tags on a Liquipedia wiki |
| `GET` | `/liquipedia/wikis` | `liquipedia-wikis` | Discover Liquipedia wikis |
| `GET` | `/liquipedia/wikitext` | `liquipedia-wikitext` | Get Liquipedia page wikitext |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-liquipedia). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md).
