# ⚾ Baseball Jersey RAG

A Retrieval-Augmented Generation (RAG) application that answers questions about MLB baseball jerseys. Ask natural language questions — "What year did the Yankees introduce pinstripes?" or "Show me all Dodgers jerseys from the 1980s" — and get accurate, sourced answers powered by a curated jersey knowledge base.

## ✨ Features

- **Natural Language Q&A**: Ask questions about MLB jersey history, designs, and teams in plain English
- **RAG Pipeline**: Combines document retrieval with an LLM to give grounded, accurate answers
- **MLB Coverage**: Covers jersey data across all 30 MLB teams
- **Notebook + App**: Includes both Jupyter notebooks for exploration and a runnable application

## 🛠️ Tech Stack

- Python 3.10+
- LangChain or LlamaIndex (RAG orchestration)
- OpenAI / Anthropic (LLM)
- ChromaDB / FAISS / Pinecone (vector store)
- Jupyter Notebook (for experimentation)

## 📁 Project Structure

```
baseballjerseyrag/
└── mlb-jersey-rag/       # Main application code
    ├── data/             # Jersey documents / knowledge base
    ├── notebooks/        # Jupyter exploration notebooks
    ├── app.py            # Main RAG application entry point
    └── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- An OpenAI or Anthropic API key

### Installation

```bash
git clone https://github.com/masteringmachines/baseballjerseyrag.git
cd baseballjerseyrag/mlb-jersey-rag
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_key_here
# or
ANTHROPIC_API_KEY=your_key_here
```

### Run the App

```bash
python app.py
```

### Explore with Notebooks

```bash
jupyter notebook
```

Open any notebook in the `notebooks/` folder to explore the RAG pipeline step by step.

## 💬 Example Queries

```
"What are the home jerseys for the Boston Red Sox?"
"Which teams have had navy blue as a primary color?"
"Tell me about the history of the Chicago Cubs uniform"
"What jersey number did Babe Ruth wear?"
```

## 🔍 How RAG Works Here

1. MLB jersey documents are chunked and embedded into a vector store
2. User submits a natural language question
3. The retriever finds the most relevant document chunks
4. The LLM receives the question + retrieved context
5. A grounded, accurate answer is generated

## 🤝 Contributing

Feel free to open issues or PRs — especially if you want to add more jersey data, support additional teams, or improve the retrieval pipeline.

## 📝 License

MIT
