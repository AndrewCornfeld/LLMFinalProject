import requests
from bs4 import BeautifulSoup
import csv

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        p_texts = [p.get_text(strip=True) for p in soup.find_all('p')]
        li_texts = [li.get_text(strip=True) for ul in soup.find_all('ul') for li in ul.find_all('li')]

        combined_text = ' '.join(p_texts + li_texts)
        return combined_text
    except Exception as e:
        print(f"Failed to extract from {url}: {e}")
        return ""

def extract_from_multiple_urls(urls, output_csv='2deep_output.csv'):
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'ExtractedText'])

        for url in urls:
            print(f"Processing {url}")
            text = extract_text_from_url(url)
            writer.writerow([url, text])

    print(f"All data saved to {output_csv}")

# Example usage
with open("links_2deep.txt", "r") as f:
    url_list = [line.strip() for line in f if line.strip()]

extract_from_multiple_urls(url_list)
