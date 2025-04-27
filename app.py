import streamlit as st
import asyncio
from scrapper_main import webScrapper
from IPython.display import Image as IPImage
import pandas as pd
from tabulate import tabulate

st.set_page_config(page_title="Web Scraper with LLM Extractor", layout="wide")
st.title("Web Scraper with LLM Extractor")
st.write("This tool allows you to scrape data from websites and summarize or extract information using powerful AI models.")
url = st.text_input("Enter the URL to scrape:", value="https://www.bbc.com/news")
default_instructions = f"""
Extract the main articles displayed on the homepage '{url}'.
Focus on items that look like news posts or blog entries.
Provide the title, full article URL, main image URL and a short excerpt for each.
"""
instructions = st.text_area("Extraction Instructions", value=default_instructions,height=150)
df=None
if st.button("Run Scraper"):
    with st.spinner("Scraping and processing with LLM..."):
        result, screenshot = asyncio.run(webScrapper(url, instructions))
    if screenshot:
        st.image(screenshot, caption="Screenshot of the scraped page", use_column_width=True)
    if result and result.article:
        df=pd.DataFrame([article.model_dump() for article in result.article])
    if df is not None:
        st.dataframe(df)
    else:
        st.warning("No articles found or an error occured during scraping.")