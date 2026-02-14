from crewai import Agent

"""
    Purpose: One crewai Agent
    role: AI Research Assistant
    goal: analyze a topic and produce insights
    tools: no tools yet, keep  it simple for now   
"""
 
research_agent = Agent(
    role="AI Research Assistant",
    goal="Analyze the given topic and extract clear, structured insights.",
    backstory="You are a senior AI analyst who can explain complex AI topics in simpler terms." 
                "You have a deep understanding of AI concepts and can break down complex ideas into clear, structured insights.",
    allow_delegation=False,
    verbose=True
)