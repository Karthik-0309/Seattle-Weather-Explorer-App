from preswald import connect, get_df, query, text, table, slider, plotly
import plotly.express as px

# Connect and load data
connect()
df = get_df("sample")

# Title and description
text("# Seattle Weather Explorer ☔️")
text("Interactively explore weather data using filters and visualizations.")

# Static query
sql = "SELECT * FROM sample WHERE precipitation > 5"
filtered_df = query(sql, "sample")
table(filtered_df, title="Days with Precipitation > 5mm")

# Interactive threshold using slider
threshold = slider("Precipitation Threshold", min_val=0, max_val=50, default=5)
table(df[df["precipitation"] > threshold], title=f"Days with Precipitation > {threshold}mm")

# Scatter plot of max vs. min temperature colored by weather type
fig = px.scatter(df, x="temp_max", y="temp_min", color="weather", title="Temperature Correlation")
plotly(fig)

from preswald import dropdown

weather_type = dropdown("Select Weather Type", options=df["weather"].unique().tolist(), default="rain")
filtered_weather_df = df[df["weather"] == weather_type]
table(filtered_weather_df, title=f"Weather Data for: {weather_type}")

from preswald import sidebar
sidebar()

fig_bar = px.bar(df.groupby("weather")["precipitation"].mean().reset_index(),
                 x="weather", y="precipitation",
                 title="Average Precipitation by Weather Type")
plotly(fig_bar)