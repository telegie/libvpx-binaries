# libvpx-binaries

## Windows x64/x86 build (UWP does not require a separate build)

1. Open WSL Ubuntu.

2. Clone repository into the Windows filesystem. The repository should be cloned from WSL to avoid an issue with WSL's make not working with Windows new lines.

3. apt install perl, apt install yasm

4. mkdir build/XXX

5. For x64, ../../libvpx/configure --target=x86_64-win64-vs16, for x86, ../../libvpx/configure --target=x86-win32-vs16

6. make -j8

7. Open Powershell

8. choco install yasm

9. Add yasm to Windows environment variable Path.

10. Open vpx.sln using VS 2019 IDE.

11. Set "Whole Program Optimzation" to "No Whole Program Optimimzation", which results in removing the /GL option, for every VS project. If not, using the resulting .lib files will cause compiler warnings.

12. Build for both debug and release using VS 2019 IDE.

13. Copy the .lib files from /build to inside the repository to a version matching its file.



## WASM

1. Open WSL Ubuntu.

2. Clone repository into the Windows filesystem. The repository should be cloned from WSL to avoid an issue with WSL's make not working with Windows new lines.

3. Install emscripten separately for WSL. Do not use the version installed for Windows.

4. apt install perl

5. mkdir build/wasm, cd build/wasm, then run scripts/build-wasm.sh

6. Copy the .a files from /build to inside the repository to a version matching its file.
