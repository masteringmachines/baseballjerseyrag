"""
Unit tests for MLB Jersey RAG system.
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.search import JerseySearch
from src.embeddings import JerseyEmbeddings
from src.vector_store import JerseyVectorStore


class TestJerseyEmbeddings:
    """Test embedding generation."""
    
    def test_embedding_initialization(self):
        """Test that embeddings model initializes."""
        embeddings = JerseyEmbeddings()
        assert embeddings.model is not None
    
    def test_create_jersey_text(self):
        """Test jersey text creation."""
        embeddings = JerseyEmbeddings()
        jersey = {
            'team': 'Test Team',
            'type': 'Home',
            'primary_color': 'Red',
            'secondary_color': 'White',
            'description': 'A test jersey',
            'special_features': 'Test features'
        }
        text = embeddings.create_jersey_text(jersey)
        assert 'Test Team' in text
        assert 'Home' in text
        assert 'Red' in text
        assert 'White' in text
    
    def test_encode_single_text(self):
        """Test encoding a single text."""
        embeddings = JerseyEmbeddings()
        result = embeddings.encode(["test text"])
        assert result.shape[0] == 1
        assert result.shape[1] > 0  # Has embedding dimensions


class TestJerseyVectorStore:
    """Test vector store operations."""
    
    def test_vector_store_initialization(self):
        """Test vector store initializes."""
        store = JerseyVectorStore(persist_directory="./test_chroma_db")
        assert store.client is not None
    
    def test_create_metadata(self):
        """Test metadata creation."""
        store = JerseyVectorStore(persist_directory="./test_chroma_db")
        jersey = {
            'id': 'test_id',
            'team': 'Test Team',
            'abbreviation': 'TST',
            'type': 'Home',
            'primary_color': 'Red',
            'secondary_color': 'White',
            'description': 'Test description',
            'year_introduced': 2020
        }
        metadata = store._create_metadata(jersey)
        assert metadata['team'] == 'Test Team'
        assert metadata['type'] == 'Home'
        assert 'year_introduced' in metadata


class TestJerseySearch:
    """Test search functionality."""
    
    @pytest.fixture
    def searcher(self):
        """Create a search instance for testing."""
        return JerseySearch(
            data_path="data/jerseys.json",
            persist_directory="./test_chroma_db"
        )
    
    def test_search_initialization(self, searcher):
        """Test search engine initializes."""
        assert searcher.embeddings is not None
        assert searcher.vector_store is not None
    
    def test_load_data(self, searcher):
        """Test loading jersey data."""
        jerseys = searcher.load_data()
        assert len(jerseys) > 0
        assert 'team' in jerseys[0]
        assert 'type' in jerseys[0]
    
    def test_list_teams(self, searcher):
        """Test listing teams."""
        teams = searcher.list_teams()
        assert len(teams) > 0
        assert 'New York Yankees' in teams or 'Boston Red Sox' in teams
    
    def test_filter_by_color(self, searcher):
        """Test filtering by color."""
        jerseys = searcher.filter_by_color("blue")
        assert len(jerseys) > 0
        for jersey in jerseys:
            assert ('blue' in jersey['primary_color'].lower() or 
                   'blue' in jersey['secondary_color'].lower())


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
