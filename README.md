# AI Search Agent

This project is a simple **AI-powered search agent** built with **LangChain**, **OpenAI GPT-4**, and **TavilySearch**.  
It demonstrates how to use LangChain's ReAct agent architecture with custom tools to perform intelligent searches.

---

## Features
- Integrates **LangChain** with **OpenAI GPT-4** for reasoning and task execution.
- Uses **TavilySearch** as a search tool for real-time information retrieval.
- Demonstrates **ReAct Agent** pattern (Reasoning + Acting).
- Loads API keys and configuration from environment variables.
- Example: Search for 10 beginner LLM Engineer paid internship opportunities in Bengaluru.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/aisearchagent.git
   cd aisearchagent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies (managed via `pyproject.toml`):
   ```bash
   pip install -e .
   ```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your keys:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
LANGSMITH_TRACING=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=
```

---

## Usage

Run the project with:

```bash
python main.py
```

### Example Query
The current default query is:
```text
Search for 10 beginner LLM Engineer paid internship opportunities focusing on LangChain in Bengaluru and list their details
```

You can modify the input in `main.py` to perform custom searches.

---

## Project Structure

```
.
├── main.py             # Main application entry point
├── pyproject.toml      # Project dependencies & metadata
├── .env.example        # Example environment variables
├── README.md           # Documentation
└── venv/               # Virtual environment (ignored in VCS)
```

---

## Next Steps
- Add support for multiple search tools (Google, Bing, Tavily, etc.).
- Implement user input instead of hardcoded queries.
- Extend with summarization and ranking of search results.
- Build a simple web UI for user interaction.

---

### Tech Stack
- Python 3.13+
- LangChain
- OpenAI GPT-4
- TavilySearch
- dotenv

---

### License
This project is licensed under the MIT License.
