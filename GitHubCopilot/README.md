# GitHub Copilot Token Usage Counter

A Python script that parses GitHub Copilot's OpenTelemetry (OTel) telemetry logs, filters out noise, and produces a per-session token usage report in Markdown.

## Prerequisites

- Python 3.8+
- GitHub Copilot with OTel export enabled in VS Code

### Enable OTel in VS Code

Add the following to your VS Code `settings.json`:

```json
"github.copilot.chat.otel.enabled": true,
"github.copilot.chat.otel.exporterType": "file",
"github.copilot.chat.otel.outfile": "/path/to/copilot-tokens.jsonl"
```

> **Note:** The `outfile` path must be an absolute path. VS Code must be restarted after changing these settings.

## Usage

```bash
python count_tokens.py [--log <path>] [--report <path>]
```

| Argument | Default | Description |
| :--- | :--- | :--- |
| `--log` | `copilot-tokens.jsonl` | Path to the Copilot OTel JSONL log file |
| `--report` | `copilot-token-report.md` | Path for the output Markdown report |

### Examples

Run with default paths (log and report in the current directory):

```bash
python count_tokens.py
```

Run with explicit paths:

```bash
python count_tokens.py --log ~/git/copilot-tokens.jsonl --report ~/reports/tokens.md
```

### Environment Variables

Instead of passing flags every time, export environment variables in your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export COPILOT_OTEL_LOG="/path/to/copilot-tokens.jsonl"
export COPILOT_REPORT="/path/to/copilot-token-report.md"
```

Then just run:

```bash
python count_tokens.py
```

Priority order: `--log`/`--report` flags > environment variables > built-in defaults.

## What It Does

1. **Reads** the JSONL log and filters only `GenAI inference` events (skipping unrelated telemetry).
2. **Cleans** the log file in-place — overwrites it with only the relevant inference lines.
3. **Aggregates** input/output token counts per session ID and model.
4. **Outputs** a summary to the terminal and saves a Markdown report to disk.

## Output

### Terminal

```text
======================================================================
 TOTAL ACTIVE SESSIONS DETECTED: 2
======================================================================

[SESSION 1] ID: abc-123-...
----------------------------------------------------------------------
  ├── Model: gpt-4o
  │    ├── Input Tokens:      12,450
  │    └── Output Tokens:      3,210
  │
  └── SESSION SUMMARY:
       ├── Total Input:       12,450
       └── Total Output:       3,210
```

### Markdown Report (`copilot-token-report.md`)

A structured report grouped by session, with per-model token breakdown tables and session summaries.
