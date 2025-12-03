"""
AlugAI - Sistema de Precificação de Aluguel de Imóveis
Frontend desenvolvido em Streamlit
Página Principal (Home)
"""

import streamlit as st
from pathlib import Path
import sys

# Adiciona o diretório raiz ao path para importações
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

from utils import config, helpers

# Configuração da página
config.set_page_config()
config.apply_custom_css()

# Inicialização de sessão
if 'consultas' not in st.session_state:
    st.session_state.consultas = []
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []

# Sidebar comum para todas as páginas
with st.sidebar:
    # Tentar carregar logo
    logo_path = current_dir.parent / "docs" / "assets" / "logo_agente.png"
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.title("🏠 AlugAI")
    
    st.markdown("---")
    st.markdown("### 💡 Dica")
    st.info("Use o formulário de busca para encontrar imóveis que atendam suas preferências!")
    
    st.markdown("---")
    st.markdown("### 📞 Suporte")
    st.markdown("Dúvidas? Entre em contato através da página **Sobre**")

# Conteúdo da página inicial
# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    logo_path = current_dir.parent / "docs" / "assets" / "logo_agente.png"
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.title("🏠 AlugAI")
    st.markdown("<h1 style='text-align: center;'>Bem-vindo ao AlugAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em; color: #666;'>Sistema Inteligente de Precificação de Aluguel de Imóveis no Distrito Federal</p>", unsafe_allow_html=True)

st.markdown("---")

# Seção de apresentação
st.markdown("""
## 🎯 Sobre o Projeto

O **AlugAI** é uma plataforma inovadora que utiliza **Inteligência Artificial** para estimar o valor justo 
de aluguel de imóveis na região do **Distrito Federal**. Nosso objetivo é reduzir a assimetria de informação 
entre locadores e locatários, promovendo **transparência e eficiência** no mercado imobiliário.
""")

# Cards de funcionalidades principais
st.markdown("### 🚀 Funcionalidades Principais")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='padding: 1.5rem; background-color: #f8f9fa; border-radius: 10px; height: 100%;'>
        <h3>🔍 Busca Inteligente</h3>
        <p>Encontre imóveis que atendam suas preferências com filtros avançados e classificação automática de custo-benefício.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 1.5rem; background-color: #f8f9fa; border-radius: 10px; height: 100%;'>
        <h3>💰 Estimativa Precisa</h3>
        <p>Obtenha estimativas de preço baseadas em modelos de Machine Learning treinados com dados reais do mercado.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='padding: 1.5rem; background-color: #f8f9fa; border-radius: 10px; height: 100%;'>
        <h3>📊 Análises Regionais</h3>
        <p>Visualize comparativos de preços por região e entenda as tendências do mercado imobiliário.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Estatísticas rápidas
st.markdown("### 📈 Estatísticas do Sistema")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Imóveis Cadastrados", "1.250+", "↗️ +50 este mês")

with col2:
    st.metric("Precisão do Modelo", "92.5%", "↗️ +2.1%")

with col3:
    st.metric("Consultas Realizadas", "3.450+", "↗️ +120 hoje")

with col4:
    st.metric("Bairros Cobertos", "22", "↗️ +2 novos")

st.markdown("---")

# Como usar
st.markdown("### 🎓 Como Usar")

steps = [
    {
        "icon": "1️⃣",
        "title": "Defina suas Preferências",
        "description": "Use o formulário de busca para informar características desejadas (área, quartos, localização, etc.)"
    },
    {
        "icon": "2️⃣",
        "title": "Visualize os Resultados",
        "description": "Veja imóveis filtrados e classificados automaticamente como vantajosos ou não"
    },
    {
        "icon": "3️⃣",
        "title": "Obtenha Estimativas",
        "description": "Consulte o preço estimado pelo modelo de IA e compare com o preço anunciado"
    },
    {
        "icon": "4️⃣",
        "title": "Analise e Decida",
        "description": "Use as análises de custo-benefício e comparativos regionais para tomar sua decisão"
    }
]

for i, step in enumerate(steps):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"<h2 style='text-align: center;'>{step['icon']}</h2>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"**{step['title']}**")
        st.markdown(step['description'])
    
    if i < len(steps) - 1:
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

# Call to action
st.markdown("### 🎯 Comece Agora!")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.info("💡 Use o menu lateral para navegar entre as páginas!")

