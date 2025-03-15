import requests
import logging
from typing import List, Dict

def fetch_papers(query: str) -> List[Dict]:
    """Fetch research papers from PubMed API."""
    url = f"https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/pubmed/?format=json&title={query}"
    response = requests.get(url)

    if response.status_code != 200:
        logging.error("Failed to fetch data from PubMed API")
        return []

    data = response.json()
    return parse_papers(data)

def parse_papers(data: Dict) -> List[Dict]:
    """Extracts required fields from API response."""
    papers = []
    for entry in data.get("records", []):
        papers.append({
            "PubmedID": entry.get("uid", "N/A"),
            "Title": entry.get("title", "Unknown"),
            "Publication Date": entry.get("pubdate", "Unknown"),
            "Authors": entry.get("authors", []),
            "Affiliations": entry.get("affiliations", []),
        })
    return papers
