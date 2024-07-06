import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'history_diagnosed' not in st.session_state:
    st.session_state.history_diagnosed = ''
if 'history_biopsies' not in st.session_state:
    st.session_state.history_biopsies = ''
if 'history_family' not in st.session_state:
    st.session_state.history_family = ''
if 'symptoms_lumps' not in st.session_state:
    st.session_state.symptoms_lumps = ''
if 'symptoms_pain' not in st.session_state:
    st.session_state.symptoms_pain = ''
if 'symptoms_discharge' not in st.session_state:
    st.session_state.symptoms_discharge = ''
if 'symptoms_size_change' not in st.session_state:
    st.session_state.symptoms_size_change = ''
if 'symptoms_skin_change' not in st.session_state:
    st.session_state.symptoms_skin_change = ''
if 'screening_mammogram' not in st.session_state:
    st.session_state.screening_mammogram = ''
if 'screening_other_tests' not in st.session_state:
    st.session_state.screening_other_tests = ''
if 'feedback' not in st.session_state:
    st.session_state.feedback = ''

# Train a simple model (for demonstration purposes)
# Create synthetic data
np.random.seed(42)
data = pd.DataFrame({
    'history_diagnosed': np.random.randint(0, 2, 100),
    'history_biopsies': np.random.randint(0, 2, 100),
    'history_family': np.random.randint(0, 2, 100),
    'symptoms_lumps': np.random.randint(0, 2, 100),
    'symptoms_pain': np.random.randint(0, 2, 100),
    'symptoms_discharge': np.random.randint(0, 2, 100),
    'symptoms_size_change': np.random.randint(0, 2, 100),
    'symptoms_skin_change': np.random.randint(0, 2, 100),
    'screening_mammogram': np.random.randint(0, 2, 100),
    'screening_other_tests': np.random.randint(0, 2, 100),
    'diagnosis': np.random.randint(0, 2, 100)
})

# Preprocessing
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Train a simple decision tree model
model = DecisionTreeClassifier()
model.fit(X, y)

def show_home():
    st.title('Breast Cancer Risk Assessment App')
    st.image("https://homecare-aid.com/wp-content/uploads/2024/04/women-hands-holding-pink-breast-cancer-ribbon-stan-2022-12-16-07-16-23-utc-1-1024x682.jpg", use_column_width=True)
    st.write("**Welcome to the Breast Cancer Risk Assessment App**")
    st.write("""
        Breast cancer is one of the most common cancers affecting women worldwide. Early detection and awareness are crucial in improving survival rates and outcomes. This app is designed to help you understand your personal risk factors for breast cancer by guiding you through a series of questions related to your medical history, symptoms, and screening practices. By providing accurate information, you can take proactive steps towards early detection and seek medical advice promptly if necessary.
        
        Our goal is to empower you with knowledge and resources to make informed decisions about your health. This app not only offers a personalized risk assessment but also provides educational resources, personalized suggestions, and access to support networks. We believe that with the right information and support, you can take charge of your breast health and contribute to the fight against breast cancer. Thank you for using our app, and we hope it serves as a valuable tool in your journey towards better health.
    """)
    st.write("### Educational Resources")
    st.write("""
    Here we provide the link for you as the resources and getting help from the worldwide support!
    - [Breast Cancer Information](https://www.cancer.org/cancer/breast-cancer.html)
    - [Preventive Measures](https://www.breastcancer.org/research-news/prevention)
    - [Support Groups](https://www.breastcancer.org/community/support)
    """)
    if st.button('Start Assessment'):
        st.session_state.page = 1

def show_history():
    st.header('Personal and Family Medical History')
    st.session_state.history_diagnosed = st.selectbox(
        'Have you ever been diagnosed with breast cancer or any other type of cancer before?',
        ['', 'No', 'Yes'],
        key='history_diagnosed'
    )
    st.session_state.history_biopsies = st.selectbox(
        'Have you had any previous breast biopsies or surgeries?',
        ['', 'No', 'Yes'],
        key='history_biopsies'
    )
    st.session_state.history_family = st.selectbox(
        'Do you have a family history of breast cancer (e.g., mother, sister, daughter)?',
        ['', 'No', 'Yes'],
        key='history_family'
    )
    if st.button('Next'):
        st.session_state.page = 2

