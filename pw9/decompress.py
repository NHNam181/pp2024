import zipfile

def decompress_files(compressed_file, extract_to):
    with zipfile.ZipFile(compressed_file, "r") as zipf:
        zipf.extractall(extract_to)

if __name__ == "__main__":
    compressed_file = "students.dat"
    
    extract_to = "students_data"

    decompress_files(compressed_file, extract_to)
