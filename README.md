This is a UVA chatbot which can answer questions about UVA. It pulls from existing UVA websites to source important information faster than manually searching for it. Created by Andrew Cornfeld, Bereket Tafesse, and Jonathan Swap.

This LLM runs completely locally, there is no internet required once it is installed.

To run this LLM, you must first install the requirements from the requirements.txt file (pip install requirements.txt).

You will then need to install Ollama. Visit ollama.com and click download. Complete the setup process. You can confirm that you've done this correctly by typing "ollama" in your terminal.

We will then pull 2 models, ollama 3.2 and mxbai-embed-large. We can do this by typing the following commands:

ollama pull llama3.2
ollama pull mxbai-embed-large

You should then be able to run main.py to run the LLM. 
