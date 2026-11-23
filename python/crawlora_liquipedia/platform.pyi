from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelLiquipediaResponse = TypedDict('ModelLiquipediaResponse', {
    'attribution': NotRequired[str],
    'data': NotRequired[Any],
    'license': NotRequired[str],
    'license_url': NotRequired[str],
    'page_url': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

LiquipediaAllPagesResponse = Any
LiquipediaAllPagesParams = TypedDict('LiquipediaAllPagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'apfrom': NotRequired[str],
    'apto': NotRequired[str],
    'apprefix': NotRequired[str],
    'apnamespace': NotRequired[int],
    'apfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'apfilterlanglinks': NotRequired[Literal['all', 'withlanglinks', 'withoutlanglinks']],
    'apminsize': NotRequired[int],
    'apmaxsize': NotRequired[int],
    'apprtype': NotRequired[list[Literal['edit', 'move', 'upload']]],
    'apprlevel': NotRequired[Literal['autoconfirmed', 'sysop']],
    'apprfiltercascade': NotRequired[Literal['all', 'cascading', 'noncascading']],
    'apprexpiry': NotRequired[Literal['all', 'definite', 'indefinite']],
    'aplimit': NotRequired[str],
    'apdir': NotRequired[Literal['ascending', 'descending']],
    'apcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaBacklinksResponse = Any
LiquipediaBacklinksParams = TypedDict('LiquipediaBacklinksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'bltitle': NotRequired[str],
    'blpageid': NotRequired[int],
    'blnamespace': NotRequired[list[str]],
    'bldir': NotRequired[Literal['ascending', 'descending']],
    'blfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'bllimit': NotRequired[str],
    'blredirect': NotRequired[bool],
    'blcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaCategoriesResponse = Any
LiquipediaCategoriesParams = TypedDict('LiquipediaCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'acfrom': NotRequired[str],
    'acto': NotRequired[str],
    'acprefix': NotRequired[str],
    'acdir': NotRequired[Literal['ascending', 'descending']],
    'acmin': NotRequired[int],
    'acmax': NotRequired[int],
    'aclimit': NotRequired[str],
    'acprop': NotRequired[list[Literal['size', 'hidden']]],
    'accontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaCategoryMembersResponse = Any
LiquipediaCategoryMembersParams = TypedDict('LiquipediaCategoryMembersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'cmtitle': NotRequired[str],
    'cmpageid': NotRequired[int],
    'cmnamespace': NotRequired[list[str]],
    'cmtype': NotRequired[list[Literal['file', 'page', 'subcat']]],
    'cmprop': NotRequired[list[Literal['ids', 'title', 'sortkey', 'sortkeyprefix', 'type', 'timestamp']]],
    'cmlimit': NotRequired[str],
    'continue': NotRequired[str],
    'cmcontinue': NotRequired[str],
    'cmsort': NotRequired[Literal['sortkey', 'timestamp']],
    'cmdir': NotRequired[Literal['asc', 'ascending', 'desc', 'descending', 'newer', 'older']],
    'cmstart': NotRequired[str],
    'cmend': NotRequired[str],
    'cmstarthexsortkey': NotRequired[str],
    'cmendhexsortkey': NotRequired[str],
    'cmstartsortkeyprefix': NotRequired[str],
    'cmendsortkeyprefix': NotRequired[str],
}, total=False)

LiquipediaEnumsResponse = Any
LiquipediaEnumsParams = TypedDict('LiquipediaEnumsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
}, total=False)

LiquipediaLinksResponse = Any
LiquipediaLinksParams = TypedDict('LiquipediaLinksParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'titles': NotRequired[list[str]],
    'pageids': NotRequired[list[int]],
    'revids': NotRequired[list[int]],
    'plnamespace': NotRequired[list[str]],
    'pllimit': NotRequired[str],
    'plcontinue': NotRequired[str],
    'pltitles': NotRequired[list[str]],
    'pldir': NotRequired[Literal['ascending', 'descending']],
    'redirects': NotRequired[bool],
    'continue': NotRequired[str],
}, total=False)

LiquipediaPageResponse = Any
LiquipediaPageParams = TypedDict('LiquipediaPageParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'page': NotRequired[str],
    'pageid': NotRequired[int],
    'oldid': NotRequired[int],
    'section': NotRequired[str],
    'redirects': NotRequired[bool],
}, total=False)

LiquipediaPrefixSearchResponse = Any
LiquipediaPrefixSearchParams = TypedDict('LiquipediaPrefixSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'pssearch': Required[str],
    'psnamespace': NotRequired[list[str]],
    'pslimit': NotRequired[str],
    'psoffset': NotRequired[int],
    'psprofile': NotRequired[Literal['classic', 'engine_autoselect', 'fast-fuzzy', 'fuzzy', 'fuzzy-subphrases', 'normal', 'normal-subphrases', 'strict']],
    'continue': NotRequired[str],
}, total=False)

LiquipediaRecentChangesResponse = Any
LiquipediaRecentChangesParams = TypedDict('LiquipediaRecentChangesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'rcstart': NotRequired[str],
    'rcend': NotRequired[str],
    'rcdir': NotRequired[Literal['newer', 'older']],
    'rcnamespace': NotRequired[list[str]],
    'rctag': NotRequired[str],
    'rcprop': NotRequired[list[Literal['comment', 'flags', 'ids', 'loginfo', 'parsedcomment', 'redirect', 'sha1', 'sizes', 'tags', 'timestamp', 'title', 'user', 'userid']]],
    'rcshow': NotRequired[list[Literal['!anon', '!autopatrolled', '!bot', '!minor', '!patrolled', '!redirect', 'anon', 'autopatrolled', 'bot', 'minor', 'patrolled', 'redirect', 'unpatrolled']]],
    'rclimit': NotRequired[str],
    'rctype': NotRequired[list[Literal['categorize', 'edit', 'external', 'log', 'new']]],
    'rctoponly': NotRequired[bool],
    'rctitle': NotRequired[str],
    'rccontinue': NotRequired[str],
    'continue': NotRequired[str],
    'rcslot': NotRequired[Literal['main']],
}, total=False)

