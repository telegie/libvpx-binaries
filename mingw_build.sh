set -e

pushd $2
"$1/libvpx/configure" --target=x86_64-win64-gcc "--prefix=$1/output/x64-windows"
make -j8
make install
pushd $2