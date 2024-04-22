import os
import google.generativeai as genai
import streamlit as st
from datetime import date




# Initialize the application's title and subtitle
st.title('AI Project Planner Planner')
st.text("Developed by : Qadir Hasan")
st.subheader('Plan your project  with AI')

# User input section in the sidebar
st.sidebar.header('Enter details to generate a Road Map for projects:')
api_key = st.sidebar.text_input('Enter Your Google API Key', type="password")

#api_key = os.getenv("GEMINI_API_KEY")
project_name = st.sidebar.text_input('Enter your Project Name', '')
project_description = st.sidebar.text_area("Project Details / Problem Statement", value="",  height=150, label_visibility="visible")


#destination = st.sidebar.text_input('Destination', 'Los Angeles')
date_input = st.sidebar.date_input('Project Start Date', min_value=date.today())
date = date_input.strftime('%Y-%m-%d')
#budget = st.sidebar.number_input('Budget', min_value=100, value=1000, step=100)
duration = st.sidebar.slider('Project Duration (days)', 1, 90, 7)


project_details = {
    'projectname': project_name,
    'projectdes': project_description,
    
    'date': date,
    
    'duration': duration
}
def get_personalized_roadmap(api_key):
    genai.configure(api_key=api_key)
    message = (
        f"First  write a summary of the {project_description} in a proper way and provide some more useful and relavant details about it and  give it a heading h1 as 'Problem Statement then after that"
        f"Create a detailed roadmap  itinerary in  focused on research, litereature review, tools and technologies, and relevant research papers and existing projects if any for the  project "
        f"{project_name} and its description  i.e {project_description}, starting on {date}, lasting for"
        f"{duration} days. Tasks or milestones should be broken down into months and weeks, Also, provide a roadmap checklist relevant to the project name and duration must be render in table format"
        f"you should also recommend recent research articles related to the {project_name} and {project_description}, These should render under a new heading with links to the articles."
        f"under a new headlines you should generate a possible Data Flow Diagram for the {project_name}  no need to generate image just  give in text form the steps involved or the process. "
        
    )
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(message)
    return response.text



# Button to generate the travel plan
if st.sidebar.button('Generate Project  Plan'):
    if  project_name and project_description and date  and duration:
        with st.spinner('Generating Project Plan...'):
            response = get_personalized_roadmap(api_key)
        st.success('Here is your personalized project plan :')
        st.markdown(response)
    else:
        st.error('Please fill in all the fields to generate the travel plan.')