LiquipediaSearchResponse = Any
LiquipediaSearchParams = TypedDict('LiquipediaSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'q': Required[str],
    'srnamespace': NotRequired[list[str]],
    'srwhat': NotRequired[Literal['nearmatch', 'text', 'title']],
    'srlimit': NotRequired[str],
    'sroffset': NotRequired[int],
    'continue': NotRequired[str],
    'srsort': NotRequired[Literal['create_timestamp_asc', 'create_timestamp_desc', 'incoming_links_asc', 'incoming_links_desc', 'just_match', 'last_edit_asc', 'last_edit_desc', 'none', 'random', 'relevance', 'title_natural_asc', 'title_natural_desc', 'user_random']],
    'srinfo': NotRequired[list[Literal['rewrittenquery', 'suggestion', 'totalhits']]],
    'srprop': NotRequired[list[Literal['size', 'wordcount', 'timestamp', 'snippet', 'titlesnippet', 'redirecttitle', 'redirectsnippet', 'sectiontitle', 'sectionsnippet', 'isfilematch', 'categorysnippet', 'extensiondata']]],
    'srinterwiki': NotRequired[bool],
    'srenablerewrites': NotRequired[bool],
    'srqiprofile': NotRequired[Literal['classic', 'classic_noboostlinks', 'empty', 'wsum_inclinks', 'wsum_inclinks_pv', 'popular_inclinks_pv', 'popular_inclinks', 'engine_autoselect']],
    'srqdprofile': NotRequired[Literal['default', 'perfield_builder', 'perfield_builder_relaxed', 'perfield_builder_title_filter', 'engine_autoselect']],
}, total=False)

