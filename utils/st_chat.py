import streamlit as st
import requests
import json
from typing import Generator

class ChatBot:
    def __init__(self, api_base_url: str = "http://localhost:8001"):
        self.api_base_url = api_base_url
        self.stream_endpoint = f"{api_base_url}/llm/stream"
    
    def send_message(self, message: str, limit: int = 5) -> Generator[str, None, None]:
        """Envia mensagem para a API e retorna stream da resposta"""
        payload = {
            "query": message,
            "limit": limit,
            "model": "gpt-4o-mini",
            "temperature": 0.1,
            "max_output_tokens": 1000
        }
        
        try:
            response = requests.post(
                self.stream_endpoint,
                json=payload,
                headers={"Accept": "text/event-stream"},
                stream=True
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data = line[6:]  # Remove 'data: ' prefix
                        if data:
                            yield data
                            
        except requests.exceptions.RequestException as e:
            yield json.dumps({"type": "error", "message": f"Erro de conexão: {str(e)}"})

def parse_stream_data(data: str) -> dict:
    """Parse dos dados do stream"""
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {"type": "unknown", "data": data}

def st_chat():
    """Componente de chat para Streamlit"""
    
    # Inicializar chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = ChatBot()
    
    # Inicializar histórico de mensagens
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Inicializar documentos fonte
    if 'source_documents' not in st.session_state:
        st.session_state.source_documents = []
    
    # Exibir histórico de mensagens
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input do usuário
    if prompt := st.chat_input("Digite sua pergunta..."):
        # Adicionar mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Exibir mensagem de assistente com placeholder
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            source_documents = []
            
            # Processar stream da resposta
            for stream_data in st.session_state.chatbot.send_message(prompt):
                parsed_data = parse_stream_data(stream_data)
                
                if parsed_data["type"] == "source_documents":
                    source_documents = parsed_data.get("documents", [])
                    st.session_state.source_documents = source_documents
                
                elif parsed_data["type"] == "text_delta":
                    full_response += parsed_data.get("delta", "")
                    message_placeholder.markdown(full_response + "▌")
                
                elif parsed_data["type"] == "text_done":
                    message_placeholder.markdown(full_response)
                
                elif parsed_data["type"] == "stream_completed":
                    break
                
                elif parsed_data["type"] == "error":
                    error_msg = parsed_data.get("message", "Erro desconhecido")
                    message_placeholder.error(f"Erro: {error_msg}")
                    full_response = error_msg
                    break
            
            # Garantir que a resposta final seja exibida
            message_placeholder.markdown(full_response)
        
        # Adicionar resposta ao histórico
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # Exibir documentos fonte se existirem
    if st.session_state.source_documents:
        with st.expander("📄 Documentos Fonte"):
            for i, doc in enumerate(st.session_state.source_documents):
                st.markdown(f"**Documento {i+1}**")
                st.text(doc.get("page_content", "")[:500] + "..." if len(doc.get("page_content", "")) > 500 else doc.get("page_content", ""))
                if doc.get("metadata"):
                    st.caption(f"Metadados: {doc.get('metadata')}")
                st.divider()

def clear_chat():
    """Limpa o histórico do chat"""
    st.session_state.messages = []
    st.session_state.source_documents = []