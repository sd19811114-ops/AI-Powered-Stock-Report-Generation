# AI-Powered Stock Report Generation

A self-contained Python system for automated stock report generation, designed to:

- ingest historical index market data
- compute growth metrics, outperformance, and momentum indicators
- generate visual performance charts
- build an AI prompt context file for market research summary generation

## Features

- `master_engine.py`: end-to-end pipeline for data ingestion, analytics, visualization, and prompt generation
- `Yfinance.py`: alternate NSE index ingestion flow using `nselib`
- `requirements.txt`: dependency list for reproducible setup
- generated outputs:
  - `Simple_NSE_Market_Data.xlsx`
  - `Market_Growth_Performance_Chart.png`
  - `Automated_Market_Report_Prompt.txt`

## Installation

From the project root (`e:\Python Projects`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

Run the main pipeline:

```powershell
python master_engine.py
```

Expected outputs after execution:

- `Simple_NSE_Market_Data.xlsx` — Excel workbook with per-index analytics sheets
- `Market_Growth_Performance_Chart.png` — generated performance visualization
- `Automated_Market_Report_Prompt.txt` — structured prompt context for AI summary generation

## Notes

- `master_engine.py` is the primary entrypoint for the complete workflow.
- `Yfinance.py` is available as an alternate ingestion script and can be run independently.
- The project currently uses `yfinance`, `pandas`, `matplotlib`, `seaborn`, and `openpyxl`.

## GitHub Repository

This project has been deployed to:

- `https://github.com/sd19811114-ops/AI-Powered-Stock-Report-Generation`

## Repository Setup

If you need to reset or reconfigure the remote, run:

```powershell
git remote remove origin
git remote add origin https://github.com/sd19811114-ops/AI-Powered-Stock-Report-Generation.git
git push -u origin main --force
```

## Contribution

Feel free to add new ingestion sources, enhance the analytics layer, or connect the prompt output to an LLM-based report generation service.
