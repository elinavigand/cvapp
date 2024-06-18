# Import libraries
import streamlit as st
import streamlit.components.v1 as components
import requests
import streamlit.components.v1 as components

# Graphs
import plotly.graph_objects as go

# Libraries for ChatGPT
import os
from openai import OpenAI

# set page title & layout
st.set_page_config(page_title='Elina Vigand Portfolio' ,layout="wide",page_icon='👩‍💻')

# -----------------  loading css  ----------------- #
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")



# Toast message
st.toast('Hi 👋 Welcome to my page')

# Heading title & image
st.title("ELINA VIGAND")
st.header("Data Science | Marketing Analytics | Project Management")
st.image("pictures/Banner-Elina-Vigand.jpg")

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
- 📫 You can reach me on [LinkedIn](https://www.linkedin.com/in/elinavigand/).  
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


# Projects
st.markdown("""
##            
## Projects 
""")

col1, col2 = st.columns(2)

with col1:
    st.image('pictures/project_nestle.jpg')
    st.markdown("""
        #### Unveiling Customer Thoughts  
        **Objective:**  Automate customer review analysis for Nestlé's product, generating deeper insights.  
        
        **Key Deliverables:**  
        - Data pipeline for efficient review collection and analysis.  
        - NLP-powered insights: sentiment, pro/con identification, topic modeling.  
        - Interactive Streamlit app for exploring trends, topics, and asking questions of a ChatGPT-powered assistant.
        """)
    st.markdown('##')
    st.image('pictures/project_bankA.jpg')
    st.markdown("""
        #### Customer Segmentation for Bank A  
        **Objective:**  Identify optimal customer segments based on purchasing behaviors for targeted marketing campaigns.
        
        **Key Deliverables:**  
        - Cluster analysis revealing three distinct customer segments: "Yuppies," "Conservatives," and "Core Base."  
        - Strategic recommendations for each segment, including credit limit adjustments, cross-selling, and personalized marketing.
        """)

with col2:
    st.image('pictures/project_migros.jpg')
    st.markdown("""
        #### Migros Store Challenge  
        **Objective:**  Identify the most promising location for new Migros store in Zürich.
        
        **Key Deliverables:**  
        - Interactive location recommender tool incorporating key performance indicators (KPIs). 
        - Weighted linear model allowing users to customize KPI importance.
        - Data-driven recommendations for specific Kreis locations.
        """)
    st.markdown('##')
    st.image('pictures/project_green_energy.jpg')
    st.markdown("""
        #### Clean Energy Sources in Switzerland  
        **Objective:**  Analyze Switzerland's renewable power plant data to identify the canton with the highest concentration of clean energy sources.
        
        **Key Deliverables:**  
        - Bar chart and interactive map displaying clean energy sources per canton.  
        - Streamlit app for interactive data exploration and insights.
        """)

# Sidebar

# Contact me
st.sidebar.header("Contact me")
st.sidebar.markdown(
    """ 
    📧 elinavigand@gmail.com \n
    ☎️ +41 78 740 0536 \n
    🚀 [linkedin.com/in/elinavigand](https://www.linkedin.com/in/elinavigand/)
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
Hi there! I'm Elina, a data analyst with a passion for uncovering insights from data and a recent graduate of the Constructor Academy Data Science Bootcamp.

Here's a quick snapshot of my background:

Skills & Interests:
- Data Analysis & Visualization
- Machine Learning
- Python
- SQL
- Hiking (Rigi & Stanserhorn are my favorites!)
- Working out (gym)
- Traveling (some cool places I've visited: Los Roques in Venzuela, Hong Kong, Haiti, Chernobyl, Bogota, Cuba)

Experience:
- **Data Science Bootcamp**: Completed an intensive program at Constructor Academy, where I gained expertise in Python, SQL, Machine Learning, and Natural Language Processing.
- **Nestlé Capstone Project**: Collaborated with a team to develop an automated data analysis pipeline for customer reviews, utilizing web scraping and NLP to uncover valuable insights.
- **Marketing Project Manager & Consultant**: 12+ years of experience leading marketing teams, analyzing data, and developing customer-centric strategies.

Languages:
- Fluent in Estonian, English, and German
- Basic level in Spanish and Russian

Education:
- BA in Product Design, University of Tallinn
- BA in Business Administration & Marketing, Estonian Business School

Favorite Books:
- All Harry Potter books
- All Auris audiobooks by Sebastian Fitzek
- Shoe Dog by Phil Knight
- The Graveyard Book by Neil Gaiman

Favorite Bodcasts:
- Smartless
- Conan O'Brien needs a friend
- The Tim Ferriss Show
- Marketing Against the Grain
- Deutschland 3000 - 'ne gute Stunde mit Eva Schulz

I'm eager to leverage my skills and experience to tackle new challenges in the field of data science. I'm a fast learner, a team player, and always ready to take on new challenges.
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
## Chat with me 💬

Ask questions about my skills, experiences or hobbies.

**Here's how you will get the best answers:**

* **Ask specific questions:**
    * "Which programming languages do you use?"
    * "What do you love about your work?"
    * "What are you favorite books/podcasts?"
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

col1, col2, col3 = st.columns(3)

with col1:
    st.image('pictures/ev1.jpg')
    st.image('pictures/ev4.jpg')


with col2:
    st.image('pictures/ev2.jpg')
    st.image('pictures/ev6.jpg')

with col3:
    st.image('pictures/ev3.jpg')
    st.image('pictures/ev5.jpg')