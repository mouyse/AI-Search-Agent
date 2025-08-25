# AI Search Agent (ReAct + Tavily + Pydantic)

An AI-powered search agent built with **LangChain**, **OpenAI GPT-4**, and **TavilySearch**.
It uses a **custom ReAct prompt** and a **Pydantic output parser** to return structured answers
with sources.

---

## Features
- Real-time web search via **TavilySearch**.
- **ReAct**-style reasoning with **LangChain**.
- **Structured outputs** using `PydanticOutputParser` and a custom `AgentResponse` schema.
- Clean separation of concerns: prompt (`prompt.py`), schema (`schemas.py`), app (`main.py`).

---

## Project Structure
```
.
├── main.py            # Builds the ReAct agent with custom prompt + Pydantic parser
├── schemas.py         # Pydantic models: AgentResponse (answer + sources), Source
├── prompt.py          # REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS (custom prompt template)
├── .env.example       # Example env vars
├── pyproject.toml     # Dependencies & metadata (Python >= 3.13)
└── README.md          # This file
```

---

## Installation

### 1) Create & activate a virtual environment
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 2) Install dependencies

**Option A (requirements.txt):**
```bash
pip install -r requirements.txt
```

**Option B (from pyproject deps directly):**
```bash
pip install "black>=25.1.0" "isort>=6.0.1"             "langchain>=0.3.27" "langchain-openai>=0.3.31"             "langchain-tavily>=0.2.11" "python-dotenv>=1.1.1"
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

## How It Works

### 1) Custom Prompt + Format Instructions
`prompt.py` defines `REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS`, extending the classic ReAct template.
In `main.py`, a `PromptTemplate` injects the **format instructions** produced by the
`PydanticOutputParser`, so the agent returns structured JSON matching `AgentResponse`.

### 2) Pydantic Output Schema
`schemas.py` contains:
- `Source` with a single field: `url: str`
- `AgentResponse` with fields:
  - `answer: str`
  - `sources: List[Source]` (defaults to an empty list)

### 3) Agent Assembly
`main.py` wires everything together:
- Loads env vars with `python-dotenv`.
- Initializes `ChatOpenAI(model="gpt-4")` and `TavilySearch()` as the tool.
- Wraps the prompt with format instructions from `PydanticOutputParser(AgentResponse)`.
- Builds a ReAct agent and executes it through `AgentExecutor`.

---

## Run

```bash
python main.py
```

By default, `main.py` asks:
> Search for 10 beginner LLM Engineer paid internship opportunities focusing on LangChain in Bengaluru and list their details

The agent will call Tavily, reason using ReAct, and return a structured response (answer + sources).

---

## Modifying the Query

Open `main.py` and change the `input` value passed to `chain.invoke(...)`. Example:

```python
result = chain.invoke(
    input={
        "input": "Find 5 recent LangChain tutorials and list their titles and URLs"
    }
)
```

---

## Notes & Tips
- **TavilySearch** requires a valid `TAVILY_API_KEY` in `.env`.
- If you enable LangSmith tracing, set `LANGSMITH_TRACING=true` and provide `LANGSMITH_API_KEY` + `LANGSMITH_PROJECT`.
- Keep versions flexible (as in `pyproject.toml`) for easier upgrades, or pin exact versions in `requirements.txt` for reproducibility.

---

## License
MIT
