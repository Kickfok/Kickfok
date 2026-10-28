<p align="center">
  <img src="assets/header.svg" width="100%" alt="Kickfok, разработчик 1С: доработки на БСП для ERP, Комплексной автоматизации и Документооборота, интеграции, локальные LLM и MCP для баз 1С, настольные приложения на C#.">
</p>

# Привет, я Kickfok

Разрабатываю на 1С: ERP, Комплексная автоматизация, Документооборот. Здесь лежат мои открытые проекты.

## 📌 Проекты

<p>
  <a href="https://github.com/Kickfok/1c-mcp-ollama"><img src="assets/card-1c-mcp-ollama.svg" width="49%" alt="1c-mcp-ollama: вопросы к базе 1С обычным языком, MCP-сервер в расширении 1С и локальная модель в Ollama"></a>
  <a href="https://github.com/Kickfok/CarService"><img src="assets/card-carservice.svg" width="49%" alt="CarService: настольное приложение для каталога услуг автосервиса"></a>
</p>

## Чем занимаюсь

В основном пишу доработки на БСП: отчеты на СКД, формы, обработки. Если задачу можно закрыть расширением,
типовую конфигурацию не трогаю, тогда ее потом спокойно обновляют.

Много времени уходит на интеграции: ERP с Документооборотом, обмены, HTTP-сервисы. Сложный обмен сначала
собираю на Python и только потом переношу на BSL. На Python проще разобраться с форматом ответа, а в 1С
переносишь уже рабочую схему.

Последнее время подключаю к базам 1С локальные модели. Так появился
[1C MCP Ollama Bridge](https://github.com/Kickfok/1c-mcp-ollama): базу спрашивают обычным языком, модель
работает на своей видеокарте, а данные 1С отдает с правами того, кто спросил. Иногда пишу на C#, например
[CarService](https://github.com/Kickfok/CarService).

## Как работаю

Перед сдачей прогоняю код через SonarQube и проверяю на копии рабочей базы: на пустой базе половина ошибок
не видна. Инструкции и снимки экрана делаю сразу, пока помню, как все устроено.

## Стек

![1C](https://img.shields.io/badge/1С:Предприятие-8.3-FFC21A?style=flat-square)
![BSL](https://img.shields.io/badge/BSL-БСП%203.1-FFC21A?style=flat-square)
![EDT](https://img.shields.io/badge/1C:EDT-Конфигуратор-FFC21A?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-LLM-1B1F3B?style=flat-square&logo=ollama&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-6E56CF?style=flat-square)
![C#](https://img.shields.io/badge/C%23-.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Entity%20Framework-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-BSL-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-GitHub%20Actions-F05032?style=flat-square&logo=git&logoColor=white)
