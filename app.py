import streamlit as st
from PIL import Image


icon = Image.open("./images/home.jpg")
st.set_page_config(page_title="Mother's Kitchen",page_icon= icon, layout='wide')
st.image("./images/img.webp",use_column_width=True)
st.snow()

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    with st.expander("**📖 How to Use This Blog**"):
        st.markdown("""
                    However you like! 🤷🏻

                    But here's my recommendation:

                    There are different dishes to choose from which you can prepare at Home at your convenience🎈.........
                    Spend a few minutes reading the tips and hopefully pick up something new.
                    """)
        

col1,col2=st.columns([0.5,2])
with col1:
    option = st.selectbox(
    'Select the Recipe',
    ('Macher Zhol', '', ''))
with col2:
    if option=="Macher Zhol":
        st.markdown("<h1 style='text-align: center; color: black;'>Macher Zhol in my Mom's Style</h1>", unsafe_allow_html=True)
        st.markdown("Ingredients")
        st.markdown("1. ginger and green chilli paste")
        st.markdown("2. half onion ( slight pasted)")
        st.markdown("3. half onion (sliced)")
        st.markdown("3. potatoes (sliced)")
        st.markdown("4. tomato (one sliced into 4 pieces)")
        st.markdown("5. mustard oil")  
        st.markdown("6. ")

    
       



