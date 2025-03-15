import argparse
import csv
import sys
from src.pubmed_fetcher import fetch_pubmed_papers

def save_to_csv(papers: list[dict], filename: str) -> None:
    """Save research papers to a CSV file."""
    fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(papers)

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename.")

    args = parser.parse_args()

    try:
        papers = fetch_pubmed_papers(args.query)
        if args.file:
            save_to_csv(papers, args.file)
            print(f"Results saved to {args.file}")
        else:
            for paper in papers:
                print(paper)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
