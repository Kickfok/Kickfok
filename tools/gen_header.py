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
    ("спросить базу 1С обычным языком", YELLOW),
    ("MCP-сервер в расширении 1С:Предприятия", VIOLET),
    ("локальная модель в Ollama, данные остаются в сети", GREEN),
    ("ответ таблицей из базы с правами пользователя", CYAN),
]
CHIPS = [("1С:Предприятие · БСП · BSL", YELLOW), ("Python · Ollama · MCP", VIOLET), ("C# · .NET · SQL Server", CYAN)]


def text(x, y, value, size, color, weight=400, family=SANS, extra=""):
    w = f' font-weight="{weight}"' if weight != 400 else ""
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}"{w}{extra}>{value}</text>'


def main():
    period = 3.2 * len(LINES)
    parts = [f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
  <title id="t">Kickfok</title>
  <desc id="d">Kickfok: разработчик 1С и локальных LLM. Делает 1C MCP Ollama Bridge: базу 1С спрашивают обычным языком, модель работает в Ollama на своей видеокарте. Стек: 1С:Предприятие, БСП, BSL, Python, Ollama, MCP, C#, .NET, SQL Server.</desc>
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
    parts.append(text(48, 182, f'Учу базы отвечать на <tspan fill="{YELLOW}">обычном языке</tspan>.', 40, TEXT, 800))

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

    # знак проекта справа: база 1С соединена с узлом модели, по связи бежит импульс
    parts.append(f'''<g transform="translate(940 90)">
    <rect width="200" height="200" rx="44" fill="{YELLOW}"/>
    <g transform="scale(6.25) translate(-0.7 0.6)">
      <g fill="none" stroke="#1B1F3B" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
        <ellipse cx="10" cy="10" rx="4.5" ry="1.8"/>
        <path d="M5.5 10 V20 C5.5 21 7.5 21.8 10 21.8 C12.5 21.8 14.5 21 14.5 20 V10"/>
        <path d="M5.5 15 C5.5 16 7.5 16.8 10 16.8 C12.5 16.8 14.5 16 14.5 15"/>
        <path id="link" d="M14.5 15 H19.5"/>
        <path d="M22 15 L26 9 M22 15 L27 15 M22 15 L26 21"/>
      </g>
      <g fill="#1B1F3B"><circle cx="22" cy="15" r="2.5"/><circle cx="26.3" cy="8.6" r="1.4"/><circle cx="27.4" cy="15" r="1.4"/><circle cx="26.3" cy="21.4" r="1.4"/></g>
      <circle r="0.9" fill="#FFFFFF"><animateMotion dur="1.6s" repeatCount="indefinite" path="M14.5 15 H21"/></circle>
    </g>
  </g>''')
    parts.append(f'<circle cx="1040" cy="190" r="128" fill="none" stroke="{YELLOW}" stroke-opacity="0.25" stroke-dasharray="3 9">'
                 f'<animateTransform attributeName="transform" type="rotate" from="0 1040 190" to="360 1040 190" dur="40s" repeatCount="indefinite"/></circle>')
    parts.append("</svg>\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n  ".join(parts), encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
