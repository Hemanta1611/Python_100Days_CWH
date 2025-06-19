import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from PIL import Image

st.title("Streamlit App")

st.write("Hello, World!")

# lets create a dataframe
df = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
st.dataframe(df)

st.line_chart(df)