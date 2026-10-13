"""Check every DOI in the bibliography against the Crossref registry.

For each `doi.org` link in docs/research/04-bibliography.md the script asks
Crossref for the registered metadata and compares the registered title with
the text of the entry. It prints one line per DOI and a list of entries that
need a look: DOIs Crossref does not know, and titles that do not appear to
match. Title matching is a heuristic (shared significant words), so a flagged
entry should be read, not automatically "fixed".

Only the Python standard library is used. Crossref is a public service; the
script sends one request per DOI, with two requests in flight at a time.

    python scripts/check_references.py
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BIBLIOGRAPHY = Path(__file__).resolve().parent.parent / "docs" / "research" / "04-bibliography.md"
USER_AGENT = "complexsystemslab-reference-check (https://github.com/wefallforbeauty/complexsystemslab)"
STOP_WORDS = {"the", "and", "for", "with", "from", "into", "that", "this", "its", "their", "model", "models"}


def words(text: str) -> set[str]:
    text = re.sub(r"<[^>]+>", " ", text).lower()
    return {w for w in re.findall(r"[a-z]{4,}", text) if w not in STOP_WORDS}


def lookup(doi: str) -> dict | None:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/:;()<>.-_")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)["message"]
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return None
            time.sleep(3 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"Crossref did not answer for {doi}")


def list_items(text: str) -> list[str]:
    """Split the bibliography into list items, joining continuation lines."""
    items: list[str] = []
    for line in text.splitlines():
        if re.match(r"\s*(?:[-*]|\d+\.)\s", line):
            items.append(line.strip())
        elif line.strip() and items and line.startswith("   "):
            items[-1] += " " + line.strip()
    return items


def doi_links(item: str) -> list[str]:
    """DOIs of all doi.org links in a list item; DOIs may contain balanced parentheses."""
    found = []
    marker = "(https://doi.org/"
    start = item.find(marker)
    while start != -1:
        i = start + len(marker)
        depth = 0
        doi = []
        while i < len(item):
            ch = item[i]
            if ch == "(":
                depth += 1
            elif ch == ")":
                if depth == 0:
                    break
                depth -= 1
            doi.append(ch)
            i += 1
        found.append(urllib.parse.unquote("".join(doi)))
        start = item.find(marker, i)
    return found


def main() -> int:
    entries = []
    for item in list_items(BIBLIOGRAPHY.read_text(encoding="utf-8")):
        for doi in doi_links(item):
            entries.append((doi, item))

    def check(item: tuple[str, str]) -> tuple[str, str, str]:
        doi, line = item
        record = lookup(doi)
        if record is None:
            return doi, "NOT FOUND", ""
        title = " ".join(record.get("title") or [""])
        expected = words(title)
        shared = expected & words(line)
        status = "ok" if not expected or len(shared) >= max(1, len(expected) // 2) else "CHECK TITLE"
        return doi, status, re.sub(r"\s+", " ", title)

    problems = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        for doi, status, title in pool.map(check, entries):
            print(f"{status:<11}  {doi}  {title[:90]}")
            if status != "ok":
                problems.append((doi, status, title))

    print(f"\n{len(entries)} DOIs checked, {len(problems)} to look at.")
    for doi, status, title in problems:
        print(f"  {status}: {doi}  (Crossref title: {title or '-'})")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
