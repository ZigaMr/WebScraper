# WebScraper
Python web scraper, built with selenium and beautifulSoup4.
Automatically detects Chrome installation and downloads the correct driver.

To run with poetry:
  - Make sure you have poetry installed (version 1.1.1)
  - Make sure you have python 3.8.0 set as global/local version (can use pyenv)
  - Clone everything and run "poetry config virtualenvs.create false && poetry install" to create new repository from existing pyproject.toml file
  - Now run "poetry run python scraper.py" or "poetry shell && python scraper.py"
  - Script takes a few seconds and returns parsed data from target website.

To run as Docker image:
  - Clone everything and make sure you have Docker installed
  - Uncomment line 60 in scraper.py to enable using standalone Chrome browser
  - sudo docker run -d -p 4444:4444 selenium/standalone-chrome  (This initializes chrome running in separate container)
  - sudo docker build --no-cache --network="host" -t <customImageName> . (Creates image from Dockerfile)

Repository also contains 2 tests in the test_scraper.py file. To test simply run "pytest" after enabling poetry environment (poetry shell && pytest).
  
