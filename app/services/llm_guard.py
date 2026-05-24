import app.services.llm as llm_service
def safe_llm_call(prompt):

    try:
        response = llm_service.llm.invoke(prompt)
        return response.content

    except Exception as e:
        print(f"LLM ERROR: {e}")

        return None