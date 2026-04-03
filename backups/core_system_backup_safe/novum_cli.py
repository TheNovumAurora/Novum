#!/usr/bin/env python3

from novum_core import load_memory, add_entry, search_memory, reflect
import datetime

# -------------------
# KEYWORDS & RESPONSES
# -------------------
KEYWORDS = {
    "construct": ["worked on", "built", "designed"],
    "reflect": ["reflect", "pattern", "trend"],
    "review": ["review", "recent", "memory"],
    "search": ["search", "find", "look for"],
    "align": ["alignment", "vision", "goal"]
}

RESPONSES = {
    "construct": "Noted your construction. Keep building momentum.",
    "reflect": "Let's examine the patterns in your work.",
    "review": "Displaying recent entries for review.",
    "search": "What keyword should I search for?",
    "align": "Checking alignment with your vision."
}

def detect_keyword(text):
    text_lower = text.lower()
    for action, keywords in KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return action
    return None

# -------------------
# MEMORY
# -------------------
memory = load_memory()

# -------------------
# GREETING
# -------------------
def greet_user(name="Ty"):
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        greeting = f"Good morning, {name}."
        prompt_line = "The horizon is open."
    elif 12 <= hour < 18:
        greeting = f"Good afternoon, {name}."
        prompt_line = "Momentum is still available."
    elif 18 <= hour < 0:
        greeting = f"Good evening, {name}."
        prompt_line = "Reflection sharpens direction."
    else:
        greeting = f"Late night, {name}?"
        prompt_line = "These are the hours that count!"

    # memory awareness
    today_str = datetime.datetime.now().strftime("%Y-%m-%d")
    today_entries = [line for line in memory if today_str in line]
    if not today_entries:
        prompt_line = "No entries recorded today. What moved forward?"
    elif any("imp:8" in line for line in today_entries):
        prompt_line = "High-weight thoughts detected earlier. Does it need action?"

    print("\nNovum Aurora Online.\n")
    print(greeting)
    print(prompt_line)
    print("\n> ", end="")  # cursor ready

# -------------------
# MAIN LOOP
# -------------------
def main():
    greet_user()

    while True:
        user_input = input().strip()

        # -------------------
        # Reserved commands
        # -------------------
        if user_input.lower() == "exit":
            print("Novum Aurora: Powering down.")
            break
        elif user_input.lower() == "memory":
            print("\nNovum Aurora Memory:")
            for line in memory[-30:]:
                print(line)
            continue
        elif user_input.lower().startswith("search"):
            parts = user_input.split(maxsplit=1)
            if len(parts) < 2:
                keyword = input("Enter search keyword: ").strip()
            else:
                keyword = parts[1]
            results = search_memory(keyword, memory)
            if results:
                print("\nSearch Results:")
                for r in results:
                    print(r)
            else:
                print("No matches found.")
            continue

        # -------------------
        # Keyword detection
        # -------------------
        action = detect_keyword(user_input)

        if action == "construct":
            result = add_entry(user_input, memory=memory)
            print(f"{RESPONSES[action]} Tags: {','.join(result['tags']) if result['tags'] else 'none'}")
        elif action == "reflect":
            summary = reflect(memory)
            print(RESPONSES[action])
            if summary["top_tag"]:
                print(f"Top tag today: {summary['top_tag']}")
            if summary["high_importance"]:
                print("High importance entries:")
                for entry in summary["high_importance"]:
                    print(f"- {entry}")
        elif action == "review":
            print(RESPONSES[action])
            for line in memory[-30:]:
                print(line)
        elif action == "search":
            keyword = input("Enter search keyword: ").strip()
            results = search_memory(keyword, memory)
            if results:
                for r in results:
                    print(r)
            else:
                print("No matches found.")
        elif action == "align":
            print(RESPONSES[action])
            # optional: add alignment check logic here
        else:
            # default logging
            result = add_entry(user_input, memory=memory)
            print(f"Entry recorded. Tags: {','.join(result['tags']) if result['tags'] else 'none'}")


if __name__ == "__main__":
    main()
