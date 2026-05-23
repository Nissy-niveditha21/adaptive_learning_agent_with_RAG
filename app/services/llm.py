class MockLLM:

    def invoke(self, prompt):

        class Response:

            def __init__(self, content):
                self.content = content

        prompt = prompt.lower()

        # -------------------------
        # QUESTION GENERATION
        # -------------------------

        if "generate 3 conceptual questions" in prompt:

            return Response(
                """
                Why are activation functions important?
                How do weights affect predictions?
                Why do neural networks need neurons?
                """
            )

        # -------------------------
        # FEYNMAN TEACHING
        # -------------------------

        elif "explain these concepts very simply" in prompt:

            return Response(
                """
                Think of a neural network like a team of workers.

                Neurons are workers that process information.

                Weights decide which information is more important.

                Activation functions help workers decide
                whether information should move forward.
                """
            )

        # -------------------------
        # DEFAULT
        # -------------------------

        return Response(
            "Default mock response"
        )


llm = MockLLM()