def show_symptoms():
    st.header('Symptoms and Physical Changes')
    st.session_state.symptoms_lumps = st.selectbox(
        'Have you noticed any lumps or changes in your breast tissue?',
        ['', 'No', 'Yes'],
        key='symptoms_lumps'
    )
    st.session_state.symptoms_pain = st.selectbox(
        'Have you experienced any pain or tenderness in your breasts?',
        ['', 'No', 'Yes'],
        key='symptoms_pain'
    )
    st.session_state.symptoms_discharge = st.selectbox(
        'Do you have any nipple discharge or changes in the appearance of your nipples?',
        ['', 'No', 'Yes'],
        key='symptoms_discharge'
    )
    st.session_state.symptoms_size_change = st.selectbox(
        'Have you observed any changes in the size, shape, or appearance of your breasts?',
        ['', 'No', 'Yes'],
        key='symptoms_size_change'
    )
    st.session_state.symptoms_skin_change = st.selectbox(
        'Have you noticed any skin changes on your breasts, such as dimpling or redness?',
        ['', 'No', 'Yes'],
        key='symptoms_skin_change'
    )
    if st.button('Next'):
        st.session_state.page = 3

def show_screening():
    st.header('Screening and Preventive Measures')
    st.session_state.screening_mammogram = st.selectbox(
        'Have you had a mammogram before, and if so, when was your last one?',
        ['', 'No', 'Yes'],
        key='screening_mammogram'
    )
    st.session_state.screening_other_tests = st.selectbox(
        'Have you undergone any other breast cancer screening tests, such as MRI or ultrasound?',
        ['', 'No', 'Yes'],
        key='screening_other_tests'
    )
    if st.button('Submit'):
        st.session_state.page = 4

def show_results():
    st.header('Assessment Results')
    input_data = pd.DataFrame({
        'history_diagnosed': [1 if st.session_state.history_diagnosed == 'Yes' else 0],
        'history_biopsies': [1 if st.session_state.history_biopsies == 'Yes' else 0],
        'history_family': [1 if st.session_state.history_family == 'Yes' else 0],
        'symptoms_lumps': [1 if st.session_state.symptoms_lumps == 'Yes' else 0],
        'symptoms_pain': [1 if st.session_state.symptoms_pain == 'Yes' else 0],
        'symptoms_discharge': [1 if st.session_state.symptoms_discharge == 'Yes' else 0],
        'symptoms_size_change': [1 if st.session_state.symptoms_size_change == 'Yes' else 0],
        'symptoms_skin_change': [1 if st.session_state.symptoms_skin_change == 'Yes' else 0],
        'screening_mammogram': [1 if st.session_state.screening_mammogram == 'Yes' else 0],
        'screening_other_tests': [1 if st.session_state.screening_other_tests == 'Yes' else 0]
    })
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("Based on your responses, there might be a higher risk of breast cancer. Please consult a healthcare professional for further evaluation.")
    else:
        st.success("Based on your responses, the risk of breast cancer appears to be lower. However, please continue regular check-ups and screenings.")

    st.header('Personalized Suggestions')
    suggestions = []
    if st.session_state.history_diagnosed == 'Yes':
        suggestions.append("Consult your healthcare provider for regular follow-ups and screenings.")
    if st.session_state.history_biopsies == 'Yes':
        suggestions.append("Inform your doctor about any previous biopsies or surgeries during consultations.")
    if st.session_state.history_family == 'Yes':
        suggestions.append("Discuss genetic counseling and testing options with your healthcare provider.")
    if st.session_state.symptoms_lumps == 'Yes':
        suggestions.append("Schedule a clinical breast exam and consider imaging tests.")
