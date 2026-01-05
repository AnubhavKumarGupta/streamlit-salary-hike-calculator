# 💰 Salary Hike Calculator

A beautiful and professional Streamlit application to calculate salary hike percentage with an elegant gradient UI.

## Features

✨ **Key Features:**
- 📊 Calculate salary hike percentage
- 💰 Display old salary, new salary, and difference
- 📈 Visual representation with color coding (green for hike, red for cut)
- 🎨 Modern gradient UI with smooth animations
- 📱 Responsive design
- ⚡ Real-time preview calculations
- 🎯 One-click calculation with detailed breakdown

## Screenshots

The application features:
- Beautiful gradient purple background
- Clean white calculator card with glassmorphism effect
- Emoji-based visual indicators
- Responsive two-column input layout
- Detailed breakdown of salary changes
- Motivational messages based on hike percentage

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Method 1: Run with Streamlit (Recommended for Development)

```bash
streamlit run salary_hike_calculator.py
```

The app will automatically open in your default browser at `http://localhost:8501`

### Method 2: Run with Batch File (Double-click)

Simply double-click `run_app.bat` on Windows. The application will start automatically.

### Method 3: Create Executable File

See `README_EXE_CONVERSION.md` for detailed instructions on converting this app to a standalone .exe file.

## How to Use the Calculator

1. **Enter Old Salary:** Input your current/previous salary in the left field
2. **Enter New Salary:** Input your new/proposed salary in the right field
3. **View Quick Preview:** See instant calculation preview below inputs
4. **Click Calculate:** Press the "Calculate Hike" button for detailed breakdown
5. **View Results:** 
   - Large percentage display with color coding
   - Detailed breakdown showing:
     - Old salary (₹)
     - New salary (₹)
     - Difference amount (₹)
     - Hike percentage (%)
   - Motivational message based on your hike

## Calculation Formula

```
Hike Percentage = ((New Salary - Old Salary) / Old Salary) × 100
```

### Examples:

**Example 1: Salary Increase**
- Old Salary: ₹50,000
- New Salary: ₹60,000
- Hike: +20.00% (₹10,000 increase)

**Example 2: Salary Decrease**
- Old Salary: ₹60,000
- New Salary: ₹50,000
- Change: -16.67% (₹10,000 decrease)

## Converting to EXE

For detailed instructions on creating a standalone executable file, please refer to:
- **Comprehensive Guide:** `README_EXE_CONVERSION.md`

**Quick Method:**
```bash
pip install auto-py-to-exe
auto-py-to-exe
```

Then follow the GUI instructions to convert `launcher.py` to a standalone executable.

## File Structure

```
Small Streamlit Application/
│
├── salary_hike_calculator.py    # Main application file
├── launcher.py                   # Launcher for EXE conversion
├── run_app.bat                   # Windows batch launcher
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── README_EXE_CONVERSION.md     # EXE conversion guide
```

## Technical Details

### Dependencies
- **Streamlit:** Web app framework
- **Pandas:** Data manipulation (used for future enhancements)

### Design Elements
- **Font:** Inter (Google Fonts)
- **Color Scheme:** Purple gradient (#667eea to #764ba2)
- **Effects:** Glassmorphism, smooth animations, box shadows
- **Responsive:** Works on different screen sizes

## Customization

### Changing Colors
Edit the CSS in `salary_hike_calculator.py`:
```python
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Changing Currency Symbol
Replace `₹` with your preferred currency symbol (e.g., `$`, `€`, `£`)

### Modifying Default Values
Change these values in the `st.number_input()` calls:
```python
value=50000.0,  # Default old salary
value=60000.0,  # Default new salary
```

## Troubleshooting

### Issue: Streamlit not found
**Solution:** Install streamlit
```bash
pip install streamlit
```

### Issue: App doesn't open in browser
**Solution:** Manually open: `http://localhost:8501`

### Issue: Port already in use
**Solution:** Use a different port
```bash
streamlit run salary_hike_calculator.py --server.port 8502
```

## Future Enhancements

Potential features to add:
- 📊 Salary comparison charts
- 💾 Save calculation history
- 📤 Export results to PDF
- 🧮 Multiple salary components breakdown
- 📅 Annual vs monthly salary calculator
- 💹 Tax impact calculator
- 🎯 Salary goal tracker

## License

Free to use and modify for personal and commercial purposes.

## Support

For issues or questions:
1. Check `README_EXE_CONVERSION.md` for EXE-related queries
2. Ensure all dependencies are installed
3. Verify Python version (3.7+)

## Credits

- Built with ❤️ using Streamlit
- Font: Inter by Rasmus Andersson
- Icons: Unicode Emoji

---

**Made for tracking career growth and planning your future! 🚀**
