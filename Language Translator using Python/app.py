import streamlit as st
from textblob import TextBlob
# Başlık
st.title("Türkçe - Fransizca Dil Cevirmeni")

# Kullanıcıdan girdi alma
input_text = st.text_area("Türkçe Metni Girin: Python kullanarak Dil Çevirmeni")

if st.button("Çevir"):
    if input_text:
        try:
            # Metni çevirme
            b = TextBlob(input_text)
            translated_text = b.translate(from_lang='tr', to='fr')
            st.success("Fransizca Ceviri: " + str(translated_text))
        except Exception as e:
            st.error("Çeviri sırasında bir hata oluştu: " + str(e))
    else:
        st.warning("Lütfen bir metin girin.")

# yukaridaki kodu kullandim ve terminal ekraninda app.py klasörünü calistirdigimda 
# #asagidaki gibi ceviriler yapabildim