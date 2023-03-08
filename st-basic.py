import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title('Avocado Prices Dashboard')

# Description
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:.  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')

#Loading Dataset (Performed)
@st.cache_data
def load_data(path):
    dataset = pd.read_csv(path)
    return dataset
avocado = load_data('avocado-updated-2020.csv')


# Summary Statistics
st.header('Summary statistcs')
avocado_stats = avocado.groupby('type')['average_price'].mean()
st.dataframe(avocado_stats)

# Chart
st.header('Line chart by geographies')
line_fig = px.line(avocado[avocado['geography'] == 'Los Angeles'],
                   x='date', y='average_price',
                   color='type',
                   title='Avocado Prices in Los Angeles')
st.plotly_chart(line_fig)

# Interactive Widgets
with st.form('line_chart'):
    selected_geography = st.selectbox(label='Geography', options=avocado['geography'].unique())
    submitted = st.form_submit_button('Submit')
    if submitted:
        filtered_avocado = avocado[avocado['geography'] == selected_geography]
        line_fig = px.line(filtered_avocado,
                        x='date', y='average_price',
                        color='type',
                        title=f'Avocado Prices in {selected_geography}')
        st.plotly_chart(line_fig)

# Sidebar
with st.sidebar:
    st.subheader('About')
    st.markdown('This dashboard was made to practice the basic of **Streamlit** :)')

    # Media Content
    st.sidebar.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=50)
    st.sidebar.image('https://media.nutrition.org/wp-content/uploads/2021/04/1.jpg', width=200)
