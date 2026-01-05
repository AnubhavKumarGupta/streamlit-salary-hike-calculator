# Quick Steps to Create EXE File

## EASIEST METHOD - Using Batch File (Recommended for users with Python)

Just double-click `run_app.bat` - No EXE needed!

---

## Create True Standalone EXE

### Option 1: Using auto-py-to-exe (GUI - EASIEST)

1. **Install the tool:**
   ```bash
   pip install auto-py-to-exe
   ```

2. **Launch GUI:**
   ```bash
   auto-py-to-exe
   ```

3. **Configure in GUI:**
   - Script Location: Browse and select `launcher.py`
   - Onefile: Select "One File"
   - Console: Select "Console Based" 
   - Additional Files: Click "Add Files" and select `salary_hike_calculator.py`
   - Advanced > Hidden Imports: Add these three:
     * streamlit
     * streamlit.web.cli
     * pandas

4. **Convert:**
   - Click "CONVERT .PY TO .EXE" button
   - Wait for completion (may take 5-10 minutes)
   - Find your EXE in the `output` folder

5. **Test:**
   - Double-click the generated EXE
   - It will open in your browser automatically

---

### Option 2: Using PyInstaller (Command Line)

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Simple Command:**
   ```bash
   pyinstaller --onefile --hidden-import=streamlit --hidden-import=streamlit.web.cli --hidden-import=pandas launcher.py
   ```

3. **Find EXE:**
   - Look in `dist` folder
   - File will be named `launcher.exe`
   - Rename it to `SalaryHikeCalculator.exe`

---

## Important Notes

⚠️ **File Size:** The EXE will be 150-250 MB (this is normal for Streamlit apps)

⚠️ **Startup Time:** First launch may take 10-30 seconds

⚠️ **Browser Requirement:** The app still opens in a browser (it's a web app)

⚠️ **Antivirus:** Some antivirus software may flag the EXE (false positive)

---

## Distribution

Once you have the EXE:

1. ✅ Copy the EXE file to any location
2. ✅ Send it to anyone (no Python needed)
3. ✅ Double-click to run
4. ✅ App opens automatically in default browser

---

## Troubleshooting

**Problem:** EXE doesn't create
- Make sure you selected `launcher.py` (not `salary_hike_calculator.py`)

**Problem:** EXE created but doesn't run
- Try running from command prompt to see error messages
- Make sure all hidden imports are added

**Problem:** Browser doesn't open
- Manually open browser and go to: http://localhost:8501

**Problem:** "Module not found" error
- Add the missing module to hidden imports

---

## Alternative: Just Share the Python Files

If creating EXE is difficult, you can share:
1. All the Python files
2. `requirements.txt`
3. `run_app.bat`

Recipients need to:
1. Install Python
2. Run: `pip install -r requirements.txt`
3. Double-click `run_app.bat`

This is often easier and more reliable than EXE!
