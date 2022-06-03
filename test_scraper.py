import pytest
from scraper import driver, create_driver_and_scrape


def test_url_error():
    #Test if scripts catches wrong URL error
    with pytest.raises(ValueError):
        data = create_driver_and_scrape(driver,
                                        'https://fin.capital/portfolio/wrongUrl',
                                        save_results=True)
def test_missing_values():
    # Test if any data is missing (title, urls...)
    data = create_driver_and_scrape(driver,
                                    'https://fin.capital/portfolio',
                                    save_results=True)
    assert len(data) == len(data.dropna())
