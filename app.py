import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('Simple Matplotlib Streamlit App')

# Generate random data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure
fig, ax = plt.subplots()
ax.plot(x, y)

# Set plot labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Sine Wave')

# Display the plot
st.pyplot(fig)
