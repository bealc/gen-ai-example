# gen-ai-example

**Use caution when using this OpenAI as it is not as secure as Azure OpenAI**

## Notes

* LangChan stable Python versions are 3.10.11 - 3.11.6
* [Python Public Package Repository](https://pypi.org/)
* Install Python Extension Package in VSCode
* OpenAI temperature sets Less Risks vs Creativity 0-1
* LangChan three basic concepts
    * Components:
        * LLM Wrappers
        * Prompt Templates
        * Indexes for information retrievel
            * Embeddings and Vector Databases usage ex:(Qdrant(Has Helm template),FAISS)
    * Chains:
        * Assemble components together
    * Agents:
        * Agent allows LLMs to interact with it's environment
        * LLM to choose a sequence of actions to take
* Hugging Face, Azure OpenAI, OpenAI are all options to use. Azure's implementation is more secure in not sharing your data, no free account access. OpenAI has pay tiers. Hugging Face also has payed deployments and lower rate limits per minute. [Open AI Rate Limits](https://platform.openai.com/docs/guides/rate-limits?context=tier-one) 

## Helpful Commands

* Create python virtual environment: python -m venv env
* Activate venv for Windows: env/Scripts/Activate.ps1
* Activate venv for Mac & Linux: ./env/Scripts/activate
* Install python packages: pip install -r requirements.txt
* Run Streamlit: streamlit run {file.py}

## Python Tips

* Can use Python formatted string literals to include method arguments within a string