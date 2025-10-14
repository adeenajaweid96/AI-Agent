from agents import Agent , Runner , FunctionTool, function_tool 
from connection import config
import os


agent = Agent(
    name="Assistant",
    instructions= "You are a helpful agent",
  
)

result = Runner.run_sync(
    agent,
    "how much water i need to drink in 1 hour",
    run_config=config
    )
print(result.final_output)