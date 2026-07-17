# ScholarScraper

[![Project Status](https://img.shields.io/badge/Project%20status-Finished-green)](https://github.com/YourUsername/ScholarScraper)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)](#)

> Simple Scholar search engine from Google Scholar.

<!-- 
@import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false}
-->

<!-- code_chunk_output -->

- [ScholarScraper](#scholarscraper)
  - [Overview](#overview)
  - [Features](#features)
  - [How It Works](#how-it-works)
  - [Evaluating How Google Scholar's Work](#evaluating-how-google-scholars-work)
  - [Tech Stack](#tech-stack)
  - [Disclaimer](#disclaimer)

<!-- /code_chunk_output -->



## Overview

**ScholarScraper** is a lightweight Python-based tool designed to extract academic publication data directly from **Google Scholar**. It provides a simple interface to search for research papers, collect metadata such as titles, authors, publication years, citation counts, and links, and structure them into a usable format for analysis or integration into larger projects.

This project aims to simplify academic data collection for intelligent information retrieval final exams project in University of Surabaya

## Features

* **Wrtier-based search** – Enter any writer's papers from Google Scholar.
* **Topic-based search** – Enter any topic or keyword to retrieve relevant papers from Google Scholar.
* **Extract structured data** – Automatically fetch and organize paper details:
  * Title
  * Authors
  * Publication year
  * Citation count
  * Source link
* **Export capability** – Save extracted data into CSV or JSON formats for further processing.
* **Lightweight and fast** 

## How It Works

1. The user inputs a search query.
2. ScholarScraper sends a formatted request to Google Scholar’s search results page.
3. It parses the HTML using **Selenium** to extract structured data (titles, authors, citations, etc.).
4. Results are stored in a **Pandas DataFrame**, allowing easy export and analysis.

## Evaluating How Google Scholar's Work
Evaluating google scholar's web page and how the page work is crucial for automation information retrieval. The evaluation can be accessed [here](documentation/evaluate_web_page.md).

## Tech Stack

* **Python 3.13**
* **Selenium** – for dynamic content scraping
* **Pandas** – for data organization and export


## Disclaimer
> [!WARNING]
This tool is intended **for educational and research purposes only**.
Google Scholar does not provide an official public API, so excessive or automated requests may violate its terms of service. Please use responsibly.

