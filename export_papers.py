import os
import csv
import requests

def fetch_papers(query):
    # Simulate fetching papers based on the query
    papers_data = [
        {'PubmedID': '40085945', 'Title': 'Endothelial cell activation...', 'Publication Date': '2025', 'Non-academic Author(s)': 'Paul Coleman, Mortimer Poncz', 'Company Affiliation(s)': 'centenary institute', 'Corresponding Author Email': 'N/A'},
        {'PubmedID': '40085436', 'Title': 'Health-related quality of life...', 'Publication Date': '2025', 'Non-academic Author(s)': 'Myung-Jae Hwang', 'Company Affiliation(s)': 'covid-19 vaccine injury compensation center', 'Corresponding Author Email': 'N/A'},
        # Add more papers here
    ]
    return papers_data

def export_to_csv(papers_data, filename="papers.csv"):
    """Write papers data to a CSV file and ensure it is created."""
    if not papers_data:
        print("⚠ No papers found. Skipping CSV creation.")
        return

    filepath = os.path.join(os.getcwd(), "papers.csv")  # Ensure correct path

    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)', 'Company Affiliation(s)', 'Corresponding Author Email'])
        writer.writeheader()
        writer.writerows(papers_data)

    print(f" Results written to: {filepath}")




def main(query):
    # Fetch papers based on the user query
    papers_data = fetch_papers(query)

    # Export fetched papers to CSV
    export_to_csv(papers_data)

    print(f"Results for query '{query}' have been written to CSV.")

# Example query
query = "Endothelial activation"
main(query)
