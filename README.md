# scripts

A personal collection of utility scripts for productivity, AI tooling, and file processing.

## Contents

| Script | Language | Description |
| :--- | :---: | :--- |
| [GitHubCopilot/count_tokens.py](GitHubCopilot/count_tokens.py) | Python | Parse GitHub Copilot OTel logs and generate a per-session token usage report |
| [FileTools/txt-splitter/txt-splitter.py](FileTools/txt-splitter/txt-splitter.py) | Python | Split a large text file into fixed-size chunks by line count |
| [FileTools/txt-splitter/txt-splitter.ps1](FileTools/txt-splitter/txt-splitter.ps1) | PowerShell | Split a large text file into fixed-size chunks by line count |

---

## GitHubCopilot / count_tokens.py

Parses GitHub Copilot's OpenTelemetry (OTel) JSONL telemetry logs, strips out noise, and produces a structured token usage report — both in the terminal and as a Markdown file.

**Requirements:** Python 3.8+, GitHub Copilot with OTel export enabled in VS Code.

**Quick start:**

```bash
python GitHubCopilot/count_tokens.py --log copilot-tokens.jsonl --report report.md
```

See [GitHubCopilot/README.md](GitHubCopilot/README.md) for full setup and usage docs.

---

## FileTools / txt-splitter

Splits a large text file into sequential chunks of a fixed number of lines, writing each chunk to a numbered output file (`part_0.txt`, `part_1.txt`, …). Available in Python and PowerShell.

**Quick start (Python):**

```bash
python FileTools/txt-splitter/txt-splitter.py /data/big-file.txt
```

**Quick start (PowerShell):**

```powershell
.\FileTools\txt-splitter\txt-splitter.ps1 -FilePath "C:\data\big-file.txt"
```

See [FileTools/txt-splitter/README.md](FileTools/txt-splitter/README.md) for full parameter reference and examples.

---

## Contributing

Scripts are self-contained — drop a new script into a descriptively named subfolder and add a row to the table above.
