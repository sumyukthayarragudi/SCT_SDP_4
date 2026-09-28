# Product Web Scraper

## About

This project is a simple Python web scraper that collects product information from an online website. It extracts the product name, price, and rating and saves the collected information into a CSV file.

I created this project to understand the basics of web scraping and to practice working with Python libraries like Requests and BeautifulSoup.

## What It Does

* Collects product information from the website
* Extracts product names
* Extracts product prices
* Extracts product ratings
* Scrapes products from multiple pages
* Saves the collected information in a CSV file

## Technologies Used

* Python
* Requests
* BeautifulSoup
* CSV

## About BeautifulSoup

BeautifulSoup is a Python library used to read and extract information from HTML webpages. In this project, it is used to find the product names, prices, and ratings from the webpage.

## Website Used

This project uses **Books to Scrape**, an existing website designed for practicing web scraping. The scraper collects the product names, prices, and ratings available on the website and stores them in a CSV file.

## How It Works

1. The program sends a request to the website.
2. The webpage content is received using the Requests library.
3. BeautifulSoup reads the HTML content.
4. The scraper finds the product name, price, and rating.
5. It repeats the process for multiple pages.
6. The collected information is saved in `products.csv`.

## How to Run

First, install the required libraries:

```bash
pip install requests beautifulsoup4
```

Then run the Python file:

```bash
python scraper.py
```

After running the program, the extracted information will be saved in `products.csv`.

## Output

The `products.csv` file contains the following information:

* Product Name
* Price
* Rating

Example:

```text
Product Name,Price,Rating
A Light in the Attic,£51.77,Three
Tipping the Velvet,£53.74,One
Soumission,£50.10,One
```

## Project Structure

```text
ProductWebScraper/
├── scraper.py
├── products.csv
└── README.md
```

