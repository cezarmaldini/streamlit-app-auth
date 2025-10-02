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
        # Mostrar botão de login
        st.info("🔐 Faça login para acessar a aplicação")
        
        # Iniciar processo de login
        try:
            st.login(provider="microsoft")
        except Exception as e:
            st.error(f"Erro no login: {e}")
            st.info("Verifique se as credenciais estão corretas no secrets.toml")
        
    else:
        # Usuário está logado - mostrar informações e conteúdo
        st.success(f"✅ Logado como: **{st.user.name}**")
        st.write(f"**Email:** {st.user.email}")
        
        # Botão de logout
        if st.button("🚪 Sair"):
            st.logout()
            st.rerun()
        
        # Conteúdo protegido da aplicação
        st.header("🎉 Bem-vindo à aplicação!")
        st.write("Aqui está o conteúdo protegido da sua aplicação.")
        
        # Exemplo de dados
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Informações do Usuário")
            user_data = {
                "Nome": st.user.name,
                "Email": st.user.email,
                "Logado desde": st.session_state.get('login_time', 'N/A')
            }
            st.json(user_data)
        
        with col2:
            st.subheader("Ações")
            if st.button("📊 Ver Dashboard"):
                st.success("Abrindo dashboard...")
            
            if st.button("👥 Gerenciar Perfil"):
                st.info("Funcionalidade de perfil em desenvolvimento")

if __name__ == "__main__":
    main()