import pandas as pd
import numpy as np
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns


st.write("""
              
# Исследование данных о чаевых
              
""")

try:
       path = st.sidebar.file_uploader(label= 'Загрузите данные с чаевыми', type='CSV')
       data = pd.read_csv(path)
                     
except Exception as e:
       st.sidebar.write(
       "<p style='color:red;'>Данные не загружены</p>", unsafe_allow_html=True
       )
       st.stop()

st.write('Общий вид DataFrame')
st.dataframe(data.head(5)) # Выводим данные 10 строк

st.write("ССводная таблица по дням недели, среднему чеку и чаевым с средними значениями")

pivot_mean = pd.pivot_table(
    data=data,  # указываем источник данных
    values=['total_bill', 'tip'],  # список столбцов для агрегации
    index='day',  # столбец для группировки по строкам
    columns='time',  # столбец для группировки по столбцам
    aggfunc='mean'  # функция агрегации
)

st.dataframe(pivot_mean)

st.write("Сводная таблица по дням недели, среднему чеку и чаевым с максимальными и минимальными значениями")

pivot_max_min = pd.pivot_table(
    data=data,
    values=['total_bill', 'tip'],
    index='day',
    aggfunc={'total_bill': ['max', 'min'], 'tip': ['max', 'min']}
)

st.dataframe(pivot_max_min)

st.write("Сводная таблица по полу клиентов, среднему чеку и чаевым с максимальными, минимальными и средними значениями")

pivot_sex = pd.pivot_table(
    data=data,
    values=['total_bill', 'tip'],
    index='sex',
    aggfunc={'total_bill': ['max', 'min', 'mean'], 'tip': ['max', 'min', 'mean']}
)

st.dataframe(pivot_sex)