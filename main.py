import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage

from pages import poxAnalysis
# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('cover.png')
display = np.array(display)
st.image(display)
st.title("Monkey Pox Disease Detection")
st.text("Pox (Affected Or Not) : To detect chances of MonkeyPox, Measles and ChickenPox")



# Add all your application here
app.add_page("Pox Analysis", poxAnalysis.app)



# The main app
app.run()
