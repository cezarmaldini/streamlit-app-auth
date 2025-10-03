import streamlit as st

def st_login():
# Tela de login
    st.info("🔐 Faça login para acessar a aplicação")
            
    st.subheader("Bem-vindo!")
    st.write("""
    Esta é uma aplicação protegida com Microsoft Entra ID.
            
    **Recursos disponíveis após login:**
    - Chatbot IA
    - Upload de Propostas
    - Perfil do usuário
    """)

    st.subheader("Login")
    st.write("Clique no botão abaixo para fazer login:")
            
    # Botão de login centralizado
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🚀 Entrar com Microsoft", 
                        type="primary", 
                        use_container_width=True,
                        key="login_button"):
            try:
                st.login(provider="microsoft")
            except Exception as e:
                st.error(f"Erro no login: {e}")
                st.info("Verifique se as credenciais estão corretas no secrets.toml")