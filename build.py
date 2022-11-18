#!/usr/bin/env python3
import os
import platform
import subprocess
from pathlib import Path


def build_arm64_mac_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/arm64-mac"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/libvpx/configure",
                    "--target=arm64-darwin20-gcc",
                    f"--prefix={here}/install/arm64-mac"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_x64_mac_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/x64-mac"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/libvpx/configure",
                    "--target=x86_64-darwin20-gcc",
                    f"--prefix={here}/install/x64-mac"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_arm64_ios_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/arm64-ios"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/libvpx/configure",
                    "--target=arm64-darwin-gcc",
                    f"--prefix={here}/install/arm64-ios"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_arm64_iphonesimulator_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/arm64-iphonesimulator"
    if not os.path.exists(build_path):
        os.makedirs(build_path)


    cc = "xcrun --sdk iphonesimulator clang"
    cxx = "xcrun --sdk iphonesimulator clang++"

    xcrun_output = subprocess.run(["xcrun",
                                   "--sdk", "iphonesimulator",
                                   "--show-sdk-path"],
                                  capture_output=True,
                                  check=True)
    iphonesimulator_sdk_path = xcrun_output.stdout.decode("utf-8").strip()
    cflags=f"-arch arm64 -isysroot {iphonesimulator_sdk_path}"

    env = {"CC": cc, "CXX": cxx, "EXTRA_CFLAGS": cflags}

    subprocess.run([f"{here}/libvpx/configure",
                    "--target=generic-gnu",
                    f"--prefix={here}/install/arm64-iphonesimulator"],
                   cwd=build_path,
                   check=True,
                   env=env)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def build_x64_linux_binaries():
    here = Path(__file__).parent.resolve()
    build_path = f"{here}/build/x64-linux"
    if not os.path.exists(build_path):
        os.makedirs(build_path)

    subprocess.run([f"{here}/libvpx/configure",
                    "--target=x86_64-linux-gcc",
                    f"--prefix={here}/install/x64-linux"],
                   cwd=build_path,
                   check=True)
    subprocess.run(["make", "-C", build_path, "-j8"], check=True)
    subprocess.run(["make", "-C", build_path, "install"], check=True)


def main():
    if platform.system() == "Darwin":
        build_arm64_mac_binaries()
        build_x64_mac_binaries()
        build_arm64_ios_binaries()
        build_arm64_iphonesimulator_binaries()
        return
    elif platform.system() == "Linux":
        build_x64_linux_binaries()
        return

    raise Exception(f"libvpx build not supported.")


if __name__ == "__main__":
	main()