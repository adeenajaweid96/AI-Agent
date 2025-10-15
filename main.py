from agents import Agent , Runner ,handoff ,  FunctionTool, function_tool 
from connection import config
import os
import rich
import asyncio
from dotenv import load_dotenv


load_dotenv()


urdu_agent= Agent(
    name="Urdu Agent",
    instructions="Your task is to tell user's query in roman urdu ",


)

triage_agent = Agent(
    name="Triage Agent",
    instructions= "You are a helpful agent, your task is to make decision according to the user query that which agent has to answer and to handoff user query to that agent",
    handoffs=[urdu_agent],
    handoff_description="You need to handsoff to urdu agent when it is needed"

  
)






async def main():
    while True:
            # msg = await asyncio.to_thread(input, "Enter your message here: ")

            msg = input("Enter your message here: ") 


            result = await  Runner.run_sync(triage_agent,msg,run_config=config)
            print(result.final_output)
            print(result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())        