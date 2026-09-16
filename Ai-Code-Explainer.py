
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from prompt import prompt


model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

prompt = PromptTemplate(
   template=prompt,
   input_variables=['language','level','code']
)

language = input("enter a languge: ")
level = input("enter a level: ")
code = input("enter a code: ")


chain = prompt | model | StrOutputParser()

result = chain.invoke({'language':language,'level':level,'code':code})

print(result)
