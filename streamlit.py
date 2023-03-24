
import pickle
import streamlit as st
import pandas as pd
import sklearn 

model = pickle.load(open('model_svc1.pkl','rb'))
df = pd.DataFrame(columns=['USMER','MEDICAL_UNIT','SEX','PATIENT_TYPE','INTUBED','PNEUMONIA','AGE','PREGNANT','DIABETES','COPD','INMSUPR','HIPERTENSION','OTHER_DISEASE','CARDIOVASCULAR','OBESITY','RENAL_CHRONIC','TOBACCO','CLASIFFICATION_FINAL','ICU'])

a = st.sidebar.radio('Select Model:', ['svc', 'knn','dtc','nb','rfc'])

st.header('Corona _Predicition_ :mending_heart:')

st.subheader('USMER', anchor=None)
usmer = st.selectbox("Enter the USMER of patient (Indicates whether the patient treated medical units level)",('1', '2', '3'))
st.write('You selected:', usmer)

st.subheader('Medical Unit', anchor=None)
medical_unit = st.selectbox("Enter Medical Unit",('1','2','3'))
st.write('You selected:', usmer)

st.subheader('Sex' ,anchor=None)
sex = st.selectbox("Enter Your Sex (1 for female and 2 for male)",('1','2'))
st.write('You selected:', usmer)

st.subheader('Age ',anchor=None)
age = st.slider('How old are you?', 0, 100, 10)
st.write("You are", age, 'years old')

st.subheader('Patient Type' ,anchor=None)
patient_type = st.selectbox("ype of care the patient received in the unit. (1 for returned home and 2 for hospitalization)",('1','2'))
st.write('You selected:', patient_type)

st.subheader('Pneumonia' ,anchor=None)
pneumonia= st.selectbox("whether the patient already have air sacs inflammation or not.",('0','1'))
st.write('You selected:',pneumonia)

st.subheader('Pregnant' ,anchor=None)
pregnant= st.selectbox("whether the patient already is pregnant or not.",('0','1'))
st.write('You selected:',pregnant)

st.subheader('Diabetes' ,anchor=None)
diabetes= st.selectbox("whether the patient already is diabetic or not.",('0','1'))
st.write('You selected:',diabetes)

st.subheader('COPD' ,anchor=None)
COPD= st.selectbox("whether the patient already has COPD or not.",('0','1'))
st.write('You selected:',COPD)

st.subheader('Immuno',anchor=None)
immuno= st.selectbox("whether the patient already has immune system problem or not.",('0','1'))
st.write('You selected:',immuno)

st.subheader('Hyper Tension',anchor=None)
hyper= st.selectbox("whether the patient already has hypertension or not.",('0','1'))
st.write('You selected:',hyper)

st.subheader('Other Disease',anchor=None)
other_disease = st.selectbox("whether the patient already has other diseases or not.",('0','1'))
st.write('You selected:',other_disease)

st.subheader('Cardio Problems',anchor=None)
cardio = st.selectbox("whether the patient already has cardio vascular problems or not.",('0','1'))
st.write('You selected:',cardio)

st.subheader('Obesity', anchor=None)
obesity = st.selectbox("whether the patient already is obese or not.",('0','1'))
st.write('You selected:',obesity)

st.subheader('Renal', anchor=None)
renal = st.selectbox("whether the patient already has renal chronic or not.",('0','1'))
st.write('You selected:',renal)

st.subheader('Tobacco', anchor=None)
tobaco = st.selectbox("whether the patient already uses tobacco or not.",('0','1'))
st.write('You selected:',tobaco)

st.subheader('Classification', anchor=None)
classification = st.selectbox("whether the patient already uses tobacco or not.",('1','2','3','4','5','6','7'))
st.write('You selected:',classification)

st.subheader('ICU', anchor=None)
icu = st.selectbox("whether the patient already was in ICU or not.",('0','1'))
st.write('You selected:',icu)

st.subheader('Intubed', anchor=None)
intubed = st.selectbox("whether the patient was connected to the ventilator",('0','1'))
st.write('You selected:',intubed)

data = [usmer,medical_unit,sex,patient_type,intubed,pneumonia,age,pregnant,diabetes,COPD,immuno,hyper,other_disease,cardio,renal,tobaco,classification,icu]
# df = pd.DataFrame([data],columns=['USMER','MEDICAL_UNIT','SEX','PATIENT_TYPE','INTUBED','PNEUMONIA','AGE','PREGNANT','DIABETES','COPD','INMSUPR','HIPERTENSION','OTHER_DISEASE','CARDIOVASCULAR','RENAL_CHRONIC','TOBACCO','CLASIFFICATION_FINAL','ICU'])
# st.write(df.values)

data = [int(x) for x in data]

if st.button("Predict"):
        prediction = model.predict([data])[0]
        print('data')
        # Display the prediction
        if prediction == 0:
                st.balloons()
                st.warning('You will not die ') 
        else:
                st.warning('You will die', icon="⚠️")

