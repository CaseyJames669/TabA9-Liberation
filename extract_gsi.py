import tarfile
import os

work_dir = r"C:\Users\casey\.gemini\antigravity\scratch\Odin_Flash_TabA9\DerpFest_Files"
tar_name = "AP_DERPFEST_15.2_Sm-X210.tar"
tar_path = os.path.join(work_dir, tar_name)
dest_dir = r"C:\Users\casey\.gemini\antigravity\scratch\Odin_Flash_TabA9"

print(f"Opening {tar_name}...")
with tarfile.open(tar_path, "r") as tar:
    for member in tar.getmembers():
        # Extact system.img (and product.img if present, GSI usually needs system)
        if member.name.endswith("system.img") or member.name.endswith("system.img.lz4"):
            print(f"Extracting {member.name}...")
            tar.extract(member, path=dest_dir)
        elif member.name.endswith("product.img") or member.name.endswith("product.img.lz4"):
             print(f"Extracting {member.name}...")
             tar.extract(member, path=dest_dir)

print("Extraction Complete.")
