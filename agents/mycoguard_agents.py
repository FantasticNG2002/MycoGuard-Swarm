# /agents/mycoguard_agents.py 
from google.adk.agents import Agent

# Cell 7
data_auditor_agent = Agent(name="data_auditor_agent", instruction="...")
classifier_forge_agent = Agent(...)
safety_validator_agent = Agent(...)
router_agent = Agent(...)

worker_agents = {
    "data_auditor_agent": data_auditor_agent,
    "classifier_forge_agent": classifier_forge_agent,
    "safety_validator_agent": safety_validator_agent,
}
