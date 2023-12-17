from pathlib import Path
from utils.convert_video import link_to_audio
from utils.convert_audio import find_audio_files, audio_to_text

root_dir = Path.cwd()
audio_dir = root_dir / Path('audio')
output_dir = root_dir / Path('text')

if __name__ == "__main__":
    link_to_audio('https://www.youtube.com/watch?v=aQk-gCqq30k&t=1s')
    files = find_audio_files(root_dir)
    audio_to_text(files, root_dir=root_dir, audio_dir=audio_dir, output_dir=output_dir)

