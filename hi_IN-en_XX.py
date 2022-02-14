#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from transformers import MBartForConditionalGeneration, MBart50Tokenizer
import streamlit as st #for streamlit

@st.cache(allow_output_mutation=True, suppress_st_warning=True)#for streamlit
def download_model():
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50Tokenizer.from_pretrained(model_name)
    return model, tokenizer

st.title('ANY language to English Translator')#for streamlit
text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()#for streamlit

if st.button('Translate to English'):#for streamlit
    if text == '':#for streamlit
        st.write('Please enter Hindi text for translation') #for streamlit
    else: 
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "hi_IN"
        encoded_hindi_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_hindi_text, forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.write('', str(out).strip('][\''))#for streamlit
        ###
st.title('¿Quieres traducirlo al español?')#for streamlit
text = st.text_area("Enter English Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()#for streamlit

if st.button('Translate to Spanish'):#for streamlit
    if text == '':#for streamlit
        st.write('English text has been translated into Spanish') #for streamlit
    else: 
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "en_XX"
        encoded_hindi_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_hindi_text, forced_bos_token_id=tokenizer.lang_code_to_id["es_XX"])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.write('', str(out).strip('][\''))#for streamlit
        #####
st.title('Vous voulez le traduire en espagnol ?')#for streamlit
text = st.text_area("Enter French Text:", value='', height=None, max_chars=None, key=None)
model, tokenizer = download_model()#for streamlit

if st.button('Translate to French'):#for streamlit
    if text == '':#for streamlit
        st.write('English text has been translated into French') #for streamlit
    else: 
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer.src_lang = "en_XX"
        encoded_hindi_text = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(**encoded_hindi_text, forced_bos_token_id=tokenizer.lang_code_to_id["fr_XX"])
        out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        st.write('', str(out).strip('][\''))#for streamlit    
        
        
else: pass
