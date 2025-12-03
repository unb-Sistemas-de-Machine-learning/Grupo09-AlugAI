# 🚀 Guia de Início Rápido - AlugAI Frontend

## Instalação e Execução

### Opção 1: Usando o Script (Recomendado)

**Linux/Mac:**
```bash
cd frontend
./run.sh
```

**Windows:**
```cmd
cd frontend
run.bat
```

### Opção 2: Instalação Manual

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Execute o aplicativo:**
```bash
streamlit run app.py
```

3. **Acesse no navegador:**
```
http://localhost:8501
```

## 📋 Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🎯 Funcionalidades Disponíveis

### 1. 🏠 Início
Página inicial com apresentação do projeto e estatísticas.

### 2. 🔍 Buscar Imóveis
- Formulário completo de busca com filtros avançados
- Classificação automática de custo-benefício
- Listagem de imóveis filtrados

### 3. 💰 Estimativa de Preço
- Formulário para estimar preço de um imóvel específico
- Comparação com preço anunciado (se fornecido)
- Visualização dos fatores que influenciaram a estimativa

### 4. 📊 Comparativo Regional
- Mapa interativo com preços por bairro
- Gráficos comparativos
- Tabela de dados detalhados

### 5. 📜 Histórico
- Visualização de consultas anteriores
- Filtros e ordenação
- Exportação para CSV

### 6. ℹ️ Sobre
Informações sobre o projeto, equipe e tecnologias utilizadas.

## 🔧 Estrutura de Dados

### Campos do Formulário de Busca:
- Tipo de Imóvel (Apartamento, Casa, Cobertura, etc.)
- Bairro
- Área (mínima e máxima)
- Número de Quartos
- Número de Banheiros
- Vagas de Garagem
- Mobiliado (Sim/Não)
- Faixa de Preço

### Campos do Formulário de Estimativa:
- Tipo de Imóvel *
- Bairro *
- Área (m²) *
- Número de Quartos *
- Número de Banheiros *
- Vagas de Garagem
- Mobiliado *
- Condomínio (R$)
- Preço Anunciado (opcional, para comparação)

## 📝 Notas Importantes

- **Dados Mock**: Atualmente, os dados exibidos são simulados para desenvolvimento
- **Histórico**: O histórico é armazenado apenas na sessão atual (não persiste após fechar o navegador)
- **Modelo de ML**: A integração com o modelo real será implementada posteriormente

## 🐛 Solução de Problemas

### Erro ao importar módulos
Certifique-se de estar executando o comando a partir do diretório `frontend`:
```bash
cd frontend
streamlit run app.py
```

### Porta 8501 já em uso
O Streamlit tentará usar a próxima porta disponível automaticamente.

### Dependências não instaladas
Execute:
```bash
pip install -r requirements.txt
```

## 📞 Suporte

Para dúvidas ou problemas, consulte:
- Documentação completa: [Documentação AlugAI](https://unb-sistemas-de-machine-learning.github.io/Grupo09-AlugAI/)
- GitHub do projeto: [Grupo09-AlugAI](https://github.com/unb-sistemas-de-machine-learning/Grupo09-AlugAI)

