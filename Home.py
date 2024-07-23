import streamlit as st
# used to read cvs data
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/DSC04678 (1).JPG")

with col2:
    st.title("Howard Miller")
    content = """
    An enthusiastic, high-achieving student with a passion for leadership, academic excellence, and community service, seeking a rewarding college experience. Dedicated to encouraging and empowering others while growing as a leader and student. Desire to pursue a degree in Computer Science and Entrepreneurship.
    """
    st.write(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, emptycol, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")


with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[2:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")


