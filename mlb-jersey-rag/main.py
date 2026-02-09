#!/usr/bin/env python3
"""
MLB Jersey RAG System - Command Line Interface
"""

import argparse
import sys
from src.search import JerseySearch


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="MLB Jersey RAG System - Search MLB jerseys using semantic search",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Initialize database (first time setup)
  python main.py --init
  
  # Search for jerseys
  python main.py --search "pinstripe jerseys"
  python main.py --search "red alternate jerseys" --top-k 3
  python main.py --search "Yankees home uniform"
  
  # List all teams
  python main.py --list-teams
  
  # Get jerseys for specific team
  python main.py --team "Boston Red Sox"
  
  # Filter by color
  python main.py --color "blue"
        """
    )
    
    # Arguments
    parser.add_argument(
        '--init',
        action='store_true',
        help='Initialize the vector database with jersey data'
    )
    
    parser.add_argument(
        '--reset',
        action='store_true',
        help='Reset the database before initializing (use with --init)'
    )
    
    parser.add_argument(
        '--search',
        type=str,
        help='Search query for jerseys'
    )
    
    parser.add_argument(
        '--top-k',
        type=int,
        default=5,
        help='Number of results to return (default: 5)'
    )
    
    parser.add_argument(
        '--list-teams',
        action='store_true',
        help='List all MLB teams'
    )
    
    parser.add_argument(
        '--team',
        type=str,
        help='Get all jerseys for a specific team'
    )
    
    parser.add_argument(
        '--color',
        type=str,
        help='Filter jerseys by color'
    )
    
    parser.add_argument(
        '--data-path',
        type=str,
        default='data/jerseys.json',
        help='Path to jersey data JSON file (default: data/jerseys.json)'
    )
    
    parser.add_argument(
        '--db-path',
        type=str,
        default='./chroma_db',
        help='Path to ChromaDB storage (default: ./chroma_db)'
    )
    
    args = parser.parse_args()
    
    # Initialize search engine
    searcher = JerseySearch(
        data_path=args.data_path,
        persist_directory=args.db_path
    )
    
    # Handle commands
    if args.init:
        print("Initializing vector database...")
        searcher.initialize_database(reset=args.reset)
        print("\nDatabase ready! You can now search for jerseys.")
        return
    
    if args.list_teams:
        teams = searcher.list_teams()
        print(f"\nFound {len(teams)} MLB teams:\n")
        for i, team in enumerate(teams, 1):
            print(f"{i:2d}. {team}")
        return
    
    if args.team:
        jerseys = searcher.filter_by_team(args.team)
        if jerseys:
            print(f"\n{args.team} Jerseys ({len(jerseys)} found):\n")
            for jersey in jerseys:
                print(f"  • {jersey['type']}: {jersey['primary_color']} / {jersey['secondary_color']}")
                print(f"    {jersey['description'][:100]}...")
                print()
        else:
            print(f"No jerseys found for team: {args.team}")
        return
    
    if args.color:
        jerseys = searcher.filter_by_color(args.color)
        if jerseys:
            print(f"\nJerseys with '{args.color}' color ({len(jerseys)} found):\n")
            for jersey in jerseys:
                print(f"  • {jersey['team']} - {jersey['type']}")
                print(f"    Colors: {jersey['primary_color']} / {jersey['secondary_color']}")
                print()
        else:
            print(f"No jerseys found with color: {args.color}")
        return
    
    if args.search:
        print(f"Searching for: '{args.search}'\n")
        results = searcher.search(args.search, top_k=args.top_k)
        searcher.print_results(results)
        return
    
    # No command provided
    parser.print_help()
    print("\nTip: Run 'python main.py --init' first to initialize the database")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)
