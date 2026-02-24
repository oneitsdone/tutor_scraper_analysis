import streamlit as st

def main():
    
    about_website = st.Page(page="mult_pages/about_website.py", 
                            title="About",
                              icon=":material/info:",
                              default=True)
    
    analytics_page = st.Page(page="mult_pages/analytics_page.py",
                             title="Analytics",
                             icon=":material/insert_chart:")
    
    webscraper = st.Page(page="mult_pages/webscraper.py",
                         title="Tutor Scraper",
                         icon=":material/data_exploration:")
    
    pg = st.navigation(pages=[about_website, webscraper, analytics_page])
    pg.run()

main()
