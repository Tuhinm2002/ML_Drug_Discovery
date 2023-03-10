import streamlit as st

def app():
    result = st.session_state["value"]
    if result == "Leukemia":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/LEUKEMIA_DRUG_DISCOVERY.ipynb")

    elif result == "Influenza B":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/INFLUENZA_B_DRUG_DISCOVERY.ipynb")

    elif result == "Influenza A":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/INFLUENZA_A_DRUG_DISCOVERY.ipynb")

    elif result == "Alzheimer":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/ALZHEIMER_DRUG_DISCOVERY.ipynb")

    elif result == "Dengue":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/DENGUE_DRUG_DISCOVERY.ipynb")

    elif result == "Lungs Cancer":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/LUNGS_CANCER_DRUG_DISCOVERY.ipynb")

    elif result == "Aromatase":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/AROMATASE_DRUG_DISCOVERY.ipynb")

    elif result == "Hepatitis B":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/HEPATITIS_B_DRUG_DISCOVERY.ipynb")

    elif result == "Hepatitis C":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/HEPATITIS_C_DRUG_DISCOVERY.ipynb")

    elif result == "CoronaVirus":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/CORONAVIRUS_DRUG_DISCOVERY.ipynb")

    elif result == "Chronic Kidney Disease":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/CHRONIC_KIDNEY_DISEASE_DRUG_DISCOVERY.ipynb")

    elif result == "Hiv":
        st.write("### https://github.com/Tuhinm2002/ML_Drug_Discovery/blob/main/Notebooks/HIV_DRUG_DISCOVERY.ipynb")

