import argparse
import hashlib
from pathlib import Path
import fitz
from app.knowledge import ensure_index,embed


def chunks(text, size = 1100, overlap=180):
    text = ' '.join(text.split())
    step = size = size-overlap
    return [text[i:i+size] for i in range(0,len(text,step) if len(text[I:I+size])> 80)]


