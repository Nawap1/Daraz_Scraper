# Daraz Scraper and EDA

This project entails scraping product data from the Daraz e-commerce website, specifically focusing on phones available in Nepal. After scraping the data, exploratory data analysis (EDA) is performed on the dataset to gain insights into the sales trends and characteristics of phone brands.
Overview

The scraper utilizes Python libraries such as BeautifulSoup and Selenium to extract product information including product name, brand, price, number of ratings, and number of reviews. The extracted data is then saved into a CSV file for further analysis.
Prerequisites

To run the scraper and perform EDA, ensure you have the following dependencies installed:

    Python 3.x
    BeautifulSoup
    Selenium
    pandas

Install the required dependencies using pip:
```
pip install beautifulsoup4 selenium pandas
```
Additionally, you need to have the Chrome WebDriver installed and its path set in the system environment variables.
Usage

Clone or download the repository to your local machine.

Open the daraz_scraper.py file in your preferred code editor.

Adjust the pages_to_parse variable to specify the number of pages you want to scrape.

Run the script using the following command:
```
python daraz_scraper.py
```
Once the scraping process is complete, the dataset will be saved as Daraz_Phone_Dataset.csv in the same directory.

Use the generated CSV file for exploratory data analysis in your preferred environment (e.g., Jupyter Notebook, Google Colab).
