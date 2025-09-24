#!/usr/bin/env python3
import subprocess
import sys

MODEL = "llama3.2:3b"
BOT_NAME = "Jane"
SYSTEM_PROMPT = f"You are a helpful assistant. Respond as short as possible. Your name is {BOT_NAME}"

def chat_with_ollama(first_message=None, model=MODEL):
    # conversation = []
    # Initialize conversation with system prompt
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

    if first_message:
        conversation.append({"role": "user", "content": first_message})

    print(f"Starting chat with {model} ({BOT_NAME}). Type 'exit' to quit.\n")

    try:
        while True:

           # Get user input
            if conversation[-1]["role"] == "user" and first_message:
                message = first_message
                first_message = None
            else:
                message = input("You: ").strip()
                if message.lower() == "exit":
                    break
                conversation.append({"role": "user", "content": message})

            # Build prompt with explicit roles
            prompt_lines = []
            for msg in conversation:
                if msg["role"] == "system":
                    prompt_lines.append(f"System: {msg['content']}")
                elif msg["role"] == "user":
                    prompt_lines.append(f"User: {msg['content']}")
                elif msg["role"] == "assistant":
                    prompt_lines.append(f"Assistant: {msg['content']}")
            prompt = "\n".join(prompt_lines) + "\nAssistant:"

            # Call Ollama
            result = subprocess.run(
                ["ollama", "run", model, prompt],
                capture_output=True,
                text=True
            )

            output = result.stdout.strip()
            if output:
                print(f"{BOT_NAME}: {output}")
                conversation.append({"role": "assistant", "content": output})

    except KeyboardInterrupt:
        print("\nExiting chat...")

    finally:
        # Unload the model to free RAM
        subprocess.run(["ollama", "stop", model], capture_output=True)
        print("Model unloaded. Goodbye!")

if __name__ == "__main__":
    first_msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    chat_with_ollama(first_msg)
