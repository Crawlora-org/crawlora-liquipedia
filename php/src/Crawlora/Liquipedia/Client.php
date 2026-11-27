<?php

declare(strict_types=1);

namespace Crawlora\Liquipedia;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'liquipedia';
    public const VERSION = '0.3.0';
    public const OPERATION_COUNT = 14;
    public const OPERATION_IDS = ["liquipedia-all-pages", "liquipedia-backlinks", "liquipedia-categories", "liquipedia-category-members", "liquipedia-embeddedin", "liquipedia-enums", "liquipedia-links", "liquipedia-page", "liquipedia-prefix-search", "liquipedia-recent-changes", "liquipedia-search", "liquipedia-tags", "liquipedia-wikis", "liquipedia-wikitext"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"liquipedia-all-pages": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-all-pages", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Source page title to start enumeration from", "in": "query", "name": "apfrom", "type": "string"}, {"description": "Source page title to stop enumeration at", "in": "query", "name": "apto", "type": "string"}, {"description": "Source page-title prefix", "in": "query", "name": "apprefix", "type": "string"}, {"description": "Source namespace ID; discover IDs with liquipedia_enums", "in": "query", "name": "apnamespace", "type": "integer"}, {"description": "Redirect filter", "enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "apfilterredir", "type": "string"}, {"description": "Language-link filter", "enum": ["all", "withlanglinks", "withoutlanglinks"], "in": "query", "name": "apfilterlanglinks", "type": "string"}, {"description": "Minimum page size in bytes", "in": "query", "name": "apminsize", "type": "integer"}, {"description": "Maximum page size in bytes; MediaWiki may disable this under miser mode", "in": "query", "name": "apmaxsize", "type": "integer"}, {"collectionFormat": "csv", "description": "Repeatable page-protection type", "in": "query", "items": {"enum": ["edit", "move", "upload"], "type": "string"}, "name": "apprtype", "type": "array"}, {"description": "Protection level; requires apprtype", "enum": ["autoconfirmed", "sysop"], "in": "query", "name": "apprlevel", "type": "string"}, {"description": "Cascading-protection filter", "enum": ["all", "cascading", "noncascading"], "in": "query", "name": "apprfiltercascade", "type": "string"}, {"description": "Protection-expiry filter", "enum": ["all", "definite", "indefinite"], "in": "query", "name": "apprexpiry", "type": "string"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "aplimit", "type": "string"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "apdir", "type": "string"}, {"description": "Native all-pages continuation token", "in": "query", "name": "apcontinue", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/all-pages", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "apfrom", "type": "string"}, {"in": "query", "name": "apto", "type": "string"}, {"in": "query", "name": "apprefix", "type": "string"}, {"in": "query", "name": "apnamespace", "type": "integer"}, {"enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "apfilterredir", "type": "string"}, {"enum": ["all", "withlanglinks", "withoutlanglinks"], "in": "query", "name": "apfilterlanglinks", "type": "string"}, {"in": "query", "name": "apminsize", "type": "integer"}, {"in": "query", "name": "apmaxsize", "type": "integer"}, {"collectionFormat": "csv", "enum": ["edit", "move", "upload"], "in": "query", "name": "apprtype", "type": "array"}, {"enum": ["autoconfirmed", "sysop"], "in": "query", "name": "apprlevel", "type": "string"}, {"enum": ["all", "cascading", "noncascading"], "in": "query", "name": "apprfiltercascade", "type": "string"}, {"enum": ["all", "definite", "indefinite"], "in": "query", "name": "apprexpiry", "type": "string"}, {"in": "query", "name": "aplimit", "type": "string"}, {"enum": ["ascending", "descending"], "in": "query", "name": "apdir", "type": "string"}, {"in": "query", "name": "apcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-backlinks": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-backlinks", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Target page title; mutually exclusive with blpageid", "in": "query", "name": "bltitle", "type": "string"}, {"description": "Target page ID; mutually exclusive with bltitle", "in": "query", "name": "blpageid", "type": "integer"}, {"collectionFormat": "multi", "description": "Repeatable referring-page namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "blnamespace", "type": "array"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "bldir", "type": "string"}, {"description": "Source redirect filter", "enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "blfilterredir", "type": "string"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "bllimit", "type": "string"}, {"description": "Include backlinks to redirects of the target page", "in": "query", "name": "blredirect", "type": "boolean"}, {"description": "Native backlinks continuation value", "in": "query", "name": "blcontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/backlinks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "bltitle", "type": "string"}, {"in": "query", "name": "blpageid", "type": "integer"}, {"collectionFormat": "multi", "in": "query", "name": "blnamespace", "type": "array"}, {"enum": ["ascending", "descending"], "in": "query", "name": "bldir", "type": "string"}, {"enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "blfilterredir", "type": "string"}, {"in": "query", "name": "bllimit", "type": "string"}, {"in": "query", "name": "blredirect", "type": "boolean"}, {"in": "query", "name": "blcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-categories": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-categories", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "First category title to enumerate from", "in": "query", "name": "acfrom", "type": "string"}, {"description": "Last category title to enumerate to", "in": "query", "name": "acto", "type": "string"}, {"description": "Category title prefix", "in": "query", "name": "acprefix", "type": "string"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "acdir", "type": "string"}, {"description": "Minimum category member count", "in": "query", "name": "acmin", "type": "integer"}, {"description": "Maximum category member count", "in": "query", "name": "acmax", "type": "integer"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "aclimit", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable category metadata property", "in": "query", "items": {"enum": ["size", "hidden"], "type": "string"}, "name": "acprop", "type": "array"}, {"description": "Native allcategories continuation token", "in": "query", "name": "accontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "acfrom", "type": "string"}, {"in": "query", "name": "acto", "type": "string"}, {"in": "query", "name": "acprefix", "type": "string"}, {"enum": ["ascending", "descending"], "in": "query", "name": "acdir", "type": "string"}, {"in": "query", "name": "acmin", "type": "integer"}, {"in": "query", "name": "acmax", "type": "integer"}, {"in": "query", "name": "aclimit", "type": "string"}, {"collectionFormat": "csv", "enum": ["size", "hidden"], "in": "query", "name": "acprop", "type": "array"}, {"in": "query", "name": "accontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-category-members": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-category-members", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Category title including Category:; mutually exclusive with cmpageid", "in": "query", "name": "cmtitle", "type": "string"}, {"description": "Category page ID; mutually exclusive with cmtitle", "in": "query", "name": "cmpageid", "type": "integer"}, {"collectionFormat": "multi", "description": "Repeatable source namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "cmnamespace", "type": "array"}, {"collectionFormat": "csv", "description": "Repeatable member type filter", "in": "query", "items": {"enum": ["file", "page", "subcat"], "type": "string"}, "name": "cmtype", "type": "array"}, {"collectionFormat": "csv", "description": "Repeatable returned metadata field", "in": "query", "items": {"enum": ["ids", "title", "sortkey", "sortkeyprefix", "type", "timestamp"], "type": "string"}, "name": "cmprop", "type": "array"}, {"description": "Page size, 1 through 500, or max (source default 10)", "in": "query", "name": "cmlimit", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}, {"description": "Category-members continuation value", "in": "query", "name": "cmcontinue", "type": "string"}, {"description": "Category sort key", "enum": ["sortkey", "timestamp"], "in": "query", "name": "cmsort", "type": "string"}, {"description": "Category sort direction", "enum": ["asc", "ascending", "desc", "descending", "newer", "older"], "in": "query", "name": "cmdir", "type": "string"}, {"description": "Timestamp start bound for cmsort=timestamp", "in": "query", "name": "cmstart", "type": "string"}, {"description": "Timestamp end bound for cmsort=timestamp", "in": "query", "name": "cmend", "type": "string"}, {"description": "Hex sort-key start bound for cmsort=sortkey", "in": "query", "name": "cmstarthexsortkey", "type": "string"}, {"description": "Hex sort-key end bound for cmsort=sortkey", "in": "query", "name": "cmendhexsortkey", "type": "string"}, {"description": "Sort-key prefix start bound for cmsort=sortkey", "in": "query", "name": "cmstartsortkeyprefix", "type": "string"}, {"description": "Sort-key prefix end bound for cmsort=sortkey", "in": "query", "name": "cmendsortkeyprefix", "type": "string"}], "path": "/liquipedia/category-members", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "cmtitle", "type": "string"}, {"in": "query", "name": "cmpageid", "type": "integer"}, {"collectionFormat": "multi", "in": "query", "name": "cmnamespace", "type": "array"}, {"collectionFormat": "csv", "enum": ["file", "page", "subcat"], "in": "query", "name": "cmtype", "type": "array"}, {"collectionFormat": "csv", "enum": ["ids", "title", "sortkey", "sortkeyprefix", "type", "timestamp"], "in": "query", "name": "cmprop", "type": "array"}, {"in": "query", "name": "cmlimit", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}, {"in": "query", "name": "cmcontinue", "type": "string"}, {"enum": ["sortkey", "timestamp"], "in": "query", "name": "cmsort", "type": "string"}, {"enum": ["asc", "ascending", "desc", "descending", "newer", "older"], "in": "query", "name": "cmdir", "type": "string"}, {"in": "query", "name": "cmstart", "type": "string"}, {"in": "query", "name": "cmend", "type": "string"}, {"in": "query", "name": "cmstarthexsortkey", "type": "string"}, {"in": "query", "name": "cmendhexsortkey", "type": "string"}, {"in": "query", "name": "cmstartsortkeyprefix", "type": "string"}, {"in": "query", "name": "cmendsortkeyprefix", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-embeddedin": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-embeddedin", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Transcluded page title such as Template:Infobox league; mutually exclusive with eipageid", "in": "query", "name": "eititle", "type": "string"}, {"description": "Transcluded page ID; mutually exclusive with eititle", "in": "query", "name": "eipageid", "type": "integer"}, {"collectionFormat": "multi", "description": "Repeatable transcluding-page namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "einamespace", "type": "array"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "eidir", "type": "string"}, {"description": "Source redirect filter", "enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "eifilterredir", "type": "string"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "eilimit", "type": "string"}, {"description": "Native embeddedin continuation value", "in": "query", "name": "eicontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/embeddedin", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "eititle", "type": "string"}, {"in": "query", "name": "eipageid", "type": "integer"}, {"collectionFormat": "multi", "in": "query", "name": "einamespace", "type": "array"}, {"enum": ["ascending", "descending"], "in": "query", "name": "eidir", "type": "string"}, {"enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "eifilterredir", "type": "string"}, {"in": "query", "name": "eilimit", "type": "string"}, {"in": "query", "name": "eicontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-enums": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-enums", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}], "path": "/liquipedia/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-links": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-links", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "description": "Source page title; mutually exclusive with pageids and revids", "in": "query", "items": {"type": "string"}, "name": "titles", "type": "array"}, {"collectionFormat": "multi", "description": "Source page ID; mutually exclusive with titles and revids", "in": "query", "items": {"type": "integer"}, "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "description": "Source revision ID; mutually exclusive with titles and pageids", "in": "query", "items": {"type": "integer"}, "name": "revids", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable linked-page namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "plnamespace", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "pllimit", "type": "string"}, {"description": "Native links continuation value", "in": "query", "name": "plcontinue", "type": "string"}, {"collectionFormat": "multi", "description": "Optional source title filter, up to 50 titles", "in": "query", "items": {"type": "string"}, "name": "pltitles", "type": "array"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "pldir", "type": "string"}, {"description": "Resolve source-page redirects", "in": "query", "name": "redirects", "type": "boolean"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/links", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "titles", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "revids", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "plnamespace", "type": "array"}, {"in": "query", "name": "pllimit", "type": "string"}, {"in": "query", "name": "plcontinue", "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "pltitles", "type": "array"}, {"enum": ["ascending", "descending"], "in": "query", "name": "pldir", "type": "string"}, {"in": "query", "name": "redirects", "type": "boolean"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-page": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-page", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Source page title; mutually exclusive with pageid and oldid", "in": "query", "name": "page", "type": "string"}, {"description": "Source page ID; mutually exclusive with page and oldid", "in": "query", "name": "pageid", "type": "integer"}, {"description": "Source revision ID; mutually exclusive with page and pageid", "format": "int64", "in": "query", "name": "oldid", "type": "integer"}, {"description": "Source section number or anchor ID", "in": "query", "name": "section", "type": "string"}, {"description": "Resolve page redirects", "in": "query", "name": "redirects", "type": "boolean"}], "path": "/liquipedia/page", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "string"}, {"in": "query", "name": "pageid", "type": "integer"}, {"in": "query", "name": "oldid", "type": "integer"}, {"in": "query", "name": "section", "type": "string"}, {"in": "query", "name": "redirects", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "liquipedia-prefix-search": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-prefix-search", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Required source prefix-search input", "in": "query", "name": "pssearch", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable namespace ID filter, or * for all; discover namespace IDs with liquipedia_enums", "in": "query", "items": {"type": "string"}, "name": "psnamespace", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "pslimit", "type": "string"}, {"description": "Non-negative source result offset", "in": "query", "name": "psoffset", "type": "integer"}, {"description": "Source prefix-search ranking profile", "enum": ["classic", "engine_autoselect", "fast-fuzzy", "fuzzy", "fuzzy-subphrases", "normal", "normal-subphrases", "strict"], "in": "query", "name": "psprofile", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/prefix-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "pssearch", "required": true, "type": "string"}, {"collectionFormat": "csv", "in": "query", "name": "psnamespace", "type": "array"}, {"in": "query", "name": "pslimit", "type": "string"}, {"in": "query", "name": "psoffset", "type": "integer"}, {"enum": ["classic", "engine_autoselect", "fast-fuzzy", "fuzzy", "fuzzy-subphrases", "normal", "normal-subphrases", "strict"], "in": "query", "name": "psprofile", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-recent-changes": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-recent-changes", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Source timestamp lower bound", "in": "query", "name": "rcstart", "type": "string"}, {"description": "Source timestamp upper bound", "in": "query", "name": "rcend", "type": "string"}, {"description": "Source ordering direction", "enum": ["newer", "older"], "in": "query", "name": "rcdir", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable namespace ID, or * for all; discover namespace IDs with liquipedia_enums", "in": "query", "items": {"type": "string"}, "name": "rcnamespace", "type": "array"}, {"description": "Current change-tag name from liquipedia_tags", "in": "query", "name": "rctag", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable metadata field, including user, userid, comment, parsedcomment and loginfo; permission-restricted patrolled is not supported", "in": "query", "items": {"enum": ["comment", "flags", "ids", "loginfo", "parsedcomment", "redirect", "sha1", "sizes", "tags", "timestamp", "title", "user", "userid"], "type": "string"}, "name": "rcprop", "type": "array"}, {"collectionFormat": "csv", "description": "Repeatable source visibility filter", "in": "query", "items": {"enum": ["!anon", "!autopatrolled", "!bot", "!minor", "!patrolled", "!redirect", "anon", "autopatrolled", "bot", "minor", "patrolled", "redirect", "unpatrolled"], "type": "string"}, "name": "rcshow", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "rclimit", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable source change type", "in": "query", "items": {"enum": ["categorize", "edit", "external", "log", "new"], "type": "string"}, "name": "rctype", "type": "array"}, {"description": "Return only the latest revision", "in": "query", "name": "rctoponly", "type": "boolean"}, {"description": "Source page title filter", "in": "query", "name": "rctitle", "type": "string"}, {"description": "Native recent-changes continuation token", "in": "query", "name": "rccontinue", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}, {"description": "Source content slot", "enum": ["main"], "in": "query", "name": "rcslot", "type": "string"}], "path": "/liquipedia/recent-changes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "rcstart", "type": "string"}, {"in": "query", "name": "rcend", "type": "string"}, {"enum": ["newer", "older"], "in": "query", "name": "rcdir", "type": "string"}, {"collectionFormat": "csv", "in": "query", "name": "rcnamespace", "type": "array"}, {"in": "query", "name": "rctag", "type": "string"}, {"collectionFormat": "csv", "enum": ["comment", "flags", "ids", "loginfo", "parsedcomment", "redirect", "sha1", "sizes", "tags", "timestamp", "title", "user", "userid"], "in": "query", "name": "rcprop", "type": "array"}, {"collectionFormat": "csv", "enum": ["!anon", "!autopatrolled", "!bot", "!minor", "!patrolled", "!redirect", "anon", "autopatrolled", "bot", "minor", "patrolled", "redirect", "unpatrolled"], "in": "query", "name": "rcshow", "type": "array"}, {"in": "query", "name": "rclimit", "type": "string"}, {"collectionFormat": "csv", "enum": ["categorize", "edit", "external", "log", "new"], "in": "query", "name": "rctype", "type": "array"}, {"in": "query", "name": "rctoponly", "type": "boolean"}, {"in": "query", "name": "rctitle", "type": "string"}, {"in": "query", "name": "rccontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}, {"enum": ["main"], "in": "query", "name": "rcslot", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-search": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-search", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "MediaWiki search query", "in": "query", "name": "q", "required": true, "type": "string"}, {"collectionFormat": "multi", "description": "Repeatable source namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "srnamespace", "type": "array"}, {"description": "Search mode", "enum": ["nearmatch", "text", "title"], "in": "query", "name": "srwhat", "type": "string"}, {"description": "Page size, 1 through 500, or max (source default 10)", "in": "query", "name": "srlimit", "type": "string"}, {"description": "Non-negative source offset", "in": "query", "name": "sroffset", "type": "integer"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}, {"description": "Source search ordering", "enum": ["create_timestamp_asc", "create_timestamp_desc", "incoming_links_asc", "incoming_links_desc", "just_match", "last_edit_asc", "last_edit_desc", "none", "random", "relevance", "title_natural_asc", "title_natural_desc", "user_random"], "in": "query", "name": "srsort", "type": "string"}, {"collectionFormat": "csv", "description": "Optional repeatable search metadata field", "in": "query", "items": {"enum": ["rewrittenquery", "suggestion", "totalhits"], "type": "string"}, "name": "srinfo", "type": "array"}, {"collectionFormat": "csv", "description": "Optional repeatable result field", "in": "query", "items": {"enum": ["size", "wordcount", "timestamp", "snippet", "titlesnippet", "redirecttitle", "redirectsnippet", "sectiontitle", "sectionsnippet", "isfilematch", "categorysnippet", "extensiondata"], "type": "string"}, "name": "srprop", "type": "array"}, {"description": "Include source interwiki results", "in": "query", "name": "srinterwiki", "type": "boolean"}, {"description": "Allow source query rewrites", "in": "query", "name": "srenablerewrites", "type": "boolean"}, {"description": "Source query-independent ranking profile", "enum": ["classic", "classic_noboostlinks", "empty", "wsum_inclinks", "wsum_inclinks_pv", "popular_inclinks_pv", "popular_inclinks", "engine_autoselect"], "in": "query", "name": "srqiprofile", "type": "string"}, {"description": "Source query-dependent ranking profile", "enum": ["default", "perfield_builder", "perfield_builder_relaxed", "perfield_builder_title_filter", "engine_autoselect"], "in": "query", "name": "srqdprofile", "type": "string"}], "path": "/liquipedia/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "q", "required": true, "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "srnamespace", "type": "array"}, {"enum": ["nearmatch", "text", "title"], "in": "query", "name": "srwhat", "type": "string"}, {"in": "query", "name": "srlimit", "type": "string"}, {"in": "query", "name": "sroffset", "type": "integer"}, {"in": "query", "name": "continue", "type": "string"}, {"enum": ["create_timestamp_asc", "create_timestamp_desc", "incoming_links_asc", "incoming_links_desc", "just_match", "last_edit_asc", "last_edit_desc", "none", "random", "relevance", "title_natural_asc", "title_natural_desc", "user_random"], "in": "query", "name": "srsort", "type": "string"}, {"collectionFormat": "csv", "enum": ["rewrittenquery", "suggestion", "totalhits"], "in": "query", "name": "srinfo", "type": "array"}, {"collectionFormat": "csv", "enum": ["size", "wordcount", "timestamp", "snippet", "titlesnippet", "redirecttitle", "redirectsnippet", "sectiontitle", "sectionsnippet", "isfilematch", "categorysnippet", "extensiondata"], "in": "query", "name": "srprop", "type": "array"}, {"in": "query", "name": "srinterwiki", "type": "boolean"}, {"in": "query", "name": "srenablerewrites", "type": "boolean"}, {"enum": ["classic", "classic_noboostlinks", "empty", "wsum_inclinks", "wsum_inclinks_pv", "popular_inclinks_pv", "popular_inclinks", "engine_autoselect"], "in": "query", "name": "srqiprofile", "type": "string"}, {"enum": ["default", "perfield_builder", "perfield_builder_relaxed", "perfield_builder_title_filter", "engine_autoselect"], "in": "query", "name": "srqdprofile", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-tags": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-tags", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable tag metadata property", "in": "query", "items": {"enum": ["active", "defined", "description", "displayname", "hitcount", "source"], "type": "string"}, "name": "tgprop", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "tglimit", "type": "string"}, {"description": "Native tag-list continuation token", "in": "query", "name": "tgcontinue", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/tags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "csv", "enum": ["active", "defined", "description", "displayname", "hitcount", "source"], "in": "query", "name": "tgprop", "type": "array"}, {"in": "query", "name": "tglimit", "type": "string"}, {"in": "query", "name": "tgcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-wikis": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-wikis", "method": "GET", "params": [], "path": "/liquipedia/wikis", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "liquipedia-wikitext": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-wikitext", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "description": "Repeatable source page titles (up to 50); exactly one of titles, pageids or revids", "in": "query", "items": {"type": "string"}, "name": "titles", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable source page IDs (up to 50); exactly one of titles, pageids or revids", "in": "query", "items": {"type": "integer"}, "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable source revision IDs (up to 50); exactly one of titles, pageids or revids", "in": "query", "items": {"type": "integer"}, "name": "revids", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable revision metadata fields; content is always included", "in": "query", "items": {"enum": ["comment", "content", "contentmodel", "flagged", "flags", "ids", "parsedcomment", "parsetree", "roles", "sha1", "size", "slotsha1", "slotsize", "tags", "timestamp", "user", "userid"], "type": "string"}, "name": "rvprop", "type": "array"}, {"description": "Section number to return (0 is the lead section)", "in": "query", "name": "rvsection", "type": "string"}, {"description": "Revisions to return for one page's history, 1 through 50 or max", "in": "query", "name": "rvlimit", "type": "string"}, {"description": "History: revision ID to start from", "format": "int64", "in": "query", "name": "rvstartid", "type": "integer"}, {"description": "History: revision ID to stop at", "format": "int64", "in": "query", "name": "rvendid", "type": "integer"}, {"description": "History: ISO 8601 timestamp to start from", "in": "query", "name": "rvstart", "type": "string"}, {"description": "History: ISO 8601 timestamp to stop at", "in": "query", "name": "rvend", "type": "string"}, {"description": "History ordering; older lists newest first", "enum": ["newer", "older"], "in": "query", "name": "rvdir", "type": "string"}, {"description": "History: only revisions by this editor", "in": "query", "name": "rvuser", "type": "string"}, {"description": "History: exclude revisions by this editor", "in": "query", "name": "rvexcludeuser", "type": "string"}, {"description": "History: only revisions with this change tag (see liquipedia_tags)", "in": "query", "name": "rvtag", "type": "string"}, {"description": "Native revisions continuation value", "in": "query", "name": "rvcontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}, {"description": "Resolve redirects for titles or page IDs", "in": "query", "name": "redirects", "type": "boolean"}, {"description": "Add each revision's top-level Infobox template parameters as raw wikitext values", "in": "query", "name": "infobox", "type": "boolean"}], "path": "/liquipedia/wikitext", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "titles", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "revids", "type": "array"}, {"collectionFormat": "multi", "enum": ["comment", "content", "contentmodel", "flagged", "flags", "ids", "parsedcomment", "parsetree", "roles", "sha1", "size", "slotsha1", "slotsize", "tags", "timestamp", "user", "userid"], "in": "query", "name": "rvprop", "type": "array"}, {"in": "query", "name": "rvsection", "type": "string"}, {"in": "query", "name": "rvlimit", "type": "string"}, {"in": "query", "name": "rvstartid", "type": "integer"}, {"in": "query", "name": "rvendid", "type": "integer"}, {"in": "query", "name": "rvstart", "type": "string"}, {"in": "query", "name": "rvend", "type": "string"}, {"enum": ["newer", "older"], "in": "query", "name": "rvdir", "type": "string"}, {"in": "query", "name": "rvuser", "type": "string"}, {"in": "query", "name": "rvexcludeuser", "type": "string"}, {"in": "query", "name": "rvtag", "type": "string"}, {"in": "query", "name": "rvcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}, {"in": "query", "name": "redirects", "type": "boolean"}, {"in": "query", "name": "infobox", "type": "boolean"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-liquipedia-php/0.3.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function all_pages(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-all-pages", $params, $responseType);
    }
    public function backlinks(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-backlinks", $params, $responseType);
    }
    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-categories", $params, $responseType);
    }
    public function category_members(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-category-members", $params, $responseType);
    }
    public function embeddedin(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-embeddedin", $params, $responseType);
    }
    public function enums(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-enums", $params, $responseType);
    }
    public function links(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-links", $params, $responseType);
    }
    public function page(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-page", $params, $responseType);
    }
    public function prefix_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-prefix-search", $params, $responseType);
    }
    public function recent_changes(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-recent-changes", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-search", $params, $responseType);
    }
    public function tags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-tags", $params, $responseType);
    }
    public function wikis(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-wikis", $params, $responseType);
    }
    public function wikitext(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("liquipedia-wikitext", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
