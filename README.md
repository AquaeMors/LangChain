Overview
---------------
-> LangChain, a powerful framework designed for building applications, utilizes language models (LLMs) and the tools to integrate said LLMs into various types of applications such as chatbots, automated content creation, and data processing. LangChain was built with modularity in mind, giving developers different components for different needs; data preprocessing, model selection, response generation, and post-processing.

->LangChain promotes the use of pipelines, where different stages of processing are chained together. This makes it easier to build complex workflows that involve multiple steps, such as fetching data, transforming it, generating text, and refining the output. LangChain is supposed to be very flexible as well in terms of working with other LLMs allowing developers to choose the best model for their application without being locked into a single ecosystem. 

Setting Up Environment
--------------------------------------
Setting up my environment, I used a virtual environment to keep my dependencies isolated. I am using `venv` to create my virtual env.
```sh
python3 -m venv langchain-env #create a virtual environment

source lanchain-env/bin/activate #activate the virtual environment
```

Using LangChain with OpenAI
-----------------------------------------------
After the env was set up, I started with a simple example to see how LangChain works. I wrote a python script, `exampleLangChain.py`.
```python
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
```
After some simple debugging, my openai api key was accepted by the code, my prompt was taken, and an output showed:

![Pasted image 20240531133427](https://github.com/AquaeMors/LangChain/assets/171375687/b9787bd7-af68-4f1d-ace4-a96684cd2b64)

Now that I had this simple code working, I went to try something more complex. I asked chatgpt to give me 4 complex prompts and added them to my prompts list.
```python
from langchain_openai import OpenAI

model = OpenAI(api_key="[OpenAI API KEY]")
prompts = [
    "Explain the principles of quantum mechanics and its implications for modern physics.",
    "Quantum mechanics is a fundamental theory in physics that describes the behavior of matter and energy at atomic and subatomic scales.",
    "It encompasses principles such as wave-particle duality, uncertainty principle, and quantum entanglement.",
    "These concepts have profound implications for fields ranging from particle physics to quantum computing and cryptography."
]

try:

    response = model.generate(prompts, max_tokens=200)  
    generated_texts = [generation.text.strip() for generation in response.generations[0]]     #extract the texts from the response

    #print each prompt and its corresponding generated response
    for i in range(len(prompts)):
        print(f"Prompt {i + 1}: {prompts[i]}")
        if i < len(generated_texts):
            print(f"Response {i + 1}: {generated_texts[i]}\n")
        else:
            print(f"No response generated for Prompt {i + 1}\n")

except Exception as e:
    print(f"Error: {e}")
```
Although my code did output each prompt and its generated text, all the 150 tokens were being exhausted on the first prompt. I also edited this code from the first one because, as seen in the first codes screenshot, the prompt ended abruptly and didn't finish the sentence.

![Pasted image 20240531134502](https://github.com/AquaeMors/LangChain/assets/171375687/7fe20786-5e81-448c-88d5-85411e6c5928)

All the "No response generated for Prompt X" meant that there were no more allocated tokens left to generate a response for that prompt. I fixed this by defining 150 token length for each prompt so that the first 1 or 2 would not token-hog.

![Pasted image 20240531135141](https://github.com/AquaeMors/LangChain/assets/171375687/d7641ff0-bc36-4196-97bd-3aa95a50e212)

After a while, I was able to output all four prompts with their specific generation, albeit the output is pretty messy.

Conclusion
----------------------------------------------
-> LangChain is a framework that facilitates the integration and orchestration of various language models and natural language processing tools, (NLPs). It aims to simplify the development and deployment of NLP applications by providing a unified interface to interact with different models and APIs.

-> In my current setup, I am primarily using OpenAI's GPT-3.5 model through the langchain_openai package. LangChain abstracts some of the complexities of interacting with different NLP APIs, providing a standardized way of using models like GPT-3.5. For future development, LangChain could be used in my code for seamlessly switching between different NLP services or models without extensive code changes.
