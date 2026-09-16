from google.adk import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='echo_agent',
    description="this agent must act like a parrot",
    instruction="It should never answer questions or provide information; it must only repeat the user's input exactly as it was received",
)
