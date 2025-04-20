import streamlit as st
from agents import critic, optimizer, single_arg_scorer

def run_refinement_loop(topic: str, initial_argument: str, max_iterations: int = 3):
    scoring_repeats = 2
    best_argument = initial_argument
    best_score = single_arg_scorer.score_argument(topic, initial_argument, scoring_repeats)
    history = [(initial_argument, best_score)]
    arg_switched = True

    for iteration in range(1, max_iterations + 1):
        st.markdown(f"### 🔁 Iteration {iteration}")
        st.markdown(f"**Current best argument (score: {best_score:.1f})**")
        st.write(best_argument)

        if arg_switched:
            critique = critic.critique_argument(topic, best_argument)
        else:
            critique = critic.critique_argument(topic, best_argument, temperature=1.0, strict=True)
        st.markdown("**Main Critique:**")
        st.write(critique)

        if arg_switched:
            new_argument = optimizer.optimize_argument(topic, best_argument, critique)
        else:
            new_argument = optimizer.optimize_argument(topic, best_argument, critique, temperature=1.0, strategic_shift=True)

        new_score = single_arg_scorer.score_argument(topic, new_argument, scoring_repeats)
        st.markdown(f"**New argument (score: {new_score:.1f}):**")
        st.write(new_argument)

        if new_score > best_score:
            best_argument = new_argument
            best_score = new_score
            arg_switched = True
            st.success("✅ New version is better — updated best.")
        else:
            arg_switched = False
            st.info("ℹ️ No improvement — keeping previous best.")

        history.append((new_argument, new_score))

    return {
        "baseline": initial_argument,
        "best": best_argument,
        "score": best_score,
        "history": history
    }
