import streamlit as st 
import pandas as pd



st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg",width=465)
    
with col2:
    st.title(" Yaya Diallo ") 
    content = """
    
    Je suis un développeur passionné avec une expertise 
    particulière dans le domaine de l'analyse de données 
    en utilisant Python. Mon parcours professionnel m'a 
    permis d'acquérir une solide expérience dans 
    le développement web ainsi que dans l'exploitation et
    l'interprétation des données pour en extraire des insig
    """
    st.info(content)
    
content2 = """



Je suis disponible par email à yeleta.pro@gmail.com ou par téléphone au 778376970.


"""
st.write(content2) 


col3, col_empty, col4 = st.columns([1.5, 0.5 , 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3 :
    for index, row  in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row['image'])
        st.write(f"[Source Code]({row['url']})")
  


with col4 :
    for index,row in df[10:].iterrows():
        st.header(row["title"])  
        st.write(row["description"]) 
        st.image("images/"+ row['image'])  
        st.write(f"[Source Code]({row['url']})")  

