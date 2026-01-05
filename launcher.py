import os
import sys
from streamlit.web import cli as stcli

if __name__ == '__main__':
    # Determine the path to the bundled files
    if getattr(sys, 'frozen', False):
        # We are running in a bundle
        base_dir = sys._MEIPASS
    else:
        # We are running in a normal Python environment
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
    app_path = os.path.join(base_dir, 'salary_hike_calculator.py')
    
    # Set up Streamlit arguments
    sys.argv = [
        "streamlit", 
        "run", 
        app_path,
        "--global.developmentMode=false",
        "--server.headless=false",  # Ensure browser (headless=false)
    ]
    
    sys.exit(stcli.main())
