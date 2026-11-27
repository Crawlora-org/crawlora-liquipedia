package net.crawlora.liquipedia;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Liquipedia endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 14;
    public static final List<String> OPERATION_IDS = List.of(
            "liquipedia-all-pages",
            "liquipedia-backlinks",
            "liquipedia-categories",
            "liquipedia-category-members",
            "liquipedia-embeddedin",
            "liquipedia-enums",
            "liquipedia-links",
            "liquipedia-page",
            "liquipedia-prefix-search",
            "liquipedia-recent-changes",
            "liquipedia-search",
            "liquipedia-tags",
            "liquipedia-wikis",
            "liquipedia-wikitext"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("liquipedia-all-pages", new Operation("liquipedia-all-pages", "GET", "/liquipedia/all-pages", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("apfrom", new Param("apfrom", "query", false, "string", List.of(), "csv")), Map.entry("apto", new Param("apto", "query", false, "string", List.of(), "csv")), Map.entry("apprefix", new Param("apprefix", "query", false, "string", List.of(), "csv")), Map.entry("apnamespace", new Param("apnamespace", "query", false, "integer", List.of(), "csv")), Map.entry("apfilterredir", new Param("apfilterredir", "query", false, "string", List.of("all", "nonredirects", "redirects"), "csv")), Map.entry("apfilterlanglinks", new Param("apfilterlanglinks", "query", false, "string", List.of("all", "withlanglinks", "withoutlanglinks"), "csv")), Map.entry("apminsize", new Param("apminsize", "query", false, "integer", List.of(), "csv")), Map.entry("apmaxsize", new Param("apmaxsize", "query", false, "integer", List.of(), "csv")), Map.entry("apprtype", new Param("apprtype", "query", false, "array", List.of("edit", "move", "upload"), "csv")), Map.entry("apprlevel", new Param("apprlevel", "query", false, "string", List.of("autoconfirmed", "sysop"), "csv")), Map.entry("apprfiltercascade", new Param("apprfiltercascade", "query", false, "string", List.of("all", "cascading", "noncascading"), "csv")), Map.entry("apprexpiry", new Param("apprexpiry", "query", false, "string", List.of("all", "definite", "indefinite"), "csv")), Map.entry("aplimit", new Param("aplimit", "query", false, "string", List.of(), "csv")), Map.entry("apdir", new Param("apdir", "query", false, "string", List.of("ascending", "descending"), "csv")), Map.entry("apcontinue", new Param("apcontinue", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-backlinks", new Operation("liquipedia-backlinks", "GET", "/liquipedia/backlinks", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("bltitle", new Param("bltitle", "query", false, "string", List.of(), "csv")), Map.entry("blpageid", new Param("blpageid", "query", false, "integer", List.of(), "csv")), Map.entry("blnamespace", new Param("blnamespace", "query", false, "array", List.of(), "multi")), Map.entry("bldir", new Param("bldir", "query", false, "string", List.of("ascending", "descending"), "csv")), Map.entry("blfilterredir", new Param("blfilterredir", "query", false, "string", List.of("all", "nonredirects", "redirects"), "csv")), Map.entry("bllimit", new Param("bllimit", "query", false, "string", List.of(), "csv")), Map.entry("blredirect", new Param("blredirect", "query", false, "boolean", List.of(), "csv")), Map.entry("blcontinue", new Param("blcontinue", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-categories", new Operation("liquipedia-categories", "GET", "/liquipedia/categories", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("acfrom", new Param("acfrom", "query", false, "string", List.of(), "csv")), Map.entry("acto", new Param("acto", "query", false, "string", List.of(), "csv")), Map.entry("acprefix", new Param("acprefix", "query", false, "string", List.of(), "csv")), Map.entry("acdir", new Param("acdir", "query", false, "string", List.of("ascending", "descending"), "csv")), Map.entry("acmin", new Param("acmin", "query", false, "integer", List.of(), "csv")), Map.entry("acmax", new Param("acmax", "query", false, "integer", List.of(), "csv")), Map.entry("aclimit", new Param("aclimit", "query", false, "string", List.of(), "csv")), Map.entry("acprop", new Param("acprop", "query", false, "array", List.of("size", "hidden"), "csv")), Map.entry("accontinue", new Param("accontinue", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-category-members", new Operation("liquipedia-category-members", "GET", "/liquipedia/category-members", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("cmtitle", new Param("cmtitle", "query", false, "string", List.of(), "csv")), Map.entry("cmpageid", new Param("cmpageid", "query", false, "integer", List.of(), "csv")), Map.entry("cmnamespace", new Param("cmnamespace", "query", false, "array", List.of(), "multi")), Map.entry("cmtype", new Param("cmtype", "query", false, "array", List.of("file", "page", "subcat"), "csv")), Map.entry("cmprop", new Param("cmprop", "query", false, "array", List.of("ids", "title", "sortkey", "sortkeyprefix", "type", "timestamp"), "csv")), Map.entry("cmlimit", new Param("cmlimit", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv")), Map.entry("cmcontinue", new Param("cmcontinue", "query", false, "string", List.of(), "csv")), Map.entry("cmsort", new Param("cmsort", "query", false, "string", List.of("sortkey", "timestamp"), "csv")), Map.entry("cmdir", new Param("cmdir", "query", false, "string", List.of("asc", "ascending", "desc", "descending", "newer", "older"), "csv")), Map.entry("cmstart", new Param("cmstart", "query", false, "string", List.of(), "csv")), Map.entry("cmend", new Param("cmend", "query", false, "string", List.of(), "csv")), Map.entry("cmstarthexsortkey", new Param("cmstarthexsortkey", "query", false, "string", List.of(), "csv")), Map.entry("cmendhexsortkey", new Param("cmendhexsortkey", "query", false, "string", List.of(), "csv")), Map.entry("cmstartsortkeyprefix", new Param("cmstartsortkeyprefix", "query", false, "string", List.of(), "csv")), Map.entry("cmendsortkeyprefix", new Param("cmendsortkeyprefix", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-embeddedin", new Operation("liquipedia-embeddedin", "GET", "/liquipedia/embeddedin", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("eititle", new Param("eititle", "query", false, "string", List.of(), "csv")), Map.entry("eipageid", new Param("eipageid", "query", false, "integer", List.of(), "csv")), Map.entry("einamespace", new Param("einamespace", "query", false, "array", List.of(), "multi")), Map.entry("eidir", new Param("eidir", "query", false, "string", List.of("ascending", "descending"), "csv")), Map.entry("eifilterredir", new Param("eifilterredir", "query", false, "string", List.of("all", "nonredirects", "redirects"), "csv")), Map.entry("eilimit", new Param("eilimit", "query", false, "string", List.of(), "csv")), Map.entry("eicontinue", new Param("eicontinue", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-enums", new Operation("liquipedia-enums", "GET", "/liquipedia/enums", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-links", new Operation("liquipedia-links", "GET", "/liquipedia/links", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("titles", new Param("titles", "query", false, "array", List.of(), "multi")), Map.entry("pageids", new Param("pageids", "query", false, "array", List.of(), "multi")), Map.entry("revids", new Param("revids", "query", false, "array", List.of(), "multi")), Map.entry("plnamespace", new Param("plnamespace", "query", false, "array", List.of(), "multi")), Map.entry("pllimit", new Param("pllimit", "query", false, "string", List.of(), "csv")), Map.entry("plcontinue", new Param("plcontinue", "query", false, "string", List.of(), "csv")), Map.entry("pltitles", new Param("pltitles", "query", false, "array", List.of(), "multi")), Map.entry("pldir", new Param("pldir", "query", false, "string", List.of("ascending", "descending"), "csv")), Map.entry("redirects", new Param("redirects", "query", false, "boolean", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-page", new Operation("liquipedia-page", "GET", "/liquipedia/page", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "string", List.of(), "csv")), Map.entry("pageid", new Param("pageid", "query", false, "integer", List.of(), "csv")), Map.entry("oldid", new Param("oldid", "query", false, "integer", List.of(), "csv")), Map.entry("section", new Param("section", "query", false, "string", List.of(), "csv")), Map.entry("redirects", new Param("redirects", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-prefix-search", new Operation("liquipedia-prefix-search", "GET", "/liquipedia/prefix-search", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("pssearch", new Param("pssearch", "query", true, "string", List.of(), "csv")), Map.entry("psnamespace", new Param("psnamespace", "query", false, "array", List.of(), "csv")), Map.entry("pslimit", new Param("pslimit", "query", false, "string", List.of(), "csv")), Map.entry("psoffset", new Param("psoffset", "query", false, "integer", List.of(), "csv")), Map.entry("psprofile", new Param("psprofile", "query", false, "string", List.of("classic", "engine_autoselect", "fast-fuzzy", "fuzzy", "fuzzy-subphrases", "normal", "normal-subphrases", "strict"), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-recent-changes", new Operation("liquipedia-recent-changes", "GET", "/liquipedia/recent-changes", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("rcstart", new Param("rcstart", "query", false, "string", List.of(), "csv")), Map.entry("rcend", new Param("rcend", "query", false, "string", List.of(), "csv")), Map.entry("rcdir", new Param("rcdir", "query", false, "string", List.of("newer", "older"), "csv")), Map.entry("rcnamespace", new Param("rcnamespace", "query", false, "array", List.of(), "csv")), Map.entry("rctag", new Param("rctag", "query", false, "string", List.of(), "csv")), Map.entry("rcprop", new Param("rcprop", "query", false, "array", List.of("comment", "flags", "ids", "loginfo", "parsedcomment", "redirect", "sha1", "sizes", "tags", "timestamp", "title", "user", "userid"), "csv")), Map.entry("rcshow", new Param("rcshow", "query", false, "array", List.of("!anon", "!autopatrolled", "!bot", "!minor", "!patrolled", "!redirect", "anon", "autopatrolled", "bot", "minor", "patrolled", "redirect", "unpatrolled"), "csv")), Map.entry("rclimit", new Param("rclimit", "query", false, "string", List.of(), "csv")), Map.entry("rctype", new Param("rctype", "query", false, "array", List.of("categorize", "edit", "external", "log", "new"), "csv")), Map.entry("rctoponly", new Param("rctoponly", "query", false, "boolean", List.of(), "csv")), Map.entry("rctitle", new Param("rctitle", "query", false, "string", List.of(), "csv")), Map.entry("rccontinue", new Param("rccontinue", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv")), Map.entry("rcslot", new Param("rcslot", "query", false, "string", List.of("main"), "csv"))), List.of("application/json")));
        operations.put("liquipedia-search", new Operation("liquipedia-search", "GET", "/liquipedia/search", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv")), Map.entry("srnamespace", new Param("srnamespace", "query", false, "array", List.of(), "multi")), Map.entry("srwhat", new Param("srwhat", "query", false, "string", List.of("nearmatch", "text", "title"), "csv")), Map.entry("srlimit", new Param("srlimit", "query", false, "string", List.of(), "csv")), Map.entry("sroffset", new Param("sroffset", "query", false, "integer", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv")), Map.entry("srsort", new Param("srsort", "query", false, "string", List.of("create_timestamp_asc", "create_timestamp_desc", "incoming_links_asc", "incoming_links_desc", "just_match", "last_edit_asc", "last_edit_desc", "none", "random", "relevance", "title_natural_asc", "title_natural_desc", "user_random"), "csv")), Map.entry("srinfo", new Param("srinfo", "query", false, "array", List.of("rewrittenquery", "suggestion", "totalhits"), "csv")), Map.entry("srprop", new Param("srprop", "query", false, "array", List.of("size", "wordcount", "timestamp", "snippet", "titlesnippet", "redirecttitle", "redirectsnippet", "sectiontitle", "sectionsnippet", "isfilematch", "categorysnippet", "extensiondata"), "csv")), Map.entry("srinterwiki", new Param("srinterwiki", "query", false, "boolean", List.of(), "csv")), Map.entry("srenablerewrites", new Param("srenablerewrites", "query", false, "boolean", List.of(), "csv")), Map.entry("srqiprofile", new Param("srqiprofile", "query", false, "string", List.of("classic", "classic_noboostlinks", "empty", "wsum_inclinks", "wsum_inclinks_pv", "popular_inclinks_pv", "popular_inclinks", "engine_autoselect"), "csv")), Map.entry("srqdprofile", new Param("srqdprofile", "query", false, "string", List.of("default", "perfield_builder", "perfield_builder_relaxed", "perfield_builder_title_filter", "engine_autoselect"), "csv"))), List.of("application/json")));
        operations.put("liquipedia-tags", new Operation("liquipedia-tags", "GET", "/liquipedia/tags", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("tgprop", new Param("tgprop", "query", false, "array", List.of("active", "defined", "description", "displayname", "hitcount", "source"), "csv")), Map.entry("tglimit", new Param("tglimit", "query", false, "string", List.of(), "csv")), Map.entry("tgcontinue", new Param("tgcontinue", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("liquipedia-wikis", new Operation("liquipedia-wikis", "GET", "/liquipedia/wikis", Map.of(), List.of("application/json")));
        operations.put("liquipedia-wikitext", new Operation("liquipedia-wikitext", "GET", "/liquipedia/wikitext", Map.ofEntries(Map.entry("wiki", new Param("wiki", "query", true, "string", List.of(), "csv")), Map.entry("titles", new Param("titles", "query", false, "array", List.of(), "multi")), Map.entry("pageids", new Param("pageids", "query", false, "array", List.of(), "multi")), Map.entry("revids", new Param("revids", "query", false, "array", List.of(), "multi")), Map.entry("rvprop", new Param("rvprop", "query", false, "array", List.of("comment", "content", "contentmodel", "flagged", "flags", "ids", "parsedcomment", "parsetree", "roles", "sha1", "size", "slotsha1", "slotsize", "tags", "timestamp", "user", "userid"), "multi")), Map.entry("rvsection", new Param("rvsection", "query", false, "string", List.of(), "csv")), Map.entry("rvlimit", new Param("rvlimit", "query", false, "string", List.of(), "csv")), Map.entry("rvstartid", new Param("rvstartid", "query", false, "integer", List.of(), "csv")), Map.entry("rvendid", new Param("rvendid", "query", false, "integer", List.of(), "csv")), Map.entry("rvstart", new Param("rvstart", "query", false, "string", List.of(), "csv")), Map.entry("rvend", new Param("rvend", "query", false, "string", List.of(), "csv")), Map.entry("rvdir", new Param("rvdir", "query", false, "string", List.of("newer", "older"), "csv")), Map.entry("rvuser", new Param("rvuser", "query", false, "string", List.of(), "csv")), Map.entry("rvexcludeuser", new Param("rvexcludeuser", "query", false, "string", List.of(), "csv")), Map.entry("rvtag", new Param("rvtag", "query", false, "string", List.of(), "csv")), Map.entry("rvcontinue", new Param("rvcontinue", "query", false, "string", List.of(), "csv")), Map.entry("continue", new Param("continue", "query", false, "string", List.of(), "csv")), Map.entry("redirects", new Param("redirects", "query", false, "boolean", List.of(), "csv")), Map.entry("infobox", new Param("infobox", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Liquipedia operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object allPages(Map<String, ?> params) { return request("liquipedia-all-pages", params); }
    public Object backlinks(Map<String, ?> params) { return request("liquipedia-backlinks", params); }
    public Object categories(Map<String, ?> params) { return request("liquipedia-categories", params); }
    public Object categoryMembers(Map<String, ?> params) { return request("liquipedia-category-members", params); }
    public Object embeddedin(Map<String, ?> params) { return request("liquipedia-embeddedin", params); }
    public Object enums(Map<String, ?> params) { return request("liquipedia-enums", params); }
    public Object links(Map<String, ?> params) { return request("liquipedia-links", params); }
    public Object page(Map<String, ?> params) { return request("liquipedia-page", params); }
    public Object prefixSearch(Map<String, ?> params) { return request("liquipedia-prefix-search", params); }
    public Object recentChanges(Map<String, ?> params) { return request("liquipedia-recent-changes", params); }
    public Object search(Map<String, ?> params) { return request("liquipedia-search", params); }
    public Object tags(Map<String, ?> params) { return request("liquipedia-tags", params); }
    public Object wikis(Map<String, ?> params) { return request("liquipedia-wikis", params); }
    public Object wikitext(Map<String, ?> params) { return request("liquipedia-wikitext", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
