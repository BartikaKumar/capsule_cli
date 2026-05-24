# A simple CLI time capsule app

## Features

- Add capsules
- Lock capsules until a future date
- Open capsules later
- Store notes as Markdown files
- List all capsules
- Remove capsules
- Local filesystem storage
- Simple CLI workflow_

## Tech Stack

- Python
- argparse
- pathlib
- json
- subprocess

(Standard library only)

## Installation

Clone the repository:

```git clone https://github.com/BartikaKumar/capsule_cli.git
cd capsule-cli```

Create a virtual environment:

```python3 -m venv .venv```

## Activate it:

Linux/macOS
```source .venv/bin/activate```

Install the package:

```pip install -e .```

# Storage

Capsules are stored locally in:

```~/.local/share/capsule_cli```

Markdown notes are stored separately from metadata.