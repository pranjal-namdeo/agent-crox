from crewai import Crew
from agent_crox.agents.research_agent import research_agent
from agent_crox.tasks.research_task import research_task

research_crew = Crew(
    agents= [research_agent],
    tasks= [research_task],
    verbose = True 
)