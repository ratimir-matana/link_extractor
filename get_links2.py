from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import re


def get_filtered_links(base_url):
    # Set up Firefox options
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Run in headless mode (no UI)

    # Set up the WebDriver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        # Open the URL
        driver.get(base_url)

        # Extract all anchor tags with 'href' attributes
        links = driver.find_elements(By.XPATH, "//a[@href]")
        print(f"Found {len(links)} links")  # Debug statement

        # Extract and resolve the full URLs, then filter them
        urls = set()  # Use a set to avoid duplicates
        pattern = re.compile(r'^/p/.*\.html$', re.IGNORECASE)

        for link in links:
            href = link.get_attribute('href')
            if pattern.match(link.get_attribute('href')):
                urls.add(href)
                print(f"Matched URL: {href}")  # Debug statement

    finally:
        driver.quit()  # Make sure to close the WebDriver

    return sorted(urls)  # Return sorted for consistency


def main():
    # Define the base URL
    base_url = 'https://www.xyz'

    # Get all filtered links from the page
    links = get_filtered_links(base_url)

    # Print the links
    for link in links:
        print(link)


if __name__ == '__main__':
    main()
