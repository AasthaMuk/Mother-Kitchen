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
    ('Macher Zhol', 'Mach Beguner Zhol', ''))
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

    if option=="Mach Beguner Zhol":
        st.markdown("<h1 style='text-align: center; color: black;'>Mach Beguner Zhol in my Mom's Style</h1>", unsafe_allow_html=True)
        st.markdown("Ingredients : ")
        st.markdown("1. ginger and green chilli paste")
        st.markdown("2. half onion ( slight pasted)")
        st.markdown("3. half onion (sliced)")
        st.markdown("4. tomato (one sliced into 4 pieces)")
        st.markdown("5. mustard oil")  
        st.markdown("6. coriander and cumin powder")
        st.markdown("7. brinjal(cut into 4 pieces)")
        st.markdown("8. fried fish")
    
        with st.container():
            st.markdown(
                f"""
                    <div>
                        <p style="color: black; font-family: 'Arial', sans-serif; font-size: 30px; font-weight: bold;">Steps</p>
                        <p style="color: black; font-family: 'Times New Roman', sans-serif; font-size: 20px; font-weight: bold;">1. Take a small brinjal, cut it onto 4 pieces. Take some oil in a pan, put the brinjal peices, give a small pinch of salt and turmeric powder abd fry it in low flame. Fry it in such a way that the brinjal pieces are not overfried but they appear light brown in color. Take them up from the pan and put it in a plate.</p>
                        <p style="color: black; font-family: 'Times New Roman', sans-serif; font-size: 20px; font-weight: bold;">2. Take some garlic pieces, 1 green chilli and half piece of onion and make a paste out of it.</p>
                        <p style="color: black; font-family: 'Times New Roman', sans-serif; font-size: 20px; font-weight: bold;">3. Now give some more oil in the pan. Put the onion pieces cut into thin slices and then fry it. Give the paste of garlic, green chilli and onion into the same pan, and a tomato cut into 4 pieces. Also , add coriander powder(dhone guro) and cumin powder ( jeere guro), a small pinch of sugar and then salt to it.</p>
                        <p style="color: black; font-family: 'Times New Roman', sans-serif; font-size: 20px; font-weight: bold;">4. Fry it to some extent and make the gravy.</p>
                        <p style="color: black; font-family: 'Times New Roman', sans-serif; font-size: 20px; font-weight: bold;">5. Then add the fried brinjal and fish into the gravy prepared.</p>
                        <p style="color: black; font-family: 'Times New Roman', sans-serif; font-size: 20px; font-weight: bold;">6. At last, give some green chilli broken lightly into 2 pieces over the gravy, and give one teaspoon of mustard oil over it. Put on the lid.</p>
                    </div>
                    """,
                unsafe_allow_html=True
            )














    
       



