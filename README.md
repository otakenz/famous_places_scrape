# famous_places_scrape
# Project Title
Aim to build a database of famous places

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Pre-requisites
Things you need to install and how to install them

```
Python 3.+
Scrapy
```

### Installing for Windows
Python: [Python 3.+](https://www.python.org/downloads/). Select the python distribution for your machine and follow the installation guide there.

Scrapy: [Latest version](https://scrapy.org/). Follow the instruction there to download and install latest scrapy on your local machine.

## Running the tests
Summary: My goal for this repo is to scrape some data from a movie website using scrapy.

Webiste: [link](https://onlocationvacations.com/category/daily-filming-locations/). This is the root link for my test.

1, To get a copy of this repo, open terminal and navigate to a location and run:
```
git clone https://github.com/otakenz/famous_places_scrape.git
```
2, To check out the source code for web crawling and scraping, on terminal:
Navigate to the spider folder, it will look something like this
```
user//xxx/famous_place/famous_place/spider/
```
3, There you could see 2 output files in json format, namely famous_locations.json and famous_movies_and_location.json

4, If you wish to test the 2 python script, on the same path, run:
```
scrapy crawl filming_locations_spider
scrapy crawl locations_spider
```
5. If you wish to output it to json file, run
```
scrapy crawl filming_locations_spider -o YOUR_FILE_NAME.json
scrapy crawl locations_spider -o YOUR_FILE_NAME.json
```
Note: scrapy support other format such as xml and csv

filming_locations_spider is programmed to index all the website links on the target webpage

locations_spider is programmed to populate the database with country state, movie title and film location.

Note: Running step 4 will takes some time, if you wish to exit, simple press keyboard "ctrl + z"

## Resources
Scrapy documentation: [link](https://docs.scrapy.org/en/latest/intro/examples.html)
