# scripts

A personal collection of utility scripts for productivity, AI tooling, and file processing.

## Contents

| Script | Language | Description |
| :--- | :---: | :--- |
| [GitHubCopilot/count_tokens.py](GitHubCopilot/count_tokens.py) | Python | Parse GitHub Copilot OTel logs and generate a per-session token usage report |
| [PowerShell/txt-splitter.ps1](PowerShell/txt-splitter.ps1) | PowerShell | Split a large text file into fixed-size chunks by line count |

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

## PowerShell / txt-splitter.ps1

Splits a large text file into sequential chunks of a fixed number of lines, writing each chunk to a numbered output file (`part_0.txt`, `part_1.txt`, …).

**Requirements:** PowerShell 5+

**Usage:** Edit the variables at the top of the script, then run it:

```powershell
# Set these before running:
$filePath      = "C:\path\to\your\file.txt"
$elementsCount = 500000   # lines per chunk
$iterationsCount = 49     # number of chunks (0-indexed, so 50 total)

.\PowerShell\txt-splitter.ps1
```

---

## Contributing

Scripts are self-contained — drop a new script into a descriptively named subfolder and add a row to the table above.
