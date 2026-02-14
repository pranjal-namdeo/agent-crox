"""
Docstring for agent_crox.main_
My entry point for running the research crew

what should  it do? 
-   accept an input topic
-   run the crew
-   print output
"""
import os

os.environ["LITELLM_LOCAL_PROXY"] = "False"
os.environ["LITELLM_MODE"] = "production"
os.environ["OPENAI_API_KEY"] = "NA"

import litellm


# 1. Disable all the background "noise"
litellm.telemetry = False
litellm.add_standard_logging_metadata = False
litellm.set_verbose = False
litellm.suppress_debug_info = True

# 2. THE ULTIMATE FIX: Empty the callback lists 
# This stops LiteLLM from even LOOKING for apscheduler/fastapi/logging
litellm.callbacks = []
litellm._logging_metadata = {}
litellm.success_callback = []
litellm.failure_callback = []

# 3. Environment Variables
os.environ["LITELLM_LOCAL_PROXY"] = "False"
os.environ["OPENAI_API_KEY"] = "NA"

# 4. Now it is safe to import your crew

from crewai import LLM

#  Set a "fake" key so CrewAI doesn't complain- Im gonna be using ollama for local testing, which doesn't require an API key. In production, you would set this to your actual OpenAI API key or configure it to work with your local model.(im running low on tokens yo
local_llm = LLM(
    # model="ollama/llama3.2",
    model= "ollama/llama3.2:1b",
    base_url="http://localhost:11434",
    max_tokens=300,
    temperature=0.2,
    timeout=120
)
# Note: I have updated my agents also to make it compatible with local testing - you can see the changes in the research_agent.py file."

# openai_api_key = get_openai_api_key()
# os.environ["OPENAI_API_KEY"] = "NA"
# os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# Now import the crew and run it
from agent_crox.crews.research_crew import research_crew


def run():
    result = research_crew.kickoff(
        inputs = {
            "topic": "Agentic AI in healthcare"
            })
    print("\n=== FINAL OUTPUT ===")
    print(result)

if __name__ == "__main__":
    run()