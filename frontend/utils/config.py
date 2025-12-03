"""
Configurações gerais da aplicação Streamlit
"""

import streamlit as st

_page_config_set = False

def set_page_config():
    """Configura as opções da página Streamlit (apenas uma vez)"""
    global _page_config_set
    if not _page_config_set:
        st.set_page_config(
            page_title="AlugAI - Precificação Inteligente de Aluguel",
            page_icon="🏠",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                'Get Help': None,
                'Report a bug': None,
                'About': "AlugAI - Sistema de precificação de aluguel de imóveis no DF"
            }
        )
        _page_config_set = True

def apply_custom_css():
    """Aplica CSS customizado para melhorar a interface"""
    st.markdown("""
    <style>
        /* Estilos gerais */
        .main {
            padding-top: 2rem;
        }
        
        /* Cards customizados */
        .property-card {
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            background-color: #ffffff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .property-card:hover {
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transition: box-shadow 0.3s ease;
        }
        
        /* Badges */
        .badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: 600;
        }
        
        .badge-success {
            background-color: #d4edda;
            color: #155724;
        }
        
        .badge-warning {
            background-color: #fff3cd;
            color: #856404;
        }
        
        .badge-danger {
            background-color: #f8d7da;
            color: #721c24;
        }
        
        .badge-info {
            background-color: #d1ecf1;
            color: #0c5460;
        }
        
        /* Métricas destacadas */
        .metric-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
        }
        
        /* Botões customizados */
        .stButton > button {
            width: 100%;
            border-radius: 5px;
            font-weight: 600;
        }
        
        /* Títulos */
        h1 {
            color: #1f2937;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        h2 {
            color: #374151;
        }
        
        h3 {
            color: #4b5563;
        }
    </style>
    """, unsafe_allow_html=True)

