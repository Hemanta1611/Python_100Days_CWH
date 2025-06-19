import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from PIL import Image

st.title("Streamlit Widgets")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age: ", 0, 100, 25)

st.write(f"Your age is: {age}")