'''
Docstring for read file chunk
reading the text in chunks

'''
def read_in_chunks(file_path, chunk_size = 1024):
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

for part in read_in_chunks("bigfile.txt", 1024):
    print(len(part))
         
with open("bigfile.txt", "rb") as f:
    data = f.read()

print("total bytes: ", len(data))
print("last 50 bytes: ", data[-50:])


with open("bigfile.txt", "rb") as f:
    f.seek(1024)
    print(f.read(14))  