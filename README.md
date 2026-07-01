# Streamlit Tutorial — From Zero to Dashboard

A hands-on tutorial for building interactive data apps with Streamlit. Each section includes a minimal working example and a screenshot of what you'll see.

---

## Prerequisites

- Python 3.9+
- pip or conda

## Installation

```bash
pip install streamlit pandas plotly
```

Verify the install:

```bash
streamlit hello
```

---

## 1. Your First App

**File:** `01_hello.py`

```python
import streamlit as st

st.title("Hello Streamlit!")
st.write("This is your first interactive app.")
name = st.text_input("What's your name?", "World")
st.success(f"Hello, {name}! 👋")
```

**Run it:**
```bash
streamlit run 01_hello.py
```

![Hello App Screenshot](https://docs.streamlit.io/images/hero.png)

---

## 2. Layouts and Columns

**File:** `02_layout.py`

```python
import streamlit as st

st.title("Page Layout Demo")

col1, col2 = st.columns(2)

with col1:
    st.header("Inputs")
    age = st.slider("Age", 0, 100, 25)
    st.write(f"Selected: {age}")

with col2:
    st.header("Output")
    if age >= 18:
        st.success("You are an adult.")
    else:
        st.error("You are a minor.")
```

![Layout Demo](https://docs.streamlit.io/images/layouts.png)

---

## 3. Data Display

**File:** `03_data.py`

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("Working with Data")

# Generate sample data
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["Sales", "Profit", "Expenses"]
)

st.subheader("Raw Data")
st.dataframe(df, use_container_width=True)

st.subheader("Statistics")
st.bar_chart(df)

st.subheader("Highlight Max")
st.dataframe(df.style.highlight_max(axis=0))
```

![Data Display](https://docs.streamlit.io/images/dataframes.png)

---

## 4. Charts and Visualization

**File:** `04_charts.py`

```python
import streamlit as st
import plotly.express as px

st.title("Interactive Charts")

df = px.data.gapminder().query("year == 2007")

chart_type = st.selectbox("Chart Type", ["Scatter", "Bar", "Pie"])

if chart_type == "Scatter":
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", log_x=True)
elif chart_type == "Bar":
    fig = px.bar(df.sort_values("pop", ascending=False).head(10), x="country", y="pop", color="continent")
else:
    fig = px.pie(df, values="pop", names="continent")

st.plotly_chart(fig, use_container_width=True)
```

![Charts Demo](https://docs.streamlit.io/images/charts.png)

---

## 5. Session State & Interactivity

**File:** `05_state.py`

```python
import streamlit as st

st.title("Counter with Session State")

if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Increment"):
        st.session_state.count += 1

with col2:
    if st.button("➖ Decrement"):
        st.session_state.count -= 1

with col3:
    if st.button("🔄 Reset"):
        st.session_state.count = 0

st.metric("Current Count", st.session_state.count)

if st.session_state.count > 5:
    st.balloons()
```

![Session State](https://docs.streamlit.io/images/session_state.png)

---

## 6. File Upload & Model Prediction

**File:** `06_upload.py`

```python
import streamlit as st
import pandas as pd

st.title("Upload & Predict")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview:")
    st.dataframe(df.head())
    
    st.subheader("Quick Profile")
    st.write(df.describe())
    
    # Simulate prediction
    if st.button("Run Prediction"):
        with st.spinner("Processing..."):
            import time
            time.sleep(2)
        st.success("Prediction complete!")
        st.write("Results saved to output.")
```

![File Upload](https://docs.streamlit.io/images/file_uploader.png)

---

## 7. Sidebar Navigation

**File:** `07_sidebar.py`

```python
import streamlit as st

st.set_page_config(page_title="Multi-Page App", layout="wide")

with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Analytics", "Settings"])
    st.markdown("---")
    st.info("Tutorial v1.0")

if page == "Home":
    st.header("Welcome")
    st.write("Select a page from the sidebar.")
elif page == "Analytics":
    st.header("Analytics")
    st.line_chart({"Revenue": [100, 200, 300, 400, 500]})
else:
    st.header("Settings")
    theme = st.selectbox("Theme", ["Light", "Dark"])
    st.write(f"Selected theme: {theme}")
```

![Sidebar Navigation](https://docs.streamlit.io/images/sidebar.png)

---

## Project Structure

```
streamlit-tutorial/
├── 01_hello.py
├── 02_layout.py
├── 03_data.py
├── 04_charts.py
├── 05_state.py
├── 06_upload.py
├── 07_sidebar.py
├── requirements.txt
└── README.md
```

**`requirements.txt`**
```
streamlit>=1.35
pandas>=2.0
plotly>=5.20
numpy>=1.26
```

---

## Running the Tutorial

```bash
# Clone or create the project folder
cd streamlit-tutorial

# Install dependencies
pip install -r requirements.txt

# Run any example
streamlit run 01_hello.py
```

---

## Quick Reference Card

| Widget | Code Snippet |
|--------|-------------|
| Button | `st.button("Click me")` |
| Slider | `st.slider("Pick", 0, 100)` |
| Text Input | `st.text_input("Name")` |
| Selectbox | `st.selectbox("Pick", ["A", "B"])` |
| File Uploader | `st.file_uploader("Upload")` |
| Success | `st.success("Done!")` |
| Error | `st.error("Failed!")` |
| Spinner | `with st.spinner("Wait..."):` |
| Balloons | `st.balloons()` |

---

## Next Steps

- Explore [Streamlit Components](https://streamlit.io/components) for custom widgets
- Deploy with [Streamlit Community Cloud](https://streamlit.io/cloud) — it's free
- Add caching with `@st.cache_data` for large datasets

Happy building! 🎈
