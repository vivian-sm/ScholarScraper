# Project models
from models.scholarScraperConfig import ScholarScraperConfig
from models.scholarPaper import ScholarPaper

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ScholarScraper:
    __BASE_URL = "https://scholar.google.com/scholar?hl=en"

    def __init__(self, query: str = "", config: ScholarScraperConfig = None):
        self.config = config or ScholarScraperConfig()
        
        if self.config._is_verbose:
            print("Initializing ScholarScraper...")

        # Internal state
        self.__query = None
        self.__query_array = []
        self.__query_url = ""
        self.__search_url = ""

        # Init webdriver (ALWAYS)
        self.__webdriver = self._init_webdriver()

        if query:
            self.set_query(query)

    # -------------------- Getters --------------------
    def get_query(self):
        return self.__query

    def get_query_array(self):
        return self.__query_array

    def get_query_url(self):
        return self.__query_url

    def get_search_url(self):
        return self.__search_url

    # -------------------- Setters --------------------
    def set_query(self, query: str):
        if not query:
            raise ValueError("Query cannot be empty or None.")
        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        self.__query = query
        self.__query_array = query.split()
        self.__query_url = "+".join(self.__query_array)
        self._build_search_url()

    def _build_search_url(self):
        self.__search_url = f"{self.__BASE_URL}&q={self.__query_url}"

        if self.config._is_verbose:
            print("Search URL built:")
            print(self.__search_url)

    # -------------------- WebDriver --------------------
    def _init_webdriver(
        self
    ):
        if self.config._is_verbose:
            print("Initializing Selenium WebDriver...")
        return webdriver.Chrome(options=self.config.apply_to_chrome_options())

    def _close_webdriver(self):
        if self.config._is_verbose:
            print("Closing Selenium WebDriver...")
        if self.__webdriver:
            self.__webdriver.quit()

    # -------------------- Status Check --------------------
    def check_request_status(self):
        if self.config._is_verbose:
            print("Checking request status...")

        if not self.__webdriver.title:
            return False

        if "scholar.google.com" not in self.__webdriver.current_url:
            return False

        return True

    # -------------------- Scraping Logic --------------------
    def request_scholar(self, query: str):
        if self.config._is_verbose:
            print(f"Scraping Google Scholar for query: {query}")

        self.set_query(query)
        self.__webdriver.get(self.get_search_url())

        if not self.check_request_status():
            raise RuntimeError("Failed to access Google Scholar.")

        if self.config._is_verbose:
            print("Page loaded successfully.")
            print("Title:", self.__webdriver.title)

    def scrape_paper_authors(self, paper_node):
        try:
            authors_info = paper_node.find_element(By.CSS_SELECTOR, "div.gs_a").text
            authors = authors_info.split("-")[0].strip()
            return authors
        except Exception:
            return "Unknown"
        
    def scrape_scholar_papers(self, count=10,output_format="dict"):
        papers = []

        WebDriverWait(self.__webdriver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.gs_ri"))
        )

        results = self.__webdriver.find_elements(By.CSS_SELECTOR, "div.gs_ri")

        for node in results[:count]:
            title = node.find_element(By.CSS_SELECTOR, "a")
            title_result = title.text
            link_result = title.get_attribute("href")
            authors = self.scrape_paper_authors(node)
            description = node.find_element(By.CSS_SELECTOR, "div.gs_rs").text.strip()
            papers.append(ScholarPaper(title_result, link_result, description, authors))

        if output_format=="json":
            return [paper.to_json() for paper in papers]
        
        if output_format=="dict":
            return [paper.to_dict() for paper in papers]

