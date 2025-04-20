import re
from core.llm import call_llm, load_prompt_file
from statistics import mean

def score_argument(topic: str, argument: str, scoring_repeats: int = 1) -> float:
    """
    Scores a single argument with respect to a given debate topic.
    
    Args:
        topic: The debate topic
        argument: The argument to score
        scoring_repeats: Number of times to repeat scoring for more reliable results
    
    Returns:
        A float score between 0 and 100, averaged over scoring_repeats runs
    """
    system_prompt, user_prompt_template = load_prompt_file("prompts/single_arg_scorer.prompt.md")

    user_prompt = user_prompt_template.format(
        topic=topic.strip(),
        argument=argument.strip()
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    scores = []

    for _ in range(scoring_repeats):
        response = call_llm(messages, model="gpt-4-turbo", temperature=0.0).strip()
        match = re.search(r"\b\d{1,3}\b", response)
        if match:
            score = int(match.group())
            if 0 <= score <= 100:
                scores.append(score)

    if not scores:
        raise ValueError(f"Could not parse a valid score from any of the {scoring_repeats} runs.")

    return mean(scores)

