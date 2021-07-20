#!/bin/bash

# from: https://github.com/brion/ogv.js/blob/master/buildscripts/compileVpxWasm.sh
STRIP=./buildscripts/fake-strip.sh \
  emconfigure ../brion-libvpx/configure \
    --prefix="../install" \
    --target=generic-gnu \
    --extra-cflags=-pthread\ -s\ USE_PTHREADS=1\ -I`dirname \`which emcc\``/system/lib/libcxxabi/include/ \
    --enable-multithread \
    --disable-shared \
    --disable-docs \
    --disable-examples \
    --disable-tools \
    --disable-unit-tests \
|| exit 1
