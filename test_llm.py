from app.services.llm import llm

response = llm.invoke(
    "Explain neural networks simply."
)

print(response.content)
"""Activation functions help neurons decide outputs.
Weights determine prediction importance."""