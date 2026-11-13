import { LiquipediaClient } from "../src/index.js";

const client = new LiquipediaClient({ apiKey: "test-key" });
void client.allPages({"wiki": "sample"});
void client.request("liquipedia-all-pages", {"wiki": "sample"});
const streamResponse: Promise<Response> = client.request("liquipedia-all-pages", {"wiki": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("liquipedia-all-pages", {"wiki": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.allPages({"wiki": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("liquipedia-all-pages", {"wiki": "sample", "apfrom": "sample", "apto": "sample", "apprefix": "sample", "apnamespace": 1, "apfilterredir": "all", "apfilterlanglinks": "all", "apminsize": 1, "apmaxsize": 1, "apprtype": ["edit"], "apprlevel": "autoconfirmed", "apprfiltercascade": "all", "apprexpiry": "all", "aplimit": "sample", "apdir": "ascending", "apcontinue": "sample", "continue": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("liquipedia-all-pages", {"wiki": "sample"}, { responseType: "text" });
void rawText;


void client.wikis();
void client.request("liquipedia-wikis");
// @ts-expect-error The selected operation requires its documented params.
void client.allPages();
