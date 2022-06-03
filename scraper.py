from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import logging

logging.basicConfig(filename='scraper.log', level=logging.INFO)


def create_driver_and_scrape(driver: webdriver.Chrome,
                             site_url: str = 'https://fin.capital/portfolio',
                             save_results: bool = True):
    """
    :param driver: Selenium Webdriver to use (default=Chrome)
    :param site_url: Target url to scrape (default=https://fin.capital/portfolio)
    :param save_results: Boolean, save results to csv.
    :return: None
    """
    # By default portfolio site lists all startups,
    # so no need to click "ALL"
    logging.info('Requesting site data')
    driver.get(site_url)
    if 'Page not found' in driver.title:
        raise ValueError('Wrong URL, ', site_url)
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    driver.quit()

    # Many different ways to scrape the same results,
    # this combination of tag+class seems the most robust.
    # Should work when additional startups are added.
    logging.info('Parsing html')
    titles = [title.find('span').text for title in soup.find_all("p", {"class": "expand_desktop"})]
    logo_urls = [img.find('img')['src'] for img in soup.find_all("div", {"class": "entry-image-ratio"})]
    startup_urls = [url.find('a')['href'] for url in soup.find_all("div", {"class": "entry-details"})]

    # assert len(titles) == len(logo_urls)
    # assert len(titles) == len(startup_urls)

    if save_results:
        logging.info('Saving data')
        # Create pandas df and save to file
        data = pd.DataFrame(data=list(zip(startup_urls, logo_urls, titles)),
                            columns=['startup_urls', 'logo_urls', 'titles'])
        data.to_csv('results.csv', index=False)
    return data


# Init webdriver object and set "headless" option
logging.info('Initializing webdriver')
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
site_url = 'https://fin.capital/portfolio'

if __name__ == '__main__':
    create_driver_and_scrape(driver,
                             site_url,
                             save_results=True)
