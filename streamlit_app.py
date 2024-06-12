# Import libraries
import json
import streamlit as st
import streamlit.components.v1 as components

# Graphs
import plotly.graph_objects as go

# Libraries for ChatGPT
import os
from openai import OpenAI
import yaml

# set page layout to wide
try:
    st.set_page_config(layout="wide")
except:
    st.beta_set_page_config(layout="wide")


# Toast message
st.toast('Hi 👋 Welcome to my page')

# Heading title & image
st.title("ELINA VIGAND")
st.header("Data Science | Marketing Analytics | Project Management")
st.image("pictures/Banner-Elina-Vigand.png")

# About me block
st.markdown(
    """ 
#### Hi there 👋 My name is Elina Vigand

- 🔭 Marketing and Customer Analytics Project Manager with 10+ years of experience in B2B SaaS marketing.  
- 🏋️ Passionate about harnessing the power of data to drive strategic marketing decisions and enhance customer experiences.  
- 🌱 I recently completed Data Science bootcamp with Constructor Academy, where we covered:  
    * Python, Web Scraping, APIs  
    * Visualization (incl. Interactive) with Python, Plotly, Streamlit  
    * Machine Learning - scikit-learn, regression, anomaly detection, clustering, ensemble methods  
    * Deep Learning - Tensorflow, Keras, neural networks, CNNs, transfer learning, image segmentation, object detection  
    * Natural Language Processing - text classification, summarization, clustering and similarity, machine translation, sentiment analysis, search and information retrieval, parsing and named entity recognition, classical NLP and transformers  
- 👯 I’m looking to collaborate on interesting Data projects.  
- 💬 Ask me about Customer Segmentation and Marketing Strategies.  
- 📫 You can reach me on LinkedIn.  
- ⚡ Fun fact: I learn German by reading and listening to Harry Potter books.  
    """
    )

# Adding white space
st.markdown('###')

# Using Tabs

tab1, tab2, tab3 = st.tabs(["👩‍💻 Experience", "👩‍🎓 Courses", "🙋‍♀️ Volunteering"])

# Work Experience
tab1.write(
        """
        **DATA SCIENTIST CONSULTANT**  
        Nestle / Februar 2024 - April 2024\n  
        **MARKETING PROJECT MANAGER**   
        3DE Disain GmbH / July 2011 - December 2023\n
        **MARKETING CONSULTANT**   
        Fujitsu Estonia AG / October 2014 - October 2021\n
        """
        )

# Courses
tab2.write(
        """
        **Google Advanced Data Analytics Certificate**, Google \n
        **Programming for Data Analysis**, HarvardX\n
        **Agile Project Management**, Google\n
        **Customer Analytics**, The Wharton School\n
        **Introduction to Programming with Python**, HarvardX\n
        **Google Data Analytics Certificate**, Google\n
        """
        )

# Volunteering
tab3.write(
        """
        **Social Media Manager**, Zug International Women's Club (ZIWC)  
        - Leading social media engagement by creating impactful content and harmonising presence across platforms.  
        - Utilising data-driven strategies to optimise content and maximise impact. \n
        **Newsletter Editor & Graphic Designer**, International Men's Club of Zug   
        - Curating and designing quarterly Newsletters to maintain club's visual identity and promote events.  
        - Creating engaging marketing materials to showcase club's vibrant community.\n
        """
        )

# Adding white space between previous text and buttons
st.markdown('##')

# Layout with columns
col1, col2, col3 = st.columns([1, 1, 2])

# Buttons to download my CV and contact me
with col1:
    with open("pictures/Elina_Vigand_Resume.pdf", "rb") as file:
        btn1 = st.download_button(
            label="Download my CV",
            data=file,
            file_name="CV_ElinaVigand.pdf",
            mime="file/pdf"
          )
with col2:  
    btn2 = st.link_button(
            "Send me an email",
            "mailto:elinavigand@gmail.com"
          )


# Sidebar

# Contact me
st.sidebar.header("Contact me")
st.sidebar.markdown(
    """ 
    📧 elinavigand@gmail.com \n
    ☎️ +41 78 740 0536 \n
    🚀 linkedin.com/in/elinavigand
    """
    )

st.sidebar.divider()

# Education
st.sidebar.header("Education")
st.sidebar.markdown(
    """ 
    **Data Science Intensive Course**, Constructor Academy, Switzerland \n
    **BA in Product Design**, University of Tallinn, Estonia\n
    **BA in Business Administration and Marketing**, Estonian Business School, Estonia
    """
    )

st.sidebar.divider()

# Personal Skills
st.sidebar.header("Skills")
st.sidebar.markdown(
    """ 
✅ Data Analysis \n
✅ Data Science \n
✅ Project Management \n 
✅ Marketing \n 
✅ Programming: Python, SQL \n 
    """
    )

st.sidebar.divider()

# Languages
st.sidebar.header("Languages")
st.sidebar.markdown(
    """ 
    🇬🇧 English\n
    🇩🇪 German\n
    🇪🇪 Estonian
    """
    )

st.sidebar.divider()

# Adding white space between timeline and images
st.markdown('###')

# Chat
# Function to load the API key from a YAML file
# def load_api_key(filepath):
    # with open(filepath, 'r') as file:
        # config = yaml.safe_load(file)
        # return config['OPENAI_API_KEY']

# Load your OpenAI API key
OPENAI_API_KEY = ""

# Create an OpenAI client instance with your API key
client = OpenAI(api_key=OPENAI_API_KEY)

