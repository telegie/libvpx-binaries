#!/usr/bin/env bash


export CC='xcrun --sdk iphonesimulator clang'
export CXX='xcrun --sdk iphonesimulator clang++'
export EXTRA_CFLAGS="-arch arm64 -mios-version-min=14.0 -isysroot $(xcrun --sdk iphonesimulator --show-sdk-path)"

../libvpx/configure --target=generic-gnu --prefix=$(dirname $(pwd))/1.10.0/arm64-iphonesimulator
