"""
Vector store module for managing ChromaDB operations.
"""

import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional
import json
from pathlib import Path


class JerseyVectorStore:
    """Manage vector storage and retrieval for MLB jerseys using ChromaDB."""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        """
        Initialize the ChromaDB vector store.
        
        Args:
            persist_directory: Directory to persist the database
        """
        self.persist_directory = persist_directory
        Path(persist_directory).mkdir(parents=True, exist_ok=True)
        
        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
        )
        
        # Collection name
        self.collection_name = "mlb_jerseys"
        
    def get_or_create_collection(self):
        """Get existing collection or create new one."""
        try:
            collection = self.client.get_collection(name=self.collection_name)
            print(f"Loaded existing collection: {self.collection_name}")
        except:
            collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"description": "MLB jersey embeddings"}
            )
            print(f"Created new collection: {self.collection_name}")
        
        return collection
    
    def add_jerseys(self, jerseys: List[dict], embeddings: List[List[float]]):
        """
        Add jerseys to the vector store.
        
        Args:
            jerseys: List of jersey dictionaries
            embeddings: List of embedding vectors
        """
        collection = self.get_or_create_collection()
        
        # Prepare data for ChromaDB
        ids = [jersey['id'] for jersey in jerseys]
        documents = [self._create_document_text(jersey) for jersey in jerseys]
        metadatas = [self._create_metadata(jersey) for jersey in jerseys]
        
        # Add to collection
        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )
        
        print(f"Added {len(jerseys)} jerseys to the vector store")
    
    def search(self, query_embedding: List[float], top_k: int = 5) -> Dict:
        """
        Search for similar jerseys.
        
        Args:
            query_embedding: Query embedding vector
            top_k: Number of results to return
            
        Returns:
            Dictionary containing search results
        """
        collection = self.get_or_create_collection()
        
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        return results
    
    def get_jersey_by_id(self, jersey_id: str) -> Optional[Dict]:
        """
        Retrieve a specific jersey by ID.
        
        Args:
            jersey_id: Jersey ID
            
        Returns:
            Jersey metadata or None
        """
        collection = self.get_or_create_collection()
        
        try:
            result = collection.get(ids=[jersey_id])
            if result['metadatas']:
                return result['metadatas'][0]
        except:
            pass
        
        return None
    
    def list_all_jerseys(self) -> List[Dict]:
        """
        List all jerseys in the database.
        
        Returns:
            List of all jersey metadata
        """
        collection = self.get_or_create_collection()
        
        results = collection.get()
        return results['metadatas'] if results['metadatas'] else []
    
    def count(self) -> int:
        """
        Get count of jerseys in the database.
        
        Returns:
            Number of jerseys
        """
        collection = self.get_or_create_collection()
        return collection.count()
    
    def reset(self):
        """Reset the database (delete all data)."""
        try:
            self.client.delete_collection(name=self.collection_name)
            print(f"Deleted collection: {self.collection_name}")
        except:
            print("Collection does not exist")
    
    def _create_document_text(self, jersey: dict) -> str:
        """Create text document for ChromaDB."""
        return f"{jersey['team']} {jersey['type']} - {jersey['description']}"
    
    def _create_metadata(self, jersey: dict) -> Dict:
        """Create metadata dictionary for ChromaDB."""
        metadata = {
            'id': jersey['id'],
            'team': jersey['team'],
            'abbreviation': jersey['abbreviation'],
            'type': jersey['type'],
            'primary_color': jersey['primary_color'],
            'secondary_color': jersey['secondary_color'],
            'description': jersey['description'],
        }
        
        # Add optional fields
        if 'year_introduced' in jersey:
            metadata['year_introduced'] = str(jersey['year_introduced'])
        if 'special_features' in jersey:
            metadata['special_features'] = jersey['special_features']
            
        return metadata
