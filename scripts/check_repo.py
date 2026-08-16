from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/overview.md",
    "docs/dictionary.md",
    "docs/spec/message-envelope.md",
    "docs/spec/directives.md",
    "docs/spec/execution-model.md",
]


def fail(message):
    print(f"error: {message}")
    return 1


def check_required_files():
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        return fail("missing required files: " + ", ".join(missing))
    return 0


def check_markdown():
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.endswith("\n"):
            return fail(f"{path.relative_to(ROOT)} must end with a newline")
        if re.search(r"[ \t]+\n", text):
            return fail(f"{path.relative_to(ROOT)} has trailing whitespace")
        if path.name != "LICENSE" and not text.lstrip().startswith("#"):
            return fail(f"{path.relative_to(ROOT)} must start with a heading")
    return 0


def check_examples():
    example_dir = ROOT / "examples"
    files = sorted(example_dir.glob("*.oilang"))
    if len(files) < 3:
        return fail("expected at least three .oilang examples")

    for path in files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("@open-ilang 0.1\n"):
            return fail(f"{path.relative_to(ROOT)} must start with @open-ilang 0.1")
        if text.count("body:\n") != text.count("\nend"):
            return fail(f"{path.relative_to(ROOT)} has an unclosed body block")
        for family in re.findall(r"^message ([a-z.]+) id=", text, flags=re.MULTILINE):
            if "." not in family and family != "receipt":
                return fail(f"{path.relative_to(ROOT)} uses unclear message family {family}")
    return 0


def main():
    checks = [check_required_files, check_markdown, check_examples]
    for check in checks:
        result = check()
        if result:
            return result
    print("repository validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
