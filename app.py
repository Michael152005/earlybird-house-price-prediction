import joblib
import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Prediksi Harga Rumah Depok", page_icon="🏠",layout="centered")
st.title("🏠 Prediksi Harga Rumah Depok")
st.caption("Estimasi berbasis listing rumah dan karakteristik fisik/lokasi. Bukan appraisal resmi atau jaminan harga transaksi.")
MODEL_PATH=Path(__file__).parent/'house_price_model.joblib'
if not MODEL_PATH.exists():
    st.error("Model belum tersedia. Jalankan notebook sampai ekspor house_price_model.joblib, lalu letakkan berkas itu di folder yang sama dengan app.py.")
    st.stop()
@st.cache_resource
def get_artifact():return joblib.load(MODEL_PATH)
a=get_artifact()
with st.form('rumah'):
    lokasi=st.selectbox('Lokasi sebagaimana tertulis pada dataset',options=a['lokasi'])
    kamar=st.number_input('Kamar tidur',min_value=1,max_value=15,value=3)
    mandi=st.number_input('Kamar mandi',min_value=0,max_value=15,value=2)
    garasi=st.number_input('Garasi / kapasitas parkir',min_value=0,max_value=12,value=1)
    lt=st.number_input('Luas tanah (m²)',min_value=1.0,max_value=20000.0,value=90.0,step=1.0)
    lb=st.number_input('Luas bangunan (m²)',min_value=1.0,max_value=10000.0,value=70.0,step=1.0)
    submit=st.form_submit_button('Prediksi harga',type='primary')
if submit:
    row=pd.DataFrame([{'kamar_tidur':float(kamar),'kamar_mandi':float(mandi),'garasi':float(garasi),
                       'luas_tanah':lt,'luas_bangunan':lb,'total_luas':lt+lb,'rasio_lb_lt':min(lb/lt,20.),'lokasi':lokasi}])
    predicted=float(a['model'].predict(row)[0])
    st.metric('Estimasi harga listing',f'Rp {predicted:,.0f}'.replace(',','.'))
    st.info(f"Model: {a.get('model_name','-')} ({a.get('stage','-')}); MAE test: Rp {a['metrik_test']['MAE_Rp']/1e6:,.1f} juta. Ini rata-rata galat absolut pengujian, bukan interval prediksi.")
st.divider()
st.markdown('**Batasan:** model dilatih pada listing berharga sekitar Rp100 juta–Rp50 miliar dan rumah dengan 1–15 kamar. Label lokasi masih mengikuti teks sumber, sehingga tidak selalu berupa kecamatan administratif resmi. Data ini merepresentasikan harga penawaran.')
