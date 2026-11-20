def greeting(name: str) -> str:
    cleaned_name = name.strip() or "developer"
    return f"Hello, {cleaned_name}!"


if __name__ == "__main__":
    print(greeting("MindCastle"))
