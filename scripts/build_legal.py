#!/usr/bin/env python3
"""Convert legal markdown files to HTML pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STYLE = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.8;
            color: #333;
            background: white;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 24px 20px 40px;
        }

        h1 {
            font-size: 40px;
            font-weight: 700;
            color: #1d1d1f;
            margin-bottom: 12px;
        }

        .date {
            color: #6e6e73;
            font-size: 17px;
            margin-bottom: 40px;
        }

        h2 {
            font-size: 28px;
            font-weight: 600;
            color: #1d1d1f;
            margin-top: 40px;
            margin-bottom: 20px;
        }

        h3 {
            font-size: 21px;
            font-weight: 600;
            color: #1d1d1f;
            margin-top: 30px;
            margin-bottom: 16px;
        }

        h4 {
            font-size: 18px;
            font-weight: 600;
            color: #1d1d1f;
            margin-top: 24px;
            margin-bottom: 12px;
        }

        p {
            font-size: 17px;
            margin-bottom: 16px;
            color: #1d1d1f;
        }

        ul, ol {
            margin-left: 24px;
            margin-bottom: 16px;
        }

        li {
            font-size: 17px;
            margin-bottom: 8px;
        }

        strong {
            font-weight: 600;
        }

        hr {
            border: none;
            border-top: 1px solid #d2d2d7;
            margin: 40px 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 16px;
        }

        th, td {
            border: 1px solid #d2d2d7;
            padding: 12px;
            text-align: left;
            font-size: 17px;
        }

        th {
            background: #f5f5f7;
            font-weight: 600;
        }

        .lang-switch {
            text-align: right;
            margin-bottom: 20px;
            font-size: 15px;
        }

        .lang-switch a {
            color: #0071e3;
            text-decoration: none;
        }

        .lang-switch a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            h1 { font-size: 32px; }
            h2 { font-size: 24px; }
            h3 { font-size: 19px; }
        }
"""


def inline(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank">\1</a>', text)
    return re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)


def should_skip_line(stripped: str) -> bool:
    if stripped == "---":
        return True
    if stripped.startswith("# "):
        return True
    if re.fullmatch(r"\*\*(生效日期|最后更新|Effective Date|Last Updated)：.+?\*\*", stripped):
        return True
    return False


def md_to_body(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False
    in_table = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if should_skip_line(stripped):
            i += 1
            continue

        if stripped.startswith("|") and "|" in stripped[1:]:
            close_lists()
            if not in_table:
                out.append("<table>")
                in_table = True
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                i += 1
                continue
            tag = "th" if out[-1] == "<table>" else "td"
            row = "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells)
            out.append(f"<tr>{row}</tr>")
            i += 1
            continue
        if in_table:
            out.append("</table>")
            in_table = False

        if not stripped:
            close_lists()
            i += 1
            continue

        if stripped.startswith("## "):
            close_lists()
            out.append(f"<h2>{inline(stripped[3:])}</h2>")
            i += 1
            continue
        if stripped.startswith("### "):
            close_lists()
            out.append(f"<h3>{inline(stripped[4:])}</h3>")
            i += 1
            continue
        if stripped.startswith("#### "):
            close_lists()
            out.append(f"<h4>{inline(stripped[5:])}</h4>")
            i += 1
            continue

        if re.match(r"^\*\*.+\*\*$", stripped) and not stripped.startswith("- "):
            close_lists()
            out.append(f"<p>{inline(stripped)}</p>")
            i += 1
            continue

        if stripped.startswith("- "):
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(stripped[2:])}")
            i += 1
            subitems = []
            while i < len(lines) and re.match(r"^\s+- ", lines[i]):
                subitems.append(f"<li>{inline(lines[i].strip()[2:])}</li>")
                i += 1
            if subitems:
                out.append("<ul>" + "".join(subitems) + "</ul>")
            out.append("</li>")
            continue

        if re.match(r"^\d+\. ", stripped):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline(re.sub(r'^\\d+\\. ', '', stripped))}</li>")
            i += 1
            continue

        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            close_lists()
            out.append(
                f'<p style="margin-top: 20px; font-style: italic; color: #6e6e73;">{inline(stripped.strip("*"))}</p>'
            )
            i += 1
            continue

        close_lists()
        out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    close_lists()
    if in_table:
        out.append("</table>")
    return "\n            ".join(out)


def extract_dates(md: str, lang: str) -> tuple[str, str]:
    if lang.startswith("zh"):
        eff = re.search(r"\*\*生效日期：(.+?)\*\*", md)
        upd = re.search(r"\*\*最后更新：(.+?)\*\*", md)
        return eff.group(1), upd.group(1)
    eff = re.search(r"\*\*Effective Date: (.+?)\*\*", md)
    upd = re.search(r"\*\*Last Updated: (.+?)\*\*", md)
    return eff.group(1), upd.group(1)


def build_page(
    md_path: Path,
    out_path: Path,
    *,
    lang: str,
    title: str,
    lang_switch: str,
    date_labels: tuple[str, str],
    body_replacements: dict[str, str] | None = None,
) -> None:
    md = md_path.read_text(encoding="utf-8")
    h1 = re.search(r"^# (.+)$", md, re.M).group(1)
    effective, updated = extract_dates(md, lang)
    body = md_to_body(md)
    if body_replacements:
        for old, new in body_replacements.items():
            body = body.replace(old, new)

    date_html = (
        f'<p class="date"><strong>{date_labels[0]}{effective}</strong><br>'
        f"<strong>{date_labels[1]}{updated}</strong></p>"
    )

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{STYLE}
    </style>
</head>
<body>
    <div class="container">
            <p class="lang-switch">{lang_switch}</p>
            <h1>{inline(h1)}</h1>
            {date_html}
            {body}
    </div>
</body>
</html>
"""
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path.name} ({len(html)} bytes)")


def main() -> None:
    build_page(
        ROOT / "隐私政策.md",
        ROOT / "privacy-policy.html",
        lang="zh-CN",
        title="隐私政策 - 实时海拔计",
        lang_switch='中文 · <a href="privacy-policy-en.html">English</a>',
        date_labels=("生效日期：", "最后更新："),
    )
    build_page(
        ROOT / "用户协议.md",
        ROOT / "terms-of-service.html",
        lang="zh-CN",
        title="用户协议 - 实时海拔计",
        lang_switch='中文 · <a href="terms-of-service-en.html">English</a>',
        date_labels=("生效日期：", "最后更新："),
        body_replacements={
            "请参阅我们的《隐私政策》。": '请参阅我们的《<a href="privacy-policy.html">隐私政策</a>》。'
        },
    )
    build_page(
        ROOT / "privacy-policy-en.md",
        ROOT / "privacy-policy-en.html",
        lang="en",
        title="Privacy Policy - AltitudeNow",
        lang_switch='<a href="privacy-policy.html">中文</a> · English',
        date_labels=("Effective Date: ", "Last Updated: "),
    )
    build_page(
        ROOT / "terms-of-service-en.md",
        ROOT / "terms-of-service-en.html",
        lang="en",
        title="Terms of Service - AltitudeNow",
        lang_switch='<a href="terms-of-service.html">中文</a> · English',
        date_labels=("Effective Date: ", "Last Updated: "),
        body_replacements={
            "please see our Privacy Policy.": 'please see our <a href="privacy-policy-en.html">Privacy Policy</a>.',
            "including the Privacy Policy": 'including the <a href="privacy-policy-en.html">Privacy Policy</a>',
        },
    )


if __name__ == "__main__":
    main()
