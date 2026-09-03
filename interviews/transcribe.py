#!/usr/bin/env python3
import sys
from pathlib import Path
from easyaligner.text import load_tokenizer
from huggingface_hub import snapshot_download
from easytranscriber.pipelines import pipeline
from easytranscriber.text.normalization import text_normalizer

snapshot_download(
    "Lauler/easytranscriber_tutorials",
    repo_type="dataset",
    local_dir="data/tutorials",
    allow_patterns="tale-of-two-cities_short-en/*",
)

tokenizer = load_tokenizer("english")
audio_files = [
    # file.name for file in Path("data/tutorials/tale-of-two-cities_short-en").glob("*")
]

exit()

pipeline(
    vad_model="pyannote",
    emissions_model="facebook/wav2vec2-base-960h",
    transcription_model="distil-whisper/distil-large-v3.5",
    audio_paths=audio_files,
    audio_dir="data/tutorials/tale-of-two-cities_short-en",
    backend="ct2",
    language="en",
    tokenizer=tokenizer,
    text_normalizer_fn=text_normalizer,
    cache_dir="models",
)
