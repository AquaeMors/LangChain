from langchain_openai import OpenAI

# Set up the OpenAI model
model = OpenAI(api_key="sk-proj-p5l4J3SogEmXDn5TTAz6T3BlbkFJPDvyIHL3mMLx8R2qwCQM")

# Define a list of prompts with corresponding max_tokens limits
prompts = [
    ("Explain the principles of quantum mechanics and its implications for modern physics.", 150),
    ("Quantum mechanics is a fundamental theory in physics that describes the behavior of matter and energy at atomic and subatomic scales.", 150),
    ("It encompasses principles such as wave-particle duality, uncertainty principle, and quantum entanglement.", 150),
    ("These concepts have profound implications for fields ranging from particle physics to quantum computing and cryptography.", 150)
]

try:
    # List to store generated texts
    generated_texts = []

    # Generate responses for each prompt
    for prompt, max_tokens in prompts:
        response = model.generate([prompt], max_tokens=max_tokens)  # Ensure prompt is passed as a list
        generated_text = response.generations[0][0].text.strip() if response.generations else "No response generated"
        generated_texts.append(generated_text)

    # Print each prompt and its corresponding generated response
    for i in range(len(prompts)):
        print(f"Prompt {i + 1}: {prompts[i][0]}")
        print(f"Response {i + 1}: {generated_texts[i]}\n")

except Exception as e:
    print(f"Error: {e}")