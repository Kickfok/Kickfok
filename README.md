<p align="center">
  <img src="assets/header.svg" width="100%" alt="Kickfok: разработчик 1С. Учу базы отвечать на обычном языке. 1С:Предприятие, БСП, BSL, Python, Ollama, MCP, C#, .NET, SQL Server.">
</p>

# Привет, я Kickfok

Пишу доработки на 1С:Предприятии и БСП: ERP, Комплексная автоматизация, Документооборот и интеграции между
ними. Сейчас делаю [1C MCP Ollama Bridge](https://github.com/Kickfok/1c-mcp-ollama): базу 1С спрашивают
обычным языком, модель работает в Ollama на своей видеокарте, а данные читает сама 1С с правами
пользователя. Открытый код, лицензия MIT.

<a href="https://github.com/Kickfok/1c-mcp-ollama/releases/latest"><img height="24" src="https://img.shields.io/github/v/release/Kickfok/1c-mcp-ollama?style=flat-square&label=1C%20MCP%20Ollama%20Bridge&color=FFC21A" alt="последний релиз"/></a>
<a href="https://github.com/Kickfok/1c-mcp-ollama/stargazers"><img height="24" src="https://img.shields.io/github/stars/Kickfok/1c-mcp-ollama?style=flat-square&logo=github&color=2ea44f" alt="звезды"/></a>
<a href="https://github.com/Kickfok/1c-mcp-ollama/forks"><img height="24" src="https://img.shields.io/github/forks/Kickfok/1c-mcp-ollama?style=flat-square&logo=github&color=8250df" alt="форки"/></a>
<a href="https://github.com/Kickfok/1c-mcp-ollama/actions/workflows/checks.yml"><img height="24" src="https://img.shields.io/github/actions/workflow/status/Kickfok/1c-mcp-ollama/checks.yml?style=flat-square&label=checks" alt="проверки"/></a>
<a href="https://github.com/Kickfok?tab=followers"><img height="24" src="https://img.shields.io/github/followers/Kickfok?style=flat-square&logo=github&color=24292f" alt="подписчики"/></a>
<img height="24" src="https://komarev.com/ghpvc/?username=Kickfok&style=flat-square&label=views&color=555555" alt="просмотры профиля"/>
<a href="https://github.com/Kickfok/1c-mcp-ollama/blob/main/LICENSE"><img height="24" src="https://img.shields.io/github/license/Kickfok/1c-mcp-ollama?style=flat-square" alt="лицензия MIT"/></a>

## 📌 Проекты

<table>
  <tr>
    <td width="50%" valign="top">
      <b><a href="https://github.com/Kickfok/1c-mcp-ollama">1c-mcp-ollama</a></b>
      <a href="https://github.com/Kickfok/1c-mcp-ollama"><img height="18" src="https://img.shields.io/badge/-Public-lightgrey?style=flat-square" alt="Public"/></a><br/>
      <sub>MCP-сервер в расширении 1С и оркестратор для модели в Ollama. 13 инструментов: таблицы, готовые отчеты БСП, журнал регистрации, запросы. Работают в сеансе пользователя и ничего не меняют в базе.</sub><br/>
      <img height="18" src="https://img.shields.io/badge/-1C%20Enterprise-FFC21A?style=flat-square" alt="1C Enterprise"/>
      <img height="18" src="https://img.shields.io/badge/-Python-3776AB?style=flat-square" alt="Python"/>
      <a href="https://github.com/Kickfok/1c-mcp-ollama/stargazers"><img height="18" src="https://img.shields.io/github/stars/Kickfok/1c-mcp-ollama?style=social" alt="звезды"/></a>
    </td>
    <td width="50%" valign="top">
      <b><a href="https://github.com/Kickfok/CarService">CarService</a></b>
      <a href="https://github.com/Kickfok/CarService"><img height="18" src="https://img.shields.io/badge/-Public-lightgrey?style=flat-square" alt="Public"/></a><br/>
      <sub>WPF-приложение для каталога услуг автосервиса: роли, поиск и фильтры, добавление и редактирование услуг.</sub><br/>
      <img height="18" src="https://img.shields.io/badge/-C%23-512BD4?style=flat-square" alt="C#"/>
      <img height="18" src="https://img.shields.io/badge/-SQL%20Server-CC2927?style=flat-square" alt="SQL Server"/>
      <a href="https://github.com/Kickfok/CarService/stargazers"><img height="18" src="https://img.shields.io/github/stars/Kickfok/CarService?style=social" alt="звезды"/></a>
    </td>
  </tr>
</table>

<a href="https://github.com/Kickfok/1c-mcp-ollama">
  <img src="https://raw.githubusercontent.com/Kickfok/1c-mcp-ollama/main/docs/assets/hero.svg" width="100%" alt="1C MCP Ollama Bridge: спросите базу 1С обычным языком">
</a>

## Что я делаю

1C MCP Ollama Bridge отвечает на вопросы о базе 1С данными самой базы. Модель выбирает инструмент, 1С читает
данные с ролями и ограничениями того, кто спросил, а в ответ попадает таблица из базы целиком. Вопросы и
данные не уходят во внешние сервисы.

Над чем работаю сейчас:

- Инструменты для руководителей и аналитиков: готовые отчеты БСП с периодом и отборами, профиль данных за
  период, сравнение периодов.
- Права и безопасность: выполнение в сеансе пользователя, токены на время вопроса, ключи в хранилище БСП.
- Работа на обычном железе: контекст 4096 токенов и видеокарта на 12 ГБ.
- Открытый протокол MCP: к базе 1С подключаются Cursor, Claude Desktop и другие клиенты.

## С чего начать

| Ресурс | Что там |
| --- | --- |
| [1C MCP Ollama Bridge](https://github.com/Kickfok/1c-mcp-ollama) | Исходники, схема работы, реальные прогоны, план развития |
| [Установка](https://github.com/Kickfok/1c-mcp-ollama/blob/main/docs/INSTALL.md) | Расширение, публикация, оркестратор, режимы работы |
| [Инструкция администратора](https://github.com/Kickfok/1c-mcp-ollama/blob/main/docs/ADMIN_GUIDE.md) | Права, настройки, диагностика, токены, неполадки |
| [Инструкция пользователя](https://github.com/Kickfok/1c-mcp-ollama/blob/main/docs/USER_GUIDE.md) | Как задать вопрос и прочитать ответ |
| [Инструменты](https://github.com/Kickfok/1c-mcp-ollama/blob/main/docs/TOOLS.md) | Все 13 инструментов и их параметры |
| [Релизы](https://github.com/Kickfok/1c-mcp-ollama/releases) | Готовое расширение `.cfe` и архив оркестратора |
| [Issues](https://github.com/Kickfok/1c-mcp-ollama/issues) | Ошибки, идеи, вопросы |

## Стек

![1C](https://img.shields.io/badge/1С:Предприятие-8.3-FFC21A?style=flat-square)
![BSL](https://img.shields.io/badge/BSL-БСП%203.1-FFC21A?style=flat-square)
![EDT](https://img.shields.io/badge/1C:EDT-Конфигуратор-FFC21A?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-qwen2.5--coder-1B1F3B?style=flat-square&logo=ollama&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-6E56CF?style=flat-square)
![C#](https://img.shields.io/badge/C%23-.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Entity%20Framework-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-BSL-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
