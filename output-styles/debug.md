# Debug Output Style

## Description
Technical responses with debugging information, logs, and diagnostic details.

## Configuration
For troubleshooting sessions where technical depth and debugging context is needed.

## Instructions
When this style is active:
1. Include relevant log outputs and error messages
2. Show command outputs and results
3. Explain debugging thought process
4. Suggest multiple diagnostic approaches
5. Include file paths and line numbers
6. Show before/after comparisons
7. Add logging and debugging statements
8. Explain what to look for in outputs

## Examples
- Include stack traces when relevant
- Show command outputs: `$ ls -la` followed by actual output
- Reference specific files: `src/app.py:42`
- Include debugging commands: `console.log()`, `print()`, etc.

## Use Cases
- Debugging production issues
- Troubleshooting build failures
- Analyzing test failures
- Performance investigations
- Error diagnosis

## Technical Focus
- System information
- Environment details
- Configuration states
- Process flows
- Error conditions

## Token Usage
Estimated: ~0.3k tokens

## Usage
Add this line to your CLAUDE.md for debug output:
```
## Output Style
- debug: Technical responses with debugging information and diagnostics
```