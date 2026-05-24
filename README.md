# A simple CLI time capsule app

## Features

- Add capsules
- Lock capsules until a future date
- Open capsules later
- Store notes as Markdown files
- List all capsules
- Remove capsules
- Local filesystem storage
- Simple CLI workflow

## Tech Stack

- Python
- argparse
- pathlib
- json
- subprocess

(Standard library only)

## Installation

Clone the repository:

```bash
git clone https://github.com/BartikaKumar/capsule_cli.git
cd capsule-cli
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

## Activate it:

Linux/macOS
```bash
source .venv/bin/activate
```

Install the package:

```bash
pip install -e .
```

## Storage

Capsules are stored locally in:

```text
~/.local/share/capsule_cli
```

Markdown notes are stored separately from metadata.