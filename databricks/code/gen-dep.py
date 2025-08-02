import os
import tempfile
import subprocess
import glob
import re

def extract_package_names(wheel_files):
    pkg_names = set()
    pattern = re.compile(r'^([A-Za-z0-9_\-\.]+)-[\d]')

    for file in wheel_files:
        base = os.path.basename(file)
        match = pattern.match(base)
        if match:
            pkg_names.add(match.group(1).lower())

    return sorted(pkg_names)

def generate_allowlist(requirements_file="requirements.txt"):
    if not os.path.exists(requirements_file):
        print(f"❌ {requirements_file} not found")
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"📦 Downloading dependencies to temp dir: {tmpdir}")
        subprocess.run([
            "pip", "download",
            "-r", requirements_file,
            "-d", tmpdir
        ], check=True)

        wheel_files = glob.glob(os.path.join(tmpdir, "*"))
        packages = extract_package_names(wheel_files)

        print("\n✅ Add these to your bandersnatch.conf [allowlist]:\n")
        for pkg in packages:
            print(pkg)

if __name__ == "__main__":
    generate_allowlist()
