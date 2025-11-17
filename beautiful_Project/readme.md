
# 💻 Laptop Specification Scraper & Data Cleaner

## 📌 Overview

This project is a Python-based web scraping tool that collects laptop product information from an online source, cleans the extracted data (such as price and ratings), and exports the final, structured dataset into a CSV file.

the web source is url = https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_d08fde46-7480-41fb-aae3-1f0842940f31_1_X1NCR146KC29_MC.HJZ2651EEY8B&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_HJZ2651EEY8B&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=HJZ2651EEY8B


The workflow includes:

1. Web Scraping
2. Data Cleaning
3. CSV Export

---

## 📊 Output Data Structure

The result will be a CSV file with the following columns:

| # | Column | Final Data Type | Description                                           |
| - | ------ | --------------- | ----------------------------------------------------- |
| 0 | Title  | String          | Full product name/title                               |
| 1 | Price  | Integer         | Cleaned price value (without currency symbols/commas) |
| 2 | Rating | Float           | Cleaned rating value (ex: 4.5)                        |
| 3 | Link   | String          | Direct product page URL                               |

---

## ⚙️ Requirements

Ensure Python is installed along with the following libraries:

* `requests` – HTTP requests to fetch webpage data
* `beautifulsoup4` – HTML parsing
* `pandas` – Data cleaning and CSV exporting
* `numpy` – Required for numeric processing

Install using:

```bash
pip install requests beautifulsoup4 pandas numpy
```

---

## 🚀 Process Breakdown

### 1️⃣ Web Scraping

Uses `requests` to fetch page content and `BeautifulSoup` to extract data fields like:

* Title
* Price
* Rating
* Product Link

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# Target search URL
url = "https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_d08fde46-7480-41fb-aae3-1f0842940f31_1_X1NCR146KC29_MC.HJZ2651EEY8B&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_HJZ2651EEY8B&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=HJZ2651EEY8B"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Each product title is inside a specific class
titles = soup.find_all("div", class_="KzDlHZ")


print("Products found:")
for t in titles:
    print("-", t.text)

prices = soup.find_all("div", class_="Nx9bqj")   # price class
ratings = soup.find_all("div", class_="XQDdHH")  # rating class
links = soup.select("a.CGtC98")


print("Price found:")
for p in prices:
    print("-", p.text)
print("rating found:")
for r in ratings:
    print("-", r.text)
print("Link found:")
for l in links:
    print("-", l.text)

### 2️⃣ Data Cleaning (pandas)

✔ **Price Cleaning**

```python
df['Price'] = df['Price'].str.replace('₹', '', regex=False).str.replace(',', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').astype('Int64')
```

✔ **Rating Cleaning**

```python
df['Rating'] = df['Rating'].astype(str).str.extract(r'(\d+\.?\d*)')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
```

✔ **(Optional) Extract Base Model Name**

```python
df['Base_Model'] = df['Title'].str.split('-', expand=True, n=1)[0].strip()
```

### 3️⃣ Exporting to CSV

```python
df.to_csv('flipkart_laptops.csv', index=False, encoding='utf-8')
```

---


You will find `flipkart_laptops.csv` in the same directory once execution completes.

---

If you'd like, I can also:

✨ Add screenshots of output
✨ Add badges (Python version, license, stars, forks)
✨ Include a sample dataset preview
✨ Provide folder structure for the project

Would you like me to generate a GitHub-ready version with visuals and badges too?
