# 🧠 Argument Refinement Loop (GUI)

This project provides a Streamlit-based graphical interface for refining arguments using a simple LLM-based agentic workflow. It allows users to select or generate a debatable topic, optionally input an initial argument, and run a multi-step refinement loop that critiques, scores, and optimizes the argument iteratively.

## 🧪 How It Works

The system runs an **argument refinement loop**, leveraging LLMs as both critics and optimizers of arguments. The loop follows this sequence:

1. **Input**  
   A debatable topic is provided (either entered by the user or suggested by the system). The user may also provide an initial argument or let the system generate one.

2. **Scoring**  
   The argument is evaluated by a scoring agent, which assigns a numerical (0-100) score, reflecting its quality based on coherence, persuasiveness, and clarity.

3. **Critique**  
   A critique agent provides constructive criticism of the argument, pointing out main weaknesses or areas for improvement.

4. **Optimization**  
   An optimizer agent generates a revised version of the argument that aims to address the critique while maintaining or enhancing the original point.

5. **Repeat**  
   The new argument is re-scored. If it improves upon the current best, it replaces it. The loop runs for a fixed number of iterations or until the user decides to abort.

The system keeps track of the **best-scoring argument** across iterations and presents it to the user along with the full refinement trace.

## 💡 Why It Should Work

LLMs are capable of meta-reasoning: they can evaluate and improve on their own outputs. By separating the roles of **scorer**, **critic**, and **optimizer**, the loop encourages focused improvement in a structured way. This division of labor is inspired by how human writers refine arguments: through review, critique, and revision.

## 🚀 Features

- Topic suggestion and manual input
- Optional user-provided argument
- Iterative critique–optimize–score loop
- Streamlit UI for interactivity and visualization
- Keeps track of the best version found

## 🛠️ Technologies

- Python
- Streamlit
- OpenAI API (or other LLM backend)

## 🖥️ Running Locally
pip install -r requirements.txt
streamlit run main.py

## 📂 Project Structure
main.py               # Streamlit GUI
iterative_runner.py  # Loop controller
agents/               # Critic, optimizer, scorer agents
prompts/              # Prompt templates
core/llm.py           # Model interaction logic

## 📎 Related Projects
arg_r: The original CLI version of the argument refinement loop

© 2025 Noam Slonim
