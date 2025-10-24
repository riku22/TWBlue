# Build a TW Blue installer.
# Must be called from root of repo
echo "Generating documentation..."
cd doc
uv run documentation_importer.py
uv run generator.py
mv documentation ..\src
cd ..
echo "done."

echo "Building binary..."
cd src
uv run python -OO -m PyInstaller main_1.spec
cd ..
echo "done."
