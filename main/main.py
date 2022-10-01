import time
import pandas as pd
import streamlit as st
import plotly.express as px
def get_data(path):

    df = pd.read_csv(path)

    return df

def teste_3(name):
    st.title("EDA (Exploration Data Analize)")

    with st.expander("Rossmann Store Sales"):
        st.markdown("O CFO em uma reunião, solicitou as vendas mensais de "
                    "cada loja nos próximos 6 meses. "
                    "Ele gostaria de reformar as lojas e precisava destes "
                    "dados para determinar o valor de investimento em cada loja. "
                    "Com base no Mind Map abaixo foram elaborates 12 Hipóteses a "
                    "serem testadas.")

        st.write("https://www.kaggle.com/c/rossmann-store-sales")

    with st.expander("Mind Map Rossmann Store"):
        st.image('img\Daily_Store_Sales.png')

    # st.write(df.columns)
    st.write("DataFrame Rossmann Store")
    df4 = df.drop(columns=['Unnamed: 0'])
    st.write(df4.head(5))

    tab1, tab2, tab3 = st.tabs(["Hipótese 1", "Hipótese 2", "Hipótese 3"])

    # "Hipótese 4", "Hipótese 5", "Hipótese 6 "
    # "Hipótese 7", "Hipótese 8", "Hipótese 9 "
    # "Hipótese 10", "Hipótese 11", "Hipótese 12"

    tab1.markdown("### Lojas com maior variedade de estoque deveriam vender mais."
                  "\n"
                  "**Falsa** - Lojas com MAIOR VARIEDADE vendem MENOS.")
    st.write("basic = Estoque básico; ")
    st.write("extented = Estoque com uma variedade um pouco maior;")
    st.write("extra = Estoque com muita variedade.")

    aux1 = df4[['assortment', 'sales']].groupby('assortment').sum().reset_index()
    fig = px.histogram(aux1, x='assortment', y='sales', color="sales")
    st.plotly_chart(fig)

    fig1 = px.scatter(aux1, x='sales', y='assortment', color='sales',
                      size='sales', hover_name='assortment')
    st.plotly_chart(fig1)

    # aux2 = df4[['year_week', 'assortment', 'sales']].groupby(['year_week', 'assortment']).sum().reset_index()
    # aux2.pivot(index='year_week', columns='assortment', values='sales').plot()
    #
    #
    # aux3 = aux2[aux2['assortment'] == 'extra']
    # aux3.pivot(index='year_week', columns='assortment', values='sales').plot()

    tab2.write("esta é tab 2")
    tab3.write("esta é tab 3")

    st.write(" ")

    st.write(""" Teste Botões """)

    st.sidebar.write("Teste sidebar")

    st.sidebar.button("Teste")

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
    df = get_data('df5_rossmann_store.csv')

    teste_3('teste_3')