LiquipediaTagsResponse = Any
LiquipediaTagsParams = TypedDict('LiquipediaTagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'wiki': Required[str],
    'tgprop': NotRequired[list[Literal['active', 'defined', 'description', 'displayname', 'hitcount', 'source']]],
    'tglimit': NotRequired[str],
    'tgcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaWikisResponse = Any
LiquipediaWikisParams = TypedDict('LiquipediaWikisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

class LiquipediaGroup:
    @overload
    def all_pages(self, **params: Unpack[LiquipediaAllPagesStreamParams]) -> BinaryIO: ...
    @overload
    def all_pages(self, **params: Unpack[LiquipediaAllPagesTextResponseParams]) -> str: ...
    @overload
    def all_pages(self, **params: Unpack[LiquipediaAllPagesDefaultParams]) -> LiquipediaAllPagesResponse: ...
    @overload
    def backlinks(self, **params: Unpack[LiquipediaBacklinksStreamParams]) -> BinaryIO: ...
    @overload
    def backlinks(self, **params: Unpack[LiquipediaBacklinksTextResponseParams]) -> str: ...
    @overload
    def backlinks(self, **params: Unpack[LiquipediaBacklinksDefaultParams]) -> LiquipediaBacklinksResponse: ...
    @overload
    def categories(self, **params: Unpack[LiquipediaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[LiquipediaCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[LiquipediaCategoriesDefaultParams]) -> LiquipediaCategoriesResponse: ...
    @overload
    def category_members(self, **params: Unpack[LiquipediaCategoryMembersStreamParams]) -> BinaryIO: ...
    @overload
    def category_members(self, **params: Unpack[LiquipediaCategoryMembersTextResponseParams]) -> str: ...
    @overload
    def category_members(self, **params: Unpack[LiquipediaCategoryMembersDefaultParams]) -> LiquipediaCategoryMembersResponse: ...
    @overload
    def enums(self, **params: Unpack[LiquipediaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[LiquipediaEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[LiquipediaEnumsDefaultParams]) -> LiquipediaEnumsResponse: ...
    @overload
    def links(self, **params: Unpack[LiquipediaLinksStreamParams]) -> BinaryIO: ...
    @overload
    def links(self, **params: Unpack[LiquipediaLinksTextResponseParams]) -> str: ...
    @overload
    def links(self, **params: Unpack[LiquipediaLinksDefaultParams]) -> LiquipediaLinksResponse: ...
    @overload
    def page(self, **params: Unpack[LiquipediaPageStreamParams]) -> BinaryIO: ...
    @overload
    def page(self, **params: Unpack[LiquipediaPageTextResponseParams]) -> str: ...
    @overload
    def page(self, **params: Unpack[LiquipediaPageDefaultParams]) -> LiquipediaPageResponse: ...
    @overload
    def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchStreamParams]) -> BinaryIO: ...
    @overload
    def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchTextResponseParams]) -> str: ...
    @overload
    def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchDefaultParams]) -> LiquipediaPrefixSearchResponse: ...
    @overload
    def recent_changes(self, **params: Unpack[LiquipediaRecentChangesStreamParams]) -> BinaryIO: ...
    @overload
    def recent_changes(self, **params: Unpack[LiquipediaRecentChangesTextResponseParams]) -> str: ...
    @overload
    def recent_changes(self, **params: Unpack[LiquipediaRecentChangesDefaultParams]) -> LiquipediaRecentChangesResponse: ...
    @overload
    def search(self, **params: Unpack[LiquipediaSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[LiquipediaSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[LiquipediaSearchDefaultParams]) -> LiquipediaSearchResponse: ...
    @overload
    def tags(self, **params: Unpack[LiquipediaTagsStreamParams]) -> BinaryIO: ...
    @overload
    def tags(self, **params: Unpack[LiquipediaTagsTextResponseParams]) -> str: ...
    @overload
    def tags(self, **params: Unpack[LiquipediaTagsDefaultParams]) -> LiquipediaTagsResponse: ...
    @overload
    def wikis(self, **params: Unpack[LiquipediaWikisStreamParams]) -> BinaryIO: ...
    @overload
    def wikis(self, **params: Unpack[LiquipediaWikisTextResponseParams]) -> str: ...
    @overload
    def wikis(self, **params: Unpack[LiquipediaWikisDefaultParams]) -> LiquipediaWikisResponse: ...

OperationId = Literal[
    'liquipedia-all-pages',
    'liquipedia-backlinks',
    'liquipedia-categories',
    'liquipedia-category-members',
    'liquipedia-enums',
    'liquipedia-links',
    'liquipedia-page',
    'liquipedia-prefix-search',
    'liquipedia-recent-changes',
    'liquipedia-search',
    'liquipedia-tags',
    'liquipedia-wikis',
]

class CrawloraClient:
    liquipedia: LiquipediaGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-all-pages'],
        params: LiquipediaAllPagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaAllPagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-backlinks'],
        params: LiquipediaBacklinksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaBacklinksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-categories'],
        params: LiquipediaCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-category-members'],
        params: LiquipediaCategoryMembersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaCategoryMembersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-enums'],
        params: LiquipediaEnumsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaEnumsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-links'],
        params: LiquipediaLinksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaLinksResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-page'],
        params: LiquipediaPageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaPageResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-prefix-search'],
        params: LiquipediaPrefixSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaPrefixSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-recent-changes'],
        params: LiquipediaRecentChangesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaRecentChangesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-search'],
        params: LiquipediaSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-tags'],
        params: LiquipediaTagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaTagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['liquipedia-wikis'],
        params: LiquipediaWikisParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaWikisResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-all-pages'],
        params: LiquipediaAllPagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaAllPagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-backlinks'],
        params: LiquipediaBacklinksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaBacklinksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-categories'],
        params: LiquipediaCategoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-category-members'],
        params: LiquipediaCategoryMembersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaCategoryMembersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-enums'],
        params: LiquipediaEnumsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaEnumsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-links'],
        params: LiquipediaLinksParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaLinksResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-page'],
        params: LiquipediaPageParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaPageResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-prefix-search'],
        params: LiquipediaPrefixSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaPrefixSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-recent-changes'],
        params: LiquipediaRecentChangesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaRecentChangesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-search'],
        params: LiquipediaSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-tags'],
        params: LiquipediaTagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaTagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['liquipedia-wikis'],
        params: LiquipediaWikisParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LiquipediaWikisResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class LiquipediaClient(CrawloraClient):
    def __enter__(self) -> LiquipediaClient: ...
    @overload
    def all_pages(self, **params: Unpack[LiquipediaAllPagesStreamParams]) -> BinaryIO: ...
    @overload
    def all_pages(self, **params: Unpack[LiquipediaAllPagesTextResponseParams]) -> str: ...
    @overload
    def all_pages(self, **params: Unpack[LiquipediaAllPagesDefaultParams]) -> LiquipediaAllPagesResponse: ...
    @overload
    def backlinks(self, **params: Unpack[LiquipediaBacklinksStreamParams]) -> BinaryIO: ...
    @overload
    def backlinks(self, **params: Unpack[LiquipediaBacklinksTextResponseParams]) -> str: ...
    @overload
    def backlinks(self, **params: Unpack[LiquipediaBacklinksDefaultParams]) -> LiquipediaBacklinksResponse: ...
    @overload
    def categories(self, **params: Unpack[LiquipediaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[LiquipediaCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[LiquipediaCategoriesDefaultParams]) -> LiquipediaCategoriesResponse: ...
    @overload
    def category_members(self, **params: Unpack[LiquipediaCategoryMembersStreamParams]) -> BinaryIO: ...
    @overload
    def category_members(self, **params: Unpack[LiquipediaCategoryMembersTextResponseParams]) -> str: ...
    @overload
    def category_members(self, **params: Unpack[LiquipediaCategoryMembersDefaultParams]) -> LiquipediaCategoryMembersResponse: ...
    @overload
    def enums(self, **params: Unpack[LiquipediaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    def enums(self, **params: Unpack[LiquipediaEnumsTextResponseParams]) -> str: ...
    @overload
    def enums(self, **params: Unpack[LiquipediaEnumsDefaultParams]) -> LiquipediaEnumsResponse: ...
    @overload
    def links(self, **params: Unpack[LiquipediaLinksStreamParams]) -> BinaryIO: ...
    @overload
    def links(self, **params: Unpack[LiquipediaLinksTextResponseParams]) -> str: ...
    @overload
    def links(self, **params: Unpack[LiquipediaLinksDefaultParams]) -> LiquipediaLinksResponse: ...
    @overload
    def page(self, **params: Unpack[LiquipediaPageStreamParams]) -> BinaryIO: ...
    @overload
    def page(self, **params: Unpack[LiquipediaPageTextResponseParams]) -> str: ...
    @overload
    def page(self, **params: Unpack[LiquipediaPageDefaultParams]) -> LiquipediaPageResponse: ...
    @overload
    def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchStreamParams]) -> BinaryIO: ...
    @overload
    def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchTextResponseParams]) -> str: ...
    @overload
    def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchDefaultParams]) -> LiquipediaPrefixSearchResponse: ...
    @overload
    def recent_changes(self, **params: Unpack[LiquipediaRecentChangesStreamParams]) -> BinaryIO: ...
    @overload
    def recent_changes(self, **params: Unpack[LiquipediaRecentChangesTextResponseParams]) -> str: ...
    @overload
    def recent_changes(self, **params: Unpack[LiquipediaRecentChangesDefaultParams]) -> LiquipediaRecentChangesResponse: ...
    @overload
    def search(self, **params: Unpack[LiquipediaSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[LiquipediaSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[LiquipediaSearchDefaultParams]) -> LiquipediaSearchResponse: ...
    @overload
    def tags(self, **params: Unpack[LiquipediaTagsStreamParams]) -> BinaryIO: ...
    @overload
    def tags(self, **params: Unpack[LiquipediaTagsTextResponseParams]) -> str: ...
    @overload
    def tags(self, **params: Unpack[LiquipediaTagsDefaultParams]) -> LiquipediaTagsResponse: ...
    @overload
    def wikis(self, **params: Unpack[LiquipediaWikisStreamParams]) -> BinaryIO: ...
    @overload
    def wikis(self, **params: Unpack[LiquipediaWikisTextResponseParams]) -> str: ...
    @overload
    def wikis(self, **params: Unpack[LiquipediaWikisDefaultParams]) -> LiquipediaWikisResponse: ...

class AsyncLiquipediaClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncLiquipediaClient: ...
    liquipedia: _AsyncLiquipediaGroup
    @overload
    async def all_pages(self, **params: Unpack[LiquipediaAllPagesStreamParams]) -> BinaryIO: ...
    @overload
    async def all_pages(self, **params: Unpack[LiquipediaAllPagesTextResponseParams]) -> str: ...
    @overload
    async def all_pages(self, **params: Unpack[LiquipediaAllPagesDefaultParams]) -> LiquipediaAllPagesResponse: ...
    @overload
    async def backlinks(self, **params: Unpack[LiquipediaBacklinksStreamParams]) -> BinaryIO: ...
    @overload
    async def backlinks(self, **params: Unpack[LiquipediaBacklinksTextResponseParams]) -> str: ...
    @overload
    async def backlinks(self, **params: Unpack[LiquipediaBacklinksDefaultParams]) -> LiquipediaBacklinksResponse: ...
    @overload
    async def categories(self, **params: Unpack[LiquipediaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[LiquipediaCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[LiquipediaCategoriesDefaultParams]) -> LiquipediaCategoriesResponse: ...
    @overload
    async def category_members(self, **params: Unpack[LiquipediaCategoryMembersStreamParams]) -> BinaryIO: ...
    @overload
    async def category_members(self, **params: Unpack[LiquipediaCategoryMembersTextResponseParams]) -> str: ...
    @overload
    async def category_members(self, **params: Unpack[LiquipediaCategoryMembersDefaultParams]) -> LiquipediaCategoryMembersResponse: ...
    @overload
    async def enums(self, **params: Unpack[LiquipediaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[LiquipediaEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[LiquipediaEnumsDefaultParams]) -> LiquipediaEnumsResponse: ...
    @overload
    async def links(self, **params: Unpack[LiquipediaLinksStreamParams]) -> BinaryIO: ...
    @overload
    async def links(self, **params: Unpack[LiquipediaLinksTextResponseParams]) -> str: ...
    @overload
    async def links(self, **params: Unpack[LiquipediaLinksDefaultParams]) -> LiquipediaLinksResponse: ...
    @overload
    async def page(self, **params: Unpack[LiquipediaPageStreamParams]) -> BinaryIO: ...
    @overload
    async def page(self, **params: Unpack[LiquipediaPageTextResponseParams]) -> str: ...
    @overload
    async def page(self, **params: Unpack[LiquipediaPageDefaultParams]) -> LiquipediaPageResponse: ...
    @overload
    async def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchTextResponseParams]) -> str: ...
    @overload
    async def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchDefaultParams]) -> LiquipediaPrefixSearchResponse: ...
    @overload
    async def recent_changes(self, **params: Unpack[LiquipediaRecentChangesStreamParams]) -> BinaryIO: ...
    @overload
    async def recent_changes(self, **params: Unpack[LiquipediaRecentChangesTextResponseParams]) -> str: ...
    @overload
    async def recent_changes(self, **params: Unpack[LiquipediaRecentChangesDefaultParams]) -> LiquipediaRecentChangesResponse: ...
    @overload
    async def search(self, **params: Unpack[LiquipediaSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[LiquipediaSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[LiquipediaSearchDefaultParams]) -> LiquipediaSearchResponse: ...
    @overload
    async def tags(self, **params: Unpack[LiquipediaTagsStreamParams]) -> BinaryIO: ...
    @overload
    async def tags(self, **params: Unpack[LiquipediaTagsTextResponseParams]) -> str: ...
    @overload
    async def tags(self, **params: Unpack[LiquipediaTagsDefaultParams]) -> LiquipediaTagsResponse: ...
    @overload
    async def wikis(self, **params: Unpack[LiquipediaWikisStreamParams]) -> BinaryIO: ...
    @overload
    async def wikis(self, **params: Unpack[LiquipediaWikisTextResponseParams]) -> str: ...
    @overload
    async def wikis(self, **params: Unpack[LiquipediaWikisDefaultParams]) -> LiquipediaWikisResponse: ...

class _AsyncLiquipediaGroup:
    @overload
    async def all_pages(self, **params: Unpack[LiquipediaAllPagesStreamParams]) -> BinaryIO: ...
    @overload
    async def all_pages(self, **params: Unpack[LiquipediaAllPagesTextResponseParams]) -> str: ...
    @overload
    async def all_pages(self, **params: Unpack[LiquipediaAllPagesDefaultParams]) -> LiquipediaAllPagesResponse: ...
    @overload
    async def backlinks(self, **params: Unpack[LiquipediaBacklinksStreamParams]) -> BinaryIO: ...
    @overload
    async def backlinks(self, **params: Unpack[LiquipediaBacklinksTextResponseParams]) -> str: ...
    @overload
    async def backlinks(self, **params: Unpack[LiquipediaBacklinksDefaultParams]) -> LiquipediaBacklinksResponse: ...
    @overload
    async def categories(self, **params: Unpack[LiquipediaCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[LiquipediaCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[LiquipediaCategoriesDefaultParams]) -> LiquipediaCategoriesResponse: ...
    @overload
    async def category_members(self, **params: Unpack[LiquipediaCategoryMembersStreamParams]) -> BinaryIO: ...
    @overload
    async def category_members(self, **params: Unpack[LiquipediaCategoryMembersTextResponseParams]) -> str: ...
    @overload
    async def category_members(self, **params: Unpack[LiquipediaCategoryMembersDefaultParams]) -> LiquipediaCategoryMembersResponse: ...
    @overload
    async def enums(self, **params: Unpack[LiquipediaEnumsStreamParams]) -> BinaryIO: ...
    @overload
    async def enums(self, **params: Unpack[LiquipediaEnumsTextResponseParams]) -> str: ...
    @overload
    async def enums(self, **params: Unpack[LiquipediaEnumsDefaultParams]) -> LiquipediaEnumsResponse: ...
    @overload
    async def links(self, **params: Unpack[LiquipediaLinksStreamParams]) -> BinaryIO: ...
    @overload
    async def links(self, **params: Unpack[LiquipediaLinksTextResponseParams]) -> str: ...
    @overload
    async def links(self, **params: Unpack[LiquipediaLinksDefaultParams]) -> LiquipediaLinksResponse: ...
    @overload
    async def page(self, **params: Unpack[LiquipediaPageStreamParams]) -> BinaryIO: ...
    @overload
    async def page(self, **params: Unpack[LiquipediaPageTextResponseParams]) -> str: ...
    @overload
    async def page(self, **params: Unpack[LiquipediaPageDefaultParams]) -> LiquipediaPageResponse: ...
    @overload
    async def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchTextResponseParams]) -> str: ...
    @overload
    async def prefix_search(self, **params: Unpack[LiquipediaPrefixSearchDefaultParams]) -> LiquipediaPrefixSearchResponse: ...
    @overload
    async def recent_changes(self, **params: Unpack[LiquipediaRecentChangesStreamParams]) -> BinaryIO: ...
    @overload
    async def recent_changes(self, **params: Unpack[LiquipediaRecentChangesTextResponseParams]) -> str: ...
    @overload
    async def recent_changes(self, **params: Unpack[LiquipediaRecentChangesDefaultParams]) -> LiquipediaRecentChangesResponse: ...
    @overload
    async def search(self, **params: Unpack[LiquipediaSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[LiquipediaSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[LiquipediaSearchDefaultParams]) -> LiquipediaSearchResponse: ...
    @overload
    async def tags(self, **params: Unpack[LiquipediaTagsStreamParams]) -> BinaryIO: ...
    @overload
    async def tags(self, **params: Unpack[LiquipediaTagsTextResponseParams]) -> str: ...
    @overload
    async def tags(self, **params: Unpack[LiquipediaTagsDefaultParams]) -> LiquipediaTagsResponse: ...
    @overload
    async def wikis(self, **params: Unpack[LiquipediaWikisStreamParams]) -> BinaryIO: ...
    @overload
    async def wikis(self, **params: Unpack[LiquipediaWikisTextResponseParams]) -> str: ...
    @overload
    async def wikis(self, **params: Unpack[LiquipediaWikisDefaultParams]) -> LiquipediaWikisResponse: ...

LiquipediaAllPagesDefaultParams = TypedDict('LiquipediaAllPagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'apfrom': NotRequired[str],
    'apto': NotRequired[str],
    'apprefix': NotRequired[str],
    'apnamespace': NotRequired[int],
    'apfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'apfilterlanglinks': NotRequired[Literal['all', 'withlanglinks', 'withoutlanglinks']],
    'apminsize': NotRequired[int],
    'apmaxsize': NotRequired[int],
    'apprtype': NotRequired[list[Literal['edit', 'move', 'upload']]],
    'apprlevel': NotRequired[Literal['autoconfirmed', 'sysop']],
    'apprfiltercascade': NotRequired[Literal['all', 'cascading', 'noncascading']],
    'apprexpiry': NotRequired[Literal['all', 'definite', 'indefinite']],
    'aplimit': NotRequired[str],
    'apdir': NotRequired[Literal['ascending', 'descending']],
    'apcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaAllPagesTextResponseParams = TypedDict('LiquipediaAllPagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'apfrom': NotRequired[str],
    'apto': NotRequired[str],
    'apprefix': NotRequired[str],
    'apnamespace': NotRequired[int],
    'apfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'apfilterlanglinks': NotRequired[Literal['all', 'withlanglinks', 'withoutlanglinks']],
    'apminsize': NotRequired[int],
    'apmaxsize': NotRequired[int],
    'apprtype': NotRequired[list[Literal['edit', 'move', 'upload']]],
    'apprlevel': NotRequired[Literal['autoconfirmed', 'sysop']],
    'apprfiltercascade': NotRequired[Literal['all', 'cascading', 'noncascading']],
    'apprexpiry': NotRequired[Literal['all', 'definite', 'indefinite']],
    'aplimit': NotRequired[str],
    'apdir': NotRequired[Literal['ascending', 'descending']],
    'apcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaAllPagesStreamParams = TypedDict('LiquipediaAllPagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'apfrom': NotRequired[str],
    'apto': NotRequired[str],
    'apprefix': NotRequired[str],
    'apnamespace': NotRequired[int],
    'apfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'apfilterlanglinks': NotRequired[Literal['all', 'withlanglinks', 'withoutlanglinks']],
    'apminsize': NotRequired[int],
    'apmaxsize': NotRequired[int],
    'apprtype': NotRequired[list[Literal['edit', 'move', 'upload']]],
    'apprlevel': NotRequired[Literal['autoconfirmed', 'sysop']],
    'apprfiltercascade': NotRequired[Literal['all', 'cascading', 'noncascading']],
    'apprexpiry': NotRequired[Literal['all', 'definite', 'indefinite']],
    'aplimit': NotRequired[str],
    'apdir': NotRequired[Literal['ascending', 'descending']],
    'apcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaBacklinksDefaultParams = TypedDict('LiquipediaBacklinksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'bltitle': NotRequired[str],
    'blpageid': NotRequired[int],
    'blnamespace': NotRequired[list[str]],
    'bldir': NotRequired[Literal['ascending', 'descending']],
    'blfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'bllimit': NotRequired[str],
    'blredirect': NotRequired[bool],
    'blcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaBacklinksTextResponseParams = TypedDict('LiquipediaBacklinksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'bltitle': NotRequired[str],
    'blpageid': NotRequired[int],
    'blnamespace': NotRequired[list[str]],
    'bldir': NotRequired[Literal['ascending', 'descending']],
    'blfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'bllimit': NotRequired[str],
    'blredirect': NotRequired[bool],
    'blcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaBacklinksStreamParams = TypedDict('LiquipediaBacklinksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'bltitle': NotRequired[str],
    'blpageid': NotRequired[int],
    'blnamespace': NotRequired[list[str]],
    'bldir': NotRequired[Literal['ascending', 'descending']],
    'blfilterredir': NotRequired[Literal['all', 'nonredirects', 'redirects']],
    'bllimit': NotRequired[str],
    'blredirect': NotRequired[bool],
    'blcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaCategoriesDefaultParams = TypedDict('LiquipediaCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'acfrom': NotRequired[str],
    'acto': NotRequired[str],
    'acprefix': NotRequired[str],
    'acdir': NotRequired[Literal['ascending', 'descending']],
    'acmin': NotRequired[int],
    'acmax': NotRequired[int],
    'aclimit': NotRequired[str],
    'acprop': NotRequired[list[Literal['size', 'hidden']]],
    'accontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaCategoriesTextResponseParams = TypedDict('LiquipediaCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'acfrom': NotRequired[str],
    'acto': NotRequired[str],
    'acprefix': NotRequired[str],
    'acdir': NotRequired[Literal['ascending', 'descending']],
    'acmin': NotRequired[int],
    'acmax': NotRequired[int],
    'aclimit': NotRequired[str],
    'acprop': NotRequired[list[Literal['size', 'hidden']]],
    'accontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaCategoriesStreamParams = TypedDict('LiquipediaCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'acfrom': NotRequired[str],
    'acto': NotRequired[str],
    'acprefix': NotRequired[str],
    'acdir': NotRequired[Literal['ascending', 'descending']],
    'acmin': NotRequired[int],
    'acmax': NotRequired[int],
    'aclimit': NotRequired[str],
    'acprop': NotRequired[list[Literal['size', 'hidden']]],
    'accontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaCategoryMembersDefaultParams = TypedDict('LiquipediaCategoryMembersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'cmtitle': NotRequired[str],
    'cmpageid': NotRequired[int],
    'cmnamespace': NotRequired[list[str]],
    'cmtype': NotRequired[list[Literal['file', 'page', 'subcat']]],
    'cmprop': NotRequired[list[Literal['ids', 'title', 'sortkey', 'sortkeyprefix', 'type', 'timestamp']]],
    'cmlimit': NotRequired[str],
    'continue': NotRequired[str],
    'cmcontinue': NotRequired[str],
    'cmsort': NotRequired[Literal['sortkey', 'timestamp']],
    'cmdir': NotRequired[Literal['asc', 'ascending', 'desc', 'descending', 'newer', 'older']],
    'cmstart': NotRequired[str],
    'cmend': NotRequired[str],
    'cmstarthexsortkey': NotRequired[str],
    'cmendhexsortkey': NotRequired[str],
    'cmstartsortkeyprefix': NotRequired[str],
    'cmendsortkeyprefix': NotRequired[str],
}, total=False)

LiquipediaCategoryMembersTextResponseParams = TypedDict('LiquipediaCategoryMembersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'cmtitle': NotRequired[str],
    'cmpageid': NotRequired[int],
    'cmnamespace': NotRequired[list[str]],
    'cmtype': NotRequired[list[Literal['file', 'page', 'subcat']]],
    'cmprop': NotRequired[list[Literal['ids', 'title', 'sortkey', 'sortkeyprefix', 'type', 'timestamp']]],
    'cmlimit': NotRequired[str],
    'continue': NotRequired[str],
    'cmcontinue': NotRequired[str],
    'cmsort': NotRequired[Literal['sortkey', 'timestamp']],
    'cmdir': NotRequired[Literal['asc', 'ascending', 'desc', 'descending', 'newer', 'older']],
    'cmstart': NotRequired[str],
    'cmend': NotRequired[str],
    'cmstarthexsortkey': NotRequired[str],
    'cmendhexsortkey': NotRequired[str],
    'cmstartsortkeyprefix': NotRequired[str],
    'cmendsortkeyprefix': NotRequired[str],
}, total=False)

LiquipediaCategoryMembersStreamParams = TypedDict('LiquipediaCategoryMembersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'cmtitle': NotRequired[str],
    'cmpageid': NotRequired[int],
    'cmnamespace': NotRequired[list[str]],
    'cmtype': NotRequired[list[Literal['file', 'page', 'subcat']]],
    'cmprop': NotRequired[list[Literal['ids', 'title', 'sortkey', 'sortkeyprefix', 'type', 'timestamp']]],
    'cmlimit': NotRequired[str],
    'continue': NotRequired[str],
    'cmcontinue': NotRequired[str],
    'cmsort': NotRequired[Literal['sortkey', 'timestamp']],
    'cmdir': NotRequired[Literal['asc', 'ascending', 'desc', 'descending', 'newer', 'older']],
    'cmstart': NotRequired[str],
    'cmend': NotRequired[str],
    'cmstarthexsortkey': NotRequired[str],
    'cmendhexsortkey': NotRequired[str],
    'cmstartsortkeyprefix': NotRequired[str],
    'cmendsortkeyprefix': NotRequired[str],
}, total=False)

LiquipediaEnumsDefaultParams = TypedDict('LiquipediaEnumsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
}, total=False)

LiquipediaEnumsTextResponseParams = TypedDict('LiquipediaEnumsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
}, total=False)

LiquipediaEnumsStreamParams = TypedDict('LiquipediaEnumsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
}, total=False)

