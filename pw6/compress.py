import zipfile

def compress_files(filenames, compressed_file, compression_method):
    with zipfile.ZipFile(compressed_file, "w") as zipf:
        for filename in filenames:
            zipf.write(filename, compress_type=compression_method)

if __name__ == "__main__":
    filenames = ["students.txt", "courses.txt", "marks.txt"]

    compressed_file = "students.dat"

    compression_method = zipfile.ZIP_DEFLATED

    compress_files(filenames, compressed_file, compression_method)
