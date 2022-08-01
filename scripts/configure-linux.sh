#!/usr/bin/env bash

export EXTRA_CLFAGS="-fPIC"

../libvpx/configure --target=x86_64-linux-gcc --prefix=$(dirname $(pwd))/1.10.0/x64-linux
