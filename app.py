import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

# Create synthetic data for demonstration purposes
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

# Streamlit app layout
st.title('Breast Cancer Risk Assessment App')
st.image('https://homecare-aid.com/wp-content/uploads/2024/04/women-hands-holding-pink-breast-cancer-ribbon-stan-2022-12-16-07-16-23-utc-1-1024x682.jpg', caption='Breast Cancer Awareness', use_column_width=True)

st.markdown("""
### Educational Resources
- [Breast Cancer Information](https://www.cancer.org/cancer/breast-cancer.html)
- [Preventive Measures](https://www.breastcancer.org/research-news/prevention)
- [Support Groups](https://www.breastcancer.org/community/support)
""")

st.header('Personal and Family Medical History')
history_diagnosed = st.selectbox('Have you ever been diagnosed with breast cancer or any other type of cancer before?', ['Select', 'No', 'Yes'], key='history_diagnosed')
history_biopsies = st.selectbox('Have you had any previous breast biopsies or surgeries?', ['Select', 'No', 'Yes'], key='history_biopsies')
history_family = st.selectbox('Do you have a family history of breast cancer (e.g., mother, sister, daughter)?', ['Select', 'No', 'Yes'], key='history_family')

st.header('Symptoms and Physical Changes')
symptoms_lumps = st.selectbox('Have you noticed any lumps or changes in your breast tissue?', ['Select', 'No', 'Yes'], key='symptoms_lumps')
symptoms_pain = st.selectbox('Have you experienced any pain or tenderness in your breasts?', ['Select', 'No', 'Yes'], key='symptoms_pain')
symptoms_discharge = st.selectbox('Do you have any nipple discharge or changes in the appearance of your nipples?', ['Select', 'No', 'Yes'], key='symptoms_discharge')
symptoms_size_change = st.selectbox('Have you observed any changes in the size, shape, or appearance of your breasts?', ['Select', 'No', 'Yes'], key='symptoms_size_change')
symptoms_skin_change = st.selectbox('Have you noticed any skin changes on your breasts, such as dimpling or redness?', ['Select', 'No', 'Yes'], key='symptoms_skin_change')

st.header('Screening and Preventive Measures')
screening_mammogram = st.selectbox('Have you had a mammogram before, and if so, when was your last one?', ['Select', 'No', 'Yes'], key='screening_mammogram')
screening_other_tests = st.selectbox('Have you undergone any other breast cancer screening tests, such as MRI or ultrasound?', ['Select', 'No', 'Yes'], key='screening_other_tests')

# Convert user inputs to binary values and make prediction
if 'Select' not in [history_diagnosed, history_biopsies, history_family, symptoms_lumps, symptoms_pain, symptoms_discharge, symptoms_size_change, symptoms_skin_change, screening_mammogram, screening_other_tests]:
    input_data = pd.DataFrame({
        'history_diagnosed': [1 if history_diagnosed == 'Yes' else 0],
        'history_biopsies': [1 if history_biopsies == 'Yes' else 0],
        'history_family': [1 if history_family == 'Yes' else 0],
        'symptoms_lumps': [1 if symptoms_lumps == 'Yes' else 0],
        'symptoms_pain': [1 if symptoms_pain == 'Yes' else 0],
        'symptoms_discharge': [1 if symptoms_discharge == 'Yes' else 0],
        'symptoms_size_change': [1 if symptoms_size_change == 'Yes' else 0],
        'symptoms_skin_change': [1 if symptoms_skin_change == 'Yes' else 0],
        'screening_mammogram': [1 if screening_mammogram == 'Yes' else 0],
        'screening_other_tests': [1 if screening_other_tests == 'Yes' else 0]
    })

    prediction = model.predict(input_data)[0]
    st.write(f'Predicted Diagnosis: {"Malignant" if prediction == 1 else "Benign"}')

    suggestions = []
    if history_diagnosed == 'Yes':
        suggestions.append("Consult your healthcare provider for regular follow-ups and screenings.")
    if history_biopsies == 'Yes':
        suggestions.append("Inform your doctor about any previous biopsies or surgeries during consultations.")
    if history_family == 'Yes':
        suggestions.append("Discuss genetic testing and preventive measures with your healthcare provider.")
    if symptoms_lumps == 'Yes' or symptoms_pain == 'Yes' or symptoms_discharge == 'Yes' or symptoms_size_change == 'Yes' or symptoms_skin_change == 'Yes':
        suggestions.append("Schedule a medical examination to evaluate your symptoms.")
    if screening_mammogram == 'No' or screening_other_tests == 'No':
        suggestions.append("Consider scheduling regular breast cancer screenings.")

    st.write("### Personalized Suggestions")
    for suggestion in suggestions:
        st.write(f"- {suggestion}")

    input_data_visual = input_data.T.reset_index()
    input_data_visual.columns = ['Feature', 'Value']
    fig = px.bar(input_data_visual, x='Feature', y='Value', title='User Input Data')
    st.plotly_chart(fig)
else:
    st.warning('Please answer all the questions to get personalized suggestions.')

st.header('Feedback')
feedback = st.text_area("Please provide your feedback here:")
if st.button('Submit Feedback'):
    st.write('Thank you for your feedback!')
