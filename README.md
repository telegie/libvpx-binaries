# libvpx-binaries

## Windows x64 Build

1. Open mingw64.
2. mkdir build
3. mkdir install
4. cd build
5. ../libvpx/configure --target=x86_64-win64-gcc --prefix=../1.10.0/x64-windows
6. make -j8
7. make install

## For Mac:

1. mkdir build
2. cd build
3. ../libvpx/configure --target=arm64-darwin20-gcc --prefix=../1.10.0/arm64-mac
4. make -j8
5. make install

## For Linux:

1. apt install build-essential yasm
2. mkdir build
3. cd build
4. ../scripts/configure-linux.sh
5. make -j8
6. make install

## For iOS:

1. mkdir build
2. cd build
3. ../libvpx/configure --target=arm64-darwin-gcc --prefix=../1.10.0/arm64-ios
4. make -j8
5. make install

## For iPhone Simulator:

1. mkdir build
2. cd build
3. ../scripts/configure-iphonesimulator.sh
4. make -j8
5. make install

