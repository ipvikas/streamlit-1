# -*- coding: utf-8 -*-
"""streamlit_practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bvvqlkWYTGTyPXmo7GM9KfN29N_XeWE
"""

import streamlit as st
st.title("Start working with streamlit")


#1. Select slider
import streamlit as st

st.title("1. Streamlit Select Sliders")

st.subheader("1.a. Using a python list:")
temp_options = ['low', 'medium','high']
temp = st.select_slider("Choose a temperature", options=temp_options)
st.write("The temperature of this :fire: is:", temp)

st.subheader("1.b. Using a python range:")
my_range = range(1,21)
number = st.select_slider("Choose a number", options=my_range, value=10)
st.write('You chose %s hearts:' %number, number*":heart:")

#############################################3
# 1. Double ended slider
import streamlit as st

st.title("2. Streamlit Double Sliders")

st.subheader("2.a. Slider")
slider_range = st.slider("Double ended slider", value=[100,400])

st.info("Our slider range has type: %s" %type(slider_range))
st.write("Slider range:", slider_range, slider_range[0], slider_range[1])

st.subheader("2.b. Select Slider")
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
start_clr, end_clr = st.select_slider("Select a range of colors from the rainbow",
    options=rainbow, value=('orange','indigo'))

st.info("Our colours have types: %s" %type(start_clr))
st.write('You chose:', start_clr, "to", end_clr)
#####################################################################################

# #3 Radio button
import streamlit as st 

st.title("3. Making a Button")

result = st.button('Click Here')
st.write(result)

if result:
    st.write(":smile:")

##########################################
# 4 Checkbox
import streamlit as st

st.title("4. Making a Checkbox")

check = st.checkbox("Click here")
st.write('State of the checkbox:', check)

if check:
  st.write(":smile:"*12)

check_2 = st.checkbox("Uncheck to remove cake", value=True)
st.write("State of 2nd checkbox", check_2)

if check_2:
  st.write(":cake:"*102)

##################################################3
#5 Select from radio button

import streamlit as st

st.title("5. Make a Radio Button")

page_names = ['Checkbox', 'Button']

page = st.radio('Navigation', page_names, index=1)
st.write("**The variable 'page' returns:**", page)

if page == 'Checkbox':
  st.subheader('Welcome to the Checkbox page!')
  st.write("Nice to see you! :wave:")
else:
  st.subheader("Welcome to the Button page!")
  st.write(":thumbsup:")
   
   
###################################################
#6. ERROR

# import streamlit as st
# st.title("Streamlit Sliders”)
# st.subheader(“Slider 1:“)
# x = st.slider(‘A number between 0-100’, value=50) # defaults to 0-100
# st.write(“Slider number:“, x)
# st.subheader(“Slider 2:“)
# y = st.slider(‘Choose between 0-1 by 0.1’, min_value=0.0, max_value=1.0, step=0.1)
# st.write(“Slider number:“, y)

#####################################
#7 https://www.youtube.com/watch?v=EnXJBsCIl_A&list=PLgkF0qak9G4_SGe50HFNEGcpuGu0pNg0b&index=7
#Radio Buttons, Checkboxes and Buttons
# import streamlit as st

# st.title("Radio Buttons, Checkboxes and Buttons")

# page_names = ['Checkbox', 'Button']
# page = st.radio('Navigation', page_names)
# st.write("**The variable 'page' returns:**", page)

# if page == 'Checkbox':
#   st.subheader('Welcome to the Checkbox page!')
#   st.write("Nice to see you! :wave:")

#   check = st.checkbox("Click here")
#   st.write('State of the checkbox:', check)

#   if check:
#       nested_btn = st.button("Button nested in Checkbox")

#       if nested_btn:
#           st.write(":cake:"*20)
# else:
#   st.subheader("Welcome to the Button page!")
#   st.write(":thumbsup:")

#   result = st.button('Click Here')
#   st.write("State of button:",result)

#   if result:
#       nested_check = st.checkbox("Checkbox nested in Button")

#       if nested_check:
#           st.write(":heart:"*20)

#################################
#8
st.title('8: Add a text box')
tgt_text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
if st.button('Click on button'):
    if tgt_text == '':    
        st.write('Please enter text to get AI Reviews')
    else:
        st.write('', str(tgt_text))#for streamlit
        
        contentDF = tgt_text
        import pandas as pd
        dataframeFinal = pd.DataFrame(contentDF)
        csv = dataframeFinal.to_csv(index=True)
        st.download_button(label="Download CSV", data=csv,mime="text/csv",file_name="AIReviews.csv")
        
    if st.button('Clear output'):
        st.text_area.empty()
