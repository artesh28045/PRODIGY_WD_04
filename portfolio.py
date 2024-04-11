import streamlit as st
def main():
    # Page layout
    st.set_page_config(
        page_title="ARTESH S - Web Developer",
        page_icon="✨",
        layout="wide",
    )

    # Header
    st.title("ARTESH S - Web Developer")
    st.subheader("Work Hard in The Silence, let your success be your noise. 🚀")
    st.image("pf.jpg", width=250, caption="ARTESH S")

    # Navigation
    nav_options = ["Home", "About Me", "Skills", "Projects", "Contact"]
    selected_page = st.sidebar.radio("Navigate", nav_options)

    # Home Page
    if selected_page == "Home":
        st.write("Welcome to my personal portfolio!")
        st.write("I am a passionate web developer with expertise in Web Development")
        st.write("Let's collaborate and turn your ideas into reality!")

    # About Me Page
    elif selected_page == "About Me":
        st.header("About Me")
        st.write("Hello! I'm ARTESH S, a web developer.")
        st.write("I have a background in BE MECHANICAL")
        st.write("Here's a snapshot of my journey:")
        st.subheader("Education")
        st.write("- BE MECHANICAL, NITTE MEENAKSHI INSTITUTE of Technology, 2022-2026")
        st.subheader("Professional Experience")
        st.write("- Project Intern,PRODIGY INFOTECH, 2024")
        

    # Skills Page
    elif selected_page == "Skills":
        st.header("Skills")
        st.write("I specialize in the following technologies:")
        st.write("- HTML, CSS, JavaScript")
        st.write("- Python, Django, Flask")
        st.write("- React, Angular")
        st.write("- SQL, MongoDB")
       

    # Projects Page
    elif selected_page == "Projects":
        st.header("Projects")
    
        # Project 1
        st.subheader("Project 1: CAR RENTAL SYSTEM")
        st.image("car.jpeg", width=500, caption="CAR RENTAL SYSTEM")
        st.write("Description: Car Rental System is a website that helps to create user, rent a car by the customers for a period of time and to add, delete, edit a car by the admin. All the details are stored in the database for future use.")
        st.write("Technologies used: HTML, CSS, JavaScript, React, MongoDb, Express, Node.js")
        st.write("Link to GitHub: [Project 1 GitHub Repo](https://github.com/ARTESH28045/CAR-RENTAL-SYSTEM)")

        # Project 2
        st.subheader("Project 2: EFFECTIVE-PREDICTION-OF-PARKINSON-DISEASE-USING-ML")
        st.image("pd.jpg", width=500, caption="EFFECTIVE-PREDICTION-OF-PARKINSON-DISEASE-USING-ML")
        st.write("Description:Effective Prediction of Parkinson Disease using ML predicts the Parkinson’s Disease with the help of Ensemble Machine Learning Algorithm, Hyperparameter Tuning and Feature Selection. Accuracy of 94.87% was achieved with the help of the developed Ensemble Machine Learning Algorithm, whereas a maximum accuracy of 92.8% was achieved by traditional ML.")
        st.write("Technologies used: Python,Numpy,Pandas,Scikit-learn,Matplotlib.")
        st.write("Link to GitHub: [Project 2 GitHub Repo](https://github.com/ARTESH28045/EFFECTIVE-PREDICTION-OF-PARKINSON-DISEASE-USING-ML)")


    # Contact Page
    elif selected_page == "Contact":
        st.header("Contact")
        st.write("Let's connect and discuss your next project!")
        st.write("Email: ARTESHSHETTY336@gmail.com")
        st.write("Phone: +91 8431068242")
        st.write("LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/ARTESHSHETTY/)")
        st.write("GitHub: [GitHub Profile](https://github.com/ARTESH28045)")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.text("© 2024 ARTESH S - Web Developer")

# Run the app
if __name__ == "__main__":
    main()
