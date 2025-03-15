import argparse
import logging
from src.pubmed_fetcher import fetch_papers
from src.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed API.")
    parser.add_argument("query", type=str, help="Search query for PubMed API")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (CSV)", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    papers = fetch_papers(args.query)

    if args.file:
        save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
