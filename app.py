
import streamlit as st
import joblib
import pandas as pd


# Load model pipeline dan label encoder

pipeline = joblib.load("final_model_pipeline.pkl")
label_encoder = joblib.load("label_encoder.pkl")


# Setup UI Streamlit

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")
st.title(" Prediksi Dropout Mahasiswa - Jaya Jaya Institut")

st.write("Silakan isi data mahasiswa berikut untuk memprediksi status kelulusan:")


# Input Form

col1, col2, col3 = st.columns(3)

with col1:
    age_at_enrollment = st.number_input("Umur saat mendaftar", 17, 70, 20)
    gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    marital_status = st.selectbox("Status Pernikahan", ["Belum Menikah", "Menikah", "Lainnya"])
    admission_grade = st.number_input("Nilai Penerimaan", 0.0, 200.0, 100.0)

with col2:
    scholarship_holder = st.selectbox("Penerima Beasiswa", ["Tidak", "Ya"])
    tuition_fees_up_to_date = st.selectbox("Biaya Kuliah Lancar", ["Tidak", "Ya"])
    curricular_units_1st_sem_approved = st.number_input("Jumlah Mata Kuliah Disetujui (Semester 1)", 0, 20, 5)
    curricular_units_1st_sem_grade = st.number_input("Rata-rata Nilai Mata Kuliah (Semester 1)", 0.0, 20.0, 10.0)

with col3:
    debtor = st.selectbox("Memiliki Tunggakan", ["Tidak", "Ya"])
    unemployment_rate = st.number_input("Tingkat Pengangguran (%)", 0.0, 100.0, 10.0)
    gdp = st.number_input("Nilai GDP", -10.0, 10.0, 0.0)
    inflation_rate = st.number_input("Tingkat Inflasi (%)", -5.0, 10.0, 0.0)


# Persiapkan input ke format dataframe sesuai model

if st.button("Prediksi Status"):
    # Mapping nilai kategorikal sesuai fitur pipeline
    gender_map = {"Laki-laki": "Male", "Perempuan": "Female"}  
    marital_map = {"Belum Menikah": "Single", "Menikah": "Married", "Lainnya": "Other"}
    yes_no_map = {"Ya": 1, "Tidak": 0}

    input_dict = {
        'Marital_status': marital_map[marital_status],
        'Gender': gender_map[gender],
        'Age_at_enrollment': age_at_enrollment,
        'Admission_grade': admission_grade,
        'Scholarship_holder': yes_no_map[scholarship_holder],
        'Tuition_fees_up_to_date': yes_no_map[tuition_fees_up_to_date],
        'Debtor': yes_no_map[debtor],
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Unemployment_rate': unemployment_rate,
        'Inflation_rate': inflation_rate,
        'GDP': gdp
    }

    input_df = pd.DataFrame([input_dict])

    # Prediksi dengan pipeline lengkap (preprocessing + model)
    prediction = pipeline.predict(input_df)
    pred_label = label_encoder.inverse_transform(prediction)[0]

    st.success(f"🎯 Prediksi Status Mahasiswa: **{pred_label.upper()}**")
