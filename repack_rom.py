import tarfile
import os
import shutil

# Paths
work_dir = r"C:\Users\casey\.gemini\antigravity\scratch\Odin_Flash_TabA9"
derpfest_tar = os.path.join(work_dir, "DerpFest_Files", "AP_DERPFEST_15.2_Sm-X210.tar")
stock_dir = os.path.join(work_dir, "Stock_U9_Files")
# Find the specific Stock AP file name
stock_ap_name = [f for f in os.listdir(stock_dir) if f.startswith("AP_")][0]
stock_ap_path = os.path.join(stock_dir, stock_ap_name)

repack_dir = os.path.join(work_dir, "Repack_Temp")
output_tar = os.path.join(work_dir, "AP_DERPFEST_FIXED_U9.tar")

print(f"Starting Repack Process...")
print(f"Source DerpFest: {derpfest_tar}")
print(f"Source Stock: {stock_ap_path}")

# 1. Create Clean Temp Dir
if os.path.exists(repack_dir):
    shutil.rmtree(repack_dir)
os.makedirs(repack_dir)

# 2. Extract DerpFest (Excluding boot/dtbo)
print("Extracting DerpFest (Skipping boot/dtbo)...")
with tarfile.open(derpfest_tar, "r") as tar:
    for member in tar.getmembers():
        if "boot.img" in member.name or "dtbo.img" in member.name:
            print(f"  Skipping bad file: {member.name}")
            continue
        tar.extract(member, path=repack_dir)
        print(f"  Extracted: {member.name}")

# 3. Extract Stock (Only boot/dtbo)
print("Extracting Stock Boot/DTBO...")
with tarfile.open(stock_ap_path, "r") as tar:
    for member in tar.getmembers():
        if member.name.endswith("boot.img.lz4") or member.name.endswith("dtbo.img.lz4"):
            tar.extract(member, path=repack_dir)
            print(f"  Injecting Stock File: {member.name}")

# 4. Repack
print(f"Creating New Tar: {output_tar}")
with tarfile.open(output_tar, "w") as tar:
    for filename in os.listdir(repack_dir):
        file_path = os.path.join(repack_dir, filename)
        tar.add(file_path, arcname=filename)
        print(f"  Added: {filename}")

print("Done! Repack Successful.")
