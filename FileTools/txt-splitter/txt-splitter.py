import argparse
import os
import sys


def split_file(file_path, lines_per_chunk, chunk_count, output_prefix, output_suffix, output_directory, encoding, verbose):
    os.makedirs(output_directory, exist_ok=True)

    with open(file_path, "r", encoding=encoding) as reader:
        for i in range(chunk_count):
            out_path = os.path.join(output_directory, f"{output_prefix}{i}{output_suffix}")
            written = 0

            with open(out_path, "w", encoding=encoding) as writer:
                while written < lines_per_chunk:
                    line = reader.readline()
                    if not line:
                        break
                    writer.write(line)
                    written += 1

            if verbose:
                print(f"Wrote {written} lines to {out_path}", file=sys.stderr)

            if written < lines_per_chunk:
                break


def main():
    parser = argparse.ArgumentParser(description="Split a large text file into fixed-size chunks by line count.")
    parser.add_argument("file_path", metavar="FILE_PATH", help="Path to the source file")
    parser.add_argument("--lines-per-chunk", type=int, default=500000, metavar="N", help="Number of lines per chunk (default: 500000)")
    parser.add_argument("--chunk-count", type=int, default=50, metavar="N", help="Maximum number of chunks to produce (default: 50)")
    parser.add_argument("--output-prefix", default="part_", help="Output filename prefix (default: part_)")
    parser.add_argument("--output-suffix", default=".txt", help="Output filename extension (default: .txt)")
    parser.add_argument("--output-directory", default=".", help="Directory to write output files into, created if missing (default: current dir)")
    parser.add_argument("--encoding", default="utf-8", help="Encoding for reading and writing (default: utf-8)")
    parser.add_argument("--verbose", action="store_true", help="Print a summary line per chunk to stderr")
    args = parser.parse_args()

    split_file(
        file_path=args.file_path,
        lines_per_chunk=args.lines_per_chunk,
        chunk_count=args.chunk_count,
        output_prefix=args.output_prefix,
        output_suffix=args.output_suffix,
        output_directory=args.output_directory,
        encoding=args.encoding,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()