LiquipediaLinksDefaultParams = TypedDict('LiquipediaLinksDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'titles': NotRequired[list[str]],
    'pageids': NotRequired[list[int]],
    'revids': NotRequired[list[int]],
    'plnamespace': NotRequired[list[str]],
    'pllimit': NotRequired[str],
    'plcontinue': NotRequired[str],
    'pltitles': NotRequired[list[str]],
    'pldir': NotRequired[Literal['ascending', 'descending']],
    'redirects': NotRequired[bool],
    'continue': NotRequired[str],
}, total=False)

LiquipediaLinksTextResponseParams = TypedDict('LiquipediaLinksTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'titles': NotRequired[list[str]],
    'pageids': NotRequired[list[int]],
    'revids': NotRequired[list[int]],
    'plnamespace': NotRequired[list[str]],
    'pllimit': NotRequired[str],
    'plcontinue': NotRequired[str],
    'pltitles': NotRequired[list[str]],
    'pldir': NotRequired[Literal['ascending', 'descending']],
    'redirects': NotRequired[bool],
    'continue': NotRequired[str],
}, total=False)

LiquipediaLinksStreamParams = TypedDict('LiquipediaLinksStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'titles': NotRequired[list[str]],
    'pageids': NotRequired[list[int]],
    'revids': NotRequired[list[int]],
    'plnamespace': NotRequired[list[str]],
    'pllimit': NotRequired[str],
    'plcontinue': NotRequired[str],
    'pltitles': NotRequired[list[str]],
    'pldir': NotRequired[Literal['ascending', 'descending']],
    'redirects': NotRequired[bool],
    'continue': NotRequired[str],
}, total=False)

