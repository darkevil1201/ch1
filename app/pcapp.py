import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("資料分析視覺化")
csv = st.sidebar.selectbox("請選擇選單",['IRIS','糖尿病了'])
num = st.sidebar.slider("請選數量",5,30)


if csv=="IRIS":
    df = pd.read_csv("app\Iris.csv")
    x = df.iloc[:,[3,4]]
    m = {"Iris-setosa":1,"Iris-versicolor":2,"Iris-virginica":3}
    y = df.Species.map(m)
    x1 = df.SepalLengthCm
    x2 = df.SepalWidthCm
else:
    df = pd.read_csv("app\diabetes.csv")
    x = df.iloc[:,[5,6]]
    y = df.Outcome
    x1 = df.DiabetesPedigreeFunction
    x2 = df.BloodPressure#BMI


st.write("### 資料前{}筆".format(num))
st.dataframe(df.head(num))

fig,ax = plt.subplots()
plt.scatter(x1,x2,c=y)
st.pyplot(fig)