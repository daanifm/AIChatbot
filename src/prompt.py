#src/prompt.py
"""
This module contains the `build_prompt` function, which constructs a prompt 
to be sent to a chat-based model, including instructions for the model's behavior 
and the user's question with relevant context.

The prompt structure includes a system message that guides the model on how to respond, 
and a user message that contains the user's question along with any previous interactions. 
This ensures that the model's responses are coherent, context-aware, and aligned with 
the desired tone and professionalism.

Functions:
- `build_prompt`: Constructs the complete prompt for the chat model based on the 
  user's question and prior interaction history.
"""
def build_prompt(question: str, interaction: str):
    """
    Constructs the complete prompt to send to the chat-based model,
    including a system message for behavior instructions
    and the user's question with context.

    Parameters:
    question (str): The question that the user asks.
    interaction (str): The prior interaction, if any.

    Returns:
    list: The list of message dictionaries to be passed to the chat model.
    """
    system_message = """
Eres un experto en el tema que se te consulte. Tu objetivo es proporcionar respuestas claras, útiles y detalladas, siempre con un tono amable, empático y profesional. 
Cuando se te dé una pregunta y un historial de interacción, responde teniendo en cuenta ese contexto para mantener coherencia y continuidad. 
"""

    user_message = f"""Interacción previa:
{interaction}

Pregunta:
{question}
"""

    return [
        {"role": "system", "content": system_message.strip()},
        {"role": "user", "content": user_message.strip()}
    ]
