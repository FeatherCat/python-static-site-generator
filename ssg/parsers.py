from importlib.resources import path
from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions: List[str] = []
    def vailidate_extension(self, extension):
        if extension in self.extensions:
            return True

    def parse(self, path, source, dest) -> Path:
        raise NotImplementedError


    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest/Path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest/Path.relative_to(source))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]
    def parse(self, path, source, dest) -> Path:
        super().copy(path, source, dest)
