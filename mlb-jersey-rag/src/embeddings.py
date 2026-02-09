"""
Embeddings module for generating vector representations of jersey descriptions.
"""

from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np


class JerseyEmbeddings:
    """Generate embeddings for jersey descriptions using sentence transformers."""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedding model.
        
        Args:
            model_name: Name of the sentence transformer model to use
        """
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)
        
    def create_jersey_text(self, jersey: dict) -> str:
        """
        Create a comprehensive text representation of a jersey for embedding.
        
        Args:
            jersey: Dictionary containing jersey information
            
        Returns:
            Combined text representation
        """
        text_parts = [
            f"Team: {jersey['team']}",
            f"Type: {jersey['type']} jersey",
            f"Colors: {jersey['primary_color']} and {jersey['secondary_color']}",
            f"Description: {jersey['description']}",
        ]
        
        if 'special_features' in jersey:
            text_parts.append(f"Features: {jersey['special_features']}")
            
        return " ".join(text_parts)
    
    def encode(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            Numpy array of embeddings
        """
        return self.model.encode(texts, show_progress_bar=True)
    
    def encode_jersey(self, jersey: dict) -> np.ndarray:
        """
        Generate embedding for a single jersey.
        
        Args:
            jersey: Dictionary containing jersey information
            
        Returns:
            Embedding vector
        """
        text = self.create_jersey_text(jersey)
        return self.model.encode(text)
    
    def encode_jerseys(self, jerseys: List[dict]) -> np.ndarray:
        """
        Generate embeddings for multiple jerseys.
        
        Args:
            jerseys: List of jersey dictionaries
            
        Returns:
            Numpy array of embeddings
        """
        texts = [self.create_jersey_text(jersey) for jersey in jerseys]
        return self.encode(texts)
