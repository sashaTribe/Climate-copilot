from core import run_llm
from dataclasses import dataclass
import os
if os.path.exists("env.py"):
    import env

# Runs the whole program
if __name__ == "__main__":
    run_llm()



# QUESTIONS TO SHOWCASE:
"""
Example Questions to ask:g
- How successful are the UK Government in implementing their plans for net zero by 2050?
- What industrial or economic barriers are there in tackling climate change?
- Are households being provided the opportunity and resources necessary to tackle climate change in a 
meaningful way?
- what is meant by ULEZ?
"""