LiquipediaPageDefaultParams = TypedDict('LiquipediaPageDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'page': NotRequired[str],
    'pageid': NotRequired[int],
    'oldid': NotRequired[int],
    'section': NotRequired[str],
    'redirects': NotRequired[bool],
}, total=False)

LiquipediaPageTextResponseParams = TypedDict('LiquipediaPageTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'page': NotRequired[str],
    'pageid': NotRequired[int],
    'oldid': NotRequired[int],
    'section': NotRequired[str],
    'redirects': NotRequired[bool],
}, total=False)

LiquipediaPageStreamParams = TypedDict('LiquipediaPageStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'page': NotRequired[str],
    'pageid': NotRequired[int],
    'oldid': NotRequired[int],
    'section': NotRequired[str],
    'redirects': NotRequired[bool],
}, total=False)

LiquipediaPrefixSearchDefaultParams = TypedDict('LiquipediaPrefixSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'pssearch': Required[str],
    'psnamespace': NotRequired[list[str]],
    'pslimit': NotRequired[str],
    'psoffset': NotRequired[int],
    'psprofile': NotRequired[Literal['classic', 'engine_autoselect', 'fast-fuzzy', 'fuzzy', 'fuzzy-subphrases', 'normal', 'normal-subphrases', 'strict']],
    'continue': NotRequired[str],
}, total=False)

