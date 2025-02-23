import streamlit as st  
from textblob import TextBlob  

st.title("Sentiment Analysis App 😊😠😐")  

# User input  
user_text = st.text_area("Enter your text:", "")  

if st.button("Analyze Sentiment"):  
    if user_text:  
        # Sentiment analysis  
        analysis = TextBlob(user_text)  
        sentiment = analysis.sentiment.polarity  

        # Determine sentiment  
        if sentiment > 0:  
            st.success("Positive 😊")  
        elif sentiment < 0:  
            st.error("Negative 😠")  
        else:  
            st.warning("Neutral 😐")  
    else:  
        st.warning("Please enter some text!")  
