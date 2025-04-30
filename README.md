# ATCRiskMind: Air Traffic Controller Risk Assessment Platform

ATCRiskMind is a web platform for assessing the professional risk of air traffic controllers based on their mental health levels. The system evaluates mental health and fatigue indicators to provide a comprehensive risk assessment using fuzzy logic algorithms.

## Features

- Language localization support (English and Ukrainian)
- Interactive data visualization using ECharts
- Risk assessment algorithms based on fuzzy logic
- Ability to customize risk levels
- Real-time calculations and visualization updates

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/toleksandr/ATCRiskMind.git
   cd ATCRiskMind
   ```

2. Create and activate a virtual environment:
   ```bash
   # For Windows
   python -m venv env
   .\env\Scripts\activate

   # For macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
ATCRiskMind/
│
├── app.py                 # Main Flask application file
├── babel.cfg              # Babel configuration
├── requirements.txt       # Python dependencies
├── messages.pot           # Translation template
│
├── static/                # Static files
│   ├── styles.min.css     # Minimized CSS
│   └── scripts.min.js     # Minimized JavaScript
│
├── templates/             # HTML templates
│   └── index.html         # Main application template
│
└── translations/          # Translation files
    ├── en/               
    │   └── LC_MESSAGES/
    │       └── messages.po/mo
    └── uk/
        └── LC_MESSAGES/
            └── messages.po/mo
```

## Usage

1. Configure system parameters (number of air traffic controllers and time periods)
2. Use sample data or generate random data for testing
3. View fatigue and mental health indicators for each controller
4. Visualize risk levels through treemap diagrams
5. Adjust risk level thresholds using sliders

## Configuring Risk Levels

The application provides two range sliders for configuration:
- Expert conclusion levels (L1-L5)
- Linguistic risk levels (R1-R5)

## Data Storage

The application automatically saves your input data to your browser's local storage every 30 seconds and when you close the page. This data will be automatically loaded when you open the application again.