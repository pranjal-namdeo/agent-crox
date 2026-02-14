from crewai import Crew, LLM

from agent_crox.agents.research_agent import research_agent
from agent_crox.tasks.research_task import research_task


def build_research_crew(llm: LLM) -> Crew:
    """
    Build a Crew configured with the provided LLM.

    We inject the LLM at construction time because some CrewAI versions
    (pydantic-based) do not allow setting `crew.llm` after creation.
    """
    agents = [research_agent]
    for agent in agents:
        # Some CrewAI versions may fall back to agent-level defaults if present.
        # Ensure the injected runtime LLM is used consistently.
        agent.llm = llm

    return Crew(
        agents=agents,
        tasks=[research_task],
        llm=llm,
        verbose=True,
    )