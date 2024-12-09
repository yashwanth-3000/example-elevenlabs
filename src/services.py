import asyncio
import os
from src.functions.function import text_to_speech,speech_to_speech,isolate_audio
from src.client import client
from src.workflows.workflow import TextToSpeechWorkflow,SpeechToSpeechWorkflow,AudioIsolationWorkflow
from watchfiles import run_process
async def main():

    await client.start_service(
        workflows=[TextToSpeechWorkflow,SpeechToSpeechWorkflow,AudioIsolationWorkflow],
        functions=[text_to_speech,speech_to_speech,isolate_audio]
    )

def run_services():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Service interrupted by user. Exiting gracefully.")

def watch_services():
    watch_path = os.getcwd()
    print(f"Watching {watch_path} and its subdirectories for changes...")
    run_process(watch_path, recursive=True, target=run_services)

