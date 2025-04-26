import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Storytelling: Análise de Vendas")

# Contexto e história
st.markdown("""
Imagine que você é o gerente de vendas de uma grande loja varejista. Seu objetivo é entender o desempenho das vendas dos diferentes produtos ao longo do tempo, identificar quais categorias trazem mais receita e descobrir quais produtos são os campeões de vendas. 
Com base nesses dados, será possível tomar decisões estratégicas para aumentar o faturamento, ajustar o estoque e direcionar campanhas promocionais de forma mais eficiente.

Acompanhe a seguir uma análise detalhada das vendas realizadas nos últimos meses.
""")

# Carregar os dados
data = pd.read_csv('../Atividade aula 1/sales_data.csv')

# Limpeza básica: remover duplicatas
data = data.drop_duplicates()

st.subheader("Visão Geral dos Dados")
st.write(data.head())

st.markdown("#### Estatísticas Descritivas")
st.write(data.describe())

# Vendas totais por categoria
st.subheader("Vendas Totais por Categoria")
sales_by_category = data.groupby('Category')['Total_Sales'].sum().reset_index()
fig_cat = px.bar(sales_by_category, x='Category', y='Total_Sales', title='Vendas Totais por Categoria')
st.plotly_chart(fig_cat)
st.markdown("Podemos observar quais categorias geram mais receita.")

# Evolução das vendas ao longo do tempo
st.subheader("Evolução das Vendas ao Longo do Tempo")
sales_by_date = data.groupby('Date_Sold')['Total_Sales'].sum().reset_index()
fig_time = px.line(sales_by_date, x='Date_Sold', y='Total_Sales', title='Vendas Totais por Data')
st.plotly_chart(fig_time)
st.markdown("Aqui vemos a tendência de vendas ao longo do tempo.")

# Produtos mais vendidos
st.subheader("Top 10 Produtos Mais Vendidos (por receita)")
top_products = data.groupby('Product_Name')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False).head(10)
fig_prod = px.bar(top_products, x='Product_Name', y='Total_Sales', title='Top 10 Produtos Mais Vendidos')
st.plotly_chart(fig_prod)
st.markdown("Esses são os produtos que mais geraram receita no período analisado.")

# Fim do storytelling
st.success("Essas análises ajudam a entender o desempenho de vendas e identificar oportunidades de negócio.")
