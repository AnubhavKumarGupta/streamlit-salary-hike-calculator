# Salary Hike Calculator - EXE Conversion Guide

## Method 1: Using PyInstaller (Recommended)

### Step 1: Install Required Packages
```bash
pip install streamlit pandas pyinstaller
```

### Step 2: Create a Hooks File
Create a file named `hooks/hook-streamlit.py` in your project directory:

```python
from PyInstaller.utils.hooks import copy_metadata, collect_data_files

datas = copy_metadata('streamlit')
datas += collect_data_files('streamlit')
```

### Step 3: Run PyInstaller
```bash
pyinstaller --onefile --windowed --add-data "C:\Users\gupta\AppData\Local\Programs\Python\Python3XX\Lib\site-packages\streamlit;streamlit" --hidden-import streamlit --hidden-import streamlit.web.cli --icon=app_icon.ico salary_hike_calculator.py
```

**Note:** Replace `Python3XX` with your Python version (e.g., Python311, Python310)

### Step 4: Alternative Simple Command
```bash
pyinstaller --onefile salary_hike_calculator.py
```

The executable will be created in the `dist` folder.

---

## Method 2: Using Streamlit Executable Script

### Step 1: Create a Launcher Script
Save this as `run_app.bat`:

```batch
@echo off
cd /d "%~dp0"
streamlit run salary_hike_calculator.py
pause
```

This creates a simple batch file that users can double-click to run the app.

---

## Method 3: Using PyInstaller with Streamlit (Advanced)

### Step 1: Create a Python Launcher
Create `launcher.py`:

```python
import os
import sys
from streamlit.web import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "salary_hike_calculator.py", 
                "--server.headless", "true",
                "--server.port", "8501",
                "--browser.gatherUsageStats", "false"]
    sys.exit(stcli.main())
```

### Step 2: Create PyInstaller Spec File
Create `salary_calculator.spec`:

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('salary_hike_calculator.py', '.')],
    hiddenimports=['streamlit', 'streamlit.web.cli', 'pandas'],
    hookspath=['hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SalaryHikeCalculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

### Step 3: Build with Spec File
```bash
pyinstaller salary_calculator.spec
```

---

## Method 4: Using Auto-py-to-exe (GUI Tool - Easiest for Beginners)

### Step 1: Install auto-py-to-exe
```bash
pip install auto-py-to-exe
```

### Step 2: Launch the GUI
```bash
auto-py-to-exe
```

### Step 3: Configure Settings in GUI
1. **Script Location:** Select `launcher.py`
2. **Onefile:** Select "One File"
3. **Console Window:** Select "Console Based"
4. **Additional Files:** Add `salary_hike_calculator.py`
5. **Hidden Imports:** Add:
   - streamlit
   - streamlit.web.cli
   - pandas
6. Click "Convert .py to .exe"

---

## Quick Start Commands

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Run Locally:
```bash
streamlit run salary_hike_calculator.py
```

### Create EXE (Simple):
```bash
pip install pyinstaller
pyinstaller --onefile salary_hike_calculator.py
```

---

## Important Notes

1. **Streamlit Challenges:** Streamlit apps are web-based and creating a true standalone EXE can be complex.

2. **Best Approach:** The batch file method (`run_app.bat`) is the simplest and most reliable for distribution if users have Python installed.

3. **True Standalone EXE:** For a true standalone executable, consider using Method 3 or 4, but be aware that:
   - The EXE file will be large (100-200 MB)
   - It takes time to start
   - It still opens in a browser

4. **Alternative:** Consider converting to a different framework (like PyQt or Tkinter) for true desktop app experience.

5. **File Size:** PyInstaller EXE files for Streamlit apps are typically 150-250 MB due to bundled dependencies.

---

## Troubleshooting

### Issue: "Module not found" errors
**Solution:** Add the missing module to hidden imports:
```bash
pyinstaller --onefile --hidden-import=MODULE_NAME salary_hike_calculator.py
```

### Issue: EXE is too large
**Solution:** Use UPX compression:
```bash
pyinstaller --onefile --upx-dir=PATH_TO_UPX salary_hike_calculator.py
```

### Issue: Browser doesn't open automatically
**Solution:** The app will print a URL in the console. Copy and paste it into your browser.

---

## Distribution

Once you have the EXE:
1. Locate it in the `dist` folder
2. Test it on a clean system (without Python installed)
3. Distribute the EXE file to users
4. Users just need to double-click to run

---

## Recommended Approach

**For users WITH Python:**
Use the `.bat` launcher file - simplest and most reliable.

**For users WITHOUT Python:**
Use Method 4 (auto-py-to-exe) with the launcher script - creates a standalone executable.
