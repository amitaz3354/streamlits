import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from textblob import TextBlob

def main():
    #scrape the shit

    def initialize_scraper():
        URL = "https://www.reuters.com/places/egypt"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup


    def scrape_the_mf_titles(soup):
        titles = soup.find_all(class_="story-title")
        titles_list = []
        for title in titles:
            titles_list.append(title.text.replace("\n","").replace("\t",""))
        return titles_list

    def scrape_the_mf_hyperlinks(soup):
        stories = soup.find_all("a",href=True)  
        hyperlinks = []
        for link in stories:
            hyperlinks.append(link.get("href"))
        return hyperlinks

    def create_the_mf_titles_columns(titles): 
        data = pd.DataFrame(data=titles, columns=["Title"])
        return data

    def calculate_sentiment_polarity(data):
        blob = TextBlob(data)
        return blob.sentiment.polarity

    
    st.title("demo data app")
    scraper = initialize_scraper()  
    data = [scrape_the_mf_titles(scraper),scrape_the_mf_hyperlinks(scraper)] 
    df = create_the_mf_titles_columns(data[0])

    df['links'] = pd.Series(data[1])
    df['polarity_score'] = df['Title'].apply(calculate_sentiment_polarity)

    st.write(df)

    


if __name__ == "__main__":
    main()     