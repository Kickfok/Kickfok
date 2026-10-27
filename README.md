<p align="center">
  <img src="assets/header.svg" width="100%" alt="Kickfok: разработчик 1С. Учу базы отвечать на обычном языке. 1С:Предприятие, БСП, BSL, Python, Ollama, MCP, C#, .NET, SQL Server.">
</p>

Пишу доработки на 1С:Предприятии и БСП: ERP, Комплексная автоматизация, Документооборот и интеграции между
ними. Сейчас подключаю к базам 1С локальные языковые модели: вопрос задается обычным языком, модель
работает на своей видеокарте, а данные читает сама 1С с правами пользователя.

## Главный проект

<a href="https://github.com/Kickfok/1c-mcp-ollama">
  <img src="https://raw.githubusercontent.com/Kickfok/1c-mcp-ollama/main/docs/assets/hero.svg" width="100%" alt="1C MCP Ollama Bridge: спросите базу 1С обычным языком">
</a>

**[1C MCP Ollama Bridge](https://github.com/Kickfok/1c-mcp-ollama)** - MCP-сервер в расширении 1С и
оркестратор для модели в Ollama.

- 13 инструментов: таблицы, готовые отчеты БСП, журнал регистрации, запросы на языке 1С. Ни один не меняет
  данные.
- Инструменты выполняются в сеансе пользователя, который задал вопрос: действуют его роли и ограничения на
  уровне записей.
- Модель не пересказывает данные: в ответ попадает таблица из базы целиком.
- Расширение без заимствованных объектов, облачные сервисы не нужны, лицензия MIT.

## Проекты

| Проект | Что это | Стек |
|---|---|---|
| [1c-mcp-ollama](https://github.com/Kickfok/1c-mcp-ollama) | Вопросы к базе 1С обычным языком через локальную модель | 1С, BSL, БСП, Python, Ollama, MCP |
| [CarService](https://github.com/Kickfok/CarService) | Каталог услуг автосервиса: роли, поиск, фильтры, редактирование | C#, WPF, .NET Framework, Entity Framework, SQL Server |

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
