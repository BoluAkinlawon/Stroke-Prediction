import pickle
import streamlit as st
print("0 means no stroke, 1 means stroke")
model = pickle.load(open('random_forest_model.pkl', 'rb'))

def main():
    st.title('Stroke Prediction System')

    #input variables
    age = st.text_input('age')
    gender = st.selectbox(
      """gender
      0: female, 1: male""",    
      ('0', '1'))
    hypertension = st.selectbox(
      """History of hypertension?
      0: No, 1: Yes""",    
      ('0', '1'))
    heart_disease = st.selectbox(
      """History of heart disease?
      0: No, 1: Yes""",    
      ('0', '1'))
    ever_married = st.selectbox(
      """Ever married?
      0: No, 1: Yes""",    
      ('0', '1'))
    work_type = st.selectbox(
      """Work Type
      0: Govt job, 1: child care, 2: Private sector, 3: self employed""",    
      ('0', '1', '2', '3'))
    Residence_type = st.selectbox(
      """Residence type
      0: Rural, 1: Urban""",    
      ('0', '1'))
    avg_glucose_level = st.text_input('avg_glucose_level')
    bmi = st.text_input('bmi')
    smoking_status = st.selectbox(
      """Do you smoke?
      0: No, 1: Yes""",    
      ('0', '1'))
    #prediction code
    if st.button('Predict'):
        makeprediction = model.predict([[age, gender, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi,smoking_status]])
        output = round(makeprediction[0],0)
        if output == 0.0:
            st.success('You are at no immediate risk of stroke')
        elif output == 1.0:
            st.success('You are at an immediate risk of stroke')


if __name__ =='__main__':
    main()