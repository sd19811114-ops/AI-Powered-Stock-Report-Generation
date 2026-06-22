# AI-Powered Automated Stock Report Generation System

A Python-based system for automated stock report generation, including data ingestion, growth metric processing, chart generation, and prompt creation for market research summaries.

## Project Contents

- `master_engine.py` — Main pipeline for ingesting market data, calculating metrics, generating charts, and writing prompt context.
- `Yfinance.py` — Alternate data ingestion script using `nselib` and NSE index data.
- `hello.py` — Sample script for project validation.
- `Automated_Market_Report_Prompt.txt` — Generated prompt context file for AI report generation.
- `Simple_NSE_Market_Data.xlsx` — Sample Excel output file.
- `Market_Growth_Performance_Chart.png` — Generated chart output.

## Setup

1. Create a Python virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Usage

Run the main report pipeline:

```powershell
python master_engine.py
```

After execution, the repository will contain:

- `Simple_NSE_Market_Data.xlsx`
- `Market_Growth_Performance_Chart.png`
- `Automated_Market_Report_Prompt.txt`

## Notes

- `master_engine.py` is the primary entrypoint.
- `Yfinance.py` provides an alternate ingestion method.
- Add a remote repository and push to GitHub after local commit.

## GitHub Deployment

1. Create a GitHub repository named `AI-Powered-Automated-Stock-Report-Generation-System`.
2. Add the remote URL:

```powershell
git remote add origin https://github.com/<your-username>/AI-Powered-Automated-Stock-Report-Generation-System.git
```

3. Push the code:

```powershell
git push -u origin main
```
