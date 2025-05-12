import feedparser


def parse_feed(url):
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title", "N/A"),
                "link": entry.get("link", "N/A"),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", "N/A")
            })
        return articles
    except Exception as e:
        print(f"[!] Erreur sur {url} : {e}")
        return []

# Exemple avec un mot-clé
keyword = "série"

with open('rss_list.txt', 'r', encoding='utf-8') as f:
    rss_urls = [line.strip() for line in f if line.strip()]

for url in rss_urls:
    print(f"Looking in {url}")
    articles = parse_feed(url)
    # Filtrage
    for article in articles:
        if keyword.lower() in article["title"].lower() or keyword.lower() in article["summary"].lower():
            print(f"{article['title']} ({article['published']})")
            print(f"🔗 {article['link']}")