import os
from crewai import LLM


def build_llm() -> LLM:
    provider = os.getenv("LLM_PROVIDER", "ollama").lower().strip()

    if provider == "ollama":
        return LLM(
            model=f"ollama/{os.getenv('OLLAMA_MODEL', 'llama3.2:1b')}",
            base_url=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            max_tokens=300,
            temperature=0.2,
            timeout=120,
        )

    if provider == "openai":
        api_key = (os.getenv("OPENAI_API_KEY") or "").strip()
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing. Set it in your environment or .env.")
        return LLM(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            api_key=api_key,
            max_tokens=300,
            temperature=0.2,
            timeout=120,
        )

    raise ValueError("Invalid LLM_PROVIDER. Use 'ollama' or 'openai'.")