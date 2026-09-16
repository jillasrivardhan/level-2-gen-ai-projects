# 🚀 Level 2 Gen AI Projects

A collection of **intermediate-level Generative AI projects** built using **Python, LangChain, and Ollama**.

This repository builds upon the fundamentals learned in Level 1 and focuses on creating more practical AI applications using **prompt engineering, LangChain chains, structured outputs, Pydantic models, and local Large Language Models (LLMs)**.

---

## 📌 Projects Included

| # | Project                    | Description                                                   | Main Concepts                               |
| - | -------------------------- | ------------------------------------------------------------- | ------------------------------------------- |
| 1 | 🤖 AI Code Explainer       | Explains source code according to the user's experience level | Prompt Engineering, LangChain Chains        |
| 2 | 🧠 Interview Q&A Generator | Generates role-specific multiple-choice interview questions   | Structured Output, Pydantic, Output Parsers |

---

# 🧠 Learning Objectives

The goal of this level is to move from simple LLM applications toward more structured and practical Gen AI systems.

You will learn:

* Advanced prompt engineering
* Dynamic prompt templates
* LangChain chains
* Ollama integration
* Local LLM inference
* Structured LLM outputs
* Pydantic models
* `PydanticOutputParser`
* `StrOutputParser`
* Input validation and output validation
* Role-based AI applications
* Building reusable AI workflows

---

# 🛠️ Technologies Used

* 🐍 Python
* 🦜 LangChain
* 🦙 Ollama
* 🧠 Qwen 2.5 3B
* 📦 Pydantic
* 🔗 LangChain Core
* 📝 Prompt Engineering

---

# 📂 Project Structure

```text
Level-2-Gen-AI-Projects/
│
├── Ai-Code-Explainer.py
├── Interview-QA-Generator.py
├── prompt.py
├── requirements.txt
└── README.md
```

---

# 🤖 Project 1 — AI Code Explainer

## 📌 Overview

The **AI Code Explainer** is a Generative AI application that analyzes source code and explains it according to the user's selected programming language and experience level.

The user provides:

* Programming language
* Explanation level
* Source code

The application then uses an Ollama-powered LLM to generate a structured explanation.

---

## 🎯 Features

* Explain code using natural language
* Supports different programming languages
* Beginner-friendly explanations
* Intermediate-level explanations
* Advanced explanations
* Explains code execution flow
* Explains variables and functions
* Explains algorithms and data structures
* Identifies potential issues
* Suggests possible improvements
* Uses different explanation depths based on user level

---

## 🔄 Workflow

```text
User
 │
 ├── Programming Language
 ├── Experience Level
 └── Source Code
        │
        ▼
   PromptTemplate
        │
        ▼
    ChatOllama
        │
        ▼
   StrOutputParser
        │
        ▼
 Code Explanation
```

---

## 🧩 Explanation Levels

### 🟢 Beginner

Designed for users with little programming experience.

The model focuses on:

* Basic terminology
* Simple explanations
* Variables
* Functions
* Loops
* Conditions
* Basic execution flow

---

### 🟡 Intermediate

Designed for developers who understand programming fundamentals.

The explanation focuses on:

* Program logic
* Execution flow
* Functions
* Data structures
* Algorithms
* Important implementation details

---

### 🔴 Advanced

Designed for experienced developers.

The explanation focuses on:

* Architecture
* Algorithms
* Performance
* Complexity
* Edge cases
* Design decisions
* Potential improvements

---

## 📝 Example

### Input

```text
Language:
Python

Level:
Beginner

Code:

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

### AI Explanation

The model can explain:

```text
The code creates a list containing five numbers.

The for loop goes through each number in the list.

