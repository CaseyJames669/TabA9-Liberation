import tarfile
import os

# Paths
work_dir = r"C:\Users\casey\.gemini\antigravity\scratch\Odin_Flash_TabA9\DerpFest_Files"
recovery_img = "recovery.img.lz4"
output_tar = r"C:\Users\casey\.gemini\antigravity\scratch\Odin_Flash_TabA9\Pure_TWRP.tar"

print(f"Packing {recovery_img} into {output_tar}...")

with tarfile.open(output_tar, "w") as tar:
    tar.add(os.path.join(work_dir, recovery_img), arcname=recovery_img)
    print("Added recovery.img.lz4")

print("Done.")
