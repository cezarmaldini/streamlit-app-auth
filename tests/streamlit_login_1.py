import streamlit as st

# Configurar a página
st.set_page_config(
    page_title="Streamlit + Microsoft Entra ID",
    page_icon="🔐"
)

def main():
    st.title("🔐 Streamlit + Microsoft Entra ID")
    
    # Verificar se o usuário está logado
    if not st.user.is_logged_in:
        st.info("🔐 Faça login para acessar a aplicação")
        
        # Layout centralizado
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.write("")  # Espaçamento
            st.write("")  # Espaçamento
            
            # Card de login
            with st.container():
                st.subheader("Login Requerido")
                st.write("Para acessar esta aplicação, faça login com sua conta Microsoft.")
                
                # Botão de login grande e centralizado
                if st.button("🔐 Entrar com Microsoft", 
                           type="primary", 
                           use_container_width=True,
                           key="main_login"):
                    try:
                        st.login(provider="microsoft")
                    except Exception as e:
                        st.error(f"Erro no login: {e}")
            
            st.write("")  # Espaçamento
            st.caption("Use suas credenciais corporativas")
        
    else:
        # Usuário logado - interface simples
        st.success(f"✅ Olá, {st.user.name}!")
        
        # Header com informações do usuário
        with st.sidebar:
            st.write(f"**Usuário:** {st.user.name}")
            st.write(f"**Email:** {st.user.email}")
            
            if st.button("🚪 Sair", use_container_width=True):
                st.logout()
                st.rerun()
        
        # Conteúdo principal
        st.header("Bem-vindo à aplicação!")
        st.write("Login realizado com sucesso. Agora você pode acessar todos os recursos.")
        
        # Exemplo de conteúdo
        if st.button("🎯 Acessar Recursos Principais"):
            st.balloons()
            st.success("Recursos carregados com sucesso!")

if __name__ == "__main__":
    main()