from pathlib import Path

import whisper
from tqdm import tqdm


def find_audio_files(root_path: Path) -> list:
    audio_path = root_path / "audio"

    mp3_files = []

    for file in audio_path.glob('*.mp3'):
        mp3_files.append(file)

    return mp3_files


def audio_to_text(mp3_list: list, root_dir: Path, audio_dir: Path, output_dir: Path):
    print("Loading whisper...")
    model = whisper.load_model("base")
    print("Loading complete")

    dir_length = len(mp3_list)
    print(f"Number of audio files: {dir_length}")

    with tqdm(total=dir_length, desc="Transcribing files") as pbar:
        for file_path in audio_dir.rglob("*.mp3"):
            audio_data = whisper.load_audio(str(file_path))
            result_text = model.transcribe(audio_data, fp16=False, verbose=True)["text"]

            text_name = file_path.stem
            text_file_path = output_dir / f"{text_name}.txt"
            with text_file_path.open("w") as file:
                file.write(result_text)
            pbar.update(1)
    print("Transcription complete")
