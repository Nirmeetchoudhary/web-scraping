# Web Scraping with BeautifulSoup

This project demonstrates a simple **web scraping script** in Python using **BeautifulSoup** and **requests** to extract data from a website and save it to a CSV file.

---

## 📝 Description

The script scrapes quotes and authors from the website [Quotes to Scrape](https://quotes.toscrape.com/) and saves the extracted data into a CSV file called `titles.csv`.  

It extracts:  
- **Authors** (`small` tags with class `"author"`)  
- **URLs** (`a` tags)  

The CSV file will have two columns: `Title` and `URL`.

---

## 💻 Technologies Used

- Python 3.x  
- BeautifulSoup (`bs4`)  
- Requests  
- CSV module (built-in)

---

## ⚡ How to Use

1. **Clone the repository:**

```bash
git clone https://github.com/Nirmeetchoudhary/web-scraping.git
cd web-scraping
