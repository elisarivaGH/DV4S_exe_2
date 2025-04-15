import streamlit as st
import numpy as np

st.title('This is page 2')

# Get info from sidebar
st.title('Gettin info from the sidebar')

player = st.session_state['Players']
team = st.session_state['Teams']

st.write('The player is:', player)
st.write('The team is:', team)

# COLUMNS
st.title('Columns')

col1, col2 = st.columns([0.6, 0.4])

col1.header('Tennis')
col1.image('https://www.mouratoglou.com/wp-content/uploads/2024/11/11dd1227-f3e1-4903-8755-cdbeeea0d97b-JUL01675-1534x1534-c-center.webp')

col2.header('Soccer')
col2.image('https://t4.ftcdn.net/jpg/00/86/41/89/360_F_86418998_mQ7NZfxcfR1hK1PDbVDSUkr6TFZbNRc0.jpg')

# With notation
st.title('More columns')

data = np.random.rand(20, 1)

colA, colB = st.columns([3, 1])

with colA:
    st.header('Data Viz')
    st.bar_chart (data)
with colB:
    st.header('Table')
    st.table(data)

# Tabs
st.title('Here we are using tabs')

tab1, tab2 = st.tabs(['Football', 'Skiing'])
tab1.subheader('Football')
tab1.image('https://usafootball.com/_next/image?url=https%3A%2F%2Fsquidex.usafootball.com%2Fapi%2Fassets%2Fusawebsite%2Fafecbd42-79b2-42a3-b3cf-3c6d79fec0d1%2F&w=1920&q=75')
tab2.subheader('Skiing')
tab2.image('https://www.chillfactore.com/perch/resources/maarten-duineveld-pmfjcn7rgiw-unsplash-w960.jpg')

# EXPANDERS

st.title('Expanders')

with st.expander('Data Viz', expanded=True):
    st.subheader('My data')
    st.line_chart(data)

with st.expander('Table', expanded=False):
    st.subheader('My table')
    st.table(data)
    
# SECRETS
st.title('Secrets')

username = st.secrets['username']
st. write(username)