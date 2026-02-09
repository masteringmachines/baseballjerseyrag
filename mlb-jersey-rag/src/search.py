"""
Search module for querying MLB jerseys using semantic search.
"""

import json
from pathlib import Path
from typing import List, Dict, Optional
from src.embeddings import JerseyEmbeddings
from src.vector_store import JerseyVectorStore


class JerseySearch:
    """Main search interface for MLB jerseys."""
    
    def __init__(self, 
                 data_path: str = "data/jerseys.json",
                 persist_directory: str = "./chroma_db"):
        """
        Initialize the jersey search engine.
        
        Args:
            data_path: Path to jersey JSON data
            persist_directory: Path to ChromaDB storage
        """
        self.data_path = data_path
        self.embeddings = JerseyEmbeddings()
        self.vector_store = JerseyVectorStore(persist_directory)
        self.jerseys = []
        
    def load_data(self) -> List[Dict]:
        """
        Load jersey data from JSON file.
        
        Returns:
            List of jersey dictionaries
        """
        with open(self.data_path, 'r') as f:
            self.jerseys = json.load(f)
        
        print(f"Loaded {len(self.jerseys)} jerseys from {self.data_path}")
        return self.jerseys
    
    def initialize_database(self, reset: bool = False):
        """
        Initialize the vector database with jersey data.
        
        Args:
            reset: Whether to reset existing database
        """
        if reset:
            self.vector_store.reset()
        
        # Check if database already has data
        count = self.vector_store.count()
        if count > 0:
            print(f"Database already initialized with {count} jerseys")
            return
        
        # Load jersey data
        if not self.jerseys:
            self.load_data()
        
        # Generate embeddings
        print("Generating embeddings...")
        embeddings = self.embeddings.encode_jerseys(self.jerseys)
        
        # Add to vector store
        self.vector_store.add_jerseys(self.jerseys, embeddings.tolist())
        
        print("Database initialization complete!")
    
    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Search for jerseys matching the query.
        
        Args:
            query: Search query text
            top_k: Number of results to return
            
        Returns:
            List of matching jerseys with scores
        """
        # Generate query embedding
        query_embedding = self.embeddings.encode([query])[0]
        
        # Search vector store
        results = self.vector_store.search(query_embedding.tolist(), top_k)
        
        # Format results
        formatted_results = []
        for i in range(len(results['ids'][0])):
            result = {
                'id': results['ids'][0][i],
                'team': results['metadatas'][0][i]['team'],
                'type': results['metadatas'][0][i]['type'],
                'primary_color': results['metadatas'][0][i]['primary_color'],
                'secondary_color': results['metadatas'][0][i]['secondary_color'],
                'description': results['metadatas'][0][i]['description'],
                'distance': results['distances'][0][i],
                'score': 1 - results['distances'][0][i]  # Convert distance to similarity
            }
            
            # Add optional fields
            if 'special_features' in results['metadatas'][0][i]:
                result['special_features'] = results['metadatas'][0][i]['special_features']
            if 'year_introduced' in results['metadatas'][0][i]:
                result['year_introduced'] = results['metadatas'][0][i]['year_introduced']
                
            formatted_results.append(result)
        
        return formatted_results
    
    def get_jersey(self, jersey_id: str) -> Optional[Dict]:
        """
        Get a specific jersey by ID.
        
        Args:
            jersey_id: Jersey ID
            
        Returns:
            Jersey data or None
        """
        return self.vector_store.get_jersey_by_id(jersey_id)
    
    def list_teams(self) -> List[str]:
        """
        Get list of all teams.
        
        Returns:
            Sorted list of team names
        """
        if not self.jerseys:
            self.load_data()
        
        teams = sorted(set(jersey['team'] for jersey in self.jerseys))
        return teams
    
    def filter_by_team(self, team: str) -> List[Dict]:
        """
        Get all jerseys for a specific team.
        
        Args:
            team: Team name
            
        Returns:
            List of jerseys for the team
        """
        if not self.jerseys:
            self.load_data()
        
        return [j for j in self.jerseys if j['team'].lower() == team.lower()]
    
    def filter_by_color(self, color: str) -> List[Dict]:
        """
        Get jerseys by color.
        
        Args:
            color: Color to search for
            
        Returns:
            List of matching jerseys
        """
        if not self.jerseys:
            self.load_data()
        
        color_lower = color.lower()
        return [j for j in self.jerseys 
                if color_lower in j['primary_color'].lower() 
                or color_lower in j['secondary_color'].lower()]
    
    def print_results(self, results: List[Dict]):
        """
        Pretty print search results.
        
        Args:
            results: List of search results
        """
        if not results:
            print("No results found.")
            return
        
        print(f"\n{'='*80}")
        print(f"Found {len(results)} results:")
        print(f"{'='*80}\n")
        
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['team']} - {result['type']} Jersey")
            print(f"   Colors: {result['primary_color']} / {result['secondary_color']}")
            print(f"   Description: {result['description']}")
            if 'special_features' in result:
                print(f"   Features: {result['special_features']}")
            print(f"   Similarity Score: {result['score']:.3f}")
            print(f"   {'-'*76}\n")
