import lzma
import shutil

input_file = "DerpFest_GSI.img.xz"
output_file = "system.img"

print(f"Decompressing {input_file} to {output_file}...")
try:
    with lzma.open(input_file, "rb") as f_in:
        with open(output_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("Decompression Complete.")
except Exception as e:
    print(f"Error: {e}")
