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
              
# Гистограммы
              
""")

def save_plot(fig):
    return fig.savefig('fig.png', dpi=300)

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

st.write("Общая гистограмма чаевых")    #Первая гистограмма

fig_hist_tips = plt.figure()
plot = sns.histplot(data['tip'], kde=False)
plot.set(
xlabel = 'чаевые, $',
ylabel = 'Количество чаевых')

st.pyplot(fig_hist_tips)

create_download_button(
    fig=fig_hist_tips,
    filename="график.png",
    label="Скачать график"
)

st.write("Гистограммы чаевых на обед и ланч")   #Вторая гистограмма

filtred_l = data[data['time'] == 'Lunch']
filtred_d = data[data['time'] == 'Dinner']  

fig_hist_tips2, axes = plt.subplots(1,2, figsize=(10,5))

sns.histplot(data=filtred_l, x='tip', ax= axes[0], label='Lunch', color='orange')
axes[0].legend()

axes[0].set(xlabel = 'чаевые, $',
         ylabel = 'Количество чаевых')


sns.histplot(data=filtred_d, x='tip', ax= axes[1], label = 'Dinner', color='blue')
axes[1].legend()

axes[1].set(xlabel = 'чаевые, $',
         ylabel = 'Количество чаевых')

st.pyplot(fig_hist_tips2)

create_download_button(
    fig=fig_hist_tips2,
    filename="график.png",
    label="Скачать график")