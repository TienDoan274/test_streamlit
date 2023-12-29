import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load sample data
data = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})

# Create a chart
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Display the chart in Streamlit app
st.pyplot(fig)
