# Crawlora Liquipedia API client for Java

The official Java client for Crawlora's hosted Liquipedia API. It exposes 12 endpoints covering wiki discovery, pages, search, categories, recent changes, links, and backlinks. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-liquipedia</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-java-console) to get an API key.

```java
import net.crawlora.liquipedia.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.wikis(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Liquipedia API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-liquipedia/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-liquipedia)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=liquipedia-java-api-docs)