During every iteration, the current number is printed.
```

---

# 🧠 Project 2 — Interview Q&A Generator

## 📌 Overview

The **Interview Q&A Generator** creates role-specific multiple-choice interview questions using a local LLM.

The user provides:

* Job role
* Years of experience
* Topic
* Difficulty level

The application generates:

* 5 interview questions
* 4 choices for each question
* Correct answer for each question

---

## 🎯 Features

* Role-specific interview questions
* Experience-based questions
* Topic-based question generation
* Difficulty selection
* Exactly 5 questions
* Exactly 4 choices per question
* One correct answer per question
* Structured output validation
* Pydantic-based response parsing

---

# 🏗️ Structured Output Architecture

The Interview Q&A Generator uses Pydantic to define the expected response structure.

```text
                 User Input
                     │
          ┌──────────┼──────────┐
          │          │          │
        Role     Experience    Topic
          │          │          │
          └──────────┼──────────┘
                     │
                Difficulty
                     │
                     ▼
              PromptTemplate
                     │
                     ▼
                ChatOllama
                     │
                     ▼
           PydanticOutputParser
                     │
                     ▼
                 QA Object
                     │
          ┌──────────┴──────────┐
          │                     │
      Question               Choices
          │                     │
          └──────────┬──────────┘
                     │
                   Answer
```

---

# 📦 Pydantic Output Schema

The project defines the expected output using two Pydantic models.

```python
class Question(BaseModel):

    question: str

    choices: list[str]

    answer: str
```

The complete response contains multiple questions:

```python
class QA(BaseModel):

    questions: list[Question]
```

This allows the LLM response to be validated against a predictable structure.

---

# 🔗 LangChain Chain

The Interview Q&A Generator uses:

```python
chain = prompt | model | parser
```

The pipeline is:

```text
Prompt
   ↓
ChatOllama
   ↓
PydanticOutputParser
   ↓
Validated Python Object
```

This is an important LangChain pattern because each component performs a specific responsibility.

---

# 📊 Example

### Input

```text
Role:
Docker DevOps Engineer

Experience:
1 year

Topic:
Docker

Difficulty:
Easy
```

### Generated Structure

```text
Question 1
--------------------------------------------------
What command is used to list running Docker containers?

Choices:
- docker images
- docker ps
- docker build
- docker pull

Correct Answer:
docker ps
--------------------------------------------------
```

The same structure is generated for five questions.

---

# 🧩 LangChain Concepts Demonstrated

## 1. PromptTemplate

The projects use:

```python
from langchain_core.prompts import PromptTemplate
```

A `PromptTemplate` allows dynamic values to be inserted into a reusable prompt.

Example:

```python
prompt = PromptTemplate(
    template="Explain this {language} code at a {level} level.",
    input_variables=["language", "level"]
)
```

---

## 2. ChatOllama

The projects use Ollama for local LLM inference.

```python
from langchain_ollama import ChatOllama
```

Example:

```python
model = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)
```

This allows the applications to run an LLM locally rather than depending entirely on a cloud API.

---

# 3. StrOutputParser

The Code Explainer uses:

```python
from langchain_core.output_parsers import StrOutputParser
```

The parser converts the model response into a normal string.

```text
LLM Response
     ↓
StrOutputParser
     ↓
String
```

This is useful when the application expects natural-language text.

---

# 4. PydanticOutputParser

The Interview Q&A Generator uses:

```python
from langchain_core.output_parsers import PydanticOutputParser
```

It validates the LLM response against a Pydantic model.

```text
LLM Response
     ↓
PydanticOutputParser
     ↓
Pydantic Model
     ↓
Validated Data
```

This is useful when an application requires structured information rather than free-form text.

---

# 5. Pydantic

Pydantic is used to define the expected structure of the generated response.

For example:

```python
class Question(BaseModel):

    question: str

    choices: list[str]

    answer: str
```

This gives the application a predictable data structure.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Level-2-Gen-AI-Projects.git
```

Navigate into the project:

```bash
cd Level-2-Gen-AI-Projects
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv genai
```

Activate it:

```bash
genai\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv genai
```

