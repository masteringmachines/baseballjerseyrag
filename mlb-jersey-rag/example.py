#!/usr/bin/env python3
"""
Example usage of the MLB Jersey RAG system.
Run this after initializing the database with: python main.py --init
"""

from src.search import JerseySearch


def main():
    """Demonstrate various search capabilities."""
    
    print("=" * 80)
    print("MLB Jersey RAG System - Example Usage")
    print("=" * 80)
    
    # Initialize searcher
    print("\nInitializing search engine...")
    searcher = JerseySearch()
    
    # Example 1: Search by style
    print("\n" + "=" * 80)
    print("EXAMPLE 1: Search for pinstripe jerseys")
    print("=" * 80)
    results = searcher.search("classic pinstripe design", top_k=3)
    searcher.print_results(results)
    
    # Example 2: Search by color
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Search for red jerseys")
    print("=" * 80)
    results = searcher.search("bright red jersey", top_k=3)
    searcher.print_results(results)
    
    # Example 3: Search by team and type
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Search for Dodgers alternate jersey")
    print("=" * 80)
    results = searcher.search("Dodgers blue alternate uniform", top_k=2)
    searcher.print_results(results)
    
    # Example 4: Search for unique/unusual jerseys
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Search for unique color schemes")
    print("=" * 80)
    results = searcher.search("unique unusual color combination jersey", top_k=3)
    searcher.print_results(results)
    
    # Example 5: Search for throwback/vintage
    print("\n" + "=" * 80)
    print("EXAMPLE 5: Search for vintage throwback jerseys")
    print("=" * 80)
    results = searcher.search("throwback vintage retro classic jersey", top_k=3)
    searcher.print_results(results)
    
    # List all teams
    print("\n" + "=" * 80)
    print("All MLB Teams in Database")
    print("=" * 80)
    teams = searcher.list_teams()
    print(f"\nTotal: {len(teams)} teams\n")
    for i, team in enumerate(teams, 1):
        print(f"{i:2d}. {team}")
    
    print("\n" + "=" * 80)
    print("Example complete! Try your own searches with:")
    print("  python main.py --search 'your search query'")
    print("=" * 80)


if __name__ == "__main__":
    main()
