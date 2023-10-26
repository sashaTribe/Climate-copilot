from core import run_llm
from dataclasses import dataclass
import os
if os.path.exists("env.py"):
    import env

# Runs the whole program
if __name__ == "__main__":
    run_llm(os.environ.get("PINECONE_ENVIRONMENT_REGION"))



