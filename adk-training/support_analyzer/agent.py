from pydantic import BaseModel
from google.adk.agents.llm_agent import Agent

class SupportAnalysis(BaseModel):
    category: str
    sentiment: str
    summary:str

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description="A helpful assistant for analyze the user's support ticket",
    instruction="""
      You are a customer support triage agent. 
      Your purpose is to read the user's message and categorize it into one of three departments: "billing", "technical", or "general".
      You must also determine the sentiment as  "positive" or "negative" or "neutral".
      Only respond with a one sentence summary of the user's issue.

      Example User Input: "My screen is completely broken and I'm very angry about it!" 
      Example Agent Output: Category: technical, sentiment: high

    """,
    output_schema=SupportAnalysis,
    output_key="last_ticket_analysis"
)
