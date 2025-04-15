import streamlit as st

page1 = st.Page('page1.py', title='Page 1')
page2 = st.Page('page2.py', title='Page 2')
page3 = st.Page('training.py', title='Training')

pg = st.navigation([page1, page2, page3])
st.set_page_config(page_title='DV4S Exe2')

# SELECT BOX
# Object like
st.sidebar.selectbox(
    'Select you player',
    ('Maradona', 'Pelè', 'Fonseca'),
    key='Players'
)
# With like
with st.sidebar:
    rb = st.radio(
        'Team',
        ('Napoli', 'Milan', 'Roma'),
        key='Teams'
    )

pg.run()