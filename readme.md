# PR Statement Generator

A Streamlit web application powered by LangGraph and Groq that generates professional and compelling PR statements for various topics.

## Overview

This AI-powered PR Statement Generator leverages Large Language Models to create high-quality PR statements. The application features an iterative refinement workflow that evaluates and improves statements until they meet quality standards.

## Features

- **AI-Powered Generation**: Creates compelling PR statements using Groq's implementation of Llama 4 Scout
- **Automated Evaluation**: Analyzes each statement for quality and clarity
- **Iterative Refinement**: Automatically improves statements based on feedback
- **User-Friendly Interface**: Clean Streamlit web interface for easy interaction
- **Workflow Visualization**: Visual representation of the statement generation process

## Getting Started

### Prerequisites

- Python 3.8+
- Groq API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/chaitanyacherukuri/PR-Statement-Generator.git
   cd PR-Statement-Generator
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.streamlit/secrets.toml` file with your Groq API key:
   ```
   GROQ_API_KEY = "your-api-key-here"
   ```

### Running the Application

```
streamlit run PR_Statement_Generator.py
```

Then open your browser to http://localhost:8501

## Usage

1. Enter a topic for your PR statement in the text input field
2. Click "Generate PR Statement"
3. The system will automatically generate, evaluate, and refine the statement
4. Review your final PR statement displayed on the page

## How It Works

The application uses a LangGraph workflow with the following steps:

1. **Statement Generation**: Creates an initial PR statement based on the provided topic
2. **Evaluation**: Analyzes the statement quality using structured output
3. **Decision**: Either accepts the statement as "good" or returns it for improvement
4. **Refinement**: If needed, improves the statement based on specific feedback
5. **Re-evaluation**: The process repeats until a high-quality statement is produced

## Technologies

- [Streamlit](https://streamlit.io/) - Web interface
- [LangGraph](https://github.com/langchain-ai/langgraph) - Workflow orchestration
- [Groq](https://groq.com/) - LLM provider for Llama 4 Scout
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and structured output

## License

[MIT](LICENSE)

## Acknowledgements

- Built with Groq's Llama 4 Scout implementation
- Workflow powered by LangGraph
- UI implemented with Streamlit