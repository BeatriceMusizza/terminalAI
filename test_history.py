from history import add_to_history, get_history

# Simulate a few interactions
add_to_history("What's AI?", "AI stands for Artificial Intelligence.")
add_to_history("What's ML?", "ML stands for Machine Learning.")
add_to_history("What's NLP?", "NLP stands for Natural Language Processing.")
add_to_history("What's DL?", "DL stands for Deep Learning.")
add_to_history("What's CV?", "CV stands for Computer Vision.")
add_to_history("What's RL?", "RL stands for Reinforcement Learning.")  # should push out the first entry

# Display history
for i, (user, reply) in enumerate(get_history(), start=1):
    print(f"{i}. Q: {user}\n   A: {reply}\n")
