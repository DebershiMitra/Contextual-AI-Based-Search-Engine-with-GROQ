import os
import time
from groq import Groq
os.environ["GROQ_API_KEY"] = "["GROQ_API_KEY"]"
client = Groq()
def generate_response_groq(relevant_text,query):
    # GROQ query
    query =f"""
    Act as a AI based search engine, Answer the user query based on the context 
    extracted  from the Web search result and if you don't know the answer give
    response such as "unsure about answer" don't hallucinate.
    answer should be in detail
    Here is the user query: {query}
    Here is the context:{relevant_text}
    Answer:
    """
    # Generate completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama3-8b-8192",
    )
    
    # Extracting the answer from GROQ response
    answer = chat_completion.choices[0].message.content

    response = f"{answer}"
    return response
