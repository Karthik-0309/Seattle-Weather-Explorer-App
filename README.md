# 🌧️ Seattle Weather Explorer

**Seattle Weather Explorer** is a lightweight, interactive data visualization dashboard built using [Preswald](https://preswald.com/). It helps users analyze historical weather data in Seattle through customizable queries and dynamic visual elements powered by Plotly. This project is ideal for learning about data storytelling, dashboard creation, and integrating SQL logic into visual interfaces.

---

## 📌 Use Case

Imagine a weather research team or data journalism organization wants to explore weather trends—such as heavy rainfall or high-temperature fluctuations—in Seattle. Rather than manually filtering spreadsheets or building complex dashboards, they can use this app to:

- Instantly visualize heavy rainfall days
- Adjust sliders to filter by temperature thresholds
- Query specific weather conditions using SQL
- Share the dashboard with stakeholders who don't know SQL or Python

This project demonstrates how non-technical users can interact with data using a no-code UI powered by Preswald and Python.

---

## 🔍 Key Features

- ✅ No-code/low-code interactive dashboard
- 📈 Visualizations built using Plotly (bar charts, scatter plots)
- 🎯 Filter and explore data with sliders and SQL queries
- 🗄️ Easily configurable data pipeline with `preswald.toml`
- 🔐 Secure credential management with `secrets.toml`
- 🧩 Extendable: Add more datasets or charts in minutes

---

## 🧱 Project Structure

```
Project/
├── hello.py             # Main Preswald app with logic, UI, and SQL queries
├── preswald.toml        # Data source configuration
├── secrets.toml         # Sensitive secrets (excluded via .gitignore)
├── pyproject.toml       # Project dependencies and environment
├── images/
│   ├── logo.png         # Dashboard logo
│   └── favicon.ico      # Browser tab icon
├── data/
│   ├── sample.csv       # Main dataset (Seattle weather)
│   └── cloudy.png       # Optional image for chart UI
├── .gitignore           # Ignore secret/config files
└── README.md            # Full documentation
```

---

## 📥 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/seattle-weather-explorer.git
cd seattle-weather-explorer/Project
```

### 2. Install Python & Preswald

Ensure you have Python 3.8+ and install Preswald CLI:

```bash
pip install preswald
```

### 3. Configure Files

#### 📄 `preswald.toml`
Define your dataset(s):

```toml
[[datasources]]
name = "sample"
path = "data/sample.csv"
```

#### 🔐 `secrets.toml`
Store any credentials (database keys, API tokens). Example:

```toml
[default]
weather_api_key = "YOUR_SECRET_API_KEY"
```

> ⚠️ This file is ignored via `.gitignore` for security.

---

## 🚀 Running the Application

Launch the app in your browser with:

```bash
preswald run hello.py
```

You’ll be directed to: [http://localhost:3000](http://localhost:3000)

---

## 🧠 How It Works

### `hello.py`

This is the main application script:

- Loads data from `sample.csv` using `get_df`
- Displays title and description
- Executes a static SQL query to show rainy days:
  ```sql
  SELECT * FROM sample WHERE precipitation > 5
  ```
- Allows interactive temperature filtering with `slider`
- Visualizes with `plotly.express` based on user input

---

## 📊 Sample Visualization

Once running, you’ll see:

- A table showing days with precipitation > 5mm
- A slider to select minimum precipitation
- An interactive bar chart of precipitation per day

> Want to visualize temperature ranges instead? Just modify the SQL and slider logic inside `hello.py`.

---

## 📈 Dataset Details

File: `data/sample.csv`  
Sample columns:

| date       | precipitation | temp_max | temp_min | wind | weather     |
|------------|----------------|----------|----------|------|-------------|
| 2012-01-01 | 0.0            | 12       | 3        | 4.7  | drizzle     |
| 2012-01-02 | 10.2           | 8        | 2        | 5.1  | rain-showers|

---

## 🔧 Customization Tips

- 🆕 Add new data: update `preswald.toml` with another dataset path
- 📐 Modify UI: edit `hello.py` to include new charts or components
- 🔄 Replace CSV with a database: Preswald supports PostgreSQL, MySQL, etc.

---

## 🔐 Security & Secrets

- Secrets are stored in `secrets.toml`
- This file is ignored by Git
- Keep API keys or passwords safe here

---

## 👩‍💻 Author

Created by **Karthik Kashyap**  
