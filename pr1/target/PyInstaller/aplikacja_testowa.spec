# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Artur\\Desktop\\PycharmProjects\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\Artur\\Desktop\\PycharmProjects\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['f:\\python\\python 3\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\Artur\\AppData\\Local\\Temp\\tmp3mn4qjho\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='aplikacja_testowa',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\Artur\\Desktop\\PycharmProjects\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='aplikacja_testowa')
