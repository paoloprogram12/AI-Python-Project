from langchain_core.messages import HumanMessage # langchain is a high level framework that allows us to build AI apps
from langchain_openai import ChatOpenAI # allows us to open AI within langchain and langgraph
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent # complex framework that allows us to build AI agents
from dotenv import load_dotenv # allows us to load environment variables 

# an AI agent has access to tools

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0) # prevents randomness

    tools = []
    agent_executor = create_react_agent(model, tools) # prebuilt agent framework

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip() # .strip removes whitespaces
