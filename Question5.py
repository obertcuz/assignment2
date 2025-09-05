from abc import ABC, abstractmethod

# -------------------------------
# Abstract Base Class
# -------------------------------

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

# -------------------------------
# Concrete Class: Text File Handler
# -------------------------------

class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

# -------------------------------
# Concrete Class: Binary File Handler
# -------------------------------

class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)

# -------------------------------
# Example Usage
# -------------------------------

if __name__ == "__main__":
    # Text file example
    text_handler = TextFileHandler("example.txt")
    text_handler.write("Hello, Tatenda!")
    print("Text file content:", text_handler.read())

    # Binary file example
    binary_handler = BinaryFileHandler("example.bin")
    binary_handler.write(b'\x48\x65\x6C\x6C\x6F')  # "Hello" in bytes
    print("Binary file content:", binary_handler.read())
