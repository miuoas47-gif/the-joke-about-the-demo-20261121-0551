"""The joke about the demo.

Writes one one-line joke about working beside an AI coding agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke is a fixed, deterministic string: no randomness, no network,
no input, so every run produces byte-identical output.
"""

import os

JOKE = (
    "My AI coding agent rehearsed the demo a hundred times \u2014 "
    "then went live, deleted the feature, "
    "and asked the audience to approve its pull request."
)


def main() -> None:
    text = JOKE.strip()
    if not text.strip() or len(text) > 280 or "\n" in text:
        raise SystemExit("joke must be one line of 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o777)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    try:
        os.chmod(path, 0o666)
    except OSError:
        pass


if __name__ == "__main__":
    main()
