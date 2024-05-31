from langchain_openai import OpenAI

model = OpenAI(api_key="[OpenAI API KEY]")
prompt = ["Once upon a time in a land far, far away, there was a"]

try:
    response = model.generate(prompt) #generate a response from the model
    generated_text = response.generations[0][0].text #extract the text from the response
    print(f"Prompt: {prompt[0]}")
    print(f"Response: {generated_text}")
    
except openai.error.OpenAIError as e:
    print(f"OpenAI error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")