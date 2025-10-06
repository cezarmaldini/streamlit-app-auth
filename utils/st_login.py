import streamlit as st
import streamlit_antd_components as sac

def st_login():
# Tela de login
    left, center, right = st.columns([1,2, 1])
    with center:
        st.title("🎯 Tático Soluções")
        st.info("🔐 Faça login para acessar a aplicação")
                
        st.subheader("Bem-vindo!")
        st.write("""
        Esta é uma aplicação protegida com Microsoft Entra ID.
                
        **Recursos disponíveis após login:**
        - Chatbot IA
        - Upload de Propostas
        - Perfil do usuário
        """)
                
        sac.buttons(
                items=[
                    sac.ButtonsItem(label='Entrar com Microsoft', icon='microsoft'),
                    sac.ButtonsItem(label='')
                ],
                label='',
                description='Clique no botão abaixo para fazer login.',
                align='center',
                direction='horizontal',
                index=None,
                variant='text',
                key='btn_microsoft'
            )

        if st.session_state['btn_microsoft'] == 'Entrar com Microsoft':
            try:
                st.login(provider="microsoft")
            except Exception as e:
                st.error(f"Erro no login: {e}")
                st.info("Verifique se as credenciais estão corretas no secrets.toml")