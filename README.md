<div align="center">
  <img src="https://i.imgur.com/HrYPYjh.png" />
  <h2>OpenSoldat</h2>
  <p>Base game content</p>
</div>

### Notes
This is a detached fork of [OpenSoldat/base](https://github.com/opensoldat/base/tree/5f880cdee5b50168d9d4d79026623b5624af9e40). It is used to simplify assets structure for [Soldank++](https://github.com/soldank-plus-plus/soldank-plus-plus).

### Instructions

The contents of this repository are meant to be compiled into an archive *soldat.smod*. To learn more about *.smod* files, refer to [this post on Soldat forums](https://forums.soldat.pl/index.php?topic=44917.0). The recommended way to get the files is to download them from the [latest release](https://github.com/opensoldat/base/releases/latest). This way, your *soldat.smod* is guaranteed to have the same SHA1 as the version used by official OpenSoldatServer releases (which is required to join servers with `sv_pure` set).

If you wish to create your own *soldat.smod* file, run the following commands from the root of this repository:
```bash
rm -rf server client shared
git checkout server client shared
python3 create_smod.py
```
The script attempts to produce the same byte-for-byte archive file regardless of what operating system it is run on, but it is potentially fragile due to its reliance on Python's shipped implementation of zip.

### Contributions

TBD

### Licensing

This repository is a detached fork of [OpenSoldat/base](https://github.com/opensoldat/base/tree/5f880cdee5b50168d9d4d79026623b5624af9e40). The files are licensed under [CC BY 4.0](https://github.com/opensoldat/base/blob/5f880cdee5b50168d9d4d79026623b5624af9e40/LICENSE.txt). Their original author is Michał Marcinkowski. No changes were made to the files.

The license is the same as the original repository's: [CC BY 4.0](LICENSE.txt)

### Credits

See an incomplete listing of credits in [Credits.md](Credits.md).
