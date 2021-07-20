# libvpx-binaries

## Windows x64 build

1. Open WSL Ubuntu.

2. Clone repository into the Windows filesystem. The repository should be cloned from WSL to avoid an issue with WSL's make not working with Windows new lines.

3. apt install perl, apt install yasm

4. mkdir build/XXX

5. ../../libvpx/configure --target=x86_64-win64-vs16

6. make -j8

7. Open Powershell

8. choco install yasm

9. Add yasm to Windows environment variable Path.

10. Open vpx.sln using VS 2019 IDE.

11. Set "Whole Program Optimzation" to "No Whole Program Optimimzation", which results in removing the /GL option, for every VS project. If not, using the resulting .lib files will cause compiler warnings.

12. Build for both debug and release using VS 2019 IDE.

13. Copy the .lib files from /build to inside the repository to a version matching its file.

## For Mac:

1. mkdir build

2. cd build

3. ../libvpx/configure --target=x86_64-darwin20-gcc --prefix="../install"

4. make

5. make install

6. Copy files of /install into a folder matching the version and platform.

## For wasm, building using a Mac:

1. mkdir build

2. cd build

3. run ../scripts/configure-wasm.sh (or configure-wasm-mt.sh)

4. emmake make

5. emmake make install

6. Copy files of /install into a folder matching the version and platform.

### TODO for wasm build

Add multithreading and SIMD when building this. SIMD support for web assembly is currently experimental, so not yet. reference: https://github.com/brion/ogv.js/blob/master/buildscripts/compileVpxWasmSIMDMT.sh

## For iOS:

1. mkdir build

2. cd build

3. ../libvpx/configure --target=arm64-darwin-gcc --prefix="../install"

4. make

5. make install

6. Copy files of /install into a folder matching the version and platform.
