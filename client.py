import streamlit as st
import requests
  
def generate_response(topic):
    response = requests.post("http://localhost:8000/essay", json={"topic": topic})
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code} - {response.text}"   
    

def main():
    st.title("Llama 3 Chatbot with FastAPI and Streamlit")
    st.write("Answer questions based on data in the databse")

    task = st.selectbox("Choose a task", ("Generate Response"))
    topic = st.text_input("Enter the topic")

    if topic:
        if task == "Generate Response":
            result = generate_response(topic)
            st.subheader("Generate Response")       

        st.write(result)
    else:
        st.write("Please enter a topic.")

if __name__ == "__main__":
    main()


# How to run this section of the project
# https://stackoverflow.com/questions/60866205/python-streamlit-run-issue
# python -m streamlit run "Name of file".py