LiquipediaPrefixSearchTextResponseParams = TypedDict('LiquipediaPrefixSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'pssearch': Required[str],
    'psnamespace': NotRequired[list[str]],
    'pslimit': NotRequired[str],
    'psoffset': NotRequired[int],
    'psprofile': NotRequired[Literal['classic', 'engine_autoselect', 'fast-fuzzy', 'fuzzy', 'fuzzy-subphrases', 'normal', 'normal-subphrases', 'strict']],
    'continue': NotRequired[str],
}, total=False)

LiquipediaPrefixSearchStreamParams = TypedDict('LiquipediaPrefixSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'pssearch': Required[str],
    'psnamespace': NotRequired[list[str]],
    'pslimit': NotRequired[str],
    'psoffset': NotRequired[int],
    'psprofile': NotRequired[Literal['classic', 'engine_autoselect', 'fast-fuzzy', 'fuzzy', 'fuzzy-subphrases', 'normal', 'normal-subphrases', 'strict']],
    'continue': NotRequired[str],
}, total=False)

LiquipediaRecentChangesDefaultParams = TypedDict('LiquipediaRecentChangesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'rcstart': NotRequired[str],
    'rcend': NotRequired[str],
    'rcdir': NotRequired[Literal['newer', 'older']],
    'rcnamespace': NotRequired[list[str]],
    'rctag': NotRequired[str],
    'rcprop': NotRequired[list[Literal['comment', 'flags', 'ids', 'loginfo', 'parsedcomment', 'redirect', 'sha1', 'sizes', 'tags', 'timestamp', 'title', 'user', 'userid']]],
    'rcshow': NotRequired[list[Literal['!anon', '!autopatrolled', '!bot', '!minor', '!patrolled', '!redirect', 'anon', 'autopatrolled', 'bot', 'minor', 'patrolled', 'redirect', 'unpatrolled']]],
    'rclimit': NotRequired[str],
    'rctype': NotRequired[list[Literal['categorize', 'edit', 'external', 'log', 'new']]],
    'rctoponly': NotRequired[bool],
    'rctitle': NotRequired[str],
    'rccontinue': NotRequired[str],
    'continue': NotRequired[str],
    'rcslot': NotRequired[Literal['main']],
}, total=False)

