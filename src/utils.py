#src/utils.py
"""
Module to handle the generation of chatbot responses using the OpenAI API.

This module contains functions that interact with the OpenAI client to generate 
responses for the chatbot. The `create_completions` function builds a prompt 
using a user’s query and previous interactions, then sends it to the 
Llama-4-Maverick model to obtain a relevant response.

Functions:
    create_completions(client, query, interaction): Generates a completion from 
    the OpenAI model based on the user's query and prior interactions.

"""
from prompt import build_prompt

def create_completions(client, query, interaction):
    """
    Generates a chatbot completion based on the user's query and previous interactions.

    This function uses the OpenAI client to generate a response for the chatbot. 
    It builds the prompt from the given query and the previous interactions and sends the 
    prompt to the `llama-4-maverick` model for a response.

    Args:
        client (OpenAI): The OpenAI client used to interact with the model.
        query (str): The query provided by the user for which a response is needed.
        interaction (list): The list of previous interactions (queries and responses) for context.

    Returns:
        str: The generated response from the model based on the 
        user's query and previous interactions.
    """
    # Build the prompt using the query and previous interactions
    messages = build_prompt(query, interaction)

    # Generate the completion from the model
    completion = client.chat.completions.create(
        extra_body={},
        model="meta-llama/llama-4-maverick:free",
        messages=messages
    )

    # Return the content of the generated response
    return completion.choices[0].message.content
