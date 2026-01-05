from PyInstaller.utils.hooks import copy_metadata, collect_data_files

# Copy metadata (version info, etc.)
datas = copy_metadata('streamlit')

# Copy all static assets (HTML, CSS, JS)
datas += collect_data_files('streamlit')
