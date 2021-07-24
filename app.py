import streamlit as st 
from yolo import detect_objects, face_main, object_main
from nlp import sentiment_analysis, entity_extraction

def main():
    # Render the readme as markdown using st.markdown.
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url('https://unsplash.com/photos/ZiQkhI7417A');
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    hide_streamlit_style = """
    
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>

    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Show Instructions", "Object Detection","Face Detection",'Sentiment Analysis', 'Entity Extraction', "About Us"])
    if app_mode == "Show Instructions":
        st.sidebar.success('To continue select an option.')
        st.title("instructions")
        st.subheader("Welcome to ML-HUB! Here is how to use our app! :nerd_face: ")
        st.write("We offer following services : ")
        st.write("  - Face  Detection")
        st.write("  - Object Detection")
        st.write("  - Sentiment Analysis")
        st.write("  - Entity Extraction")
        st.markdown("""---""")
        st.header("Face Detection")
        st.write("businesses don't have to spend fortunes to detect faces anymore. Just drag and drop images into our custom model and you'll know if a person exists in the photo. Video support is planned in the future to let you install our models in smart door bells or CCTVs. Possibilities are endless!")
        st.write("Please select 'Face Detection' from the sidebar to continue")
        st.markdown("""---""")
        st.header("Object Detection")
        st.write("Based on the same YOLO model, our object detection model can help you identify objects from 80 different categories. Be it toothbrush or pizza, carrot or broccoli, we can detect it!")
        st.write("Please select 'Object Detection' from the sidebar to continue")
        st.markdown("""---""")
        st.header("Sentiment Analysis")
        st.write("The world is now disturbed by emergence of fake news and hate speech. Our model, based on NLTK library can help you detect if a paragraph of text is positive speech or hate speech. It can also separate facts from fake news!")
        st.write("Please select 'Sentiment Analysis' from the sidebar to continue")
        st.markdown("""---""")
        st.header("Entity Extraction")
        st.write("We provide entity extraction exclusively for our fellow data miners. We get how hard it is to clean raw data. Deep learning to the rescue! Our model is capable of scraping dates, names, organizations, numbers and locations from pile of data. It's smart! It does your job for you (for free!)")
        st.write("Please select 'Entity Extraction' from the sidebar to continue")
        st.markdown("""---""")

    elif app_mode == "About Us":
        st.title("About Us")
        st.header("Welcome to ML-HUB")
        st.subheader("We try to make ML accessible to everyone")
        st.write("ML-Hub.ai is a Machine Learning solution for businesses and individuals wanting to make use of the State-of-the-art Neural Networks in Computer Vision and Natural Language Processing domains. ")
        st.write("We provide simple drag-and-drop approach to problems that require tremendous coding and knowledge of data science domain.")
        st.write("Instead of spending time building neural networks and models, you can focus on what matters the most -- Results.")
        st.write("We take care of all the modelling and processing behind the scenes on our Heroku server.")
        st.write("We provide solutions for :")
        st.write("Object Detection | Face Detection | Sentiment Analysis | Entity Extraction")
        st.markdown("""---""")
        st.header("Meet Our Team Members")
        st.write("Aditya Patkar - Lead Developer")
        st.write("Rakesh Kumar - Frontend Developer")
        st.write("Radhika Sahastrabudhe - Design Expert")
        st.write("Apoorva Parashar - Backend and Diagrams ")
    elif app_mode == "Object Detection":
        object_main()
    elif app_mode == "Face Detection":
        face_main()
    elif app_mode == "Sentiment Analysis":
        sentiment_analysis()
    elif app_mode == "Entity Extraction":
        entity_extraction()


if __name__ == '__main__':
    main()