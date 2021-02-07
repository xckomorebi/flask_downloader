import os

def classify(directory: str) -> dict:
    extension_mapping = {
        "mp3": "backing",
        "wav": "backing",
        "krig": "preset",
        "pdf": "tabs",
        "gp": "tabs",
        "gtp": "tabs",
        "gp5": "tabs",
        "gp4": "tabs",
        "gp3": "tabs",
        "gpx": "tabs",
    }
    files = {"backing": [], "tabs": [], "preset": []}

    def atomic_classify(file):
        _, file_extension = os.path.splitext(file)
        if file_extension:
            file_type = extension_mapping.get(file_extension[1:])
            files[file_type].append(file)

    for file in os.listdir(directory):
        atomic_classify(file)
    
    return files