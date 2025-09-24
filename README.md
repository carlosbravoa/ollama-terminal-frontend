# Local LLM CLI Assistant

A lightweight command-line interface (CLI) to interact with a local Ollama LLM model (`llama3.2:3b`).  
Supports single-message queries as command-line arguments or multi-turn conversations with persistent context.  
Includes a system prompt to guide the assistant’s behavior and automatically frees RAM when exiting.

---

## Features

- Call the bot with a **first message** directly from the command line:
  ```bash
  bot "Summarize AI in one sentence"

- Interactive multi-turn conversation:
  ```bash
  bot

- Uses a system prompt to guide assistant behavior (e.g., “Respond as short as possible”).
- Automatically releases RAM by stopping the Ollama model after exiting.
- Works entirely with local LLMs, no internet connection required.

## Requirements
- Python 3.10+
- Ollama Installed
- An LLM model previously installed (i.e. `ollama pull llama3.2:3b`)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/local-llm-bot.git
    cd local-llm-bot
    ```

2. Make the bot script executable and move it to your system PATH:
    ```bash
    chmod +x bot.py
    sudo mv bot.py /usr/local/bin/bot
    ```

3. Ensure Ollama is installed and the model is available:
   ```bash
   ollama pull llama3.2:3b
   ```

## Usage
1. One-shot command

Send a message and start the conversation immediately:    
```
bot "What is the capital of Chile?"
```

2. Interactive conversation

Start without arguments:

```
bot
```

3. Exiting
  - Type exit or press Ctrl+C to quit.
  - The bot will automatically stop the model and release RAM.

## Configuration
There are three parameters to configure inside the script:

```python
MODEL = "llama3.2:3b"
BOT_NAME = "Jane"
SYSTEM_PROMPT = f"You are a helpful assistant. Respond as short as possible. Your name is {BOT_NAME}"
```

## Contributions
Feel free to contribute. This code is far from perfect and also we may need to package it accordingly for system-wide installation

## License
MIT License © Carlos Bravo

