#!/bin/bash

# Script para executar o frontend AlugAI

echo "🏠 Iniciando AlugAI Frontend..."
echo ""

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale o Python 3.8 ou superior."
    exit 1
fi

# Verificar se o Streamlit está instalado
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "📦 Instalando dependências..."
    pip install -r requirements.txt
fi

# Executar o aplicativo
echo "🚀 Iniciando aplicativo Streamlit..."
echo "📱 Acesse: http://localhost:8501"
echo ""

streamlit run app.py

