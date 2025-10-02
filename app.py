import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# Configurar a página
st.set_page_config(
    page_title="Tático Soluções",
    page_icon="🎯",
    layout='wide'
)

def main():
    st.title("🎯 Tático Soluções")
    
    # Verificar se o usuário está logado
    if not st.user.is_logged_in:
        # Tela de login
        st.info("🔐 Faça login para acessar a aplicação")
            
        st.subheader("Bem-vindo!")
        st.write("""
        Esta é uma aplicação protegida com Microsoft Entra ID.
            
        **Recursos disponíveis após login:**
        - 🤖 Chatbot IA
        - 📃 Upload de Propostas
        - 👤 Perfil do usuário
        """)

        st.subheader("Login")
        st.write("Clique no botão abaixo para fazer login:")
            
        # Botão de login centralizado
        if st.button("🚀 Entrar com Microsoft", 
                        type="primary", 
                        use_container_width=True,
                        key="login_button"):
            try:
                st.login(provider="microsoft")
            except Exception as e:
                st.error(f"Erro no login: {e}")
                st.info("Verifique se as credenciais estão corretas no secrets.toml")
        
    else:
        # Usuário está logado - mostrar informações e conteúdo
        st.success(f"✅ Logado como: **{st.user.name}**")
        st.write(f"**Email:** {st.user.email}")
        
        # Sidebar com informações do usuário
        with st.sidebar:
            option = option_menu(
                menu_title="Navegação",
                options=["Chatbot", "Upload"],
                icons=["robot", "folder-plus"],
                menu_icon="card-list",
                default_index=0
            )
            st.subheader("👤 Perfil")
            st.write(f"**Nome:** {st.user.name}")
            st.write(f"**Email:** {st.user.email}")
            
            # Botão de logout na sidebar
            if st.button("Sair", use_container_width=True):
                st.logout()
                st.rerun()
        
        # Conteúdo protegido da aplicação
        st.header("🎉 Bem-vindo à aplicação!")
        st.write("Aqui está o conteúdo protegido da sua aplicação.")
        
        # Exemplo de abas com conteúdo
        tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "👤 Meu Perfil", "⚙️ Configurações"])
        
        with tab1:
            st.subheader("Dashboard Principal")
            st.write("**Métricas do usuário:**")
            
            # Exemplo de métricas
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Acessos Hoje", "12", "+3")
            with col2:
                st.metric("Tarefas", "8", "-2")
            with col3:
                st.metric("Desempenho", "87%", "+5%")
            
            st.divider()
            st.write("**Atividades recentes:**")
            st.info("Conteúdo personalizado do dashboard aqui...")
        
        with tab2:
            st.subheader("Meu Perfil")
            
            # Informações do usuário em formato mais organizado
            profile_data = {
                "Nome completo": st.user.name,
                "Email": st.user.email,
                "ID do usuário": getattr(st.user, 'id', 'N/A'),
                "Data de login": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            
            for key, value in profile_data.items():
                st.write(f"**{key}:** {value}")
            
            # Opções de perfil
            st.divider()
            st.subheader("Configurações do Perfil")
            if st.button("🔄 Atualizar Perfil"):
                st.info("Funcionalidade em desenvolvimento")
        
        with tab3:
            st.subheader("Configurações da Aplicação")
            st.write("Configurações personalizadas baseadas no seu perfil:")
            
            # Exemplo de configurações
            setting1 = st.checkbox("Receber notificações por email", value=True)
            setting2 = st.selectbox("Tema da aplicação", ["Claro", "Escuro", "Automático"])
            setting3 = st.slider("Notificações por dia", 1, 20, 5)
            
            if st.button("💾 Salvar Configurações"):
                st.success("Configurações salvas com sucesso!")

if __name__ == "__main__":
    main()