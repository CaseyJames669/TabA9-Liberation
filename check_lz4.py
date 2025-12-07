import os
import lz4.block
# Samsung LZ4 format is often just standard LZ4 Block format with a header.
# Actually, the user doesn't have `lz4` installed in python environment likely.
# I will try to use the `tar` command in windows or just tell user to flash the `.tar` via Odin?
# Wait, Phase 2 is "Infiltration via Root".
# I need raw image.
# Alternative: I can use the tablet's own tools?
# The tablet has `lz4` binary? Unlikely.
# Let's try to assume the user can just push the `.tar` and extract it on device?
# Android `tar` might support it.
# Better: Just use the `Pure_TWRP.tar` we made. It contains `recovery.img.lz4`.
# We transfer `Pure_TWRP.tar`.
# On device (root): `tar -xvf Pure_TWRP.tar`.
# Then we have `recovery.img.lz4`.
# Does Android `dd` support lz4? No.
# WE NEED RAW IMG.
# I will download a windows `lz4.exe` tool or use python.
# Let's check if python lz4 is available.

try:
    import lz4.block
    print("lz4 available")
except ImportError:
    print("lz4 NOT available")
