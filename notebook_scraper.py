import feedparser

with open('rss_list.txt', 'r', encoding='utf-8') as f:
    rss_urls = [line.strip() for line in f if line.strip()]



for url in rss_urls:
    print(f"URL du feed : {url}")
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print("Titre:", entry.get("title", "N/A"))
        print("Publication:", entry.get("published", "N/A"))
        print("URL:", entry.get("link", "N/A"))
        print("\n")


    