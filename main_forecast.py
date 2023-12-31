import streamlit as st
import plotly.express as px
from forecast_data import get_data

st.title('Weather Forecast Tool')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecast days')
option = st.selectbox('Select Data to View', ('Temperature', 'Sky'))

if place:
    try:
        st.subheader(f'{option} for the next {days} days in {place}')

        # get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == 'Temperature':
            dates = [dict['dt_txt'] for dict in filtered_data]
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=120)

    except KeyError:
        st.write('The place does not exist!')
