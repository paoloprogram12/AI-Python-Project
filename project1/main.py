from langchain_core.messages import HumanMessage # langchain is a high level framework that allows us to build AI apps
from langchain_openai import ChatOpenAI # allows us to open AI within langchain and langgraph
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent # complex framework that allows us to build AI agents
from dotenv import load_dotenv # allows us to load environment variables 

# an AI agent has access to tools

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0) # prevents randomness

    # tool is a external service that the agent can call to and utilize
    tools = []
    agent_executor = create_react_agent(model, tools) # prebuilt agent framework

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip() # .strip removes whitespaces

        if (user_input == quit): break

        print("\nAssistant: ", end="")

        # chunks are parts of a response coming from our agent
        for chunk in agent_executor.stream( # stream wte the output
            {"messages": [HumanMessage(content=user_input)]} # passes the user_input message into the AI
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

# runs main function
if __name__ == "__main__":
    main()
