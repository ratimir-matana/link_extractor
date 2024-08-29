import requests
from bs4 import BeautifulSoup
import re

base_url = "https://t******s*****.com/?p="
start = 1000
end = 2000  # change as needed

seen_links = set()
counter = 1  # Initialize the counter

for i in range(start, end):
    url = f"{base_url}{i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if re.match(r'base_url\d+', href) and href not in seen_links:
            # Avoiding duplicate links
            seen_links.add(href)
            response_link = requests.get(href)
            soup_link = BeautifulSoup(response_link.text, 'html.parser')
            title = soup_link.find('h1', class_='entry-title')
            title_text = title.get_text(strip=True) if title else 'No title found'
            print(f"{counter}. {href} - {title_text}")  # Print the number, link, and title
            counter += 1  # Increment the counter
