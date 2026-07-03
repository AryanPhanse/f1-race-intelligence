# 🏎️ F1 Intelligence Platform

An end-to-end telemetry analytics and predictive ML platform for Formula 1 racing. This project automatically ingests F1 telemetry, stores it in a relational database, and provides advanced race strategy analytics and predictions.

## Current Tech Stack
- **Data Source:** FastF1 / Ergast APIs
- **Data Manipulation:** Pandas / NumPy
- **Environment:** Python (Virtual Environment)

---

## Local Environment Setup (Mac OS)

To run this project locally, you will need Python installed. We use a virtual environment to manage project-specific dependencies.

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/AryanPhanse/f1-race-intelligence.git
cd f1-race-intelligence
\`\`\`

### 2. Create and Activate the Virtual Environment
\`\`\`bash
python3 -m venv env
source env/bin/activate
\`\`\`

### 3. Install Core Dependencies
\`\`\`bash
pip install fastf1 pandas
\`\`\`

### 4. Run the API Test Script
To verify that the FastF1 connection is working and data caching is correctly configured, run the test script. This will download telemetry for the 2024 Monaco GP and print the finishing order.
\`\`\`bash
python test_api.py
\`\`\`

---

## 📅 Milestone Log

### Phase 1: Environment & Architecture Initialization
- **Status:** Completed ✅
- **Tasks Delivered:**
  - Initialized isolated Python virtual environment (`env`) on macOS.
  - Configured project-specific `.gitignore` rules to shield local development cache from version control.
  - Successfully fetched real-world Formula 1 telemetry via `FastF1` API integration testing.
  - Linked local development workspace to remote GitHub origin repository.