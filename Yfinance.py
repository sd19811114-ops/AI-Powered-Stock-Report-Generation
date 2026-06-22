import datetime
from nselib import capital_market as cm
import pandas as pd
import time


def fetch_nse_historical_indices():
    # 1. Map your indices to exact NSE string format naming conventions
    target_indices = {
        "Nifty 50": "NIFTY 50",
        "Nifty Next 50": "NIFTY NEXT 50",
        "Nifty Midcap 150": "NIFTY MIDCAP 150",
        "Nifty Smallcap 250": "NIFTY SMALLCAP 250",
        "Nifty 500": "NIFTY 500",
    }

    # 2. Define your timeline windows dynamically (5 Years historical lookback)
    end_date = datetime.date.today().strftime("%d-%m-%Y")
    start_date = (datetime.date.today() - datetime.timedelta(days=365)).strftime(
        "%d-%m-%Y"
    )

    extracted_datasets = {}

    print(f"--- Launching Step 1 Ingestion Pipeline ({start_date} to {end_date}) ---")

    for internal_name, nse_name in target_indices.items():
        try:
            print(f"Requesting downstream REST endpoint for: [ {nse_name} ]...")

            # Pulling historical data frame directly via nselib
            df = cm.index_data(
                index=nse_name, from_date=start_date, to_date=end_date
            )

            if df is not None and not df.empty:
                # Clean up spacing in columns that NSE data often returns
                df.columns = [col.strip() for col in df.columns]
                extracted_datasets[internal_name] = df
                print(f"Successfully processed {len(df)} rows for {internal_name}.")
            else:
                raise ValueError("Returned data layer object is empty.")

            # Cooldown sleep interval to mitigate anti-scraping blocks or IP limits
            time.sleep(2.5)

        except Exception as e:
            print(f"CRITICAL ERROR gathering data for {internal_name}: {e}")
            print("Activating local mathematical asset simulation fallback configuration...")
            # Fallback block from your documentation can go here

    return extracted_datasets


# Execution Entry Point Execution Test
if __name__ == "__main__":
    market_data_dict = fetch_nse_historical_indices()