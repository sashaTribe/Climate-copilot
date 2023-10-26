from core import run_llm

if __name__ == "__main__":
    while True:
        user_input = input("Welcome! Ask me anything about Climate Change...")
        if not user_input:
            print("Your query is empty, please try again: ")
            continue
        else:
            break

print(run_llm)