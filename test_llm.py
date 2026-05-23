from app.services.llm import llm

response = llm.invoke(
    "Explain neural networks simply."
)

print(response.content)