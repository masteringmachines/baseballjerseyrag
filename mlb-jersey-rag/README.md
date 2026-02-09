# MLB Jersey RAG System

A Retrieval Augmented Generation (RAG) system for searching and exploring MLB team jerseys using semantic search.

## Features

- 🔍 **Semantic Search**: Find jerseys by description, color, style, or team
- 🎯 **Vector Database**: Powered by ChromaDB for fast similarity search
- 📊 **Rich Metadata**: Includes team info, colors, jersey types, and descriptions
- 🚀 **Easy to Use**: Simple CLI interface with optional web UI

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mlb-jersey-rag.git
cd mlb-jersey-rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```bash
# Initialize the vector database (first time only)
python main.py --init

# Search for jerseys
python main.py --search "pinstripe jerseys"
python main.py --search "red alternate jerseys"
python main.py --search "Yankees home uniform"

# Search with custom number of results
python main.py --search "blue jerseys" --top-k 5
```

## Usage Examples

### Command Line Interface

```bash
# Search by style
python main.py --search "classic pinstripe design"

# Search by color
python main.py --search "navy blue with red accents"

# Search by team and type
python main.py --search "Dodgers alternate jersey"
```

### Python API

```python
from src.search import JerseySearch

# Initialize search engine
searcher = JerseySearch()

# Perform search
results = searcher.search("red jerseys with white text", top_k=3)

for jersey in results:
    print(f"{jersey['team']} - {jersey['type']}")
    print(f"Description: {jersey['description']}")
    print(f"Similarity: {jersey['score']:.2f}\n")
```

## Project Structure

```
mlb-jersey-rag/
├── data/
│   ├── jerseys.json          # Jersey database
│   └── mlb_teams.json        # Team information
├── src/
│   ├── data_collector.py     # Data collection utilities
│   ├── vector_store.py       # ChromaDB operations
│   ├── embeddings.py         # Embedding generation
│   └── search.py             # Search functionality
├── notebooks/
│   └── demo.ipynb           # Interactive demo
├── tests/
│   └── test_search.py       # Unit tests
├── chroma_db/               # Vector database (auto-generated)
├── requirements.txt
├── README.md
└── main.py                  # CLI entry point
```

## Data Format

Each jersey entry includes:
- Team name and abbreviation
- Jersey type (Home, Away, Alternate, Special)
- Primary and secondary colors
- Detailed description
- Year introduced
- Special features

## Technologies

- **ChromaDB**: Vector database for similarity search
- **sentence-transformers**: Generate semantic embeddings
- **Python 3.8+**: Core language
- **LangChain** (optional): For RAG enhancements

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Acknowledgments

- MLB team data sourced from official MLB sources
- Built with ChromaDB and sentence-transformers
