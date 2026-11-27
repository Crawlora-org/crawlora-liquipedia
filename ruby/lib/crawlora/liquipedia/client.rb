require "json"
require "net/http"
require "uri"

module Crawlora
  module Liquipedia
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"liquipedia-all-pages": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-all-pages", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Source page title to start enumeration from", "in": "query", "name": "apfrom", "type": "string"}, {"description": "Source page title to stop enumeration at", "in": "query", "name": "apto", "type": "string"}, {"description": "Source page-title prefix", "in": "query", "name": "apprefix", "type": "string"}, {"description": "Source namespace ID; discover IDs with liquipedia_enums", "in": "query", "name": "apnamespace", "type": "integer"}, {"description": "Redirect filter", "enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "apfilterredir", "type": "string"}, {"description": "Language-link filter", "enum": ["all", "withlanglinks", "withoutlanglinks"], "in": "query", "name": "apfilterlanglinks", "type": "string"}, {"description": "Minimum page size in bytes", "in": "query", "name": "apminsize", "type": "integer"}, {"description": "Maximum page size in bytes; MediaWiki may disable this under miser mode", "in": "query", "name": "apmaxsize", "type": "integer"}, {"collectionFormat": "csv", "description": "Repeatable page-protection type", "in": "query", "items": {"enum": ["edit", "move", "upload"], "type": "string"}, "name": "apprtype", "type": "array"}, {"description": "Protection level; requires apprtype", "enum": ["autoconfirmed", "sysop"], "in": "query", "name": "apprlevel", "type": "string"}, {"description": "Cascading-protection filter", "enum": ["all", "cascading", "noncascading"], "in": "query", "name": "apprfiltercascade", "type": "string"}, {"description": "Protection-expiry filter", "enum": ["all", "definite", "indefinite"], "in": "query", "name": "apprexpiry", "type": "string"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "aplimit", "type": "string"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "apdir", "type": "string"}, {"description": "Native all-pages continuation token", "in": "query", "name": "apcontinue", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/all-pages", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "apfrom", "type": "string"}, {"in": "query", "name": "apto", "type": "string"}, {"in": "query", "name": "apprefix", "type": "string"}, {"in": "query", "name": "apnamespace", "type": "integer"}, {"enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "apfilterredir", "type": "string"}, {"enum": ["all", "withlanglinks", "withoutlanglinks"], "in": "query", "name": "apfilterlanglinks", "type": "string"}, {"in": "query", "name": "apminsize", "type": "integer"}, {"in": "query", "name": "apmaxsize", "type": "integer"}, {"collectionFormat": "csv", "enum": ["edit", "move", "upload"], "in": "query", "name": "apprtype", "type": "array"}, {"enum": ["autoconfirmed", "sysop"], "in": "query", "name": "apprlevel", "type": "string"}, {"enum": ["all", "cascading", "noncascading"], "in": "query", "name": "apprfiltercascade", "type": "string"}, {"enum": ["all", "definite", "indefinite"], "in": "query", "name": "apprexpiry", "type": "string"}, {"in": "query", "name": "aplimit", "type": "string"}, {"enum": ["ascending", "descending"], "in": "query", "name": "apdir", "type": "string"}, {"in": "query", "name": "apcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-backlinks": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-backlinks", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Target page title; mutually exclusive with blpageid", "in": "query", "name": "bltitle", "type": "string"}, {"description": "Target page ID; mutually exclusive with bltitle", "in": "query", "name": "blpageid", "type": "integer"}, {"collectionFormat": "multi", "description": "Repeatable referring-page namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "blnamespace", "type": "array"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "bldir", "type": "string"}, {"description": "Source redirect filter", "enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "blfilterredir", "type": "string"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "bllimit", "type": "string"}, {"description": "Include backlinks to redirects of the target page", "in": "query", "name": "blredirect", "type": "boolean"}, {"description": "Native backlinks continuation value", "in": "query", "name": "blcontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/backlinks", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "bltitle", "type": "string"}, {"in": "query", "name": "blpageid", "type": "integer"}, {"collectionFormat": "multi", "in": "query", "name": "blnamespace", "type": "array"}, {"enum": ["ascending", "descending"], "in": "query", "name": "bldir", "type": "string"}, {"enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "blfilterredir", "type": "string"}, {"in": "query", "name": "bllimit", "type": "string"}, {"in": "query", "name": "blredirect", "type": "boolean"}, {"in": "query", "name": "blcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-categories": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-categories", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "First category title to enumerate from", "in": "query", "name": "acfrom", "type": "string"}, {"description": "Last category title to enumerate to", "in": "query", "name": "acto", "type": "string"}, {"description": "Category title prefix", "in": "query", "name": "acprefix", "type": "string"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "acdir", "type": "string"}, {"description": "Minimum category member count", "in": "query", "name": "acmin", "type": "integer"}, {"description": "Maximum category member count", "in": "query", "name": "acmax", "type": "integer"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "aclimit", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable category metadata property", "in": "query", "items": {"enum": ["size", "hidden"], "type": "string"}, "name": "acprop", "type": "array"}, {"description": "Native allcategories continuation token", "in": "query", "name": "accontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "acfrom", "type": "string"}, {"in": "query", "name": "acto", "type": "string"}, {"in": "query", "name": "acprefix", "type": "string"}, {"enum": ["ascending", "descending"], "in": "query", "name": "acdir", "type": "string"}, {"in": "query", "name": "acmin", "type": "integer"}, {"in": "query", "name": "acmax", "type": "integer"}, {"in": "query", "name": "aclimit", "type": "string"}, {"collectionFormat": "csv", "enum": ["size", "hidden"], "in": "query", "name": "acprop", "type": "array"}, {"in": "query", "name": "accontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-category-members": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-category-members", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Category title including Category:; mutually exclusive with cmpageid", "in": "query", "name": "cmtitle", "type": "string"}, {"description": "Category page ID; mutually exclusive with cmtitle", "in": "query", "name": "cmpageid", "type": "integer"}, {"collectionFormat": "multi", "description": "Repeatable source namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "cmnamespace", "type": "array"}, {"collectionFormat": "csv", "description": "Repeatable member type filter", "in": "query", "items": {"enum": ["file", "page", "subcat"], "type": "string"}, "name": "cmtype", "type": "array"}, {"collectionFormat": "csv", "description": "Repeatable returned metadata field", "in": "query", "items": {"enum": ["ids", "title", "sortkey", "sortkeyprefix", "type", "timestamp"], "type": "string"}, "name": "cmprop", "type": "array"}, {"description": "Page size, 1 through 500, or max (source default 10)", "in": "query", "name": "cmlimit", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}, {"description": "Category-members continuation value", "in": "query", "name": "cmcontinue", "type": "string"}, {"description": "Category sort key", "enum": ["sortkey", "timestamp"], "in": "query", "name": "cmsort", "type": "string"}, {"description": "Category sort direction", "enum": ["asc", "ascending", "desc", "descending", "newer", "older"], "in": "query", "name": "cmdir", "type": "string"}, {"description": "Timestamp start bound for cmsort=timestamp", "in": "query", "name": "cmstart", "type": "string"}, {"description": "Timestamp end bound for cmsort=timestamp", "in": "query", "name": "cmend", "type": "string"}, {"description": "Hex sort-key start bound for cmsort=sortkey", "in": "query", "name": "cmstarthexsortkey", "type": "string"}, {"description": "Hex sort-key end bound for cmsort=sortkey", "in": "query", "name": "cmendhexsortkey", "type": "string"}, {"description": "Sort-key prefix start bound for cmsort=sortkey", "in": "query", "name": "cmstartsortkeyprefix", "type": "string"}, {"description": "Sort-key prefix end bound for cmsort=sortkey", "in": "query", "name": "cmendsortkeyprefix", "type": "string"}], "path": "/liquipedia/category-members", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "cmtitle", "type": "string"}, {"in": "query", "name": "cmpageid", "type": "integer"}, {"collectionFormat": "multi", "in": "query", "name": "cmnamespace", "type": "array"}, {"collectionFormat": "csv", "enum": ["file", "page", "subcat"], "in": "query", "name": "cmtype", "type": "array"}, {"collectionFormat": "csv", "enum": ["ids", "title", "sortkey", "sortkeyprefix", "type", "timestamp"], "in": "query", "name": "cmprop", "type": "array"}, {"in": "query", "name": "cmlimit", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}, {"in": "query", "name": "cmcontinue", "type": "string"}, {"enum": ["sortkey", "timestamp"], "in": "query", "name": "cmsort", "type": "string"}, {"enum": ["asc", "ascending", "desc", "descending", "newer", "older"], "in": "query", "name": "cmdir", "type": "string"}, {"in": "query", "name": "cmstart", "type": "string"}, {"in": "query", "name": "cmend", "type": "string"}, {"in": "query", "name": "cmstarthexsortkey", "type": "string"}, {"in": "query", "name": "cmendhexsortkey", "type": "string"}, {"in": "query", "name": "cmstartsortkeyprefix", "type": "string"}, {"in": "query", "name": "cmendsortkeyprefix", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-embeddedin": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-embeddedin", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Transcluded page title such as Template:Infobox league; mutually exclusive with eipageid", "in": "query", "name": "eititle", "type": "string"}, {"description": "Transcluded page ID; mutually exclusive with eititle", "in": "query", "name": "eipageid", "type": "integer"}, {"collectionFormat": "multi", "description": "Repeatable transcluding-page namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "einamespace", "type": "array"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "eidir", "type": "string"}, {"description": "Source redirect filter", "enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "eifilterredir", "type": "string"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "eilimit", "type": "string"}, {"description": "Native embeddedin continuation value", "in": "query", "name": "eicontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/embeddedin", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "eititle", "type": "string"}, {"in": "query", "name": "eipageid", "type": "integer"}, {"collectionFormat": "multi", "in": "query", "name": "einamespace", "type": "array"}, {"enum": ["ascending", "descending"], "in": "query", "name": "eidir", "type": "string"}, {"enum": ["all", "nonredirects", "redirects"], "in": "query", "name": "eifilterredir", "type": "string"}, {"in": "query", "name": "eilimit", "type": "string"}, {"in": "query", "name": "eicontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-enums": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-enums", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}], "path": "/liquipedia/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-links": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-links", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "description": "Source page title; mutually exclusive with pageids and revids", "in": "query", "items": {"type": "string"}, "name": "titles", "type": "array"}, {"collectionFormat": "multi", "description": "Source page ID; mutually exclusive with titles and revids", "in": "query", "items": {"type": "integer"}, "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "description": "Source revision ID; mutually exclusive with titles and pageids", "in": "query", "items": {"type": "integer"}, "name": "revids", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable linked-page namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "plnamespace", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "pllimit", "type": "string"}, {"description": "Native links continuation value", "in": "query", "name": "plcontinue", "type": "string"}, {"collectionFormat": "multi", "description": "Optional source title filter, up to 50 titles", "in": "query", "items": {"type": "string"}, "name": "pltitles", "type": "array"}, {"description": "Source ordering direction", "enum": ["ascending", "descending"], "in": "query", "name": "pldir", "type": "string"}, {"description": "Resolve source-page redirects", "in": "query", "name": "redirects", "type": "boolean"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/links", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "titles", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "revids", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "plnamespace", "type": "array"}, {"in": "query", "name": "pllimit", "type": "string"}, {"in": "query", "name": "plcontinue", "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "pltitles", "type": "array"}, {"enum": ["ascending", "descending"], "in": "query", "name": "pldir", "type": "string"}, {"in": "query", "name": "redirects", "type": "boolean"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-page": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-page", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Source page title; mutually exclusive with pageid and oldid", "in": "query", "name": "page", "type": "string"}, {"description": "Source page ID; mutually exclusive with page and oldid", "in": "query", "name": "pageid", "type": "integer"}, {"description": "Source revision ID; mutually exclusive with page and pageid", "format": "int64", "in": "query", "name": "oldid", "type": "integer"}, {"description": "Source section number or anchor ID", "in": "query", "name": "section", "type": "string"}, {"description": "Resolve page redirects", "in": "query", "name": "redirects", "type": "boolean"}], "path": "/liquipedia/page", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "string"}, {"in": "query", "name": "pageid", "type": "integer"}, {"in": "query", "name": "oldid", "type": "integer"}, {"in": "query", "name": "section", "type": "string"}, {"in": "query", "name": "redirects", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "liquipedia-prefix-search": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-prefix-search", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Required source prefix-search input", "in": "query", "name": "pssearch", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable namespace ID filter, or * for all; discover namespace IDs with liquipedia_enums", "in": "query", "items": {"type": "string"}, "name": "psnamespace", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "pslimit", "type": "string"}, {"description": "Non-negative source result offset", "in": "query", "name": "psoffset", "type": "integer"}, {"description": "Source prefix-search ranking profile", "enum": ["classic", "engine_autoselect", "fast-fuzzy", "fuzzy", "fuzzy-subphrases", "normal", "normal-subphrases", "strict"], "in": "query", "name": "psprofile", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/prefix-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "pssearch", "required": true, "type": "string"}, {"collectionFormat": "csv", "in": "query", "name": "psnamespace", "type": "array"}, {"in": "query", "name": "pslimit", "type": "string"}, {"in": "query", "name": "psoffset", "type": "integer"}, {"enum": ["classic", "engine_autoselect", "fast-fuzzy", "fuzzy", "fuzzy-subphrases", "normal", "normal-subphrases", "strict"], "in": "query", "name": "psprofile", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-recent-changes": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-recent-changes", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "Source timestamp lower bound", "in": "query", "name": "rcstart", "type": "string"}, {"description": "Source timestamp upper bound", "in": "query", "name": "rcend", "type": "string"}, {"description": "Source ordering direction", "enum": ["newer", "older"], "in": "query", "name": "rcdir", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable namespace ID, or * for all; discover namespace IDs with liquipedia_enums", "in": "query", "items": {"type": "string"}, "name": "rcnamespace", "type": "array"}, {"description": "Current change-tag name from liquipedia_tags", "in": "query", "name": "rctag", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable metadata field, including user, userid, comment, parsedcomment and loginfo; permission-restricted patrolled is not supported", "in": "query", "items": {"enum": ["comment", "flags", "ids", "loginfo", "parsedcomment", "redirect", "sha1", "sizes", "tags", "timestamp", "title", "user", "userid"], "type": "string"}, "name": "rcprop", "type": "array"}, {"collectionFormat": "csv", "description": "Repeatable source visibility filter", "in": "query", "items": {"enum": ["!anon", "!autopatrolled", "!bot", "!minor", "!patrolled", "!redirect", "anon", "autopatrolled", "bot", "minor", "patrolled", "redirect", "unpatrolled"], "type": "string"}, "name": "rcshow", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "rclimit", "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable source change type", "in": "query", "items": {"enum": ["categorize", "edit", "external", "log", "new"], "type": "string"}, "name": "rctype", "type": "array"}, {"description": "Return only the latest revision", "in": "query", "name": "rctoponly", "type": "boolean"}, {"description": "Source page title filter", "in": "query", "name": "rctitle", "type": "string"}, {"description": "Native recent-changes continuation token", "in": "query", "name": "rccontinue", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}, {"description": "Source content slot", "enum": ["main"], "in": "query", "name": "rcslot", "type": "string"}], "path": "/liquipedia/recent-changes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "rcstart", "type": "string"}, {"in": "query", "name": "rcend", "type": "string"}, {"enum": ["newer", "older"], "in": "query", "name": "rcdir", "type": "string"}, {"collectionFormat": "csv", "in": "query", "name": "rcnamespace", "type": "array"}, {"in": "query", "name": "rctag", "type": "string"}, {"collectionFormat": "csv", "enum": ["comment", "flags", "ids", "loginfo", "parsedcomment", "redirect", "sha1", "sizes", "tags", "timestamp", "title", "user", "userid"], "in": "query", "name": "rcprop", "type": "array"}, {"collectionFormat": "csv", "enum": ["!anon", "!autopatrolled", "!bot", "!minor", "!patrolled", "!redirect", "anon", "autopatrolled", "bot", "minor", "patrolled", "redirect", "unpatrolled"], "in": "query", "name": "rcshow", "type": "array"}, {"in": "query", "name": "rclimit", "type": "string"}, {"collectionFormat": "csv", "enum": ["categorize", "edit", "external", "log", "new"], "in": "query", "name": "rctype", "type": "array"}, {"in": "query", "name": "rctoponly", "type": "boolean"}, {"in": "query", "name": "rctitle", "type": "string"}, {"in": "query", "name": "rccontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}, {"enum": ["main"], "in": "query", "name": "rcslot", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-search": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-search", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"description": "MediaWiki search query", "in": "query", "name": "q", "required": true, "type": "string"}, {"collectionFormat": "multi", "description": "Repeatable source namespace ID filter, or * for all", "in": "query", "items": {"type": "string"}, "name": "srnamespace", "type": "array"}, {"description": "Search mode", "enum": ["nearmatch", "text", "title"], "in": "query", "name": "srwhat", "type": "string"}, {"description": "Page size, 1 through 500, or max (source default 10)", "in": "query", "name": "srlimit", "type": "string"}, {"description": "Non-negative source offset", "in": "query", "name": "sroffset", "type": "integer"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}, {"description": "Source search ordering", "enum": ["create_timestamp_asc", "create_timestamp_desc", "incoming_links_asc", "incoming_links_desc", "just_match", "last_edit_asc", "last_edit_desc", "none", "random", "relevance", "title_natural_asc", "title_natural_desc", "user_random"], "in": "query", "name": "srsort", "type": "string"}, {"collectionFormat": "csv", "description": "Optional repeatable search metadata field", "in": "query", "items": {"enum": ["rewrittenquery", "suggestion", "totalhits"], "type": "string"}, "name": "srinfo", "type": "array"}, {"collectionFormat": "csv", "description": "Optional repeatable result field", "in": "query", "items": {"enum": ["size", "wordcount", "timestamp", "snippet", "titlesnippet", "redirecttitle", "redirectsnippet", "sectiontitle", "sectionsnippet", "isfilematch", "categorysnippet", "extensiondata"], "type": "string"}, "name": "srprop", "type": "array"}, {"description": "Include source interwiki results", "in": "query", "name": "srinterwiki", "type": "boolean"}, {"description": "Allow source query rewrites", "in": "query", "name": "srenablerewrites", "type": "boolean"}, {"description": "Source query-independent ranking profile", "enum": ["classic", "classic_noboostlinks", "empty", "wsum_inclinks", "wsum_inclinks_pv", "popular_inclinks_pv", "popular_inclinks", "engine_autoselect"], "in": "query", "name": "srqiprofile", "type": "string"}, {"description": "Source query-dependent ranking profile", "enum": ["default", "perfield_builder", "perfield_builder_relaxed", "perfield_builder_title_filter", "engine_autoselect"], "in": "query", "name": "srqdprofile", "type": "string"}], "path": "/liquipedia/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"in": "query", "name": "q", "required": true, "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "srnamespace", "type": "array"}, {"enum": ["nearmatch", "text", "title"], "in": "query", "name": "srwhat", "type": "string"}, {"in": "query", "name": "srlimit", "type": "string"}, {"in": "query", "name": "sroffset", "type": "integer"}, {"in": "query", "name": "continue", "type": "string"}, {"enum": ["create_timestamp_asc", "create_timestamp_desc", "incoming_links_asc", "incoming_links_desc", "just_match", "last_edit_asc", "last_edit_desc", "none", "random", "relevance", "title_natural_asc", "title_natural_desc", "user_random"], "in": "query", "name": "srsort", "type": "string"}, {"collectionFormat": "csv", "enum": ["rewrittenquery", "suggestion", "totalhits"], "in": "query", "name": "srinfo", "type": "array"}, {"collectionFormat": "csv", "enum": ["size", "wordcount", "timestamp", "snippet", "titlesnippet", "redirecttitle", "redirectsnippet", "sectiontitle", "sectionsnippet", "isfilematch", "categorysnippet", "extensiondata"], "in": "query", "name": "srprop", "type": "array"}, {"in": "query", "name": "srinterwiki", "type": "boolean"}, {"in": "query", "name": "srenablerewrites", "type": "boolean"}, {"enum": ["classic", "classic_noboostlinks", "empty", "wsum_inclinks", "wsum_inclinks_pv", "popular_inclinks_pv", "popular_inclinks", "engine_autoselect"], "in": "query", "name": "srqiprofile", "type": "string"}, {"enum": ["default", "perfield_builder", "perfield_builder_relaxed", "perfield_builder_title_filter", "engine_autoselect"], "in": "query", "name": "srqdprofile", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-tags": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-tags", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "csv", "description": "Repeatable tag metadata property", "in": "query", "items": {"enum": ["active", "defined", "description", "displayname", "hitcount", "source"], "type": "string"}, "name": "tgprop", "type": "array"}, {"description": "Page size from 1 through 500, or max; source default is 10", "in": "query", "name": "tglimit", "type": "string"}, {"description": "Native tag-list continuation token", "in": "query", "name": "tgcontinue", "type": "string"}, {"description": "Global MediaWiki continuation token", "in": "query", "name": "continue", "type": "string"}], "path": "/liquipedia/tags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "csv", "enum": ["active", "defined", "description", "displayname", "hitcount", "source"], "in": "query", "name": "tgprop", "type": "array"}, {"in": "query", "name": "tglimit", "type": "string"}, {"in": "query", "name": "tgcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}], "security": ["ApiKeyAuth"]}, "liquipedia-wikis": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-wikis", "method": "GET", "params": [], "path": "/liquipedia/wikis", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "liquipedia-wikitext": {"bodyParam": null, "bodyRequired": false, "id": "liquipedia-wikitext", "method": "GET", "params": [{"description": "Liquipedia wiki slug from liquipedia_wikis", "in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "description": "Repeatable source page titles (up to 50); exactly one of titles, pageids or revids", "in": "query", "items": {"type": "string"}, "name": "titles", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable source page IDs (up to 50); exactly one of titles, pageids or revids", "in": "query", "items": {"type": "integer"}, "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable source revision IDs (up to 50); exactly one of titles, pageids or revids", "in": "query", "items": {"type": "integer"}, "name": "revids", "type": "array"}, {"collectionFormat": "multi", "description": "Repeatable revision metadata fields; content is always included", "in": "query", "items": {"enum": ["comment", "content", "contentmodel", "flagged", "flags", "ids", "parsedcomment", "parsetree", "roles", "sha1", "size", "slotsha1", "slotsize", "tags", "timestamp", "user", "userid"], "type": "string"}, "name": "rvprop", "type": "array"}, {"description": "Section number to return (0 is the lead section)", "in": "query", "name": "rvsection", "type": "string"}, {"description": "Revisions to return for one page's history, 1 through 50 or max", "in": "query", "name": "rvlimit", "type": "string"}, {"description": "History: revision ID to start from", "format": "int64", "in": "query", "name": "rvstartid", "type": "integer"}, {"description": "History: revision ID to stop at", "format": "int64", "in": "query", "name": "rvendid", "type": "integer"}, {"description": "History: ISO 8601 timestamp to start from", "in": "query", "name": "rvstart", "type": "string"}, {"description": "History: ISO 8601 timestamp to stop at", "in": "query", "name": "rvend", "type": "string"}, {"description": "History ordering; older lists newest first", "enum": ["newer", "older"], "in": "query", "name": "rvdir", "type": "string"}, {"description": "History: only revisions by this editor", "in": "query", "name": "rvuser", "type": "string"}, {"description": "History: exclude revisions by this editor", "in": "query", "name": "rvexcludeuser", "type": "string"}, {"description": "History: only revisions with this change tag (see liquipedia_tags)", "in": "query", "name": "rvtag", "type": "string"}, {"description": "Native revisions continuation value", "in": "query", "name": "rvcontinue", "type": "string"}, {"description": "Global MediaWiki continuation value", "in": "query", "name": "continue", "type": "string"}, {"description": "Resolve redirects for titles or page IDs", "in": "query", "name": "redirects", "type": "boolean"}, {"description": "Add each revision's top-level Infobox template parameters as raw wikitext values", "in": "query", "name": "infobox", "type": "boolean"}], "path": "/liquipedia/wikitext", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "wiki", "required": true, "type": "string"}, {"collectionFormat": "multi", "in": "query", "name": "titles", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "pageids", "type": "array"}, {"collectionFormat": "multi", "in": "query", "name": "revids", "type": "array"}, {"collectionFormat": "multi", "enum": ["comment", "content", "contentmodel", "flagged", "flags", "ids", "parsedcomment", "parsetree", "roles", "sha1", "size", "slotsha1", "slotsize", "tags", "timestamp", "user", "userid"], "in": "query", "name": "rvprop", "type": "array"}, {"in": "query", "name": "rvsection", "type": "string"}, {"in": "query", "name": "rvlimit", "type": "string"}, {"in": "query", "name": "rvstartid", "type": "integer"}, {"in": "query", "name": "rvendid", "type": "integer"}, {"in": "query", "name": "rvstart", "type": "string"}, {"in": "query", "name": "rvend", "type": "string"}, {"enum": ["newer", "older"], "in": "query", "name": "rvdir", "type": "string"}, {"in": "query", "name": "rvuser", "type": "string"}, {"in": "query", "name": "rvexcludeuser", "type": "string"}, {"in": "query", "name": "rvtag", "type": "string"}, {"in": "query", "name": "rvcontinue", "type": "string"}, {"in": "query", "name": "continue", "type": "string"}, {"in": "query", "name": "redirects", "type": "boolean"}, {"in": "query", "name": "infobox", "type": "boolean"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["liquipedia-all-pages", "liquipedia-backlinks", "liquipedia-categories", "liquipedia-category-members", "liquipedia-embeddedin", "liquipedia-enums", "liquipedia-links", "liquipedia-page", "liquipedia-prefix-search", "liquipedia-recent-changes", "liquipedia-search", "liquipedia-tags", "liquipedia-wikis", "liquipedia-wikitext"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-liquipedia-ruby/0.3.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('all_pages') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-all-pages', params, response_type: response_type)
      end
      define_method('backlinks') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-backlinks', params, response_type: response_type)
      end
      define_method('categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-categories', params, response_type: response_type)
      end
      define_method('category_members') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-category-members', params, response_type: response_type)
      end
      define_method('embeddedin') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-embeddedin', params, response_type: response_type)
      end
      define_method('enums') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-enums', params, response_type: response_type)
      end
      define_method('links') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-links', params, response_type: response_type)
      end
      define_method('page') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-page', params, response_type: response_type)
      end
      define_method('prefix_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-prefix-search', params, response_type: response_type)
      end
      define_method('recent_changes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-recent-changes', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-search', params, response_type: response_type)
      end
      define_method('tags') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-tags', params, response_type: response_type)
      end
      define_method('wikis') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-wikis', params, response_type: response_type)
      end
      define_method('wikitext') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('liquipedia-wikitext', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
