#!/usr/bin/env python3
"""Detect local Cubase and Steinberg tooling without modifying the system."""

from __future__ import annotations

import json
import os
import plistlib
import shutil
from glob import glob
from pathlib import Path


def app_info(app_path: str) -> dict:
    info_path = Path(app_path) / "Contents" / "Info.plist"
    result = {"path": app_path, "name": Path(app_path).name}
    if info_path.exists():
        try:
            with info_path.open("rb") as f:
                plist = plistlib.load(f)
            result.update(
                {
                    "bundle_id": plist.get("CFBundleIdentifier"),
                    "display_name": plist.get("CFBundleDisplayName")
                    or plist.get("CFBundleName"),
                    "short_version": plist.get("CFBundleShortVersionString"),
                    "bundle_version": plist.get("CFBundleVersion"),
                }
            )
        except Exception as exc:  # pragma: no cover - defensive local probing
            result["plist_error"] = str(exc)
    return result


def existing_dirs(paths: list[str]) -> list[str]:
    return [path for path in paths if Path(path).exists()]


def main() -> None:
    home = Path.home()
    app_globs = [
        "/Applications/Cubase*.app",
        "/Applications/Steinberg*.app",
        str(home / "Applications" / "Cubase*.app"),
        str(home / "Applications" / "Steinberg*.app"),
    ]
    apps = []
    for pattern in app_globs:
        apps.extend(app_info(path) for path in sorted(glob(pattern)))

    vst_dirs = existing_dirs(
        [
            "/Library/Audio/Plug-Ins/VST3",
            "/Library/Audio/Plug-Ins/VST",
            str(home / "Library/Audio/Plug-Ins/VST3"),
            str(home / "Library/Audio/Plug-Ins/VST"),
            str(home / "Library/Audio/Plug-Ins/Components"),
        ]
    )

    utilities = {
        "steinberg_download_assistant": bool(
            glob("/Applications/Steinberg Download Assistant.app")
            or glob(str(home / "Applications/Steinberg Download Assistant.app"))
        ),
        "audio_midi_setup": Path("/System/Applications/Utilities/Audio MIDI Setup.app").exists(),
        "auval": shutil.which("auval") is not None,
    }

    print(
        json.dumps(
            {
                "platform": os.uname().sysname,
                "apps": apps,
                "vst_dirs": vst_dirs,
                "utilities": utilities,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
