💻 Laptop Specification Scraper and Data Cleaner

Project Overview

This project is a Python-based web scraper designed to extract product data (Laptops, in this case) from a web source, clean the extracted string-based data (like price and rating), and export the final, structured dataset into a clean CSV file.

Target Data Structure
the web source is url = https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_d08fde46-7480-41fb-aae3-1f0842940f31_1_X1NCR146KC29_MC.HJZ2651EEY8B&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_HJZ2651EEY8B&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=HJZ2651EEY8B


The resulting CSV file will contain four columns with the following final data types:

#

Column

Final Data Type

Description

0

Title

object (String)

The full product name/title.

1

Price

int (Integer)

The cleaned numerical price (currency symbols and commas removed).

2

Rating

float (Float)

The cleaned numerical rating (e.g., 4.5 instead of '4.5 out of 5').

3

Link

object (String)

The direct URL to the product page.

⚙️ Prerequisites

To run this project, you need Python installed, along with the following libraries:

requests (for making HTTP requests to the target website)

beautifulsoup4 (for parsing HTML content)

pandas (for data cleaning and CSV export)

numpy (often used alongside pandas)

You can install these dependencies using pip:

pip install requests beautifulsoup4 pandas numpy


🚀 Web Scraping Steps

The entire workflow consists of three main stages: Scraping, Cleaning, and Exporting.

1. Web Scraping (Using requests and BeautifulSoup)

This stage involves fetching the HTML content and extracting the required elements (Title, Price, Rating, and Link) using CSS selectors or XPath expressions specific to the target website.

Key operations:

Send a GET request to the target URL.

Parse the response HTML using BeautifulSoup.

Iterate through the product containers and extract the text and attributes (like the href for the link).

2. Data Cleaning and Transformation (Using pandas)

This is the critical step to ensure Price and Rating are converted to numerical types for accurate analysis.

A. Cleaning the Price Column

The initial price is a string (e.g., '₹20,990'). This must be converted to an integer.

# 1. Remove the currency symbol ('₹') and commas (',')
df['Price'] = df['Price'].str.replace('₹', '', regex=False).str.replace(',', '', regex=False)

# 2. Convert the cleaned string to a numeric integer type
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').astype('Int64') 
# Use 'Int64' to allow for NaN values if needed


B. Cleaning the Rating Column

The rating may contain text (e.g., '4.5 out of 5'). This needs to be isolated and converted to a float.

# 1. Extract the numeric part (e.g., '4.5' from '4.5 out of 5') using a regex
df['Rating'] = df['Rating'].astype(str).str.extract('(\d+\.?\d*)')

# 2. Convert to a float type
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')


C. Splitting the Title (Optional but Recommended)

As discussed, you can split the complex title strings to isolate the base product name:

# Create a new column 'Base_Model' containing only the text before the first hyphen
df['Base_Model'] = df['Title'].str.split('-', expand=True, n=1)[0].str.strip()


3. Export to CSV

Finally, use the .to_csv() method to save the cleaned DataFrame to a file. Always use index=False to prevent saving the internal pandas row index.

# Export the final, cleaned DataFrame to a CSV file
df.to_csv('cleaned_product_data.csv', index=False, encoding='utf-8')


💡 How to Run the Project

Clone this repository:

git clone [YOUR_REPO_URL]
cd [YOUR_REPO_NAME]


Install dependencies (see Prerequisites).

Execute the main scraping script:

python scrape_data.py # Or whatever your main script is named


The final output file, cleaned_product_data.csv, will be generated in the root directory.
