from json import load, dump

def load_from(directory: str):
    with open(directory, 'r', encoding='utf-8') as f:
        file_content = load(f)
    return file_content
def save_to(directory: str, data: dict):
    with open(directory, 'w', encoding='utf-8') as f:
        dump(data, f)