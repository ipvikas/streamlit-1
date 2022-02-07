# -*- coding: utf-8 -*-
"""OCR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YnDZ5ZaaYB6QD24GOX9tcIrjXIeu9Ypl
"""

# !pip uninstall googletrans
# !pip install googletrans==3.1.0a0

import streamlit as st
@st.cache(allow_output_mutation=True, suppress_st_warning=True)

st.title('OCR_Image_to_Text')


# from google.colab import drive
# drive.mount('/content/drive')
# # path = '/content/drive/My Drive/Colab Notebooks/Projects/OCR_Project/english.png'
# path = '/content/drive/My Drive/Colab Notebooks/Parag_Letter.jfif'
# open(path,mode ='r')
path = st.file_uploader("Choose a file")
if path is not None:
    # To read file as bytes:
    bytes_data = path.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(path.getvalue().decode("utf-8"))
    st.write(stringio)
    
    
    

#      # To read file as string:
#      string_data = stringio.read()
#      st.write(string_data)

#      # Can be used wherever a "file-like" object is accepted:
#      dataframe = pd.read_csv(uploaded_file)
#      st.write(dataframe)





import PIL
from PIL import ImageDraw
im = PIL.Image.open(path)
im

# !pip uninstall opencv-python-headless==4.5.5.62

# !pip install opencv-python-headless==4.5.2.52

# !pip install easyocr
#change run type to GPU
# !pip install googletrans
from googletrans import Translator

import easyocr
reader = easyocr.Reader(['en']) #IMP 'hi'
translator = Translator()
bounds = reader.readtext(path,add_margin = 0.1,width_ths=0.5, link_threshold=0.4,decoder='beamsearch', blocklist='=-' )
bounds



def draw_boxes(image,bounds,color= 'yellow',width =2):
  draw = ImageDraw.Draw(image)
  for bound in bounds:
    p0,p1,p2,p3=bound[0]
    draw.line([*p0,*p1,*p2,*p3,*p0], fill = color, width = width)
  return image

# draw_boxes(im, bounds)

text_list = reader.readtext(path,add_margin = 0.55,width_ths=0.7, link_threshold=0.8,decoder='beamsearch', blocklist='=-',detail = 0 )
# print(text_list)

text_comb =' '.join(text_list) #changed into a single line
# print(text_comb)
text_comb

# %cd '/content/drive/My Drive/Colab Notebooks/'
# fhand = open('OCR_Output.txt','w')
# fhand.write(text_comb) # Erass all, already writtena and write what has been passed
# fhand.close()
