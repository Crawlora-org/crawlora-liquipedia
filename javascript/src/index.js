import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class LiquipediaClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-liquipedia-js/0.2.0" });
    this["allPages"] = (...args) => this.request("liquipedia-all-pages", ...args);
    this["backlinks"] = (...args) => this.request("liquipedia-backlinks", ...args);
    this["categories"] = (...args) => this.request("liquipedia-categories", ...args);
    this["categoryMembers"] = (...args) => this.request("liquipedia-category-members", ...args);
    this["enums"] = (...args) => this.request("liquipedia-enums", ...args);
    this["links"] = (...args) => this.request("liquipedia-links", ...args);
    this["page"] = (...args) => this.request("liquipedia-page", ...args);
    this["prefixSearch"] = (...args) => this.request("liquipedia-prefix-search", ...args);
    this["recentChanges"] = (...args) => this.request("liquipedia-recent-changes", ...args);
    this["search"] = (...args) => this.request("liquipedia-search", ...args);
    this["tags"] = (...args) => this.request("liquipedia-tags", ...args);
    this["wikis"] = (...args) => this.request("liquipedia-wikis", ...args);
  }
}

export { LiquipediaClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.2.0";
export default LiquipediaClient;
