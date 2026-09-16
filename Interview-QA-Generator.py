from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


# -----------------------------------------
# Model
# -----------------------------------------

model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)


# -----------------------------------------
# Pydantic Output Schema
# -----------------------------------------

class Question(BaseModel):

    question: str = Field(
        description="The multiple choice question"
    )

    choices: list[str] = Field(
        description="Exactly 4 choices for the question"
    )

    answer: str = Field(
        description="The correct answer"
    )


class QA(BaseModel):

    questions: list[Question] = Field(
        description="Exactly 5 multiple choice questions"
    )


# -----------------------------------------
# Parser
# -----------------------------------------

parser = PydanticOutputParser(
    pydantic_object=QA
)


# -----------------------------------------
# Prompt
# -----------------------------------------

prompt = PromptTemplate(
    template="""
Generate exactly 5 multiple choice questions.

Role:
{role}

Experience:
{experience} years

Topic:
{topic}

Difficulty:
{difficulty}

Requirements:

1. Generate exactly 5 questions.
2. Each question must have exactly 4 choices.
3. Each question must have one correct answer.
4. Questions should be appropriate for the given role.
5. Questions should match the requested difficulty.
6. Questions should be related to the given topic.
7. Do NOT return the JSON schema.
8. Do NOT return explanations.
9. Return ONLY the final JSON object.
10. Follow the required format exactly.

{format_instructions}
""",

    input_variables=[
        "role",
        "experience",
        "topic",
        "difficulty"
    ],

    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


# -----------------------------------------
# User Input
# -----------------------------------------

role = input("Enter a role: ")

experience = input("Enter experience: ")

topic = input("Enter a topic: ")

difficulty = input("Enter a difficulty level: ")


# -----------------------------------------
# Chain
# -----------------------------------------

chain = prompt | model | parser


# -----------------------------------------
# Invoke
# -----------------------------------------

response = chain.invoke({
    "role": role,
    "experience": experience,
    "topic": topic,
    "difficulty": difficulty
})

for i, question in enumerate(response.questions,1):

    print(f"\nQuestion {i}")
    print("-" * 50)

    print(question.question)

    print("\nChoices:")

    for choice in question.choices:
        print(f"- {choice}")

    print("\nCorrect Answer:")
    print(question.answer)

    print("-" * 50)

