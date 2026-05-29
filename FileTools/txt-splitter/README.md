# txt-splitter

Splits a large text file into sequential fixed-size chunks by line count.

Both scripts stop early if the source file is exhausted before the maximum chunk count is reached.

---

## txt-splitter.py

**Requirements:** Python 3.6+

**Usage:**

```bash
python txt-splitter.py FILE_PATH [options]
```

**Arguments:**

| Argument | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `FILE_PATH` | yes | — | Path to the source file |
| `--lines-per-chunk` | no | `500000` | Number of lines per chunk |
| `--chunk-count` | no | `50` | Maximum number of chunks to produce |
| `--output-prefix` | no | `part_` | Output filename prefix |
| `--output-suffix` | no | `.txt` | Output filename extension |
| `--output-directory` | no | `.` (current dir) | Directory to write output files into (created if missing) |
| `--encoding` | no | `utf-8` | Encoding for reading and writing |
| `--verbose` | no | — | Print a summary line per chunk to stderr |

**Examples:**

Minimal:

```bash
python txt-splitter.py /data/big-file.txt
```

Custom chunk size and count:

```bash
python txt-splitter.py /data/big-file.txt --lines-per-chunk 100000 --chunk-count 10
```

Custom output naming and directory:

```bash
python txt-splitter.py /data/big-file.txt --output-prefix chunk_ --output-suffix .log --output-directory /data/chunks
```

---

## txt-splitter.ps1

**Requirements:** PowerShell 5+

**Parameters:**

| Parameter | Required | Default | Description |
| :--- | :---: | :---: | :--- |
| `-FilePath` | yes | — | Path to the source file |
| `-LinesPerChunk` | no | `500000` | Number of lines per chunk |
| `-ChunkCount` | no | `50` | Maximum number of chunks to produce |
| `-OutputPrefix` | no | `part_` | Output filename prefix |
| `-OutputSuffix` | no | `.txt` | Output filename extension |
| `-OutputDirectory` | no | `.` (current dir) | Directory to write output files into (created if missing) |
| `-Encoding` | no | `UTF8` | Encoding for reading and writing (any .NET encoding name) |
| `-Verbose` | no | — | Print a summary line per chunk (lines written, output path) |

**Examples:**

Minimal:

```powershell
.\txt-splitter.ps1 -FilePath "C:\data\big-file.txt"
```

Custom chunk size and count:

```powershell
.\txt-splitter.ps1 -FilePath "C:\data\big-file.txt" -LinesPerChunk 100000 -ChunkCount 10
```

Custom output naming and directory:

```powershell
.\txt-splitter.ps1 -FilePath "C:\data\big-file.txt" -OutputPrefix "chunk_" -OutputSuffix ".log" -OutputDirectory "C:\data\chunks"
```

Output files are named `part_0.txt`, `part_1.txt`, …, `part_N.txt` (or using your custom prefix/suffix).
