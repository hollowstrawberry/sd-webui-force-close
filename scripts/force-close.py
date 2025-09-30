import gradio as gr
import os

def on_ui_tabs():
    with gr.Blocks() as tab:
        close_button = gr.Button("Force close webui")
        close_button.click(lambda: os._exit(0))
    return [(tab, "Force Close", "force_close")]

def on_app_started(blocks, app):
    @app.post("/force_close")
    async def force_close():
        os._exit(0)

try:
    from modules import script_callbacks
    script_callbacks.on_ui_tabs(on_ui_tabs)
    script_callbacks.on_app_started(on_app_started)
except Exception as e:
    print(e)
