import streamlit as st

st.write("""
# 101 Hesaplama! 🎰
""")

# Using "with" notation
with st.sidebar:
    st.markdown(" <h2 style='text-align:center;'> AÇMA TÜRÜ </h2>", unsafe_allow_html=True)

    set_type = st.radio(
    "Tür",('Normal', 'Çift'))

    if set_type == 'Normal':
        st.write(f'{set_type} seçeneği seçildi.')
        # this part will trigger the normal set functions.

    if set_type == 'Çift':
        st.write(f'{set_type} seçeneği seçildi.')
        # this part will trigger the double set functions.
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(" <h2 style='text-align:center;'> OKEY </h2>", unsafe_allow_html=True)

    okey_number = st.slider('Sayı', 1, 13)
    
    color = st.select_slider(
    'Renk',
    options=['kırmızı', 'sarı', 'mavi', 'siyah'])
    if color == 'kırmızı': color = 'red' 
    if color == 'sarı': color = 'yellow'
    if color == 'mavi': color = 'blue'
    if color == 'siyah': color = 'black'

    st.markdown(f"<h1 style='text-align:center;'>Okey: <font color={color}></font>  <font color={color}>{okey_number}</font></h1>", unsafe_allow_html=True)
    
    okey = (color, okey_number)
    # st.write(okey)  # debug
    


check = st.checkbox('Kamerayı Aç/Kapa')
if check:
    picture = st.camera_input(label='camera', label_visibility='hidden')
    if picture:
        st.image(picture)
col1, col2 =  st.columns(2)

with col1:
    st.button('Hesapla')
    
with col2:
    st.button('Maksimize Et')



    

