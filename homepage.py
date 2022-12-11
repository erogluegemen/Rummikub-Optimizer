import streamlit as st

st.write("""
# 101 Calculation App!🎰
""")
st.snow()


# Using "with" notation
with st.sidebar:
    st.markdown(" <h1 style='text-align:center;'> SELECT OKEY</h1>", unsafe_allow_html=True)
    okey_number = st.slider('Okey Number', 1, 13)
    

    color = st.select_slider(
    'Okey Color',
    options=['red', 'yellow', 'blue', 'black'])
    

    st.markdown(f"<h1 style='text-align:center;'>Okey is: <font color={color}></font>  <font color={color}>{okey_number}</font></h1>", unsafe_allow_html=True)

    okey = (color, okey_number)
    # st.   write(okey)  # debug
    


check = st.checkbox('Open/Close Camera')
if check:
    picture = st.camera_input(label='camera', label_visibility='hidden')


col1, col2, col3, col4 = st.columns(4)

with col1.empty():
    pass
    
with col2:
    st.button('Calculate')

with col3:
    st.button('Maximize')

with col4.empty():
    pass
    



    

