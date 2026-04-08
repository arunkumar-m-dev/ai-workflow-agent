# ai-workflow-agent

This project demonstrates an AI agent that converts natural language into structured enterprise workflows such as reporting, task execution, and system automation.

python -m venv venv
venv\Scripts\activate
pip install langgraph langgraph-cli langchain openai langsmith python-dotenv

To enable:
DB checkpointing
persistent workflows
pip install -U "langgraph-cli[inmem]"
For production-style setup:
pip install "langgraph-cli[postgres]"

langgraph dev
