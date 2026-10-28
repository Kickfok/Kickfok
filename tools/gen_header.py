"""Анимированная шапка профиля GitHub Kickfok в стиле логотипа АрсанСофт: светлый фон, черный текст,
красный, желтый и оранжевый 1С, концентрические дуги и линии скорости. Справа логотип 1C MCP Ollama Bridge.
Анимация - SMIL, первый кадр читается без нее.

    python tools/gen_header.py
"""
import pathlib
from xml.sax.saxutils import escape

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "header.svg"
SANS = "Inter, 'Segoe UI', Arial, Helvetica, sans-serif"
MONO = "'JetBrains Mono', Consolas, 'DejaVu Sans Mono', monospace"
W, H = 1200, 360
RED, YELLOW, ORANGE, INK, GREY, PAPER = "#E5231B", "#FFC000", "#FF6A13", "#16181D", "#5C6270", "#FBFAF7"

LINES = [
    "доработки на БСП: ERP, КА, Документооборот",
    "интеграции 1С: HTTP-сервисы, обмены, отчеты",
    "локальные LLM и MCP для баз 1С",
    "настольные приложения на C# и .NET",
]
CHIPS = [("1С:Предприятие · БСП · BSL", RED), ("Python · Ollama · MCP", ORANGE), ("C# · .NET · SQL Server", INK)]

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


def text(x, y, value, size, color, weight=400, family=SANS, extra=""):
    w = f' font-weight="{weight}"' if weight != 400 else ""
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}"{w}{extra}>{value}</text>'


def main():
    period = 3.2 * len(LINES)
    p = [f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Kickfok</title>
  <desc id="d">Kickfok: разработчик 1С. Доработки на БСП для ERP, Комплексной автоматизации и Документооборота, интеграции, локальные LLM и MCP для баз 1С, настольные приложения на C#. Справа логотип проекта 1C MCP Ollama Bridge.</desc>
  <defs>
    <linearGradient id="speed" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{ORANGE}" stop-opacity="0"/><stop offset="1" stop-color="{ORANGE}"/>
    </linearGradient>
    <clipPath id="card"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <rect width="{W}" height="{H}" rx="18" fill="{PAPER}"/>
  <g clip-path="url(#card)">"""]
    # концентрические дуги знака 1С за логотипом
    for r, color, width in ((150, RED, 24), (120, YELLOW, 20), (92, RED, 16)):
        p.append(f'<circle cx="1050" cy="180" r="{r}" fill="none" stroke="{color}" stroke-width="{width}" stroke-opacity="0.13"/>')
    # линии скорости: оранжевые полосы, которые бегут к логотипу
    for i, (y, w, dur) in enumerate(((118, 260, 2.6), (150, 180, 2.1), (214, 220, 2.9), (246, 150, 2.3))):
        p.append(f'<rect x="-300" y="{y}" width="{w}" height="6" rx="3" fill="url(#speed)" opacity="0.55">'
                 f'<animate attributeName="x" values="-300;{W - 340}" dur="{dur}s" begin="{i * 0.5}s" repeatCount="indefinite"/></rect>')
    p.append("</g>")
    p.append(f'<rect x="0" y="0" width="10" height="{H}" fill="{RED}" clip-path="url(#card)"/>')

    p.append(text(48, 64, "ПРИВЕТ, Я KICKFOK", 13, RED, 700, MONO, ' letter-spacing="2.5"'))
    p.append(text(48, 126, f'Разработчик 1С<tspan fill="{ORANGE}">.</tspan>', 48, INK, 800))
    p.append(text(48, 182, f'Доработки, интеграции и <tspan fill="{RED}">локальные LLM</tspan>.', 38, INK, 800))
    # наклонная оранжевая плашка под словом, как полоса в логотипе
    p.append(f'<path d="M48 196 H492 L484 206 H40 Z" fill="{ORANGE}"/>')

    p.append(f'<rect x="48" y="226" width="640" height="46" rx="10" fill="#FFFFFF" stroke="#E4E1DA" stroke-width="1.5"/>')
    p.append(text(68, 256, "$", 17, GREY, 700, MONO))
    colors = [RED, ORANGE, INK, RED]
    for i, line in enumerate(LINES):
        start, end = i / len(LINES), (i + 1) / len(LINES)
        if i == 0:
            keys, values, first = f"0;{end - 0.01:.3f};{end:.3f};0.99;1", "1;1;0;0;1", 1
        else:
            keys, values, first = f"0;{start:.3f};{start + 0.01:.3f};{end - 0.01:.3f};{end:.3f};1", "0;0;1;1;0;0", 0
        p.append(f'<text x="88" y="256" font-family="{MONO}" font-size="17" font-weight="600" fill="{colors[i]}" opacity="{first}">'
                 f'{escape(line)}<animate attributeName="opacity" values="{values}" keyTimes="{keys}" dur="{period}s" repeatCount="indefinite"/></text>')

    x = 48
    for label, color in CHIPS:
        w = len(label) * 8.4 + 40
        p.append(f'<rect x="{x}" y="292" width="{w:.0f}" height="34" rx="17" fill="{color}" fill-opacity="0.08" stroke="{color}" stroke-opacity="0.6"/>')
        p.append(f'<circle cx="{x + 18}" cy="309" r="4" fill="{color}"/>')
        p.append(text(x + 32, 314, escape(label), 14, color, 700))
        x += w + 12

    p.append(f'<svg x="940" y="80" width="200" height="200" viewBox="0 0 32 32">{LOGO}</svg>')
    p.append("</svg>\n")
    OUT.write_text("\n  ".join(p), encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
