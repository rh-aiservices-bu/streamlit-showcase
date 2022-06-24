# based on data available in https://insights.stackoverflow.com/survey
import streamlit as st
import pandas as pd
import urllib.request
import zipfile

st.markdown("# StackOverflow Survey 🎈")

st.sidebar.markdown("# Stack Overflow Survey 🎈")


def DownloadData():
    print("start")

    # we only download the data if the dataframe does not already exist
    so2021 = pd.DataFrame()

    if so2021.empty:

        url_2021 = "https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip"
        zip_location = "/tmp/stack-overflow-developer-survey-2021.zip"

        urllib.request.urlretrieve(url_2021, zip_location)

        with zipfile.ZipFile(zip_location, "r") as zip_ref:
            zip_ref.extractall("/tmp/2021/")

        import os

        os.listdir("/tmp/2021")


def ShowData():
    so2021 = pd.read_csv("/tmp/2021/survey_results_public.csv")
    # st.write(so2021.shape)
    # so2021.head()
    # st.dataframe(so2021,10,10)
    # st.table(so2021)abs
    st.bar_chart(so2021)


st.button(
    "get data",
    key=None,
    help=None,
    on_click=DownloadData,
)
st.button(
    "show data",
    key=None,
    help=None,
    on_click=ShowData,
)
