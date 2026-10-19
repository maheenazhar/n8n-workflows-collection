import os
import sys
import subprocess
import time

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = r"C:\Users\Lenovo\.gemini\antigravity\scratch\n8n-workflows"

REPOS_TO_PUSH = [
    (11, "11-chat-with-pdf-rag-chatbot", "n8n-11-chat-with-pdf-rag-chatbot", "Chat with PDF - RAG Chatbot (Groq & BM25) workflow in n8n (Workflow #11)"),
    (12, "12-use-of-supabase", "n8n-12-use-of-supabase", "Supabase PostgreSQL Database Integration & CRUD workflow in n8n (Workflow #12)"),
    (13, "13-ai-contact-form-triage", "n8n-13-ai-contact-form-triage", "AI Contact Form Triage & Routing (Groq + Supabase + Gmail) workflow in n8n (Workflow #13)"),
    (14, "14-voice-task-emailer", "n8n-14-voice-task-emailer", "Voice Task Emailer with Human-in-the-Loop workflow in n8n (Workflow #14)"),
    (15, "15-ecommerce-arbitrage-po-engine", "n8n-15-ecommerce-arbitrage-po-engine", "E-Commerce Arbitrage PO Engine (Feeds, Margin Engine, AI Copy, Slack Approval & POs) workflow in n8n (Workflow #15)"),
]

def push_one(idx, folder, repo_name, desc):
    folder_path = os.path.join(BASE_DIR, folder)
    print(f"\n---> Pushing #{idx:02d}: {repo_name}...")
    cmd = [
        "gh", "repo", "create", f"maheenazhar/{repo_name}",
        "--public",
        "--source=.",
        "--remote=origin",
        "--push",
        f"--description={desc}"
    ]
    r = subprocess.run(cmd, cwd=folder_path, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode == 0:
        print(f"[SUCCESS] https://github.com/maheenazhar/{repo_name}")
        return True
    else:
        err = r.stderr.strip() or r.stdout.strip()
        print(f"[FAILED] ({r.returncode}): {err}")
        return False

def push_master():
    print(f"\n---> Pushing Master Collection Repository: n8n-workflows-collection...")
    cmd = [
        "gh", "repo", "create", "maheenazhar/n8n-workflows-collection",
        "--public",
        "--source=.",
        "--remote=origin",
        "--push",
        "--description=Master portfolio and curated collection of 15 production-ready n8n workflows"
    ]
    r = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode == 0:
        print(f"[SUCCESS MASTER] https://github.com/maheenazhar/n8n-workflows-collection")
        return True
    else:
        err = r.stderr.strip() or r.stdout.strip()
        print(f"[FAILED MASTER] {err}")
        return False

if __name__ == "__main__":
    print("Checking remaining repositories to push to GitHub...")
    for idx, folder, repo_name, desc in REPOS_TO_PUSH:
        push_one(idx, folder, repo_name, desc)
        time.sleep(2)
        
    push_master()
