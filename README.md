# Backend Takehome Project  
This project fetches research papers from the PubMed API.  

# Get Papers List

This is a command-line program that fetches research papers from PubMed based on a user-specified query, filters them for non-academic authors affiliated with pharmaceutical/biotech companies, and outputs the results as a CSV file.

## Features
- Fetch papers from PubMed using its full query syntax.
- Identify non-academic authors and company affiliations.
- Export results to a CSV or print to console.

## Installation

1. Install Poetry (if not already installed):  
   `pip install poetry`
   
2. Install dependencies:
   ```bash
   poetry install
