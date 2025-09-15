# Concise Output Style

## Description
Balanced responses that are brief but complete, providing necessary information without excess.

## Configuration
Default style for most development tasks - informative but not verbose.

## Instructions
When this style is active:
1. Provide complete but brief answers
2. Include essential context only
3. One paragraph maximum for simple questions
4. Focus on actionable information
5. Avoid unnecessary elaboration
6. Include key details but skip obvious explanations
7. Structure responses with clear sections

## Examples
- User: "How to install package?" → Assistant: "Run `uv add package-name` to install. This adds it to your pyproject.toml and installs in the virtual environment."
- User: "Git commit failed" → Assistant: "Check `git status` for unstaged files. Use `git add .` then `git commit -m "message"`. Ensure commit message follows project conventions."

## Balance
- More detail than minimal style
- Less verbose than verbose style
- Professional and efficient
- Suitable for most workflows

## Use Cases
- Regular development work
- Code reviews
- Quick consultations
- Standard documentation
- General problem solving

## Token Usage
Estimated: ~0.15k tokens

## Usage
Add this line to your CLAUDE.md for concise output:
```
## Output Style
- concise: Balanced brief responses with essential information
```