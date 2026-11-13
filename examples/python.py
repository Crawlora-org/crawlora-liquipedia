import os

from crawlora_liquipedia import LiquipediaClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with LiquipediaClient(api_key=api_key) as client:
    wikis = client.wikis()
    print('wikis', wikis)
    search = client.search(wiki='counterstrike', q='Major', srlimit='5')
    print('search', search)
