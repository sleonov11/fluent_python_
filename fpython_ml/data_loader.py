import logging
from pypdf import PDFReader
import docx2txt
from abc import ABC, abstractmethod
from typing import Dict, Optional, Union, List
from pathlib import Path

from rapidfuzz.process_cpp_impl import extract

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FileHandler(ABC):
    @abstractmethod
    def read(self, file_path: Union[str, Path]) -> Optional[str]:
        pass

    @classmethod
    @abstractmethod
    def can_handle(cls, extension: str) -> bool:
        pass

class TxtHandler(FileHandler):
    def read(self, file_path: Union[str, Path]) -> Optional[str]:

        path = Path(file_path)
        try:
            text = path.read_text(encoding='utf-8')
            logger.info(f"успешно загружен TXT: {path.name}")
            return text
        except Exception as e:
            logger.error(f"шибка чтения{path.name}: {e}")
            return None

    @classmethod
    def can_handle(cls, extension: str) -> bool:
        return extension.lower() == '.txt'

class PDFHandler(FileHandler):
    def read(self, file_path: Union[str, Path]) -> Optional[str]:
        path = Path(file_path)
        try:
            reader = PDFReader(path)
            text_pages = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text_pages.append(page_text)
            text = '\n'.join(text_pages)
            logger.info(f"PDF успешно загружен: {path.name}")
            return text
        except Exception as e:
            logger.error(f"Ошибка чтения PDF {path.name}: {e}")
            return None

    @abstractmethod
    def can_handle(cls, extension: str) -> bool:
        return extension.lower() == '.pdf'


