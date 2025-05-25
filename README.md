# Cerebras Code Explainer

A real-time code explanation tool powered by Cerebras's Qwen3 model, delivering instant technical analysis with sub-second inference speeds.

## Features
- **AI-Powered Explanations**: Get bullet-point breakdowns of Python code using Cerebras Qwen3
- **Lightning Fast**: Average response time <0.5 seconds
- **Interactive CLI**: Paste code directly or provide file paths
- **Error Resilient**: Handles API failures and invalid inputs 

## Tech Stack
- **Cerebras Inference API** (Qwen3 model)
- Python 3.10+
- `requests` for API communication
- `python-dotenv` for secure credential management

## Usage
```bash
python3 main.py

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/cerebras-code-explainer.git
cd cerebras-code-explainer

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
