import { LiquipediaClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new LiquipediaClient({ apiKey });

  const wikis = await client.wikis({  });
  console.log("wikis", wikis);
  const search = await client.search({ wiki: "counterstrike", q: "Major", srlimit: "5" });
  console.log("search", search);
