import streamlit as st


def set_page_configuration(self):
    st.set_page_config(page_title='Snowflake', layout='wide')
    st.image("./images/ungifted_amateur_v5.png", use_column_width=True )
    st.snow()

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    with st.expander("**📖 How to Use This Blog**"):
        st.markdown("""
                    However you like! 🤷🏻

                    But here's my recommendation:

                    There are different dishes to choose from which you can prepare at Home at your convenience🎈... sorry, I mean streamlined, I have removed options and arguments that are not frequently used in each command. 
                    Spend a few minutes reading the tips and hopefully pick up something new.
                    """)
       



set_page_configuration()