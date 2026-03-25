import os
import datetime

# -------------------
# CONFIGURATION
# -------------------
MEMORY_FILE = "memory.txt"
DEFAULT_IMPORTANCE = 5

# -------------------
# MEMORY UTILITIES
# -------------------
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_memory(entry):
    with open(MEMORY_FILE, "a") as f:
        f.write(entry + "\n")

# -------------------
# TAGGING UTILITIES
# -------------------
def extract_tags(text):
    return [word[1:].lower() for word in text.split() if word.startswith("#")]

# -------------------
# ENTRY FUNCTIONS
# -------------------
def add_entry(text, importance=DEFAULT_IMPORTANCE, memory=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tags = extract_tags(text)
    tag_string = ",".join(tags) if tags else "none"
    entry = f"[{timestamp}] | imp:{importance} | tags:{tag_string} | {text}"

    save_memory(entry)
    if memory is not None:
        memory.append(entry)

    return {"status": "stored", "tags": tags, "importance": importance, "entry": entry}

# -------------------
# SEARCH
# -------------------
def search_memory(keyword, memory):
    keyword = keyword.lower()
    results = []
    for line in memory:
        try:
            ts_part, imp_part, tags_part, content_part = [p.strip() for p in line.split("|")]
            if keyword in content_part.lower() or keyword in tags_part.lower():
                results.append(line)
        except ValueError:
            if keyword in line.lower():
                results.append(line)
    return results

# -------------------
# REFLECTION
# -------------------
def reflect(memory):
    tag_counts = {}
    high_importance = []

    for line in memory:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 4:
            ts, imp_part, tags_part, content_part = parts
            try:
                imp = int(imp_part.replace("imp:", ""))
            except:
                imp = DEFAULT_IMPORTANCE
        elif len(parts) == 3:
            ts, tags_part, content_part = parts
            imp = DEFAULT_IMPORTANCE
        else:
            continue

        for tag in tags_part.replace("tags:", "").split(","):
            if tag != "none":
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        if imp >= 8:
            high_importance.append(content_part)

    top_tag = max(tag_counts, key=tag_counts.get) if tag_counts else None
    return {"top_tag": top_tag, "high_importance": high_importance[-5:]}
