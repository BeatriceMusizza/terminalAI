# Terminal AI Assistant

A simple, modular, and extensible command-line AI assistant powered by Hugging Face model.
It can answer questions with a professional persona, explain terminal commands, rephrase text for specific audiences, and generate documentation for source code files. It also maintains a short persistent history of your recent interactions.

## Features

| Command    | Description                                                                 |
| ---------- | --------------------------------------------------------------------------- |
| `qa`       | Ask general questions — optionally answered from a professional's viewpoint |
| `explain`  | Get Linux-style man page explanations for terminal commands                 |
| `rephrase` | Reword any text using custom style, tone, and audience                      |
| `doc`      | Generate documentation for source code, inline or high-level or both        |
| `history`  | View the last 5 interactions with the assistant                             |

## Usage

Each command is run using:

```bash
python main.py <command> [OPTIONS]
```
###  `qa` 
Ask anything, optionally impersonating a professional.
**Parameters:**
* `question` *(required)*: the question to ask
* `--profession` *(optional)*: role to adopt when answering (default: `general`)
**Examples:**
```bash
python main.py qa "What is quantum computing?"
python main.py qa "How does a blockchain work?" --profession lawyer
python main.py qa "What is recursion?" --profession teacher
```

###  `rephrase` 
Reword text with a specific writing style, tone, and audience.
**Parameters:**
* `text` *(required)*: the sentence or paragraph to rephrase
* `--style` *(optional)*: writing style (e.g., formal, casual, poetic)
* `--tone` *(optional)*: tone of voice (e.g., persuasive, cheerful)
* `--audience` *(optional)*: target audience (e.g., kids, boss)
**Examples:**
```bash
python main.py rephrase "We must reduce CO₂ emissions." --style formal
python main.py rephrase "This app sucks." --style polite --tone respectful --audience manager
python main.py rephrase "Gravity makes things fall." --style casual --audience kids
```

### `explain` 
Explain any terminal command in a man-page style.
**Parameters:**
* `command` *(required)*: the shell command to explain
**Example:**
```bash
python main.py explain "grep -r 'main' ."
```

### `doc` 
Summarize or comment on your source code.
**Parameters:**
* `file` *(required)*: path to the code file
* `--scope` *(optional)*: one of `functions`, `general`, or `both`

  * `functions`: inline comments for functions
  * `general`: high-level summary
  * `both`: summary + inline comments
**Examples:**
```bash
python main.py doc ~/Documents/GitHub/embedding.py --scope general
python main.py doc ./example.py --scope functions
```

### `history` – View Recent Interactions
Shows the last 5 user–assistant interactions.
```bash
python main.py history
```

## Project Structure

```
terminalAI/
├── main.py               # CLI entrypoint
├── ai_client.py          # Hugging Face model interaction
├── history.py            # Persistent history tracking
├── modules/
│   ├── qa.py             # General Q&A logic
│   ├── explain.py        # Command explanation logic
│   ├── rephrase.py       # Rephrasing logic
│   └── doc_gen.py        # Code documentation logic
└── .ai_history.json      # Local file storing the last 5 interactions
```

## Setup

1. Clone the repo

```bash
git clone https://github.com/yourusername/terminalAI.git
cd terminalAI
```

2. Set your Hugging Face token

Create a token at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and set it:

```bash
export HF_TOKEN=hf_...
```
