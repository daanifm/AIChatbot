#src/app.py
"""
This module defines the chatbot interface using Gradio, handles user interactions, 
and manages the conversation history.

It includes the following functions:
- `chatbot_interface`: Handles the user input, fetches the response from the chatbot, 
  and updates the conversation history.
- `launch_gradio_interface`: Sets up and launches the Gradio interface for the chatbot, 
  defining the UI components and connecting them to the chatbot logic.

Additionally, the module uses:
- `create_completions`: A utility function to get a response from 
the chatbot model based on user input.
- `init_client`: Initializes the client to interact with the OpenAI API.
- `get_html`: Loads custom CSS for the chatbot's appearance.
"""

import gradio as gr
from utils import create_completions
from config import init_client
from interface import get_html

# Define the interaction history as an empty list
interaccion = []  # We define interaction as an empty list

def chatbot_interface(query, history):
    """
    This function handles the user input, gets the response from the chatbot, 
    and updates the conversation history.

    Args:
    - query (str): The user's query input.
    - history (list): The current conversation history.

    Returns:
    - history (list): The updated conversation history.
    """
    global interaccion  # Indicate that we are using the global variable 'interaccion'
    # Initialize the client and fetch the response using the query
    client = init_client()
    response = create_completions(client, query, interaccion)
    # Append the query and response to the conversation history
    history.append((query, response))
    # Store the conversation in 'interaccion'
    interaccion.append((query, response))
    return history, history


def launch_gradio_interface():
    """
    This function sets up and launches the Gradio interface for the chatbot. 
    It loads the external CSS, creates the necessary components, and 
    links the button and text input to the chatbot logic.

    Returns:
    - None
    """
    chatbot_css = get_html()
    # Load the external CSS and define the interface
    with gr.Blocks(title="My Custom Chatbot") as demo:
        # Title of the application
        gr.HTML(chatbot_css)
        gr.Markdown("# 🤖 My Smart Chatbot", elem_id="header")
        # Chatbot interface area
        chatbot = gr.Chatbot(elem_id="chatbot")
        # Row with the input box and the button
        with gr.Row(elem_id="input_row"):
            query_input = gr.Textbox(
                placeholder="Type your message here...",
                show_label=False,
                elem_id="query_input"
            )
            submit_button = gr.Button("Send", elem_id="submit_button")
        # Connect the button to the chatbot interface logic
        submit_button.click(
            chatbot_interface,
            inputs=[query_input, chatbot],
            outputs=[chatbot, chatbot]
        )
        # Allow pressing 'Enter' as a submit action
        query_input.submit(
            chatbot_interface,
            inputs=[query_input, chatbot],
            outputs=[chatbot, chatbot]
        )

    # Launch the interface
    demo.launch()
