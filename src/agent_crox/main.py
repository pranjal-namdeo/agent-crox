"""
agent_crox.main

Entry point for running Agent Crox.

Responsibilities:
- load environment variables from .env (local dev only)
- build an LLM backend (Ollama or OpenAI) via llm_factory
- build the Crew with that LLM (compatible across CrewAI versions)
- run the crew and print the output
"""

from dotenv import load_dotenv

from agent_crox.configs.llm_factory import build_llm
from agent_crox.crews.research_crew import build_research_crew


def run() -> None:
    # Local development convenience. In production, env vars come from the host.
    load_dotenv(override=True)

    llm = build_llm()
    research_crew = build_research_crew(llm)

    result = research_crew.kickoff(
        inputs={"topic": "Agentic AI in healthcare"},
    )

    print("\n=== FINAL OUTPUT ===")
    print(result)


if __name__ == "__main__":
    run()
