import time

import streamlit as st


def teste_3 (name):
    # Use a breakpoint in the code line below to debug your script.


    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    tab1.write("esta é tab 1")
    tab2.write("esta é tab 2")
    tab3.write("esta é tab 3")
    st.write(" ")

    with st.expander("Abra para ver mais"):
        st.write("https://github.com/FernandoAndrada")
        st.write("# teste")
        st.write( 1 + 1 )
        st.write( "?" )

    st.write(""" # Teste Streamlit """)

    st.write(""" Teste Botões """)

    st.sidebar.write ("Teste sidebar")

    st.sidebar.button( "Teste")

    st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    # Using "with" notation
    with st.sidebar:
        st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

    with st.sidebar:
        with st.echo():
            st.write("This code will be printed to the sidebar.")

        with st.spinner("Loading..."):
            time.sleep(5)
        st.success("Done!")

    window = st.slider(" # Botão slider ")

    # st.balloons()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    teste_3 ( 'teste_3' )

