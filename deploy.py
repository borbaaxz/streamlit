import streamlit as st
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
    import analise  # Importa o script separado para Análise de Dados

#  🔹 3. Executando o Dashboard
# No terminal, rode:  
# pip install streamlit pandas numpy matplotlib seaborn scipy
# ```sh
# streamlit run deploy.py
# pip install openpyxl
#pip install streamlit pandas numpy matplotlib seaborn scipy openpyxl


# git add requirements.txt
# git commit -m "Adicionando matplotlib ao requirements.txt"
# git push origin main