# Contributing to MLB Jersey RAG

Thank you for your interest in contributing! Here are some guidelines.

## How to Contribute

### Reporting Bugs

- Check if the bug has already been reported in Issues
- Include detailed steps to reproduce
- Provide system information (OS, Python version)
- Include error messages and logs

### Suggesting Features

- Check existing feature requests first
- Clearly describe the feature and its use case
- Explain how it would benefit users

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add docstrings to functions and classes
   - Include type hints where appropriate
   - Add unit tests for new functionality

4. **Run tests**
   ```bash
   pytest tests/
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Describe your changes clearly
   - Reference any related issues
   - Ensure all tests pass

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and modular
- Maximum line length: 88 characters (Black formatter style)

## Adding New Jersey Data

To add more jersey data:

1. Edit `data/jerseys.json`
2. Follow the existing JSON structure:
   ```json
   {
     "id": "unique_id",
     "team": "Team Name",
     "abbreviation": "ABC",
     "type": "Home|Away|Alternate|Special",
     "primary_color": "Color",
     "secondary_color": "Color",
     "description": "Detailed description...",
     "year_introduced": 2020,
     "special_features": "Notable features"
   }
   ```
3. Run database initialization to update embeddings

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/mlb-jersey-rag.git
cd mlb-jersey-rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8

# Run tests
pytest tests/ -v
```

## Documentation

- Update README.md if adding new features
- Add docstrings to all public functions
- Include usage examples for new features

## Questions?

Feel free to open an issue for any questions or concerns.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
