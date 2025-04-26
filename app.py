import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Storytelling: Análise de Vendas", layout="wide")

st.title("📊 Data Storytelling: Análise de Vendas")

# Contexto e história
st.info("""
Imagine que você é o gerente de vendas de uma grande loja varejista. Seu objetivo é entender o desempenho das vendas dos diferentes produtos ao longo do tempo, identificar quais categorias trazem mais receita e descobrir quais produtos são os campeões de vendas.  
Com base nesses dados, será possível tomar decisões estratégicas para aumentar o faturamento, ajustar o estoque e direcionar campanhas promocionais de forma mais eficiente.
""")
st.caption("Acompanhe a seguir uma análise detalhada das vendas realizadas nos últimos meses.")

st.divider()

# Carregar os dados
data = pd.read_csv('./sales_data.csv')
data = data.drop_duplicates()

st.subheader("👀 Visão Geral dos Dados")
st.dataframe(data.head(), use_container_width=True)

st.markdown("#### 📈 Estatísticas Descritivas")
st.write(data.describe())
st.caption(
    "A primeira coluna da tabela acima mostra as métricas estatísticas calculadas para cada coluna numérica do conjunto de dados, como média (mean), desvio padrão (std), valores mínimo e máximo (min, max), e os quartis (25%, 50%, 75%). Essas métricas ajudam a entender a distribuição e a variação dos dados numéricos."
)

st.divider()

# Vendas totais por categoria
st.subheader("🏷️ Vendas Totais por Categoria")
sales_by_category = data.groupby('Category')['Total_Sales'].sum().reset_index()
fig_cat = px.bar(sales_by_category, x='Category', y='Total_Sales', title='Vendas Totais por Categoria', color='Category', text_auto='.2s')
st.plotly_chart(fig_cat, use_container_width=True)
st.markdown("🔎 **Observação:** Podemos observar quais categorias geram mais receita.")

st.divider()

# Evolução das vendas ao longo do tempo
st.subheader("📅 Evolução das Vendas ao Longo do Tempo")
sales_by_date = data.groupby('Date_Sold')['Total_Sales'].sum().reset_index()
fig_time = px.line(sales_by_date, x='Date_Sold', y='Total_Sales', title='Vendas Totais por Data', markers=True)
st.plotly_chart(fig_time, use_container_width=True)
st.markdown("🔎 **Observação:** Aqui vemos a tendência de vendas ao longo do tempo.")

st.divider()

# Produtos mais vendidos
st.subheader("🏆 Top 10 Produtos Mais Vendidos (por receita)")
top_products = data.groupby('Product_Name')['Total_Sales'].sum().reset_index().sort_values(by='Total_Sales', ascending=False).head(10)
fig_prod = px.bar(top_products, x='Product_Name', y='Total_Sales', title='Top 10 Produtos Mais Vendidos', color='Total_Sales', text_auto='.2s')
st.plotly_chart(fig_prod, use_container_width=True)
st.markdown("🔎 **Observação:** Esses são os produtos que mais geraram receita no período analisado.")

st.divider()

st.success("Essas análises ajudam a entender o desempenho de vendas e identificar oportunidades de negócio. 🚀")
