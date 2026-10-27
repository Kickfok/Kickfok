"""Анимированная шапка профиля GitHub Kickfok в стиле 1C MCP Ollama Bridge: темный фон с сеткой, желтый 1С,
фиолетовый цвет модели. Анимация - SMIL, первый кадр читается без нее.

    python tools/gen_header.py
"""
import pathlib
from xml.sax.saxutils import escape

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "header.svg"
SANS = "Inter, 'Segoe UI', Arial, Helvetica, sans-serif"
MONO = "'JetBrains Mono', Consolas, 'DejaVu Sans Mono', monospace"
W, H = 1200, 360
YELLOW, VIOLET, GREEN, CYAN, TEXT, DIM, MUTED = "#FFC21A", "#8B7CFF", "#5EE0A0", "#6CCFF6", "#E9ECF8", "#9AA1C9", "#6B7199"

# Строки "терминала": сменяют друг друга по кругу
LINES = [
    ("доработки на БСП: ERP, КА, Документооборот", YELLOW),
    ("интеграции 1С: HTTP-сервисы, обмены, отчеты", CYAN),
    ("локальные LLM и MCP для баз 1С", VIOLET),
    ("настольные приложения на C# и .NET", GREEN),
]
CHIPS = [("1С:Предприятие · БСП · BSL", YELLOW), ("Python · Ollama · MCP", VIOLET), ("C# · .NET · SQL Server", CYAN)]


def text(x, y, value, size, color, weight=400, family=SANS, extra=""):
    w = f' font-weight="{weight}"' if weight != 400 else ""
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}"{w}{extra}>{value}</text>'


def main():
    period = 3.2 * len(LINES)
    parts = [f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Kickfok</title>
  <desc id="d">Kickfok: разработчик 1С. Доработки на БСП для ERP, Комплексной автоматизации и Документооборота, интеграции, локальные LLM и MCP для баз 1С, настольные приложения на C#. Стек: 1С:Предприятие, БСП, BSL, Python, Ollama, MCP, C#, .NET, SQL Server.</desc>
  <defs>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#FFFFFF" stroke-opacity="0.045"/></pattern>
    <radialGradient id="gy" cx="10%" cy="0%" r="65%"><stop offset="0" stop-color="{YELLOW}" stop-opacity="0.24"/><stop offset="1" stop-color="{YELLOW}" stop-opacity="0"/></radialGradient>
    <radialGradient id="gv" cx="95%" cy="100%" r="60%"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0.22"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="18" fill="#0B0E1C"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#gy)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#gv)"/>"""]
    parts.append(text(48, 64, "ПРИВЕТ, Я KICKFOK", 13, YELLOW, family=MONO, extra=' letter-spacing="2.5"'))
    parts.append(text(48, 126, f'Разработчик 1С<tspan fill="{VIOLET}">.</tspan>', 48, TEXT, 800))
    parts.append(text(48, 182, f'Доработки, интеграции и <tspan fill="{YELLOW}">локальные LLM</tspan>.', 40, TEXT, 800))

    # терминал со сменяющимися строками
    parts.append('<rect x="48" y="220" width="640" height="48" rx="12" fill="#141831" stroke="#262B4E" stroke-width="1.5"/>')
    parts.append(text(68, 251, "$", 17, MUTED, 700, MONO))
    for i, (line, color) in enumerate(LINES):
        start, show = i / len(LINES), (i + 1) / len(LINES)
        keys = f"0;{start:.3f};{start + 0.01:.3f};{show - 0.01:.3f};{show:.3f};1"
        values = "0;0;1;1;0;0" if i else "1;1;1;1;0;0"
        if i == 0:
            keys = f"0;{show - 0.01:.3f};{show:.3f};0.99;1"
            values = "1;1;0;0;1"
        parts.append(f'<text x="88" y="251" font-family="{MONO}" font-size="17" font-weight="600" fill="{color}" opacity="{1 if i == 0 else 0}">'
                     f'{escape(line)}<animate attributeName="opacity" values="{values}" keyTimes="{keys}" dur="{period}s" repeatCount="indefinite"/></text>')

    x = 48
    for label, color in CHIPS:
        w = len(label) * 8.4 + 40
        parts.append(f'<rect x="{x}" y="292" width="{w:.0f}" height="34" rx="17" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-opacity="0.5"/>')
        parts.append(f'<circle cx="{x + 18}" cy="309" r="4" fill="{color}"/>')
        parts.append(text(x + 32, 314, escape(label), 14, color, 600))
        x += w + 12

    # монограмма справа: буква K из линий, по ней бегут импульсы
    parts.append(f'''<g transform="translate(940 90)">
    <rect width="200" height="200" rx="44" fill="{YELLOW}"/>
    <g fill="none" stroke="#1B1F3B" stroke-width="18" stroke-linecap="round" stroke-linejoin="round">
      <path d="M68 46 V154"/>
      <path id="armUp" d="M72 104 L134 46"/>
      <path id="armDown" d="M96 82 L138 154"/>
    </g>
    <circle r="6" fill="#FFFFFF"><animateMotion dur="1.8s" repeatCount="indefinite" path="M72 104 L134 46"/></circle>
    <circle r="6" fill="#FFFFFF"><animateMotion dur="1.8s" begin="0.9s" repeatCount="indefinite" path="M96 82 L138 154"/></circle>
  </g>''')
    parts.append(f'<circle cx="1040" cy="190" r="112" fill="none" stroke="{YELLOW}" stroke-opacity="0.25" stroke-dasharray="3 9">'
                 f'<animateTransform attributeName="transform" type="rotate" from="0 1040 190" to="360 1040 190" dur="40s" repeatCount="indefinite"/></circle>')
    parts.append("</svg>\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n  ".join(parts), encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
