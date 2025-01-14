import streamlit as st
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt 
import plotly.graph_objects as go


st.title("BUISNESS DASHBOARD")

nav = st.sidebar.radio("Navigation", ["Home", "Country", "Customer"])

if(nav == "Home"):
    st.text("This is Home Page")


if(nav == "Country"):

    data = pd.read_csv(r"C:\Users\khyal\Desktop\monitor\codes\python\python_projectsssss\Country_dataframe.csv")
    st.header("COUNTRY STATISTICS")

    try:
        name = st.text_input("ENTER THE COUNTRY NAME")
        if name: #Make sure the user has entered something
            result = data[data["Country"] == name]
            if not result.empty:
                st.write(result)
            else:
                st.write("Country not found. Please enter a valid country.")
        else:
            st.write("Please enter a country name.")
    except KeyError:
        st.write("Country column not found in data")
    except Exception as e:   
        st.write(f"An error occured: {e}. Please retry with valid input")

    date = st.date_input("Enter a date")
    time = st.time_input("Enter a time")

    


if(nav == "Customer"):
    data = pd.read_csv(r"C:\Users\khyal\Desktop\monitor\codes\python\python_projectsssss\Customer_dataframe.csv")
    st.header("CUSTOMER STATISTICS")
    try:
        userid = st.number_input("ENTER THE CUSTOMER ID", step = 1)
        if userid: #Make sure the user has entered something
            result = data[data["UserId"] == userid]
            if not result.empty:
                st.write(result)
            else:
                st.write("User not found. Please enter a valid UserId.")
        else:
            st.write("Please enter a UserId.")
    except KeyError:
        st.write("UserId column not found in data")
    # except TypeError:
    #     st.write("An invalid operation is made with incompatible data type")
    # except ValueError as e:
    #     st.write(f"Invalid number: {e}. Please enter a valid integer.")
    # except ZeroDivisionError as e:
    #     st.write(f"Cannot divide by zero: {e}. Please enter a non-zero number.")
    except Exception as e:   
        st.write(f"An error occured: {e}. Please retry with valid input")

    