# <p align="center"> News Scrap </p>
<div align="center"> <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT license." /> <img src="https://img.shields.io/github/last-commit/mahendra-shah/news_scrapy?style=for-each-one&label=Last%20Commit" alt="Last Commit"> <img src="https://img.shields.io/github/stars/mahendra-shah/news_scrapy.svg?style=" />
<img src="https://img.shields.io/github/contributors/mahendra-shah/news_scrapy" alt="Contributors">
<img src="https://img.shields.io/github/forks/mahendra-shah/news_scrapy.svg?style">
<img src="https://img.shields.io/github/issues/mahendra-shah/news_scrapy.svg">
</div>
<hr>
<br>

## Description
This project is built using Python and the Scrapy framework to scrape news websites for the latest articles and news updates. The project extracts data from the news articles and stores them in a csv file for further analysis.


## Project Structure
``` r
    ├── spiders                           # Contains spiders
        ├── news.py                # Contains main logic of extracting data
    ├── LICENSE 
    ├── README.md                       # Documentation
    ├── items.py                            
    ├── middlewares.py                   
    ├── pipelines.py                    
    ├── settings.py                   # Configuration file for the Scrapy project.
```

## Installation
1. Clone the repository:
   ``` r
   git clone https://github.com/mahendra-shah/news_scrapy.git

2. Install the required dependencies:
    ``` r
      pip install -r requirements.txt
    ```

## Usage
- Navigate to the project directory.
- Run the following command to start the news scraping process:
   ``` r
    scrapy crawl news
   ```

## Contact
For any questions or feedback, feel free to contact the project owner at mahendra21@navgurukul.org.

