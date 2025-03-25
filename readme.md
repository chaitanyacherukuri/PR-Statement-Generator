# AI-Powered PR Statement Generator

This project generates compelling Public Relations (PR) statements using an AI-based language model. It also evaluates the generated statement for clarity, engagement, and overall effectiveness before re-generating if needed.

## Features

- **PR Statement Generation:** Creates professional and engaging PR statements based on a user-defined topic.
- **Evaluation Workflow:** Assesses the generated PR statement and provides feedback on whether it is well-formed or requires improvement.
- **Interactive UI:** Built with Streamlit, offering a user-friendly interface to input the topic and display results.
- **Workflow Visualization:** Includes a sidebar diagram of the PR statement generation workflow.

## Technology Stack

- **Python**
- **Streamlit** - For the web UI.
- **LangChain Groq** - For leveraging the open source large language models from groq.
- **Pydantic** - For modeling structured feedback.
- **LangGraph** - For managing the workflow states and transitions.

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chaitanyacherukuri/PR-Statement-Generator.git
   cd PR-Statement-Generator
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**

   - Make sure to set your `GROQ_API_KEY` in the Streamlit secrets file (`.streamlit/secrets.toml`):

     ```toml
     GROQ_API_KEY = "your_groq_api_key"
     ```

## Usage

Run the Streamlit application with the following command:

```bash
streamlit run PR_Statement_Generator.py
```

On launching the app, you can:

1. Enter a topic for the PR statement in the provided text box.
2. Click on **Generate PR Statement**.
3. View the generated PR statement along with its evaluation.

## Project Structure

- **PR_Statement_Generator.py:** Main application file handling the generation and evaluation workflow.
- **README.md:** Project documentation.
- **requirements.txt:** List of Python dependencies.
- **.streamlit/secrets.toml:** Configuration file for Streamlit secrets (e.g., API keys).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or fixes.

Powered by **LangGraph** and **Groq**.