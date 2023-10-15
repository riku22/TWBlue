# -*- mode: python ; coding: utf-8 -*-

import platform
from PyInstaller.utils.hooks import collect_data_files

def get_architecture_files():
	""" Returns architecture files for 32 or 64 bits. """
	if platform.architecture()[0][:2] == "32":
		return [
			("..\\windows-dependencies\\x86\\oggenc2.exe", "."),
			("..\\windows-dependencies\\x86\\bootstrap.exe", "."),
			("..\\windows-dependencies\\x86\\*.dll", "."),
			("..\\windows-dependencies\\x86\\plugins", "plugins"),
		]
	elif platform.architecture()[0][:2] == "64":
		return [
			("..\\windows-dependencies\\x64\\oggenc2.exe", "."),
			("..\\windows-dependencies\\x64\\bootstrap.exe", "."),
			("..\\windows-dependencies\\x64\\*.dll", "."),
			("..\\windows-dependencies\\x64\\plugins", "plugins"),
		]

a = Analysis(
    ['main.py'],
    pathex=[],
             binaries=[("sounds", "sounds"),
("documentation", "documentation"),
("locales", "locales"),
("keymaps", "keymaps"),
#("keys/lib", "keys/lib"),
("..\\windows-dependencies\\dictionaries", "enchant\\share\\enchant\\myspell"),
#("app-configuration.defaults", "."),
#("conf.defaults", "."),
("*.defaults", "."),
("icon.ico", "."),
]+get_architecture_files(),
             datas=[]
+collect_data_files('twitter_text')
+collect_data_files('demoji'),
#             hiddenimports=["twitter_text", "yt_dlp", "mastodon"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
