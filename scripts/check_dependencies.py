"""Quick dependency checker for local runs.

This script verifies that core runtime dependencies are available before
running the main agents. It prints helpful installation hints (including for
proxy-restricted environments) so users can fix issues proactively.
"""
from __future__ import annotations

import importlib.util
import sys
from typing import Dict, Iterable

REQUIRED_PACKAGES: Dict[str, str] = {
    "openai": "pip install openai",
    "dotenv": "pip install python-dotenv",
    "typing_extensions": "pip install typing_extensions",
}


def has_package(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def format_install_hint(cmd: str) -> str:
    return (
        f"  - Try: `{cmd}`\n"
        "  - If behind a proxy/firewall, download the wheel on a machine with\n"
        "    internet access and install via `pip install <downloaded>.whl`.\n"
        "    You can also set a proxy with `pip install --proxy <host:port> ...`.\n"
    )


def check_dependencies(names: Iterable[str]) -> int:
    missing = []
    for pkg in names:
        if not has_package(pkg):
            missing.append(pkg)

    if not missing:
        print("✅ All required packages are installed. You can run the agents now.")
        return 0

    print("❌ Missing required packages:\n")
    for pkg in missing:
        hint_cmd = REQUIRED_PACKAGES.get(pkg, f"pip install {pkg}")
        print(f"- {pkg}\n{format_install_hint(hint_cmd)}")

    print("Once installed, re-run this checker or start the desired script, e.g.:\n"
          "  python Novel-Approach/DRTAG-llm-selection.py")
    return 1


if __name__ == "__main__":
    sys.exit(check_dependencies(REQUIRED_PACKAGES))
