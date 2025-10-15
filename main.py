from agents import Agent, Runner,trace, input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
from connection import config
import requests
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
from pydantic import BaseModel
import sys
import os
# import rich

load_dotenv()

class UserOutput(BaseModel):
    response: str
    isProblem: bool

input_guard_agent = Agent(
    name = "Input Guard Agent",
    instructions = "You are Input Guardrail agent. your task is to validate the user's prompt or input and check weather the user is asking for a legal and ethical work and didn't ask for any hacking related questions or asking for generating any kind ok serial key. If user does ask for hacking or any serial key or any work that is illegal and unethical then politely say sorry and tell them that you can't do it.",
    output_type= UserOutput

)


@input_guardrail
async def security_guardrail(ctx, agent, input):
    result = Runner.run_streamed(
        input_guard_agent,
        input,
        run_config = config
    )
    final_output = ''
    async for event in result.stream_events():
        if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
            final_output += event.data.delta

    final_response = result.final_output
    # print(final_response.response)

    return GuardrailFunctionOutput(
        output_info= result.final_output.response,
        tripwire_triggered= result.final_output.isProblem
    )


basic_querry_agent = Agent(
    name = "Basic Querry Agent",
    instructions = """You are a best basic querry agent. your task is to solve user's basic querry's like if user wants to add two numbers or ask for some science questions or ask any questions related to some other fields. you are free to solve any querry to user.
    """
)
coding_agent = Agent(
    name = "Coding Agent",
    instructions = """You are a best coding agent. your task is to write and explain the code to user which user ask for. you can create any app or website or any program weather it is small, easy or complex. just do and explain coding for user in any language in which user wants to do.
    """
)


async def get_user_input_interactive(prompt_text="\nEnter prompt:\n "):
    """Run built-in input() in a thread so it doesn't block the event loop."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, lambda: input(prompt_text))


async def main():

    triage_agent = Agent(
        name = 'Triage Agent',
        instructions =
        """ You are a best querry analyzer your task is to analyze the querry of the user. If the user wants to ask any basic or any sort of querry delegate the task to basic querry agent. If the poetry is Narrative delegate the poetry to the narrative poetry agent. If the poetry is dramatic delegate the poetry to narrative agent. If the poetry is not in any of these categories then gracefully apologies the user. 
        """,
        handoffs= [basic_querry_agent, coding_agent],
        input_guardrails= [security_guardrail]
    )

    print("🚀 AI CLI is ready! Type 'exit' or 'quit' to close.\n")

    # if len(sys.argv) > 1:
    #     user_input = " ".join(sys.argv[1:])
    # else:
    #     user_input = await get_user_input_interactive()
    while True:
        try:
            user_input = await get_user_input_interactive()

            if user_input.lower().strip() in {'exit', 'quit'}:
                print("👋 Exiting the session. Goodbye!")
                break
            try:
                result = Runner.run_streamed(
                    triage_agent, 
                    input = user_input,
                    run_config=config
                )
                async for event in result.stream_events():
                    if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
                        print(event.data.delta, end="", flush=True)
            except InputGuardrailTripwireTriggered:
                print("Sorry, I can't help you with that.")
        except (KeyboardInterrupt, asyncio.CancelledError):
            print("\n👋 Session closed by user.")
            break

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("\n👋 Session closed by user.")