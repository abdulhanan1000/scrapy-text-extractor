# Scrapy Text Extractor

## Overview

The **GoogleSearchSpider** is a simple web scraper built using the Scrapy framework. This spider is designed to extract text from HTML tags such as `<h3>`, `<a>`, and `<span>` from a given web page. The extracted data is stored in a JSON file.

## Prerequisites

Before running the spider, ensure you have the following installed:

- Python 3.x
- Scrapy

If you don't have Scrapy installed, you can install it using pip:

```bash
pip install scrapy
```
## Getting Started

### 1. Clone the Repository (if applicable):
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Modify the Spider:
- Open the text_extractor.py file.
- In the start_requests method, replace the url variable with the URL of the web page you want to scrape.
```python
url = 'https://example.com'  # Replace with your target URL
```
### 3. Run the Spider:
To execute the spider and scrape the target website, use the following command:
```
scrapy runspider text_extractor.py
```

### 4. Output:

After running the spider, the extracted data will be saved in a file named output.json in the same directory as the spider script.

The structure of the output JSON will be as follows:

```json
{
    "headings": [
        "Heading 1",
        "Heading 2"
    ],
    "urls": [
        "https://example.com/page1",
        "https://example.com/page2"
    ],
    "spans": [
        "Text from span 1",
        "Text from span 2"
    ]
}
```

## Customization

- CSS Selectors: To extract data from different HTML tags, modify the CSS selectors in the parse method.

```python
headings = response.css('h3::text').getall()  # Modify for different tags
```
- Headers: The headers dictionary in the start_requests method contains the user-agent string. You can modify it to mimic a different browser or platform if needed.

