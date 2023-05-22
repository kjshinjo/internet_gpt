import os
os.environ["GOOGLE_API_KEY"] = '...'
os.environ["GOOGLE_CSE_ID"] = '...'
os.environ["OPENAI_API_KEY"] = '...'

from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent

search = GoogleSearchAPIWrapper()
tools = [
    Tool(
        name = 'search',
        func =search.run,
        description = 'useful for when you need an answer to a question'
    ),
    
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = ChatOpenAI(temperature=0)
agent_chain = initialize_agent(tools,llm, agent="chat-conversational-react-description",
                              verbose=True, memory=memory)


exit_command = 'exit'
while True:
    user_input = input("Ask a quesiton or type 'exit' to quit:")
    if user_input == exit_command:
        print('Thank you, Goodbye!')
        break
    else:
        answer = agent_chain.run(input = user_input)
        print(answer)
