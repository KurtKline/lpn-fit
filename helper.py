from pathlib import Path
from typing import Dict

def get_files(folder: str, regex: str = '*.csv') -> Dict:
    return {filename:filename.name for filename in Path(folder).glob(regex)}