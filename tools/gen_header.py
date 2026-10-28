"""Анимированная шапка профиля GitHub Kickfok в стиле 1C MCP Ollama Bridge: темно-синяя карточка с сеткой и
свечением, желтый 1С, фиолетовый цвет модели. Карточка со своим фоном одинаково смотрится в темной и светлой
теме GitHub. Анимация - SMIL, первый кадр читается без нее.

    python tools/gen_header.py
"""
import pathlib
from xml.sax.saxutils import escape

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "header.svg"
SANS = "Inter, 'Segoe UI', Arial, Helvetica, sans-serif"
MONO = "'JetBrains Mono', Consolas, 'DejaVu Sans Mono', monospace"
W, H = 1200, 340
BG, CARD, LINE = "#0B0E1C", "#141831", "#262B4E"
TEXT, DIM, MUTED = "#E9ECF8", "#9AA1C9", "#6B7199"
YELLOW, VIOLET, GREEN, CYAN = "#FFC21A", "#8B7CFF", "#5EE0A0", "#6CCFF6"
LINES = [
    ("доработки на БСП: ERP, КА, Документооборот", YELLOW),
    ("интеграции 1С: HTTP-сервисы, обмены, отчеты", CYAN),
    ("локальные LLM и MCP для баз 1С", VIOLET),
    ("настольные приложения на C# и .NET", GREEN),
]
CHIPS = [("1С:Предприятие · БСП · BSL", YELLOW), ("Python · Ollama · MCP", VIOLET), ("C# · .NET · SQL Server", CYAN)]
# Логотип 1C MCP Ollama Bridge на сетке 32 x 32, центр знака (16, 16)
LOGO = """
  <rect width="32" height="32" rx="7" fill="#FFC21A"/>
  <g transform="translate(-0.7 0.6)">
    <g fill="none" stroke="#1B1F3B" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <ellipse cx="10" cy="10" rx="4.5" ry="1.8"/>
      <path d="M5.5 10 V20 C5.5 21 7.5 21.8 10 21.8 C12.5 21.8 14.5 21 14.5 20 V10"/>
      <path d="M5.5 15 C5.5 16 7.5 16.8 10 16.8 C12.5 16.8 14.5 16 14.5 15"/>
      <path d="M14.5 15 H19.5"/>
      <path d="M22 15 L26 9 M22 15 L27 15 M22 15 L26 21"/>
    </g>
    <g fill="#1B1F3B"><circle cx="22" cy="15" r="2.5"/><circle cx="26.3" cy="8.6" r="1.4"/><circle cx="27.4" cy="15" r="1.4"/><circle cx="26.3" cy="21.4" r="1.4"/></g>
    <circle r="0.9" fill="#FFFFFF"><animateMotion dur="1.6s" repeatCount="indefinite" path="M14.5 15 H21"/></circle>
  </g>"""
CX, CY, LOGO_SIZE = 1030, 170, 128


def text(x, y, value, size, color, weight=400, family=SANS, extra=""):
    w = f' font-weight="{weight}"' if weight != 400 else ""
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}"{w}{extra}>{value}</text>'


def main():
    period = 3.2 * len(LINES)
    p = [f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Kickfok</title>
  <desc id="d">Kickfok, разработчик 1С: доработки на БСП для ERP, Комплексной автоматизации и Документооборота, интеграции, локальные LLM и MCP для баз 1С, настольные приложения на C#.</desc>
  <defs>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#FFFFFF" stroke-opacity="0.045"/></pattern>
    <radialGradient id="gy" cx="8%" cy="0%" r="60%"><stop offset="0" stop-color="{YELLOW}" stop-opacity="0.2"/><stop offset="1" stop-color="{YELLOW}" stop-opacity="0"/></radialGradient>
    <radialGradient id="gv" cx="86%" cy="50%" r="35%"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0.28"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="18" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#gy)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#gv)"/>"""]

    # логотип: тонкое пунктирное кольцо и точка, которая обходит его по орбите
    p.append(f'<circle cx="{CX}" cy="{CY}" r="112" fill="none" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<circle cx="{CX}" cy="{CY}" r="112" fill="none" stroke="{YELLOW}" stroke-opacity="0.45" stroke-width="1.5" stroke-dasharray="4 10">'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="40s" repeatCount="indefinite"/></circle>')
    p.append(f'<circle r="5" fill="{VIOLET}"><animateMotion dur="9s" repeatCount="indefinite" '
             f'path="M{CX} {CY - 112} a112 112 0 1 1 -0.1 0"/></circle>')
    half = LOGO_SIZE / 2
    p.append(f'<svg x="{CX - half}" y="{CY - half}" width="{LOGO_SIZE}" height="{LOGO_SIZE}" viewBox="0 0 32 32">{LOGO}</svg>')

    p.append(text(48, 56, "ПРИВЕТ, Я KICKFOK", 13, YELLOW, family=MONO, extra=' letter-spacing="2.5"'))
    p.append(f'<path d="M232 51 H700" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(text(48, 116, f'Разработчик 1С<tspan fill="{VIOLET}">.</tspan>', 48, TEXT, 800))
    p.append(text(48, 166, f'Доработки, интеграции и <tspan fill="{YELLOW}">локальные LLM</tspan>.', 34, TEXT, 700))

    p.append(f'<rect x="48" y="196" width="640" height="46" rx="10" fill="{CARD}" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(text(68, 226, "$", 17, MUTED, 700, MONO))
    for i, (line, color) in enumerate(LINES):
        start, end = i / len(LINES), (i + 1) / len(LINES)
        if i == 0:
            keys, values, first = f"0;{end - 0.01:.3f};{end:.3f};0.99;1", "1;1;0;0;1", 1
        else:
            keys, values, first = f"0;{start:.3f};{start + 0.01:.3f};{end - 0.01:.3f};{end:.3f};1", "0;0;1;1;0;0", 0
        p.append(f'<text x="88" y="226" font-family="{MONO}" font-size="17" font-weight="600" fill="{color}" opacity="{first}">'
                 f'{escape(line)}<animate attributeName="opacity" values="{values}" keyTimes="{keys}" dur="{period}s" repeatCount="indefinite"/></text>')

    x = 48
    for i, (label, color) in enumerate(CHIPS):
        w = len(label) * 8.4 + 40
        p.append(f'<rect x="{x}" y="264" width="{w:.0f}" height="34" rx="17" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-opacity="0.5"/>')
        p.append(f'<circle cx="{x + 18}" cy="281" r="4" fill="{color}"><animate attributeName="opacity" values="1;0.3;1" dur="2.4s" begin="{i * 0.8}s" repeatCount="indefinite"/></circle>')
        p.append(text(x + 32, 286, escape(label), 14, color, 600))
        x += w + 12
    p.append("</svg>\n")
    OUT.write_text("\n  ".join(p), encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
