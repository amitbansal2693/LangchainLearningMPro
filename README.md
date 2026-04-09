# LangChain Practice Project

## Project Overview
This project is a comprehensive exploration of LangChain and related tools. It includes various implementations, workflows, and demonstrations of language models, embeddings, document loaders, and runnable workflows. The project is structured into multiple directories, each focusing on specific aspects of LangChain and its applications.

## Directory Structure

### 1. ChatModels
Contains implementations of various chat models, including OpenAI, Anthropic, Gemini, Huggingface, and an all-in-one integration.

### 2. CoursexRevision
Includes resources for prompt engineering and structured output demonstrations. Subdirectories contain JSON schemas, Pydantic demos, TypedDict demos, and more.

### 3. EmbeddedModels
Placeholder for embedded model implementations.

### 4. LLMs
Demonstrates the use of large language models (LLMs) with LangChain. Includes Python scripts and Jupyter notebooks.

### 5. langchain-document-loaders-main
Contains scripts for loading various document types, such as CSV, PDF, and text files. Includes example files and a `books/` directory with sample documents.

### 6. langchain-runnables-main
Demonstrates the use of LangChain runnables, including branches, lambdas, parallel execution, and sequences.

### 7. langgraph-tutorials-main
A collection of Jupyter notebooks showcasing various workflows, such as BMI calculation, prompt chaining, quadratic equation solving, and chatbot creation.

## Key Files
- `app.py`: Main application script.
- `test.py`: Script to test the LangChain installation and version.
- `requirements.txt`: Lists the dependencies required for the project.
- `note.ipynb`: Jupyter notebook for additional notes or experiments.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the test script to verify the setup:
   ```bash
   python test.py
   ```

## Usage
Explore the directories and run the scripts or notebooks to learn about LangChain and its capabilities. Each directory contains specific examples and workflows.
