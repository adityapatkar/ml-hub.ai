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
    elif app_mode == "About Us":
        st.text("Hi")
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