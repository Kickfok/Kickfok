"""Карточки проектов для профиля: одинаковый размер, название, описание в три строки, бейджи стека внизу на одной
высоте. Картинки, а не таблица Markdown: у таблицы высота строк зависит от длины текста, и карточки расходятся.

    python tools/gen_cards.py
"""
import pathlib
from xml.sax.saxutils import escape

ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"
SANS = "Inter, 'Segoe UI', Arial, Helvetica, sans-serif"
W, H = 560, 180

CARDS = [
    ("card-1c-mcp-ollama.svg", "1c-mcp-ollama", "#FFC21A",
     ["Вопросы к базе 1С обычным языком: MCP-сервер", "в расширении 1С и локальная модель в Ollama.",
      "Данные читает 1С с правами пользователя."],
     [("1С:Предприятие", "#FFC21A"), ("BSL", "#FFC21A"), ("Python", "#5A9FD4"), ("MCP", "#8B7CFF")]),
    ("card-carservice.svg", "CarService", "#6CCFF6",
     ["Настольное приложение для каталога услуг", "автосервиса: роли, поиск и фильтры,",
      "добавление и редактирование услуг."],
     [("C#", "#8B7CFF"), ("WPF", "#6CCFF6"), ("Entity Framework", "#5EE0A0"), ("SQL Server", "#FF6B7A")]),
]


def card(name, color, lines, tags):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(name)}: {escape(" ".join(lines))}">',
           f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="#11152B" stroke="#262B4E" stroke-width="1.5"/>',
           f'<rect x="1" y="20" width="4" height="{H - 40}" rx="2" fill="{color}"/>',
           f'<path d="M26 26 h9 l3 3 v13 h-12 z" fill="none" stroke="#9AA1C9" stroke-width="1.6" stroke-linejoin="round"/>',
           f'<text x="48" y="41" font-family="{SANS}" font-size="20" font-weight="800" fill="{color}">{escape(name)}</text>']
    pub_x = W - 26 - 58
    out.append(f'<rect x="{pub_x:.0f}" y="25" width="58" height="22" rx="11" fill="none" stroke="#3A4070"/>')
    out.append(f'<text x="{pub_x + 29:.0f}" y="40" font-family="{SANS}" font-size="12" fill="#9AA1C9" text-anchor="middle">Public</text>')
    for k, line in enumerate(lines):
        out.append(f'<text x="26" y="{78 + k * 22}" font-family="{SANS}" font-size="15" fill="#C9CEE8">{escape(line)}</text>')
    x = 26
    for label, c in tags:
        w = len(label) * 7.4 + 22
        out.append(f'<rect x="{x:.0f}" y="{H - 40}" width="{w:.0f}" height="24" rx="12" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-opacity="0.55"/>')
        out.append(f'<text x="{x + w / 2:.0f}" y="{H - 23}" font-family="{SANS}" font-size="12.5" font-weight="600" fill="{c}" text-anchor="middle">{escape(label)}</text>')
        x += w + 8
    out.append("</svg>\n")
    return "\n".join(out)


for file, name, color, lines, tags in CARDS:
    (ASSETS / file).write_text(card(name, color, lines, tags), encoding="utf-8", newline="\n")
    print(file)
