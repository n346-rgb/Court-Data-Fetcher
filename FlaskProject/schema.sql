CREATE TABLE IF NOT EXISTS case_queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_type TEXT,
    case_number TEXT,
    filing_year TEXT,
    timestamp TEXT,
    raw_response TEXT
);
