import feedparser
import asyncio
import aiohttp
import time

def load_feed(file):
    with open(file, 'r', encoding='utf-8') as f:
       return [line.strip() for line in f if line.strip()]

def load_keyword(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [mot.strip().lower() for mot in f if mot.strip()]

def write_result(file, result):
    with open(file, "w", encoding='utf-8') as f:
        f.write(result)
    

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            content = await response.text()
            feed = feedparser.parse(content)
            return feed.entries
    except Exception as e:
        print(f"Erreur pour :{url}, erreur: {e}")
        return []


async def main():
    result = ""
    mot_clef = load_keyword('mot-cle.txt')
    rss_urls = load_feed('rss_list.txt')

    async with aiohttp.ClientSession() as session:
        fetched_url = [fetch(session, url) for url in rss_urls]
        list_entries = await asyncio.gather(*fetched_url)

        for entries in list_entries:
            for entry in entries:
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

start = time.time()
asyncio.run(main())
end = time.time()

print(f"Temps final : {end - start:2f}")




    