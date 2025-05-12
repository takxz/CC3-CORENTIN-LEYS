import feedparser

with open('rss_list.txt', 'r', encoding='utf-8') as f:
    rss_urls = [line.strip() for line in f if line.strip()]

def load_keyword(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [mot.strip().lower() for mot in f if mot.strip()]


def write_result(file, result):
    with open(file, "w", encoding='utf-8') as f:
        f.write(result)
    
result = ""

mot_clef = load_keyword('mot-cle.txt')


for url in rss_urls:
    print(f"URL du feed : {url}")
    feed = feedparser.parse(url)
    for entry in feed.entries:
        filtre = f"{entry.get('title', '')} {entry.get('summary', '')}".lower()
        for mot in mot_clef:
            if mot in filtre:
                title = entry.get("title", "N/A")
                date = entry.get("published", "N/A")
                url = entry.get("link", "N/A")
                print("Titre: ", title)
                print("Date de publication: ", date)
                print("URL:", url)
                print("mot clé correspondant:", mot)
                print("\n")
                result += f"Titre: {title} \n"
                result += f"Date: {date}\n"
                result += f"URL: {url}\n"
                result += f"mot-clé correspndant: {mot}\n"
                result += "------------------------\n"
            
write_result('resultat.txt', result)






    