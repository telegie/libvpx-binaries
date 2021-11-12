# libvpx-binaries

## Windows x64 Build

1. Open msys2 from x64 Native Tools Command Prompt for VS 2022 with the following to open a msys2 shell inheriting PATH environment variable of the command prompt: msys2_shell.cmd -full-path

2. mkdir build

3. mkdir install

4. cd build

5. ../libvpx/configure --target=x86_64-win64-vs16 --prefix=../install

6. make -j8

7. make install

## For wasm, building using a Mac:

1. mkdir build

2. cd build

3. run ../scripts/configure-wasm.sh (or configure-wasm-mt.sh). Note that these scripts use brion-libvpx, a fork of libvpx optimized for wasm.

4. emmake make

5. emmake make install

6. Copy files of /install into a folder matching the version and platform.

### TODO for wasm build

Add multithreading and SIMD when they are supported by browser. Multihreading is not supported by Safari and SIMD support for web assembly is currently experimental in all browsers (i.e., Chrome, Firefox, and Safari). See following for implementation: https://github.com/brion/ogv.js/blob/master/buildscripts/compileVpxWasmSIMDMT.sh

## For iOS:

1. mkdir build

2. cd build

3. ../libvpx/configure --target=arm64-darwin-gcc --prefix="../install"

--target=arm64-darwin20-gcc is macOS only...)

4. make

5. make install

6. Copy files of /install into a folder matching the version and platform.
