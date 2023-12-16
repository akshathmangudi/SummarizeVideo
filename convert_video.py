import os
from pathlib import Path
from pytube import YouTube


def link_to_audio(yt_link):
    """
    The following function converts a given YouTube link and converts it .mp3 (audio) file.

    :param yt_link: The YouTube link
    :return: returns a .mp3 file inside the /audio directory.
    """

    # The root path and output path being defined here.
    root_path = Path.cwd()
    output_path = root_path / "audio"

    # Calling the constructor for the link and only extracting the audio.
    youtube = YouTube(yt_link)
    video = youtube.streams.filter(only_audio=True).first()

    # If the output path does not exist, create one.
    if output_path.is_dir():
        print(f"{output_path} already exists.")
    else:
        print(f"{output_path} not found, creating one...")
        output_path.mkdir(parents=True, exist_ok=True)

    # Download the file and save it into the 'audio' directory
    out_file = video.download(output_path=output_path)
    base, ext = os.path.splitext(out_file)

    # Rename the file and save it as .mp3
    result_file = base + '.mp3'
    os.rename(out_file, result_file)
