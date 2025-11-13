def help_text():
    return """
Available commands:
- help                : Show this list
- suggest [topic]     : Suggest code (optionally for a topic)
- explain <code>      : Explain code (basic support)
- read <filename>     : Show the contents of a file
- edit <filename> <content> : Write content to filename
- plugin <name> <args>: Run a plugin
- quit                : Exit agent
"""

def suggest(topic=""):
    if topic.lower().startswith("sort"):
        return """def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(0, n-i-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]\n    return arr"""
    elif topic.lower().startswith("hello"):
        return 'print("Hello, world!")'
    elif topic.lower() == "file read":
        return """with open('yourfile.txt') as f:\n    data = f.read()\n    print(data)"""
    return f"Example placeholder code for topic: {topic or 'general'}"

def explain(code=""):
    # Simple/explainer for beginner
    if not code.strip():
        return "Please provide code to explain."
    if "for" in code and "in" in code:
        return "This code uses a for-loop to iterate over something."
    if "def " in code:
        return "This code defines a Python function."
    if "open(" in code:
        return "This code opens a file."
    return "Sorry, I can only give basic explanations right now. Try asking about Python basics!"

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"Wrote to {filename}"
    except Exception as e:
        return f"Error writing file: {e}"