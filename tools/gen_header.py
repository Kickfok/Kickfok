"""Анимированная шапка профиля GitHub Kickfok в стиле логотипа АрсанСофт: красный, желтый и оранжевый 1С,
кольца вокруг логотипа 1C MCP Ollama Bridge, линии скорости. Фон прозрачный, под ним фон страницы GitHub;
две версии - под темную и светлую тему (README выбирает через <picture>). Анимация - SMIL.

    python tools/gen_header.py
"""
import pathlib
from xml.sax.saxutils import escape

ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"
SANS = "Inter, 'Segoe UI', Arial, Helvetica, sans-serif"
MONO = "'JetBrains Mono', Consolas, 'DejaVu Sans Mono', monospace"
W, H = 1200, 340
YELLOW, ORANGE = "#FFC000", "#FF6A13"
THEMES = {
    "dark": {"ink": "#E6EDF3", "grey": "#8B949E", "box": "#161B22", "line": "#30363D", "red": "#FF4D42"},
    "light": {"ink": "#1F2328", "grey": "#59636E", "box": "#F6F8FA", "line": "#D0D7DE", "red": "#E5231B"},
}
LINES = [
    "доработки на БСП: ERP, КА, Документооборот",
    "интеграции 1С: HTTP-сервисы, обмены, отчеты",
    "локальные LLM и MCP для баз 1С",
    "настольные приложения на C# и .NET",
]
# Логотип 1C MCP Ollama Bridge, сетка 32 x 32. Центр знака - (16, 16)
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
CX, CY, LOGO_SIZE = 1030, 170, 132


def text(x, y, value, size, color, weight=400, family=SANS, extra=""):
    w = f' font-weight="{weight}"' if weight != 400 else ""
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}"{w}{extra}>{value}</text>'


def build(theme):
    c = THEMES[theme]
    ink, grey, red = c["ink"], c["grey"], c["red"]
    period = 3.2 * len(LINES)
    p = [f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Kickfok</title>
  <desc id="d">Kickfok, разработчик 1С: доработки на БСП для ERP, Комплексной автоматизации и Документооборота, интеграции, локальные LLM и MCP для баз 1С, настольные приложения на C#.</desc>
  <defs>
    <linearGradient id="speed" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{ORANGE}" stop-opacity="0"/><stop offset="1" stop-color="{ORANGE}"/>
    </linearGradient>
  </defs>"""]
    # линии скорости бегут слева к логотипу и гаснут у колец
    for i, (y, w, dur) in enumerate(((96, 260, 2.6), (128, 180, 2.1), (210, 220, 2.9), (242, 150, 2.3))):
        p.append(f'<rect x="-300" y="{y}" width="{w}" height="5" rx="2.5" fill="url(#speed)" opacity="0.45">'
                 f'<animate attributeName="x" values="-300;{CX - 170 - w}" dur="{dur}s" begin="{i * 0.5}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="0;0.45;0.45;0" keyTimes="0;0.15;0.8;1" dur="{dur}s" begin="{i * 0.5}s" repeatCount="indefinite"/></rect>')
    # кольца с общим центром с логотипом
    for r, color, width in ((150, red, 10), (126, YELLOW, 8), (103, red, 6)):
        p.append(f'<circle cx="{CX}" cy="{CY}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}" stroke-opacity="0.4"/>')
    p.append(f'<circle cx="{CX}" cy="{CY}" r="150" fill="none" stroke="{ORANGE}" stroke-width="10" stroke-dasharray="70 872" stroke-linecap="round">'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="6s" repeatCount="indefinite"/></circle>')
    half = LOGO_SIZE / 2
    p.append(f'<svg x="{CX - half}" y="{CY - half}" width="{LOGO_SIZE}" height="{LOGO_SIZE}" viewBox="0 0 32 32">{LOGO}</svg>')

    p.append(text(24, 50, "ПРИВЕТ, Я KICKFOK", 13, red, 700, MONO, ' letter-spacing="2.5"'))
    p.append(text(24, 110, f'Разработчик 1С<tspan fill="{ORANGE}">.</tspan>', 48, ink, 800))
    p.append(text(24, 164, f'Доработки, интеграции и <tspan fill="{red}">локальные LLM</tspan>.', 38, ink, 800))
    p.append(f'<path d="M24 178 H468 L460 188 H16 Z" fill="{ORANGE}"/>')

    p.append(f'<rect x="24" y="208" width="640" height="46" rx="10" fill="{c["box"]}" stroke="{c["line"]}" stroke-width="1.5"/>')
    p.append(text(44, 238, "$", 17, grey, 700, MONO))
    colors = [red, ORANGE, ink, red]
    for i, line in enumerate(LINES):
        start, end = i / len(LINES), (i + 1) / len(LINES)
        if i == 0:
            keys, values, first = f"0;{end - 0.01:.3f};{end:.3f};0.99;1", "1;1;0;0;1", 1
        else:
            keys, values, first = f"0;{start:.3f};{start + 0.01:.3f};{end - 0.01:.3f};{end:.3f};1", "0;0;1;1;0;0", 0
        p.append(f'<text x="64" y="238" font-family="{MONO}" font-size="17" font-weight="600" fill="{colors[i]}" opacity="{first}">'
                 f'{escape(line)}<animate attributeName="opacity" values="{values}" keyTimes="{keys}" dur="{period}s" repeatCount="indefinite"/></text>')

    x = 24
    for label, color in (("1С:Предприятие · БСП · BSL", red), ("Python · Ollama · MCP", ORANGE), ("C# · .NET · SQL Server", ink)):
        w = len(label) * 8.4 + 40
        p.append(f'<rect x="{x}" y="274" width="{w:.0f}" height="34" rx="17" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-opacity="0.6"/>')
        p.append(f'<circle cx="{x + 18}" cy="291" r="4" fill="{color}"/>')
        p.append(text(x + 32, 296, escape(label), 14, color, 700))
        x += w + 12
    p.append("</svg>\n")
    out = ASSETS / f"header-{theme}.svg"
    out.write_text("\n  ".join(p), encoding="utf-8", newline="\n")
    print(out)


if __name__ == "__main__":
    for name in THEMES:
        build(name)
