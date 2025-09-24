import pandas as pd
import numpy as np
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import uuid

# Функция для создания кнопки скачивания
def create_download_button(fig, filename, label="Скачать график"):
    try:
        # Создаем буфер памяти
        buf = BytesIO()
        
        # Сохраняем график в буфер
        fig.savefig(buf, format="png", bbox_inches='tight')
        buf.seek(0)
        
        # Создаем кнопку скачивания с уникальным ключом
        st.download_button(
            label=label,
            data=buf,
            file_name=filename,
            mime="image/png",
            key=str(uuid.uuid4())  # Уникальный ключ для избежания ошибок
        )
        
        # Очищаем буфер
        buf.close()
        
    except Exception as e:
        st.error(f"Ошибка при создании файла: {str(e)}")

st.write("""
              
# Скаттерплоты
              
""")

try:
       path = st.sidebar.file_uploader(label= 'Загрузите данные с чаевыми', type='CSV')
       data = pd.read_csv(path)
       data['time_order'] = pd.to_datetime(
       np.random.choice(
              pd.date_range(start='2023-01-01', end='2023-01-31'),
              size=len(data)
              )
              )
       data['time_order'] = pd.to_datetime(data['time_order'])
              
except Exception as e:
       st.sidebar.write(
       "<p style='color:red;'>Данные не загружены</p>", unsafe_allow_html=True
       )
       st.stop()


st.write("scatterplot, показывающий связь между total_bill and tip")    #Первый скаттерплот
fig_scatter1 = plt.figure()
plot = sns.scatterplot(x=data['total_bill'], y=data['tip'])
plot.set(
       xlabel = 'Общий чек, $',
       ylabel = 'Чаевые, $')
st.pyplot(fig_scatter1)

create_download_button(
    fig=fig_scatter1,
    filename="график.png",
    label="Скачать график"
)

st.write("scatterplot, связывающий Размер чека, Чаевые, и Количество людей")    #Второй скаттерплот
fig_scatter2 = plt.figure()
palette = sns.color_palette("rocket_r")
plot = sns.scatterplot(x=data['total_bill'], y=data['tip'],size=data['size'],hue=data['size'], palette=palette, edgecolor = 'black')
plot.set(xlabel = 'Общий чек, $',
         ylabel = 'Чаевые, $')
st.pyplot(fig_scatter2)

create_download_button(
    fig=fig_scatter2,
    filename="график.png",
    label="Скачать график")

st.write("scatterplot, связывающий размер чека с чаевыми для мужчин и женщин")    #3rd скаттерплот

fig_scatter3, axes = plt.subplots(1, 2, figsize=(10,7))

sns.scatterplot(data = data[data['sex'] == 'Male'], 
                x='total_bill', 
                y='tip',
                ax= axes[0],
                size=None, 
                hue='smoker', 
                palette= ["m", "g"], 
                edgecolor = 'black')
axes[0].set(xlabel = 'Общий чек мужчин, $',
            ylabel = 'Чаевые, $')                


sns.scatterplot(data = data[data['sex'] == 'Female'], 
                x='total_bill', 
                y='tip',
                ax=axes[1],
                size=None, 
                hue='smoker', 
                palette= ["m", "g"], 
                edgecolor = 'black')
axes[1].set(xlabel = 'Общий чек мужчин, $',
            ylabel = 'Чаевые, $') 
                

plt.suptitle('Связь чека с чаевыми для мужчин и женщин')
st.pyplot(fig_scatter3)

create_download_button(
    fig=fig_scatter3,
    filename="график.png",
    label="Скачать график")