```bash
source genai/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Ollama Setup

These projects use **Ollama** to run the LLM locally.

Install Ollama on your system and then pull the model:

```bash
ollama pull qwen2.5:3b
```

Verify that the model is available:

```bash
ollama list
```

You should see the downloaded model in the list.

> **Hardware Note:** Local model performance depends on your CPU, GPU, RAM, and available VRAM. You can use another compatible Ollama model by changing the `model` value in the Python files.

---

# ▶️ Running the Projects

## AI Code Explainer

Run:

```bash
python Ai-Code-Explainer.py
```

You will be asked:

```text
enter a language:
enter a level:
enter a code:
```

Example:

```text
enter a language: Python
enter a level: beginner
enter a code: print("Hello World")
```

---

## Interview Q&A Generator

Run:

```bash
python Interview-QA-Generator.py
```

You will be asked:

```text
Enter a role:
Enter experience:
Enter a topic:
Enter a difficulty level:
```

Example:

```text
Enter a role: Python Developer
Enter experience: 2
Enter a topic: Python
Enter a difficulty level: Medium
```

The application then generates five interview questions.

---

# 🔐 Why Use Local LLMs?

Using Ollama provides several useful advantages for learning and experimentation:

* Local inference
* No API key required for the local model
* Can experiment without cloud API costs
* Data can remain on the local machine
* Easy model switching
* Useful for learning LLM application development

---

# 🆚 Level 1 vs Level 2

| Level   | Main Focus                                         |
| ------- | -------------------------------------------------- |
| Level 1 | Gen AI and LangChain fundamentals                  |
| Level 2 | Practical AI applications and structured workflows |
| Level 1 | Basic prompts and parsers                          |
| Level 2 | More advanced prompting and structured responses   |
| Level 1 | Simple LLM applications                            |
| Level 2 | Role-specific and developer-focused applications   |

---

# 📈 Learning Progression

```text
Level 1
│
├── LLM Basics
├── Prompt Templates
├── Output Parsers
├── Structured Output
└── Basic Chains
        │
        ▼
Level 2
│
├── Advanced Prompting
├── Code Understanding
├── Structured Q&A Generation
├── Pydantic Models
└── Output Validation
        │
        ▼
Level 3
│
├── RAG
├── Embeddings
├── Vector Databases
├── Agents
├── Tools
└── Memory
        │
        ▼
Advanced Gen AI
│
├── AI Agents
├── Multi-Agent Systems
├── Agent Memory
├── Production LLM Apps
└── Deployment
```

---

# 🚀 Future Improvements

Possible enhancements for these projects include:

### AI Code Explainer

* Add Streamlit UI
* Add syntax highlighting
* Upload source-code files
* Add conversation history
* Support multiple Ollama models
* Add code comparison
* Add code optimization suggestions

### Interview Q&A Generator

* Add Streamlit UI
* Add more question types
* Add coding questions
* Add difficulty-based question banks
* Add scoring functionality
* Add answer explanations
* Export questions to JSON/PDF
* Add interview simulation mode

---

# 🧪 Error Handling

When working with local LLMs, generated output may not always match the expected format.

For structured-output applications, Pydantic validation helps detect responses that don't match the required schema.

For example:

```text
Expected:
{
    "questions": [...]
}

Received:
{
    "properties": {...}
}
```

This type of validation is useful when developing reliable LLM applications.

---

# 📚 Key Takeaways

After completing these projects, you should understand:

* How to connect LangChain with Ollama
* How to build reusable prompts
* How to create LangChain chains
* How to use output parsers
* How to define structured outputs
* How Pydantic validates generated data
* How to build role-specific LLM applications
* How to build practical AI tools using local models

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new Gen AI project"
```

5. Push your branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

# ⭐ Support

If you find this repository useful for learning Generative AI, LangChain, and Ollama, consider giving the repository a ⭐.

---

# 📄 License

This project is created for **educational and learning purposes**.

You are free to experiment with, modify, and extend the projects for your own learning.

---

## 👨‍💻 Author

**Jilla srivardhan**

### Currently Learning

* 🤖 Generative AI
* 🦜 LangChain
* 🦙 Ollama
* 🧠 Large Language Models
* 🐍 Python
* 🔗 AI Application Development

---

> **Learn → Build → Experiment → Level Up 🚀**
