set /p version="Version: "
".\env\Scripts\nuitka.bat" PixelColor.py --standalone --onefile --disable-console --assume-yes-for-downloads --remove-output --enable-plugin=tk-inter --windows-icon-from-ico=icon.ico --windows-company-name="SerpentModding" --windows-product-name="PixelColor" --windows-product-version=%version% --windows-file-description="PixelColor"
