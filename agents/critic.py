from core.llm import call_llm, load_prompt_file

def critique_argument(topic: str, argument: str, strict: bool = False, temperature: float = 0.7) -> str:
    system_prompt, user_prompt_template = load_prompt_file("prompts/critic.prompt.md")

    strict_note = (
        "Try to identify flaws or limitations that haven't been pointed out before. "
        "Be especially strict, and avoid repeating prior critique phrasing or shallow observations."
        if strict else ""
    )

    user_prompt = user_prompt_template.format(
        topic=topic.strip(),
        argument=argument.strip(),
        strict_note=strict_note
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    return call_llm(messages, temperature=temperature).strip()