LiquipediaRecentChangesTextResponseParams = TypedDict('LiquipediaRecentChangesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'rcstart': NotRequired[str],
    'rcend': NotRequired[str],
    'rcdir': NotRequired[Literal['newer', 'older']],
    'rcnamespace': NotRequired[list[str]],
    'rctag': NotRequired[str],
    'rcprop': NotRequired[list[Literal['comment', 'flags', 'ids', 'loginfo', 'parsedcomment', 'redirect', 'sha1', 'sizes', 'tags', 'timestamp', 'title', 'user', 'userid']]],
    'rcshow': NotRequired[list[Literal['!anon', '!autopatrolled', '!bot', '!minor', '!patrolled', '!redirect', 'anon', 'autopatrolled', 'bot', 'minor', 'patrolled', 'redirect', 'unpatrolled']]],
    'rclimit': NotRequired[str],
    'rctype': NotRequired[list[Literal['categorize', 'edit', 'external', 'log', 'new']]],
    'rctoponly': NotRequired[bool],
    'rctitle': NotRequired[str],
    'rccontinue': NotRequired[str],
    'continue': NotRequired[str],
    'rcslot': NotRequired[Literal['main']],
}, total=False)

LiquipediaRecentChangesStreamParams = TypedDict('LiquipediaRecentChangesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'rcstart': NotRequired[str],
    'rcend': NotRequired[str],
    'rcdir': NotRequired[Literal['newer', 'older']],
    'rcnamespace': NotRequired[list[str]],
    'rctag': NotRequired[str],
    'rcprop': NotRequired[list[Literal['comment', 'flags', 'ids', 'loginfo', 'parsedcomment', 'redirect', 'sha1', 'sizes', 'tags', 'timestamp', 'title', 'user', 'userid']]],
    'rcshow': NotRequired[list[Literal['!anon', '!autopatrolled', '!bot', '!minor', '!patrolled', '!redirect', 'anon', 'autopatrolled', 'bot', 'minor', 'patrolled', 'redirect', 'unpatrolled']]],
    'rclimit': NotRequired[str],
    'rctype': NotRequired[list[Literal['categorize', 'edit', 'external', 'log', 'new']]],
    'rctoponly': NotRequired[bool],
    'rctitle': NotRequired[str],
    'rccontinue': NotRequired[str],
    'continue': NotRequired[str],
    'rcslot': NotRequired[Literal['main']],
}, total=False)

