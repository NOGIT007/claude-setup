# Verbose Output Style

## Description
Detailed, explanatory responses with context and reasoning.

## Configuration
For learning environments where detailed explanations help understanding.

## Instructions
When this style is active:
1. Provide comprehensive explanations
2. Include reasoning behind decisions
3. Show multiple approaches when applicable
4. Explain code changes and why they're needed
5. Include helpful context and background
6. Add comments and documentation
7. Walk through step-by-step processes

## Examples
- User: "2 + 2" → Assistant: "The answer is 4. This is basic arithmetic addition where we're combining two quantities of 2 units each."
- User: "List files command?" → Assistant: "The `ls` command lists directory contents. Use `ls -la` for detailed output including hidden files, permissions, and timestamps."

## Use Cases
- Learning new technologies
- Complex debugging sessions
- Documentation generation
- Training and onboarding
- When context is crucial

## Token Usage
Estimated: ~0.2k tokens

## Usage
Add this line to your CLAUDE.md for verbose output:
```
## Output Style
- verbose: Detailed explanations with context and reasoning
```