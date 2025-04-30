import pandas as pd
import plotly.express as px

data = {
    "Job Role": ["Machine Learning Engineer", "Data Scientist", "AI Risk Analyst",
                 "Software Developer", "Mechanical Engineer", "Customer Service Rep"],
    "AI-Powered": ["Yes", "Yes", "Yes", "No", "No", "No"],
    "Average Salary ($)": [140000, 125000, 118000, 95000, 85000, 45000]
}

df = pd.DataFrame(data)

fig = px.bar(df, x="Job Role", y="Average Salary ($)", color="AI-Powered",
             title="AI vs. Non-AI Job Salaries in 2024",
             labels={"Job Role": "Career Path", "Average Salary ($)": "Annual Salary ($)"},
             barmode="group")

fig.show()
