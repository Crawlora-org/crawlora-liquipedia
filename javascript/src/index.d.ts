import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class LiquipediaClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  allPages(params: OperationParamsMap["liquipedia-all-pages"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  backlinks(params: OperationParamsMap["liquipedia-backlinks"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params: OperationParamsMap["liquipedia-categories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categoryMembers(params: OperationParamsMap["liquipedia-category-members"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  enums(params: OperationParamsMap["liquipedia-enums"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  links(params: OperationParamsMap["liquipedia-links"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  page(params: OperationParamsMap["liquipedia-page"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  prefixSearch(params: OperationParamsMap["liquipedia-prefix-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  recentChanges(params: OperationParamsMap["liquipedia-recent-changes"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["liquipedia-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tags(params: OperationParamsMap["liquipedia-tags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  wikis(params?: OperationParamsMap["liquipedia-wikis"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  allPages(params: OperationParamsMap["liquipedia-all-pages"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  backlinks(params: OperationParamsMap["liquipedia-backlinks"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params: OperationParamsMap["liquipedia-categories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categoryMembers(params: OperationParamsMap["liquipedia-category-members"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  enums(params: OperationParamsMap["liquipedia-enums"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  links(params: OperationParamsMap["liquipedia-links"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  page(params: OperationParamsMap["liquipedia-page"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  prefixSearch(params: OperationParamsMap["liquipedia-prefix-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  recentChanges(params: OperationParamsMap["liquipedia-recent-changes"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["liquipedia-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tags(params: OperationParamsMap["liquipedia-tags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  wikis(params?: OperationParamsMap["liquipedia-wikis"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  allPages(...args: OperationRequestArgs<"liquipedia-all-pages">): Promise<OperationResponseMap["liquipedia-all-pages"]>;
  backlinks(...args: OperationRequestArgs<"liquipedia-backlinks">): Promise<OperationResponseMap["liquipedia-backlinks"]>;
  categories(...args: OperationRequestArgs<"liquipedia-categories">): Promise<OperationResponseMap["liquipedia-categories"]>;
  categoryMembers(...args: OperationRequestArgs<"liquipedia-category-members">): Promise<OperationResponseMap["liquipedia-category-members"]>;
  enums(...args: OperationRequestArgs<"liquipedia-enums">): Promise<OperationResponseMap["liquipedia-enums"]>;
  links(...args: OperationRequestArgs<"liquipedia-links">): Promise<OperationResponseMap["liquipedia-links"]>;
  page(...args: OperationRequestArgs<"liquipedia-page">): Promise<OperationResponseMap["liquipedia-page"]>;
  prefixSearch(...args: OperationRequestArgs<"liquipedia-prefix-search">): Promise<OperationResponseMap["liquipedia-prefix-search"]>;
  recentChanges(...args: OperationRequestArgs<"liquipedia-recent-changes">): Promise<OperationResponseMap["liquipedia-recent-changes"]>;
  search(...args: OperationRequestArgs<"liquipedia-search">): Promise<OperationResponseMap["liquipedia-search"]>;
  tags(...args: OperationRequestArgs<"liquipedia-tags">): Promise<OperationResponseMap["liquipedia-tags"]>;
  wikis(...args: OperationRequestArgs<"liquipedia-wikis">): Promise<OperationResponseMap["liquipedia-wikis"]>;
}
export { LiquipediaClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default LiquipediaClient;
