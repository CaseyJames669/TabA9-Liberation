# Galaxy Tab A9+ (SM-X210) DerpFest A15 Flashing Guide

> [!WARNING]
> **READ BEFORE PROCEEDING**
> *   **Data Wipe**: Unlocking the bootloader will **erase all data** on your tablet.
> *   **Warranty**: This will void your warranty and trip Knox.
> *   **Risk**: Flashing custom ROMs carries a risk of bricking your device. Proceed at your own risk.

## 1. Preparation

### Included Files (in this folder)
*   **Samsung_USB_Driver.exe**: Official Samsung Drivers. Run this first!

### Files You Must Download
*   **DerpFest A15 ROM (+ Odin)**: [DerpFest_A15.zip (Google Drive)](https://drive.google.com/file/d/15brUGXWrHB1DIFMV56tXBR0JIE5AQNEb/view?usp=sharing)
    *   *Note: This file is ~2GB. Download it and extract it to a folder.*

---

## 2. Install Drivers
1.  Double-click `Samsung_USB_Driver.exe` in this folder.
2.  Follow the prompts to install the drivers.
3.  Reboot your computer if requested.

---

## 3. Unlock Bootloader (If not already done)
1.  Enable **Developer Options** on your tablet:
    *   Go to *Settings > About Tablet > Software Information*.
    *   Tap *Build Number* 7 times until it says "Developer mode has been turned on".
2.  Enable **OEM Unlocking**:
    *   Go to *Settings > Developer Options*.
    *   Toggle *OEM Unlocking* ON.
3.  **Enter Download Mode**:
    *   Power off the tablet completely.
    *   Hold both **Volume Up** and **Volume Down** buttons.
    *   While holding the buttons, plug the USB cable into the PC.
    *   Release buttons when the blue/green warning screen appears.
4.  **Unlock**:
    *   Long press **Volume Up** (Device Unlock Mode).
    *   Press **Volume Up** again to confirm "Yes" (Wipe Data).
    *   The tablet will reboot and wipe. You will need to set it up again quickly to verify OEM Unlock is greyed out (Unlocked).

---

## 4. Flash the ROM
1.  **Extract** the `DerpFest...zip` you downloaded.
2.  Run `Odin3_v3.14.4.exe` (found inside the extracted folder).
3.  **Boot into Download Mode** again (Power off -> Hold Vol Up+Down -> Plug in).
    *   Press Volume Up once to continue to the "Source" screen.
    *   Odin should show a blue box in `ID:COM` (e.g., `0:[COM3]`).
4.  **Select File**:
    *   Click the **AP** button in Odin.
    *   Select the `.tar.md5` file from the extracted ROM folder (e.g., `ap_gsi...`).
5.  **Flash**:
    *   Click **Start**.
    *   Wait for the "PASS!" message. The tablet will reboot.

---

## 5. Critical Final Step (Recovery Wipe)
1.  As soon as the tablet reboots, or if it bootloops, you must enter **Recovery Mode**.
    *   (Usually: Power off, then Hold Power + Vol Up while connected to USB).
    *   *Note: DerpFest recovery might look different than stock.*
2.  Select **Factory Reset / Wipe Data**.
3.  Select **Format Data**.
4.  Reboot System.

> [!TIP]
> If you get stuck or the device doesn't boot, verify you were on the correct **Binary 7 Firmware** (OneUI 6.0 / Android 14 base) before flashing.
