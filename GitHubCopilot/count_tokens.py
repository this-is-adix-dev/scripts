import json
import os

def count_clean_and_report(log_path, report_path):
    if not os.path.exists(log_path):
        print(f"[-] Error: Log file does not exist at path:\n    {log_path}")
        return

    sessions = {}
    needed_lines = []  # Store only lines with actual token usage data

    # 1. Read and filter data in memory
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                
                # Filter only actual model operations (inference)
                if data.get("_body") and "GenAI inference" in data["_body"]:
                    needed_lines.append(line)
                    
                    attrs = data.get("attributes", {})
                    resource = data.get("resource", {})
                    
                    # Extract Session ID
                    session_id = "Unknown session"
                    raw_attrs = resource.get("_rawAttributes", [])
                    for attr in raw_attrs:
                        if len(attr) == 2 and attr[0] == "session.id":
                            session_id = attr[1]
                            break
                    
                    # Get model name and token counts
                    model = attrs.get("gen_ai.request.model", "Other model")
                    input_tokens = attrs.get("gen_ai.usage.input_tokens", 0)
                    output_tokens = attrs.get("gen_ai.usage.output_tokens", 0)
                    
                    # Aggregate data
                    if session_id not in sessions:
                        sessions[session_id] = {}
                    if model not in sessions[session_id]:
                        sessions[session_id][model] = {"input": 0, "output": 0}
                        
                    sessions[session_id][model]["input"] += input_tokens
                    sessions[session_id][model]["output"] += output_tokens
                    
            except json.JSONDecodeError:
                continue

    # 2. Clear log file – overwrite it ONLY with saved inference lines
    try:
        with open(log_path, 'w', encoding='utf-8') as f:
            f.writelines(needed_lines)
        print(f"[+] Log file successfully cleaned of telemetry noise.")
    except Exception as e:
        print(f"[-] Warning: Failed to clean log file: {e}")

    # 3. Generate Markdown Content and Terminal Output
    md_lines = []
    md_lines.append("# GitHub Copilot Token Usage Report\n")
    md_lines.append(f"**Total Active Sessions Detected:** {len(sessions)}\n\n")
    md_lines.append("---\n\n")

    print("=" * 70)
    print(f" TOTAL ACTIVE SESSIONS DETECTED: {len(sessions)}")
    print("=" * 70)

    for idx, (session_id, models) in enumerate(sessions.items(), 1):
        # Console output
        print(f"\n[SESSION {idx}] ID: {session_id}")
        print("-" * 70)
        
        # Markdown session header & table configuration
        md_lines.append(f"## Session {idx}\n")
        md_lines.append(f"- **Session ID:** `{session_id}`\n\n")
        md_lines.append("| Model | Input Tokens | Output Tokens |\n")
        md_lines.append("| :--- | :---: | :---: |\n")
        
        session_input = 0
        session_output = 0
        
        for model_name, tokens in models.items():
            # Console print
            print(f"  ├── Model: {model_name:<25}")
            print(f"  │    ├── Input Tokens:  {tokens['input']:>10,}")
            print(f"  │    └── Output Tokens: {tokens['output']:>10,}")
            
            # Markdown row
            md_lines.append(f"| `{model_name}` | {tokens['input']:,} | {tokens['output']:,} |\n")
            
            session_input += tokens["input"]
            session_output += tokens["output"]
            
        # Console summary print
        print(f"  │")
        print(f"  └── SESSION SUMMARY:")
        print(f"       ├── Total Input:   {session_input:>10,}")
        print(f"       └── Total Output:  {session_output:>10,}")
        print("-" * 70)
        
        # Markdown summary section
        md_lines.append(f"\n### Summary for Session {idx}\n")
        md_lines.append(f"- **Total Input Tokens:** {session_input:,}\n")
        md_lines.append(f"- **Total Output Tokens:** {session_output:,}\n")
        md_lines.append("\n---\n\n")

    # 4. Save the Markdown report to disk
    try:
        with open(report_path, 'w', encoding='utf-8') as rf:
            rf.writelines(md_lines)
        print(f"[+] Beautiful Markdown report saved to:\n    {report_path}")
    except Exception as e:
        print(f"[-] Error: Failed to write markdown report: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Parse GitHub Copilot OTel telemetry logs and generate a token usage report."
    )
    parser.add_argument(
        "--log",
        default=os.environ.get("COPILOT_OTEL_LOG", "copilot-tokens.jsonl"),
        help="Path to the Copilot OTel JSONL log file (env: COPILOT_OTEL_LOG)",
    )
    parser.add_argument(
        "--report",
        default=os.environ.get("COPILOT_REPORT", "copilot-token-report.md"),
        help="Path for the output Markdown report (env: COPILOT_REPORT)",
    )
    args = parser.parse_args()

    count_clean_and_report(args.log, args.report)