import os
import asyncio
import gradio as gr
from fastapi import BackgroundTasks

async def do_exit():
    await asyncio.sleep(0.2)
    os._exit(0)

def on_ui_tabs():
    with gr.Blocks() as tab:
        close_button = gr.Button("Force close webui")
        close_button.click(do_exit)
    return [(tab, "Force Close", "force_close")]

def on_app_started(blocks, app):
    @app.post("/force_close")
    async def force_close(background_tasks: BackgroundTasks):
        background_tasks.add_task(do_exit)
        return {"message": "Shutting down..."}

try:
    from modules import script_callbacks
    script_callbacks.on_ui_tabs(on_ui_tabs)
    script_callbacks.on_app_started(on_app_started)
except Exception as e:
    print(e)