LiquipediaSearchDefaultParams = TypedDict('LiquipediaSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'q': Required[str],
    'srnamespace': NotRequired[list[str]],
    'srwhat': NotRequired[Literal['nearmatch', 'text', 'title']],
    'srlimit': NotRequired[str],
    'sroffset': NotRequired[int],
    'continue': NotRequired[str],
    'srsort': NotRequired[Literal['create_timestamp_asc', 'create_timestamp_desc', 'incoming_links_asc', 'incoming_links_desc', 'just_match', 'last_edit_asc', 'last_edit_desc', 'none', 'random', 'relevance', 'title_natural_asc', 'title_natural_desc', 'user_random']],
    'srinfo': NotRequired[list[Literal['rewrittenquery', 'suggestion', 'totalhits']]],
    'srprop': NotRequired[list[Literal['size', 'wordcount', 'timestamp', 'snippet', 'titlesnippet', 'redirecttitle', 'redirectsnippet', 'sectiontitle', 'sectionsnippet', 'isfilematch', 'categorysnippet', 'extensiondata']]],
    'srinterwiki': NotRequired[bool],
    'srenablerewrites': NotRequired[bool],
    'srqiprofile': NotRequired[Literal['classic', 'classic_noboostlinks', 'empty', 'wsum_inclinks', 'wsum_inclinks_pv', 'popular_inclinks_pv', 'popular_inclinks', 'engine_autoselect']],
    'srqdprofile': NotRequired[Literal['default', 'perfield_builder', 'perfield_builder_relaxed', 'perfield_builder_title_filter', 'engine_autoselect']],
}, total=False)

LiquipediaSearchTextResponseParams = TypedDict('LiquipediaSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'q': Required[str],
    'srnamespace': NotRequired[list[str]],
    'srwhat': NotRequired[Literal['nearmatch', 'text', 'title']],
    'srlimit': NotRequired[str],
    'sroffset': NotRequired[int],
    'continue': NotRequired[str],
    'srsort': NotRequired[Literal['create_timestamp_asc', 'create_timestamp_desc', 'incoming_links_asc', 'incoming_links_desc', 'just_match', 'last_edit_asc', 'last_edit_desc', 'none', 'random', 'relevance', 'title_natural_asc', 'title_natural_desc', 'user_random']],
    'srinfo': NotRequired[list[Literal['rewrittenquery', 'suggestion', 'totalhits']]],
    'srprop': NotRequired[list[Literal['size', 'wordcount', 'timestamp', 'snippet', 'titlesnippet', 'redirecttitle', 'redirectsnippet', 'sectiontitle', 'sectionsnippet', 'isfilematch', 'categorysnippet', 'extensiondata']]],
    'srinterwiki': NotRequired[bool],
    'srenablerewrites': NotRequired[bool],
    'srqiprofile': NotRequired[Literal['classic', 'classic_noboostlinks', 'empty', 'wsum_inclinks', 'wsum_inclinks_pv', 'popular_inclinks_pv', 'popular_inclinks', 'engine_autoselect']],
    'srqdprofile': NotRequired[Literal['default', 'perfield_builder', 'perfield_builder_relaxed', 'perfield_builder_title_filter', 'engine_autoselect']],
}, total=False)

LiquipediaSearchStreamParams = TypedDict('LiquipediaSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'q': Required[str],
    'srnamespace': NotRequired[list[str]],
    'srwhat': NotRequired[Literal['nearmatch', 'text', 'title']],
    'srlimit': NotRequired[str],
    'sroffset': NotRequired[int],
    'continue': NotRequired[str],
    'srsort': NotRequired[Literal['create_timestamp_asc', 'create_timestamp_desc', 'incoming_links_asc', 'incoming_links_desc', 'just_match', 'last_edit_asc', 'last_edit_desc', 'none', 'random', 'relevance', 'title_natural_asc', 'title_natural_desc', 'user_random']],
    'srinfo': NotRequired[list[Literal['rewrittenquery', 'suggestion', 'totalhits']]],
    'srprop': NotRequired[list[Literal['size', 'wordcount', 'timestamp', 'snippet', 'titlesnippet', 'redirecttitle', 'redirectsnippet', 'sectiontitle', 'sectionsnippet', 'isfilematch', 'categorysnippet', 'extensiondata']]],
    'srinterwiki': NotRequired[bool],
    'srenablerewrites': NotRequired[bool],
    'srqiprofile': NotRequired[Literal['classic', 'classic_noboostlinks', 'empty', 'wsum_inclinks', 'wsum_inclinks_pv', 'popular_inclinks_pv', 'popular_inclinks', 'engine_autoselect']],
    'srqdprofile': NotRequired[Literal['default', 'perfield_builder', 'perfield_builder_relaxed', 'perfield_builder_title_filter', 'engine_autoselect']],
}, total=False)

LiquipediaTagsDefaultParams = TypedDict('LiquipediaTagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'wiki': Required[str],
    'tgprop': NotRequired[list[Literal['active', 'defined', 'description', 'displayname', 'hitcount', 'source']]],
    'tglimit': NotRequired[str],
    'tgcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaTagsTextResponseParams = TypedDict('LiquipediaTagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'wiki': Required[str],
    'tgprop': NotRequired[list[Literal['active', 'defined', 'description', 'displayname', 'hitcount', 'source']]],
    'tglimit': NotRequired[str],
    'tgcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaTagsStreamParams = TypedDict('LiquipediaTagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'wiki': Required[str],
    'tgprop': NotRequired[list[Literal['active', 'defined', 'description', 'displayname', 'hitcount', 'source']]],
    'tglimit': NotRequired[str],
    'tgcontinue': NotRequired[str],
    'continue': NotRequired[str],
}, total=False)

LiquipediaWikisDefaultParams = TypedDict('LiquipediaWikisDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

LiquipediaWikisTextResponseParams = TypedDict('LiquipediaWikisTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

LiquipediaWikisStreamParams = TypedDict('LiquipediaWikisStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)
