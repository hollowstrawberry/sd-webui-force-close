import gradio as gr
import os

def on_ui_tabs():
    with gr.Blocks() as tab:
        close_button = gr.Button("Force close webui")
        close_button.click(lambda: os._exit(0))
    return [(tab, "Force Close", "force_close")]

try:
    from modules import script_callbacks
    script_callbacks.on_ui_tabs(on_ui_tabs)
except Exception as e:
    print(e)
