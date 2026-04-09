import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_huggingface import HuggingFaceEndpoint
from langchain_openai import ChatOpenAI

# ---------------------------
# Default Model Options
# ---------------------------
MODEL_OPTIONS = {
    "OpenAI": ["gpt-4.1-nano", "gpt-4o-mini"],
    "Hugging Face": ["google/flan-t5-base", "mistralai/Mistral-7B-Instruct-v0.2"],
    "Anthropic": ["claude-3-sonnet-20240229", "claude-3-opus-20240229"],
    "Gemini": ["gemini-1.5-pro", "gemini-1.5-flash"],
}


# ---------------------------
# LLM Factory
# ---------------------------
class LLMFactory:
    @staticmethod
    def get_llm(provider: str, model: str, api_key: str, max_tokens: int):
        """Return appropriate LLM instance based on provider"""
        if provider == "OpenAI":
            return ChatOpenAI(model=model, openai_api_key=api_key, max_tokens=max_tokens)

        elif provider == "Hugging Face":
            return HuggingFaceEndpoint(
                repo_id=model,
                huggingfacehub_api_token=api_key,
                task="text-generation",
                max_new_tokens=max_tokens,
            )

        elif provider == "Anthropic":
            from langchain_anthropic import ChatAnthropic
            return ChatAnthropic(model=model, api_key=api_key, max_tokens=max_tokens)

        elif provider == "Gemini":
            from langchain_google_genai import ChatGoogleGenerativeAI
            return ChatGoogleGenerativeAI(
                model=model, google_api_key=api_key, max_output_tokens=max_tokens
            )

        return None


# ---------------------------
# Chat App
# ---------------------------
class ChatApp:
    def __init__(self):
        st.set_page_config(page_title="Multi-Provider Chat", layout="wide")
        st.title("🤖 Multi-Provider Multi-Thread Chat")

        if "threads" not in st.session_state:
            st.session_state.threads = {}

        self.provider = None
        self.api_key = None
        self.model = None
        self.max_tokens = 100
        self.thread_key = None

    def sidebar(self):
        """Sidebar configuration"""
        with st.sidebar:
            st.header("⚙️ Configuration")

            # Provider
            self.provider = st.selectbox(
                "Provider", ["OpenAI", "Hugging Face", "Anthropic", "Gemini"]
            )

            # API Key
            self.api_key = st.text_input("API Key", type="password")

            # Model selection
            if self.provider and self.api_key:
                model_choice = st.selectbox(
                    "Select Model", MODEL_OPTIONS[self.provider] + ["Other"]
                )
                if model_choice == "Other":
                    custom_model = st.text_input("Enter custom model name/repo_id")
                    if custom_model:
                        self.model = custom_model
                        if custom_model not in MODEL_OPTIONS[self.provider]:
                            MODEL_OPTIONS[self.provider].append(custom_model)
                else:
                    self.model = model_choice

            # Max tokens
            self.max_tokens = st.number_input(
                "Max tokens", min_value=10, max_value=2000, value=100, step=10
            )

            # Thread key = provider+model
            if self.provider and self.model:
                new_thread_key = f"{self.provider}-{self.model}"

                if new_thread_key not in st.session_state.threads:
                    st.session_state.threads[new_thread_key] = {"history": []}

                self.thread_key = new_thread_key

            # Switch threads
            if st.session_state.threads:
                selected_thread = st.selectbox(
                    "💬 Switch Chat Thread",
                    list(st.session_state.threads.keys()),
                    index=list(st.session_state.threads.keys()).index(self.thread_key)
                    if self.thread_key in st.session_state.threads
                    else 0,
                )
                self.thread_key = selected_thread

            # Reset current thread
            if self.thread_key and st.button("🗑️ Clear this chat"):
                st.session_state.threads[self.thread_key]["history"] = []

    def handle_message(self, user_input: str):
        """Handle user input and fetch model response"""
        if not self.thread_key:
            st.warning("Please configure provider, API key and model first.")
            return

        # Ensure thread exists
        if self.thread_key not in st.session_state.threads:
            st.session_state.threads[self.thread_key] = {"history": []}

        # Save + render user message immediately
        st.session_state.threads[self.thread_key]["history"].append(
            {"type": "human", "content": user_input}
        )
        st.chat_message("user").write(user_input)

        try:
            llm = LLMFactory.get_llm(
                self.provider, self.model, self.api_key, self.max_tokens
            )
            if not llm:
                raise ValueError("Unsupported provider")

            # Build full message history
            messages = [
                HumanMessage(content=m["content"])
                if m["type"] == "human"
                else AIMessage(content=m["content"])
                for m in st.session_state.threads[self.thread_key]["history"]
            ]

            # Stream AI response
            reply_text = ""
            with st.chat_message("ai"):
                placeholder = st.empty()
                for chunk in llm.stream(messages):
                    token = chunk.content if hasattr(chunk, "content") else str(chunk)
                    reply_text += token
                    placeholder.markdown(reply_text)

            # Save AI reply
            st.session_state.threads[self.thread_key]["history"].append(
                {"type": "ai", "content": reply_text}
            )

        except Exception as e:
            error_msg = f"⚠️ Unable to fetch response: {str(e)}. Try switching model/provider."
            st.session_state.threads[self.thread_key]["history"].append(
                {"type": "ai", "content": error_msg}
            )
            st.error(error_msg)

    def render_chat(self):
        """Render chat history for current thread"""
        if self.thread_key and self.thread_key in st.session_state.threads:
            for msg in st.session_state.threads[self.thread_key]["history"]:
                if msg["type"] == "human":
                    st.chat_message("user").write(msg["content"])
                else:
                    st.chat_message("ai").write(msg["content"])

    def run(self):
        """Run the app"""
        self.sidebar()
        user_input = st.chat_input("Ask me something...")

        if user_input and self.model and self.api_key:
            self.handle_message(user_input)

        self.render_chat()


# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    ChatApp().run()