# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY* : CODTECH IT SOLUTIONS
*NAME* : SAKSHI KAILASH RAMTEKE
*INTERN ID* : CT4MTDF290
*DOMAIN* : PYTHON PROGRAMMING
*DURATION* : 16 WEEKS
*MENTOR* : NEELA SANTHOSH KUMAR

## 🔹 Objective
Fetch weather data from a public API and visualize it using Python libraries.

## 🔹 Tech Stack
- Python 3.10+
- Requests (API calls)
- Pandas (data handling)
- Matplotlib / Seaborn (plots)
- Streamlit (interactive dashboard)

## 🔹 Installation
```bash
git clone <repo-url>
cd codtech-task1
python -m venv venv
venv\Scripts\activate    # (Windows)
# OR
source venv/bin/activate # (Mac/Linux)
pip install -r requirements.txt
```

## 🔹 Run Command-line Script
```bash
python weather_api.py
```
- Prints forecast (first 5 rows)
- Saves outputs:
  - `outputs/forecast.csv`
  - `outputs/forecast_plot.png`

## 🔹 Run Dashboard (Streamlit)
```bash
streamlit run streamlit_app.py
```
Open browser: http://localhost:8501

## 🔹 Example Output
```
Fetching forecast (Mumbai by default)...

First 5 rows of forecast data:
                time  temperature_2m  relative_humidity_2m  windspeed_10m
2025-09-22 00:00:00            26.8                    88            4.3
2025-09-22 01:00:00            26.6                    89            4.1
2025-09-22 02:00:00            26.4                    90            3.8
2025-09-22 03:00:00            26.2                    91            3.5
2025-09-22 04:00:00            26.0                    92            3.3
```

## Output

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/0da03218-83e6-428e-a92a-a31f2d585766" />
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/3204e97d-c03b-4a07-afc4-be03171753c8" />
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/1be99188-2119-4e42-b1b9-252e41dea8d7" />
