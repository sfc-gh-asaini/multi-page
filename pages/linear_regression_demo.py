import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression


# Write directly to the app
st.title("Sklearn Linear Regression Example :balloon:")

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)

st.subheader('Regression score')
st.write(reg.score(X, y))

st.subheader('Regression Coefficients')
st.write(reg.coef_)

st.subheader('Regression Intercept')
st.write(reg.intercept_)

st.subheader('Regression prediction')
st.write(reg.predict(np.array([[3, 5]])))