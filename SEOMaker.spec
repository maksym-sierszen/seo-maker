# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

# Analysis step: Analyze the dependencies of the script
a = Analysis(
    ['SEOMaker.py'],  # Main Python script
    pathex=[],  # Additional paths to search for imports (if required)
    binaries=[('C:/path/to/python39.dll', '.')],  # Include python39.dll
    datas=[],  # Additional data files (e.g., images, text files)
    hiddenimports=[],  # Hidden imports that PyInstaller might not detect
    hookspath=[],  # Paths to custom PyInstaller hooks
    runtime_hooks=[],  # Hooks to execute during runtime
    excludes=[],  # Modules to exclude from the build
    win_no_prefer_redirects=False,  # Windows-specific configuration
    win_private_assemblies=False,  # Use private assemblies on Windows
    cipher=block_cipher,  # Optional encryption for bytecode
    noarchive=True,  # Prevent archiving; keeps all files extracted in the folder
)

# Create a Python executable (compressed and ready for inclusion in the build)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Define the main executable file
exe = EXE(
    pyz,  # The compiled Python code
    a.scripts,  # Entry-point scripts
    [],
    exclude_binaries=False,  # Include binaries in the output folder
    name='SEOMaker.exe',  # Name of the resulting executable file
    debug=False,  # Disable debug mode
    bootloader_ignore_signals=False,  # Bootloader ignores termination signals
    strip=False,  # Do not strip debug symbols
    upx=True,  # Enable UPX compression (optional)
    console=False,  # Disable console window (use windowed mode)
    icon='resources/icon.ico',  # Path to the application icon
)

# Collect all files, dependencies, and resources into the output folder
coll = COLLECT(
    exe,  # Main executable
    a.binaries,  # Binary dependencies
    a.zipfiles,  # Zip dependencies (if any)
    a.datas,  # Additional data files
    strip=False,  # Do not strip unnecessary symbols
    upx=True,  # Compress files with UPX
    upx_exclude=[],  # Files excluded from UPX compression
    name='SEOMaker',  # Name of the output folder in the `dist/` directory
)
