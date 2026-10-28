import gradio as gr
from summarizer import summarize

gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(label="Enter URL", placeholder="Enter the URL of the website to summarize"),
    outputs=gr.Markdown(label="Summary"),
    title="Website Summarizer",
    description="Enter the URL of a website, and this tool will fetch its contents and provide a concise summary using Grok.",
    theme="default",
).launch(share=True)