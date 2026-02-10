from crewai import Task
from agent_crox.agents.research_agent import research_agent

"""
    Purpose: one Task
    Input variable : topic
    Output: short, structured explanation
"""

research_task = Task(
    description = "Research and explain the topic: {topic}",
    expected_output = "A clear, structured explanation of topic with key points.",
    agent = research_agent,

)