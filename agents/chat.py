from core.llm import call_llm
from uuid import uuid4
from collections import deque  # Needed for topic history

# Maintain recent topic history (max 20)
recent_topics = deque(maxlen=20)

prompt_handler = input
def prompt_user(prompt: str) -> str:
    return prompt_handler(prompt).strip()

def load_prompt(filepath: str) -> tuple[str, str]:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    system, user = content.split("### User")
    return system.replace("### System", "").strip(), user.strip()

def choose_topic(interactive: bool = True) -> str:
    if interactive:
        choice = prompt_user("Do you want to suggest a debatable topic? (yes/no): ").lower()
        if choice.startswith("y"):
            return prompt_user("Please enter your debatable topic: ")

    system, user = load_prompt("prompts/topic_suggestion.prompt.md")
    recent_str = "\n".join(f"- {t}" for t in recent_topics) or "None yet."
    system = system.replace("{{recent_topics}}", recent_str)

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user}
    ]
    topic = call_llm(messages).strip()
    recent_topics.append(topic)
    return topic


def get_initial_argument(topic: str, interactive: bool = True) -> str:
    if interactive:
        choice = prompt_user("Do you want to write the initial argument? (yes/no): ").lower()
        if choice.startswith("y"):
            return prompt_user("Please enter your argument supporting this topic: ")

    system, user = load_prompt("prompts/initial_argument.prompt.md")
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user.format(topic=topic)}
    ]
    return call_llm(messages)