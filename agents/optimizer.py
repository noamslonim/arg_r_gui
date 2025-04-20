from core.llm import call_llm, load_prompt_file

def optimize_argument(topic: str, argument: str, critique: str, temperature: float = 0.7, strategic_shift: bool = False) -> str:
    """
    Suggests an improved version of the argument based on the critique.
    If strategic_shift is True, the model is encouraged to either reframe the argument or add supporting evidence.
    """
    system_prompt, user_prompt_template = load_prompt_file("prompts/optimizer.prompt.md")

    extra_hint = (
        "\n\nTry either (1) reframing the argument from a new angle — such as ethics, economics, or global precedent — "
        "OR (2) adding a brief, relevant piece of evidence to strengthen the point."
        if strategic_shift else ""
    )

    user_prompt = user_prompt_template.format(
        topic=topic.strip(),
        argument=argument.strip(),
        critique=critique.strip()
    ) + extra_hint

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    return call_llm(messages, temperature=temperature)