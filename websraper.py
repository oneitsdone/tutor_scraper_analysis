import streamlit as st

def main():
    st.set_page_config(page_title="Tutor Scraper", layout="wide")

    st.title("Tutor Scraper AI")

    control_col, results_col = st.columns([1, 3])

    subjects = [
    "Mathematics", "Algebra", "Geometry", "Trigonometry", "Precalculus",
    "Calculus", "Statistics", "Physics", "Chemistry", "Biology",
    "Environmental Science", "Computer Science", "Programming", "Data Science",
    "English", "Literature", "Writing", "Grammar",
    "History", "World History", "U.S. History", "Government", "Economics",
    "Psychology", "Sociology", "Philosophy",
    "SAT Prep", "ACT Prep", "GRE Prep", "GMAT Prep", "LSAT Prep", "MCAT Prep",
    "AP Calculus", "AP Biology", "AP Chemistry", "AP Physics", "AP U.S. History",
    "IB Math", "TOEFL Prep", "IELTS Prep",
    "Python", "Java", "C++", "JavaScript", "SQL",
    "Web Development", "Data Structures", "Algorithms",
    "Machine Learning", "Artificial Intelligence",
    "Cybersecurity", "Cloud Computing",
    "Spanish", "French", "German", "Mandarin Chinese",
    "Japanese", "Arabic", "Latin", "ESL",
    "Music Theory", "Piano", "Guitar",
    "Drawing", "Painting", "Graphic Design",
    "Public Speaking", "Study Skills", "Time Management"
]
    with control_col:
        st.header("select a website")
        website_1 = st.checkbox("Wyzant")
        website_2 = st.checkbox("Tutor.com")
        website_3 = st.checkbox("Varsity Tutors")
        subject_option = st.selectbox("Subject", sorted(subjects))
        location = st.text_input("Location")
        online_only = st.checkbox("Online Only")
        max_results = st.slider("Max Results", 10, 200, 50)
        scrape_button = st.button("Start Scraping")

    with results_col:
        st.subheader("Results", divider=True)
        results_placeholder = st.empty()

        if scrape_button:
            results_placeholder.write("Scraping in progress...")

if __name__ == "__main__":
    main()
