import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, poisson
from pathlib import Path

st.title("📊 Análise de Dados Aplicada")

# Caminho do arquivo Excel
excel_path = "wholesale-trade-survey-december-2024-quarter.xlsx"

# Verifica se o arquivo existe antes de carregar
if Path(excel_path).exists():
    df = pd.read_excel(excel_path)
    st.write("### 📌 Dados Carregados")
    st.dataframe(df.head())

    # Exibição dos tipos de dados das colunas para diagnóstico
    st.write("### Tipos de dados das colunas:")
    st.write(df.dtypes)

    # Resumo estatístico dos dados
    st.write("### Resumo Estatístico")
    st.write(df.describe())

    # Tenta forçar a conversão de colunas numéricas
    df = df.apply(pd.to_numeric, errors='coerce')

    # Filtra as colunas numéricas
    col_numericas = df.select_dtypes(include=[np.number]).columns

    if not col_numericas.empty:
        st.subheader("1. Correlação entre as variáveis numéricas")
        correlation_matrix = df[col_numericas].corr()
        st.dataframe(correlation_matrix)

        plt.figure(figsize=(10, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Matriz de Correlação")
        st.pyplot(plt)

        st.subheader("2. Distribuição Normal")
        var = col_numericas[0]
        mean_val = df[var].mean()
        std_val = df[var].std()

        x = np.linspace(df[var].min(), df[var].max(), 100)
        p_normal = norm.pdf(x, mean_val, std_val)
        plt.figure(figsize=(10, 5))
        plt.plot(x, p_normal, 'k', linewidth=2)
        plt.title(f"Distribuição Normal de {var}")
        st.pyplot(plt)

        st.subheader("3. Distribuição Poisson")
        lambda_poisson = df[var].mean()
        p_poisson = poisson.pmf(np.arange(0, 15), lambda_poisson)
        plt.figure(figsize=(10, 5))
        plt.bar(np.arange(0, 15), p_poisson, color='orange')
        plt.title(f"Distribuição Poisson de {var}")
        st.pyplot(plt)

        st.subheader("4. Análise de Outliers")
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df[col_numericas])
        plt.title("Análise de Outliers")
        st.pyplot(plt)

    else:
        st.warning("Não há colunas numéricas suficientes para análise.")

else:
    st.error(f"Arquivo **{excel_path}** não encontrado.")
