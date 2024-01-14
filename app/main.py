import streamlit as st
import numpy as np
import pandas as pd

st.title("AAAA")
st.write("# 11111")
st.write("## 11111")
st.info("5555")
a = np.array([1,2,3,4,5])
st.write(a)
st.table(a)

st.write("美食")
ch = st.checkbox("美食")
if ch:
    st.info("愛美食")
else:
    st.info("不愛美食")

st.write("美食")
ch = st.checkbox("美食",key="a1")
if ch:
    st.info("愛美食")
else:
    st.info("不愛美食")

txt1=" "
chs = st.columns(3)
with chs[0]:
    c0 = st.checkbox("飯",key="c0")
    if c0:
        st.write("要白飯")
        txt1 += "加飯"
with chs[1]:
    c1 = st.checkbox("小菜",key="c1")
    if c1:
        st.write("要小菜")
        txt1 += "加小菜"
with chs[2]:
    c2 = st.checkbox("湯",key="c2")
    if c2:
        st.write("要湯")
        txt1 += "加湯"
st.info(txt1)

gender = st.radio("請選擇:",['男','女','不知'])
st.info(gender)

col1,col2 = st.columns(2)
with col1:
    ra1 = st.number_input("請輸入數字")
with col2:
    ra2 = st.number_input("請輸入數字",key = "ra2")
ra3 = st.radio("請選符號",['+','-','*','/'])

num = st.slider("請選數字",1.00,20.00,step=0.01)
st.info(num)

city = st.selectbox("請選則",('台北','台中','台南'),index=1)
st.info(city)

file = st.file_uploader("請選選擇")
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)

