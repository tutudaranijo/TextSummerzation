import gradio as gr
from openai import OpenAI
from key import openKey
import mlflow

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=openKey)

def summarize_text(text):
    # Start an MLflow run
    with mlflow.start_run():
        # Log the length of the input text as a parameter
        mlflow.log_param("input_text_length", len(text))

        system_message = "You are a highly skilled AI trained in language comprehension and summarization. Your task is to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ]
        )

        summary = response.choices[0].message.content

        # Log the length of the summarized text as a metric
        mlflow.log_metric("summary_length", len(summary))

        return summary

# Create a Gradio interface
iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=10, placeholder="Type your paragraph here..."),
    outputs="text",
    title="Text Summarizer",
    description="A simple text summarizer using OpenAI's GPT."
)