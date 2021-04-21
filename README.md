# libvpx-binaries

Use WSL Ubuntu.

apt install yasm

../../libvpx/configure --target=x86_64-win64-vs16

choco install yasm

make -j8

Add yasm to Windows environment variable Path.

Build for debug and release with VS 2019 IDE.

Copy the .lib files.



For x86-uwp, in WSL (no extra care for UWP required):

../../libvpx/configure --target=x86-win32-vs16
