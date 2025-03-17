import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, poisson
from pathlib import Path

# Configuração do layout
st.set_page_config(page_title="CP-01-Gabriel-Borba", layout="wide")

# Sidebar para navegação
st.sidebar.title("Navegação")
aba = st.sidebar.radio("Escolha uma página:", ["Home", "Formação e Experiência", "Skills", "Análise de Dados"])

# ---- HOME ----
if aba == "Home":
    st.title("\U0001F44B Bem-vindo ao Meu Dashboard Profissional")
    
    # Foto de Perfil
    if Path("foto.jpg").exists():
        st.image("foto.jpg", width=300, caption="Gabriel Borba")
    else:
        st.warning("Imagem de perfil não encontrada.")
    
    st.write("""
    Olá! Meu nome é **Gabriel Borba** e sou estudante de **Engenharia de Software na FIAP**.
    Tenho grande interesse em **Análise de Dados** e **Desenvolvimento Web**, sempre buscando aprimorar minhas habilidades e aplicar tecnologia de forma inovadora.
    
    Este dashboard foi criado para apresentar meu perfil profissional, destacando minha formação, certificações, projetos e habilidades.
    Além disso, trago uma análise de dados aplicada a um problema real de mercado, utilizando técnicas estatísticas e visuais interativos.
    
    Explore as abas para conhecer mais sobre minha trajetória e minhas competências! 🚀📊
    """)
    
    # Botões para LinkedIn e GitHub
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<a href="https://www.linkedin.com/in/gabriel-borba-b79777292/" target="_blank">'
            '<button style="background-color:#0077b5;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:16px;cursor:pointer;">'
            '🔗 LinkedIn</button></a>', unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<a href="https://github.com/borbaaxz" target="_blank">'
            '<button style="background-color:#24292e;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:16px;cursor:pointer;">'
            '🐙 GitHub</button></a>', unsafe_allow_html=True
        )
    
    # Botão para Download do Currículo
    st.markdown("---")
    st.subheader("📄 Baixe meu currículo")
    
    with open("curriculo.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Currículo",
            data=file,
            file_name="Gabriel_Borba_Curriculo.pdf",
            mime="application/pdf"
        )

# ---- FORMAÇÃO E EXPERIÊNCIA ----
elif aba == "Formação e Experiência":
    st.title("📚 Formação Acadêmica e Experiência")
    
    st.subheader("🎓 Formação Acadêmica")
    st.write("""
    - **Engenharia de Software** - FIAP (2024 - 2027)
      - Foco em desenvolvimento de software, análise de dados, inteligência artificial e gestão de projetos.
    """)
    
    st.subheader("📜 Certificações")
    st.write("""
    - Gestão Financeira de Empresas - FIAP  
    - Análise de Dados com Python  
    - Gestão Ágil e Design Thinking - FIAP  
    - Cybersecurity Fundamentals - FIAP  
    """)
    
    st.subheader("💼 Experiência Profissional e Projetos")
    st.write("""
    - **Desenvolvimento de um Site Institucional para o Hospital das Clínicas**  
      - Projeto acadêmico em parceria com o hospital, focado na acessibilidade e experiência do usuário.  

    - **Sistema de Gestão Ágil para Projeto Literário**  
      - Criação de um sistema baseado no Trello para gerenciar um livro de ficção científica.  

    - **Dashboard Profissional Interativo (Projeto CP1 - FIAP)**  
      - Desenvolvimento de um dashboard utilizando Streamlit e Python para análise de dados e apresentação de perfil profissional.  
    """)

# ---- SKILLS ----
elif aba == "Skills":
    st.title("🛠️ Minhas Skills")
    st.write("Abaixo estão algumas das minhas principais habilidades e o nível de proficiência em cada uma:")
    
    skills = {
        "Python": 90,
        "JavaScript": 85,
        "React": 80,
        "SQL": 75,
        "Power BI": 70,
        "Git": 90,
        "Excel": 80,
        "Streamlit": 85,
        "Tailwind": 70,
    }
    
    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(level / 100)

# ---- ANÁLISE DE DADOS ----
elif aba == "Análise de Dados":
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

        # Verifica se existem colunas numéricas
        if not col_numericas.empty:
            # 1. **Matriz de Correlação**
            st.subheader("1. Correlação entre as variáveis numéricas")
            correlation_matrix = df[col_numericas].corr()
            st.write("Matriz de correlação:")
            st.dataframe(correlation_matrix)

            plt.figure(figsize=(10, 6))
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
            plt.title("Matriz de Correlação")  # Título para a heatmap
            st.pyplot(plt)

            # 2. **Distribuição Normal**
            st.subheader("2. Distribuição Normal de uma variável numérica")
            var = col_numericas[0]  # Pegando a primeira coluna numérica
            mean_val = df[var].mean()
            std_val = df[var].std()

            x = np.linspace(df[var].min(), df[var].max(), 100)
            p_normal = norm.pdf(x, mean_val, std_val)
            plt.figure(figsize=(10, 5))
            plt.plot(x, p_normal, 'k', linewidth=2)
            plt.title(f"Distribuição Normal de {var}")  # Título para o gráfico
            plt.xlabel(var)
            plt.ylabel("Densidade de Probabilidade")
            st.pyplot(plt)

            # 3. **Distribuição Poisson**
            st.subheader("3. Distribuição Poisson de uma variável numérica")
            lambda_poisson = df[var].mean()
            p_poisson = poisson.pmf(np.arange(0, 15), lambda_poisson)
            plt.figure(figsize=(10, 5))
            plt.bar(np.arange(0, 15), p_poisson, color='orange')
            plt.title(f"Distribuição Poisson de {var}")  # Título para o gráfico
            plt.xlabel(var)
            plt.ylabel("Probabilidade")
            st.pyplot(plt)

            # 4. **Análise de Outliers**
            st.subheader("4. Análise de Outliers")
            st.write("Verificando outliers para as colunas numéricas utilizando o boxplot.")
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=df[col_numericas])
            plt.title("Análise de Outliers nas Variáveis Numéricas")
            st.pyplot(plt)

            # 5. **Insights sobre os Dados**
            st.subheader("5. Insights sobre os Dados")
            st.write("""
            - A partir da análise de correlação, podemos observar quais variáveis têm relações fortes ou fracas entre si.
            - A distribuição normal é uma boa forma de verificar a normalidade de uma variável. Se os dados seguem uma forma de sino, isso pode indicar normalidade.
            - A distribuição Poisson é útil para modelar eventos que ocorrem em intervalos de tempo fixos. Se a variável seguir esse padrão, podemos usá-la para prever a probabilidade de ocorrência de certos eventos.
            - A análise de outliers com o boxplot ajuda a identificar valores que se distanciam significativamente da média, o que pode ser importante para compreender a variabilidade dos dados.
            """)

        else:
            st.warning("Não há colunas numéricas suficientes para calcular a correlação. Verifique os tipos de dados das colunas.")
    else:
        st.error(f"Arquivo **{excel_path}** não encontrado. Certifique-se de que o arquivo está na mesma pasta do código.")

#  🔹 3. Executando o Dashboard
# No terminal, rode:  
# pip install streamlit pandas numpy matplotlib seaborn scipy
# ```sh
# streamlit run dashboard.py
# pip install openpyxl
#pip install streamlit pandas numpy matplotlib seaborn scipy openpyxl
