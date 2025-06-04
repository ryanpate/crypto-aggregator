import json
import requests
import re

try:
    import feedparser
except ImportError:
    raise ImportError(
        "feedparser is required. Install with: pip install feedparser")

# HTML parsing
from bs4 import BeautifulSoup

# Selenium imports for dynamic HTML scraping
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False


def get_article_summary(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Try meta description first
        meta = soup.find('meta', attrs={'name': 'description'})
        if meta and meta.get('content'):
            return meta['content'].strip()
        # Fallback: first paragraph text
        p = soup.find('p')
        if p:
            return p.get_text(strip=True)
    except Exception:
        return ''
    return ''


# If you plan to use Selenium for sites with strict protections:
def get_soup_selenium(url):
    if not SELENIUM_AVAILABLE:
        raise RuntimeError(
            "Selenium is required for fetching this site. Install selenium and a webdriver.")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return BeautifulSoup(html, 'html.parser')


# Define RSS feed URLs for each site
rss_feeds = {
    'CoinDesk': 'https://www.coindesk.com/arc/outboundfeeds/rss/',
    'Cointelegraph': 'https://cointelegraph.com/rss',
    'CryptoSlate': 'https://cryptoslate.com/feed/',
    'NewsBTC': 'https://www.newsbtc.com/feed/',
    'Bitcoin Magazine': 'https://bitcoinmagazine.com/feed',
    'Decrypt': 'https://decrypt.co/feed',
    'CryptoBriefing': 'https://cryptobriefing.com/feed',
    'AMBcrypto': 'https://ambcrypto.com/feed'
}


def scrape_rss(name, url):
    # Use requests to fetch RSS feed with custom headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    feed = feedparser.parse(response.content)

    articles = []
    seen_titles = set()

    if not feed.entries or len(feed.entries) == 0:
        print(f"Warning: No entries found for {name} ({url})")
    for entry in feed.entries[:5]:
        title = entry.get('title', '').strip()
        link = entry.get('link', '').strip()
        # Skip duplicate titles
        if title in seen_titles:
            continue
        seen_titles.add(title)
        summary = entry.get('summary', '').strip() or entry.get('description', '').strip()
        # Remove "This post..." trailing sections, including any leading whitespace
        summary = re.sub(r'(?si)\s*This post.*', '', summary)
        summary = re.sub(r'(?si)\s*The post.*', '', summary)
        # Remove title and site name occurrences, trimming surrounding whitespace
        summary = re.sub(r'\s*' + re.escape(title) + r'\s*', ' ', summary)
        summary = re.sub(r'\s*' + re.escape(name) + r'\s*', ' ', summary)
        # Replace newline characters with a space
        summary = summary.replace('\r', ' ').replace('\n', ' ')
        # Collapse multiple whitespace into single space and trim edges
        summary = re.sub(r'\s+', ' ', summary).strip()

        if title and link:
            articles.append({'title': title, 'link': link, 'summary': summary})
    return articles


def scrape_all_sites():
    data = {}
    for name, rss_url in rss_feeds.items():
        try:
            articles = scrape_rss(name, rss_url)
            data[name] = articles
        except Exception as e:
            print(f"Error fetching RSS for {name}: {e}")
            data[name] = []
    return data


if __name__ == '__main__':
    crypto_data = scrape_all_sites()
    with open('./crypto-aggregator/data/crypto.json', 'w') as f:
        json.dump(crypto_data, f, indent=2)
    print("Scraping complete. Data saved to crypto.json")