context = """
Hallo! 👋 Ich bin Robert, ein Neuntklässler an der Schule Oberägeri mit einer Leidenschaft für App-Entwicklung 📱.

Hier ist ein kurzer Überblick über mich:

* **Fähigkeiten & Interessen:**
    * Angestrebter App-Entwickler (ab August Praktikum bei Lonza AG!)
    * Geniesse Volleyball 🏐, Gitarre spielen 🎸, Anime, Manga und alles Japanische 🇯🇵
    * Fliessend in Englisch 🇬🇧, Deutsch 🇩🇪 und Schweizerdeutsch 🇨🇭 (lerne auch Französisch 🇫🇷!)
* **Akademische Leistungen:**
    * Gute Noten in Mathematik (Durchschnitt 4.5), Informatik (Durchschnitt 5.5+), und Englisch, Deutsch und Wissenschaft (Durchschnitt 5+)
    * Hohe Punktzahlen im Multicheck-Test (95% berufsspezifische Fähigkeiten, 88% Potenzial, 77% Schulwissen)
* **Erfahrung:**
    * Schnupperlehren in der App-Entwicklung bei mehreren Unternehmen (Lonza AG, Landis + Gyr AG, Roche AG, Business Systems Integration AG, Exanic AG) abgeschlossen
    * Plattformentwicklung bei Roche AG erkundet
* **Gemeinschaftliches Engagement:**
    * Aktiver Freiwilliger im Jugendzentrum in Ägeri, organisiere Veranstaltungen, helfe mit und vernetze mich mit Menschen 🤝
* **Kenntnisse & Erfahrungen:**
    * Programmiersprachen: Ich bin ziemlich gut in Python und kenne mich mit HTML und ein bisschen SQL aus.
    * Praktikum bei Lonza AG: Ich will so viel wie möglich lernen und dem Unternehmen helfen. Ich möchte schnell Programmierkenntnisse erwerben, um für das Team nützlich zu sein.
    * Schnupperlehre: Ich habe die Grundlagen von Python, SQL und HTML gelernt, was mir eine gute Grundlage gab.
    * Zukünftige Projekte: Ich bin mir noch nicht sicher, aber ich bin gespannt, an welchen Projekten ich in Zukunft arbeiten kann.
* **Interessen & Hobbys:**
    * Anime/Manga: Jujutsu Kaisen und Demon Slayer sind meine Favoriten. Ich mag die Action, die Charaktere und die gesamten Geschichten.
    * Volleyball & Gitarre: Ich habe mit Volleyball angefangen, nachdem ich den Anime Haikyuu!! gesehen hatte. Es sah nach viel Spaß aus, und das ist es auch! Ich habe angefangen Gitarre zu spielen, weil ich ein Instrument lernen wollte.
    * Japanische Kultur: Ich weiß noch nicht so viel über die japanische Kultur, aber ich bin daran interessiert, mehr zu erfahren.
* **Schule & Persönliche Entwicklung:**
    * Lieblingsfächer: Sport (macht einfach Spaß), Biologie (ist interessant), Geografie (ich mag die Themen) und Informatik (weil ich gerne programmiere und wir unsere Projekte selbst wählen können).
    * Ziele für die Zukunft: Ich möchte als App-Entwickler bei Lonza AG arbeiten.
    * Persönliche Eigenschaften: Ich denke, ich bin ein schneller Lerner und nehme gerne neue Herausforderungen an. Ich bin auch ein guter Teamplayer und immer bereit zu helfen.
"""

# Function to query OpenAI's GPT model
def query_gpt(question, context):
    prompt = f"{context}\n\nFrage: {question}\nAntwort:"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Du bist Robert, ein Neuntklässler an der Schule Oberägeri. Antworte immer basierend auf den folgenden Informationen:\n{context}\nAntworte immer auf Deutsch."},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    return response.choices[0].message.content

# Chat history stored in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat UI in the main page
st.markdown("""
#### Chat with me 💬

Ask questions about my skills, experiences or hobbies.

**Here's how you will get the best answers:**

* **Ask specific questions:**
    * "Which programming languages do you use?"
    * "What do you love about your work?"
    * "What are you favorite books?"
* **Be clear and specific:** This helps me to give relevant answers.
* **My answers are based on my personal knowledge and experience:** I will do my best to answer all of your questions about me.

Are you ready to chat? Ask your question. 
""")

def add_to_chat(author, message):
    # Prepend the new message to the beginning of the chat history
    st.session_state.chat_history.insert(0, f"{author}: {message}")

user_message = st.text_input("Your question:", key="user_query")

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    # Handling the chat interaction
    if st.button("Ask"):
        if user_message:
            # Add user message to chat
            add_to_chat("You", user_message)
            # Use the general summary for every query
            response = query_gpt(user_message, context)
            add_to_chat("Bot", response)
        else:
            st.warning("Please write your message.")
with col2:
    # Optionally, you might want to clear the chat
    if st.button("Clear"):
        st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    st.text(chat)
     
# Adding white space between timeline and images
st.markdown('###')

# Image Gallery

col1, col2 = st.columns(2)

with col1:
    st.image('pictures/IMG_3068.jpg')
    st.image('pictures/IMG_9354.jpg')


with col2:
    st.image('pictures/IMG_8926.jpg')
    st.image('pictures/IMG_3407.jpg')

# with col3:
    # st.image('pictures/IMG_9939.jpg')
    # st.image('pictures/IMG_9781.jpg')