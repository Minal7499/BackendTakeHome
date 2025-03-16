import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[Dict[str, str]]:
    """Fetch research papers from PubMed API using a given query."""
    params = {"db": "pubmed", "term": query, "retmax": max_results, "retmode": "xml"}
    response = requests.get(PUBMED_SEARCH_URL, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    paper_ids = [id_elem.text for id_elem in root.findall(".//Id")]

    papers = get_paper_details(paper_ids)

    print("Fetched Papers:", papers)

    return papers


def get_paper_details(paper_ids: List[str]) -> List[Dict[str, str]]:
    """Retrieve paper details using PubMed IDs."""
    if not paper_ids:
        return []

    params = {"db": "pubmed", "id": ",".join(paper_ids), "retmode": "xml"}
    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.find(".//PMID").text
        title = article.find(".//ArticleTitle").text
        pub_date_elem = article.find(".//PubDate/Year")
        pub_date = pub_date_elem.text if pub_date_elem is not None else "Unknown"

        authors, affiliations, email = extract_authors_and_affiliations(article)

        papers.append({
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(authors),
            "Company Affiliation(s)": ", ".join(affiliations),
            "Corresponding Author Email": email or "N/A"
        })

    return papers

def extract_authors_and_affiliations(article) -> tuple[List[str], List[str], Optional[str]]:
    """Extract authors, affiliations, and email addresses."""
    authors, affiliations, email = [], [], None

    for author in article.findall(".//Author"):
        last_name = author.find("LastName")
        first_name = author.find("ForeName")
        full_name = f"{first_name.text} {last_name.text}" if first_name is not None and last_name is not None else "Unknown"

        affiliation_elem = author.find(".//Affiliation")
        if affiliation_elem is not None:
            affil_text = affiliation_elem.text.lower()
            if "university" not in affil_text and "lab" not in affil_text:
                authors.append(full_name)
                affiliations.append(affil_text)
                if "@" in affil_text:
                    email = affil_text

    return authors, affiliations, email
