# -*- mode: python -*-

block_cipher = None


a = Analysis(['interface.py/Users/jjxu/anaconda3/envs/py36/bin/pythonw', '/Users/jjxu/Documents/GitHub/LEO/interface.py'],
             pathex=['/Users/jjxu/Documents/GitHub/LEO'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pythonw',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='pythonw.app',
             icon=None,
             bundle_identifier=None)
