import yt_dlp
import os

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_youtube_audio(url: str) -> str:

    output_path = os.path.join(
        DOWNLOAD_DIR,
        "%(title)s.%(ext)s"
    )

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "quiet": False,
        "noplaylist": True,
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return filename


def process_input(source: str) -> list:

    source = source.strip()

    if source.startswith("http://") or source.startswith("https://"):
        print("Downloading YouTube audio...")
        file_path = download_youtube_audio(source)
        return [file_path]

    if os.path.exists(source):
        print("Using local file...")
        return [source]

    raise FileNotFoundError(
        f"File not found:\n{source}"
    )