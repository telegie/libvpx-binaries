#!/bin/bash

# from: https://github.com/brion/ogv.js/blob/master/buildscripts/compileVpxWasm.sh
STRIP=./buildscripts/fake-strip.sh \
  emconfigure ../libvpx/configure \
    --target=generic-gnu \
    --prefix="../install" \
    --extra-cflags=-s\ WASM=1\ -DWASM\ -I`dirname \`which emcc\``/system/lib/libcxxabi/include/ \
    --disable-multithread \
    --disable-shared \
    --disable-docs \
    --disable-examples \
    --disable-tools \
    --disable-unit-tests \
|| exit 1
