"""Карточки проектов для профиля: одинаковый размер, название, описание в три строки, бейджи стека внизу на одной
высоте. Картинки, а не таблица Markdown: у таблицы высота строк зависит от длины текста, и карточки расходятся.
Карточка со своим темным фоном в палитре 1C MCP Ollama Bridge, одинаково смотрится в обеих темах GitHub.

    python tools/gen_cards.py
"""
import pathlib
from xml.sax.saxutils import escape

ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"
SANS = "Inter, 'Segoe UI', Arial, Helvetica, sans-serif"
W, H = 560, 180
THEMES = {
    "dark": {"text": "#C9CEE8", "muted": "#9AA1C9", "line": "#262B4E", "bg": "#141831", "red": "#FFC21A",
             "violet": "#8B7CFF", "blue": "#6CCFF6", "green": "#5EE0A0", "sql": "#F28CB1"},
}
ORANGE = "#FF6A13"

CARDS = [
    ("1c-mcp-ollama", "red",
     ["Вопросы к базе 1С обычным языком: MCP-сервер", "в расширении 1С и локальная модель в Ollama.",
      "Данные читает 1С с правами пользователя."],
     [("1С:Предприятие", "red"), ("BSL", "red"), ("Python", "blue"), ("MCP", "violet")]),
    ("CarService", "blue",
     ["Настольное приложение для каталога услуг", "автосервиса: роли, поиск и фильтры,",
      "добавление и редактирование услуг."],
     [("C#", "violet"), ("WPF", "blue"), ("Entity Framework", "green"), ("SQL Server", "sql")]),
]


def card(theme, name, accent, lines, tags):
    c = dict(THEMES[theme], orange=ORANGE)
    color = c[accent]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(name)}: {escape(" ".join(lines))}">',
           f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{c["bg"]}" stroke="{c["line"]}" stroke-width="1.5"/>',
           f'<rect x="1" y="20" width="4" height="{H - 40}" rx="2" fill="{color}"/>',
           f'<path d="M26 26 h9 l3 3 v13 h-12 z" fill="none" stroke="{c["muted"]}" stroke-width="1.6" stroke-linejoin="round"/>',
           f'<text x="48" y="41" font-family="{SANS}" font-size="20" font-weight="800" fill="{color}">{escape(name)}</text>']
    pub_x = W - 26 - 58
    out.append(f'<rect x="{pub_x}" y="25" width="58" height="22" rx="11" fill="none" stroke="{c["line"]}"/>')
    out.append(f'<text x="{pub_x + 29}" y="40" font-family="{SANS}" font-size="12" fill="{c["muted"]}" text-anchor="middle">Public</text>')
    for k, line in enumerate(lines):
        out.append(f'<text x="26" y="{78 + k * 22}" font-family="{SANS}" font-size="15" fill="{c["text"]}">{escape(line)}</text>')
    x = 26
    for label, key in tags:
        tc = c[key]
        w = len(label) * 7.4 + 22
        out.append(f'<rect x="{x:.0f}" y="{H - 40}" width="{w:.0f}" height="24" rx="12" fill="{tc}" fill-opacity="0.1" stroke="{tc}" stroke-opacity="0.6"/>')
        out.append(f'<text x="{x + w / 2:.0f}" y="{H - 23}" font-family="{SANS}" font-size="12.5" font-weight="600" fill="{tc}" text-anchor="middle">{escape(label)}</text>')
        x += w + 8
    out.append("</svg>\n")
    return "\n".join(out)


for theme in THEMES:
    for name, accent, lines, tags in CARDS:
        file = ASSETS / f"card-{name.lower()}.svg"
        file.write_text(card(theme, name, accent, lines, tags), encoding="utf-8", newline="\n")
        print(file.name)
