# Testing Commands

## Description
Testing commands and best practices for various frameworks.

## Python Testing
```bash
# Run pytest
pytest

# Run with coverage
pytest --cov=src

# Run specific test
pytest tests/test_specific.py

# Run with verbose output
pytest -v
```

## JavaScript/Node.js Testing
```bash
# Run npm tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- --testPathPattern=specific.test.js

# Run in watch mode
npm test -- --watch
```

## Django Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test myapp

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## Testing Best Practices
1. Write tests before implementation (TDD)
2. Test edge cases and error conditions
3. Use descriptive test names
4. Keep tests independent
5. Mock external dependencies

## Token Usage
Estimated: ~0.2k tokens

## Usage
Add this line to your CLAUDE.md for testing support:
```
## Active Commands
- testing: Testing commands and best practices
```