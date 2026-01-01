# Scraper for Google Scholar papers
from models.scholarScraper import ScholarScraper
# Calculation needed for information retrieval
from models.scholarComputation import ScholarComputation
# Library to process input and output format
import json

if __name__ == "__main__":
    scraper = ScholarScraper()
    scraper.request_scholar("Joko Siswantoro")
    papers = scraper.scrape_scholar_papers(5,output_format="dict")
    print(papers)

