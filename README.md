Author: Travis Slade
Date: May 19th, 2025

# 🎳 Bowling Ball Web Scraper

This Python project scrapes bowling ball product listings from [BowlersMart.com](https://www.bowlersmart.com), including product titles, links, images, and pricing (original and discounted). It supports pagination and outputs the results to a CSV file.

---

## 🔍 Features

- Scrapes all bowling ball products from paginated product listings
- Extracts:
  - Product title
  - Product page URL
  - Product image URL
  - Original price (if available)
  - Discounted price (if available)
- Saves all data to a `bowling_balls.csv` file
- Written in lightweight Python using `requests`, `BeautifulSoup`, and `pandas`

---

## 📦 Requirements

- Python 3.7+
- Required packages (install with pip):

```bash
pip install requests beautifulsoup4 pandas
