import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
import spacy
from spacy import displacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")
import nltk
nltk.download('punkt')


def sentiment_analysis():
    st.title("Sentiment Analysis")
    st.subheader("Enter the text you'd like to analyze.")
    text = st.text_input('Enter text') #text is stored in this variable
    if st.button('Submit'):
        st.subheader("Text you entered : ")
        st.write(text)
        st.markdown("""---""")
        sents = sent_tokenize(text)
        entireText = TextBlob(text)
        sentScores = []
        for sent in sents:
            text1 = TextBlob(sent)
            score = text1.sentiment[0]
            sentScores.append(score)

        #Plotting sentiment scores per sentencein line graph
        st.subheader("Sentiment per sentence")
        st.line_chart(sentScores)
        st.markdown("""---""")

        #Polarity and Subjectivity of the entire text inputted
        sentimentTotal = entireText.sentiment
        st.write("The sentiment of the overall text : ")
        st.write(sentimentTotal)
    



def entity_extraction():
    st.title("Entity Extraction")
    st.subheader("Enter the text you'd like to analyze.")
    text = st.text_input('Enter text')
     #text is stored in this variable
    def entRecognizer(entDict, typeEnt):
        entList = [ent for ent in entDict if entDict[ent] == typeEnt]
        return entList
    entities = []
    entityLabels = []
    doc = nlp(text)
    for ent in doc.ents:
        entities.append(ent.text)
        entityLabels.append(ent.label_)
    entDict = dict(zip(entities, entityLabels)) #Creating dictionary with entity and entity types

    #Using function to create lists of entities of each type
    entOrg = entRecognizer(entDict, "ORG")
    entCardinal = entRecognizer(entDict, "CARDINAL")
    entPerson = entRecognizer(entDict, "PERSON")
    entDate = entRecognizer(entDict, "DATE")
    entGPE = entRecognizer(entDict, "GPE")

    #Displaying entities of each type
    if st.button('Submit'):
        st.subheader("Text you entered : ")
        st.write(text)
        st.markdown("""---""")
        st.subheader("Organizations")
        for item in entOrg:
            st.write(item)
        st.markdown("""---""")
        st.subheader("Cardinal")
        for item in entCardinal:
            st.write(item)
        st.markdown("""---""")
        st.subheader("Persons")
        for item in entPerson:
            st.write(item)
        st.markdown("""---""")
        st.subheader("Dates")
        for item in entDate:
            st.write(item)
        st.markdown("""---""")
        st.subheader("Locations")
        for item in entGPE:
            st.write(item)
        st.markdown("""---""")
