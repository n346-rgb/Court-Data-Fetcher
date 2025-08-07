
from flask import Flask, render_template, request
from playwright.sync_api import sync_playwright
import sqlite3
import datetime
import os

app = Flask(__name__)

# Initialize database from schema.sql
def init_db():
    conn = sqlite3.connect("queries.db")
    cursor = conn.cursor()
    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

# Log query to database
def log_query(case_type, case_number, filing_year, raw_response):
    conn = sqlite3.connect("queries.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO case_queries (case_type, case_number, filing_year, timestamp, raw_response)
        VALUES (?, ?, ?, ?, ?);
    """, (case_type, case_number, filing_year, datetime.datetime.now().isoformat(), raw_response))
    conn.commit()
    conn.close()

# Scrape court data using Playwright
def fetch_case_data(case_type, case_number, filing_year):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto("https://services.ecourts.gov.in/ecourtindia_v6/")
            # Replace with actual selectors
            page.fill("#case_type_input", case_type)
            page.fill("#case_number_input", case_number)
            page.fill("#filing_year_input", filing_year)
            page.click("#search_button")
        except Exception as e:
            browser.close()
            raise RuntimeError("Could not complete search. Check input selectors.") from e

        page.wait_for_timeout(3000)
        html = page.content()

        data = {
            "parties": "John Doe vs State",  # Placeholder
            "filing_date": "12-Jan-2023",
            "next_hearing": "15-Sep-2025",
            "pdf_link": "https://example.com/latest_order.pdf",
            "raw_html": html
        }

        browser.close()
        return data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fetch", methods=["POST"])
def fetch():
    try:
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        filing_year = request.form["filing_year"]

        data = fetch_case_data(case_type, case_number, filing_year)
        log_query(case_type, case_number, filing_year, data["raw_html"])

        return render_template("case_details.html",
            parties=data["parties"],
            filing_date=data["filing_date"],
            next_hearing=data["next_hearing"],
            pdf_link=data["pdf_link"]
        )
    except Exception as e:
        return render_template("error.html", error=str(e))

# Run the Flask app
if __name__ == "__main__":
    if not os.path.exists("queries.db"):
        init_db()
    app.run(debug=True)

