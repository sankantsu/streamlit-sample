import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Write string
st.write("Hello, streamlit!")

# Generate random data
data = np.random.normal(size=10000)

# Plot
fig, ax = plt.subplots()
ax.hist(data)
ax.set_xlabel("Value")
ax.set_ylabel("Count")
st.pyplot(fig)

# Plot (Japanese label)
fig, ax = plt.subplots()
ax.hist(data)
ax.set_xlabel("値")
ax.set_ylabel("出現回数")
st.pyplot(fig)
