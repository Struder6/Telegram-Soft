# README: Telegram-бот для автоматизации взаимодействий

### Описание проекта:

Данный бот предназначен для выполнения массовых операций в Telegram. Он упрощает рассылку сообщений, инвайтинг участников в группы или каналы и парсинг пользователей. Администраторам доступен пошаговый интерфейс с инлайн-кнопками, позволяющий легко контролировать каждый этап

### Цель проекта:

1. Экономия времени за счёт автоматизации рутинных действий
2. Управление большими аудиториями без сложных скриптов
3. Гибкое использование шаблонов и фильтров для точной настройки рассылки, инвайтинга и парсинга

--------------------------------------------------------------------------------

### Функциональность после нажатия /start:

После нажатия кнопки /start пользователю отображается приветственное сообщение с bold форматированием, в котором указано его имя. Над текстом сообщения должна располагаться картинка (например, баннер или логотип). Ниже приветственного текста пользователь видит четыре инлайн-кнопки:

1. Рассылка  
2. Инвайтинг  
3. Парсинг  
4. Настройки  

Все кнопки расположены в одном сообщении, что упрощает навигацию по функционалу бота. При выборе любой из кнопок бот переходит в соответствующий сценарий, где пошагово спрашивает у пользователя нужную информацию (например, текст сообщения для рассылки, целевой чат или настройки фильтров для парсинга), а затем выводит «анкету» с итоговыми параметрами и кнопками подтверждения или возврата в начало

### Основные функции

# Рассылка сообщений
1. В стартовом меню бот предлагает кнопку Рассылка  
2. Пользователь выбирает направление:  
   a) По чатам  
   b) По личным сообщениям  

3. Вводится текст для рассылки  
   - Пользователь отправляет его обычным сообщением в чат боту

4. Бот спрашивает, добавлять ли URL-кнопку  
   a) «Добавить URL-кнопку»  
      - Сначала бот запрашивает ссылку (URL), которая будет находиться с самого низа итогого сообщения и открываться по нажатию  
      - Затем бот спрашивает, какое название (текст) будет у этой кнопки  
      - В итоге данная URL-кнопка будет добавлена под сообщением, которое бот рассылает  
   b) «Пропустить»  
      - Переход к следующему шагу без добавления каких-либо кнопок  

5. Выбор чатов или ЛС  
   a) Указать вручную  
      - Пользователь может прислать список в виде обычного сообщения (каждый чат или пользователь в новой строке)  
      - Или приложить *.txt файл со списком чатов/пользователей  
      - Бот обрабатывает полученную информацию и запоминает, куда именно будет отправляться рассылка  
   b) Выбрать из шаблона (если был сохранён ранее)  
      - Если пользователь когда-то уже создавал и сохранял шаблон списков чатов/ЛС, бот предложит выбрать один из имеющихся шаблонов  
      - Шаблон создаётся таким образом: пользователю выпадают его заранее указанные шаблоны, в случае если ни одного шаблона нет, ниже будет кнопка "Добавить шаблон", пользователь скидывает туда нужный список/файл содержащий набор чатов или пользователей и даёт ему имя (например, «Чаты для рекламы»). После подтверждения бот сохраняет такой шаблон в памяти или в базе данных  
      - При выборе шаблона не нужно вручную заново вводить список: бот автоматически применит ранее сохранённые чаты или ЛС  

6. Указание аккаунтов, с которых ведётся отправка  
   a) Ввести вручную  
      - Пользователь указывает список логинов или идентификаторов аккаунтов (при необходимости — пароли или ключи, если используется мультиаккаунт-логика)  
      - Формат может быть обычным текстом или файлом, аналогично пункту 5  
   b) Использовать шаблон аккаунтов  
      - Аналогично шаблонам чатов, заранее сохранённые данные об аккаунтах могут быть выбраны одним нажатием  
      - Это позволяет быстро переключаться между разными наборами аккаунтов для разных рассылок  

7. Установка интервала отправки (1, 3, 5, 10, 60 минут)  
   - Бот предлагает ряд готовых интервалов  
   - Пользователь нажимает на соответствующую кнопку, например «3 минуты», и бот запоминает этот интервал для текущей рассылки  
   - Если пользователь хочет другой интервал, не указанный в списке, реализация зависит от бота (должен быть предусмотрен ввод вручную)  

8. Бот формирует анкету с параметрами  
   - Текст сообщения  
   - Наличие URL-кнопки (если добавлена)  
   - Список чатов или ЛС  
   - Аккаунты для отправки  
   - Интервал отправки  
   После формирования анкеты бот отправляет её пользователю для проверки, чтобы убедиться, что всё введено корректно  

9. Под анкетой две кнопки  
   a) «Приступить»  
      - Запускает рассылку  
      - Бот уведомляет о начале процесса
   b) «Вернуться в начало»  
      - Отменяет текущие настройки и возвращает к выбору направления рассылки (по чатам или по ЛС)  

10. Во время рассылки доступна кнопка «Остановить рассылку»  
    - При нажатии останавливает дальнейшую отправку сообщений  
    - Также в дальнейшем будут кнопки «Перенастроить» и «Подробная статистика», чтобы пользователь мог изменить ход рассылки или просмотреть её детальные результаты, на текущий момент добавлять не стоит

Ниже приведён дополненный блок про инвайтинг, где учитывается возможность выбора аккаунтов (аналогично тому, как это реализовано в рассылке). Если бот не умеет приглашать пользователей от своего имени, этот пункт можно использовать для указания, с каких именно аккаунтов будет выполняться инвайтинг:

# Инвайтинг
1. В стартовом меню выбирается кнопка «Инвайтинг»

2. Пользователь загружает список (текстом или файлом)  
   - Если текстом, то перечисляет пользователей или их идентификаторы построчно  
   - Если файлом, то обычно это *.txt, где каждый пользователь прописан в новой строке  
   - Бот обрабатывает полученную информацию и запоминает, кого нужно будет приглашать  

3. Указывается чат или канал для приглашения  
   - С помощью ссылки или @username чата/канала  
   - Важно: бот должен иметь права администратора, либо использовать другие аккаунты-«агенты» с правами добавления участников  
   - Если ранее сохранили шаблон чата/канала, его можно выбрать одним нажатием  

4. Указывается, с каких аккаунтов будет выполняться инвайтинг  
   a) Ввести вручную  
      - Пользователь указывает список аккаунтов или логинов, под которыми есть право приглашать людей (например, для обхода лимитов)  
   b) Использовать шаблон аккаунтов  
      - Если ранее сохранили шаблон (например, «Тестовые аккаунты» или «Аккаунты сотрудников»), то достаточно выбрать его, и все указанные аккаунты будут задействованы  

5. Выбирается периодичность приглашений (1, 3, 5, 10, 60 минут)  
   - Аналогично рассылке: бот предлагает готовые интервалы  
   - Если нужен другой интервал, это можно реализовать отдельным пунктом (например, «Другое значение»)  

6. Отображается итоговая анкета настроек  
   - Список пользователей, которых нужно пригласить  
   - Чат или канал, куда они будут приглашены  
   - Аккаунты, с которых ведётся инвайтинг  
   - Интервал (периодичность) отправки приглашений  

7. Кнопки под анкетой  
   a) «Приступить» — бот начинает приглашать пользователей, отправляя им приглашения от выбранных аккаунтов  
   b) «Вернуться в начало» — отменяет текущие настройки и возвращает к предыдущему шагу (выбор пользователей, чата или аккаунтов)  

8. Во время инвайтинга отображается сообщение с кнопкой «Остановить инвайтинг»  
   - При нажатии бот прекращает дальнейшую рассылку приглашений  
   - В дальнейшем будет заложена функция статистики, могут быть доступны кнопки «Перенастроить» или «Подробная статистика», где пользователь видит количество успешно приглашённых участников и т.п.Таким образом, при использовании нескольких аккаунтов бот может приглашать пользователей «от имени» разных профилей, что даёт возможность обходить некоторые лимиты и баны

# Парсинг пользователей
1. В стартовом меню выбирается кнопка Парсинг  
2. Пользователь указывает чаты/каналы для сбора данных  
   - Либо отправляя их вручную  
   - Либо выбирая уже сохранённый шаблон чатов  
   - Формат аналогичен: обычный текст с перечислением @username групп, ссылки на группы или .txt файл  

3. Настраиваются фильтры  
   - Статус: премиум или обычный  
   - Активность: последний раз: сегодня, меньше дня назад, меньше недели назад  
   - Пол: мужской или женский  
   - Страна регистрации номера: СНГ, Америка  
   При необходимости можно добавить дополнительные критерии, если бот это поддерживает  

4. Бот формирует анкету с выбранными критериями  
   - Кратко перечисляет, какие чаты выбраны, и какие фильтры применяются  
   - Пользователь проверяет правильность настройки  

5. Под анкетой:  
   a) «Приступить»  
      - Начинает парсинг  
      - Бот уведомляет о начале процесса и может скрыть промежуточные шаги  
   b) «Вернуться в начало»  
      - Отменяет настройки и возвращает к выбору чатов для парсинга        

6. При запущенном парсинге доступна кнопка «Остановить парсинг»  
   - Останавливает сбор данных из чатов  
   - В дальнейшем будет предусмотрена подробная статистика, пользователь может посмотреть количество спарсенных пользователей, их статус, пол и т.д

Таким образом, каждый из трёх основных сценариев (рассылка, инвайтинг, парсинг) максимально детализирован: от момента загрузки списков или ввода текста до формирования конечной анкеты с итоговыми параметрами и запуска процесса

--------------------------------------------------------------------------------

### Структура файлов и папок

1. config/
   - `config.py`  
     Файл для общих настроек бота (например, токен или параметры подключения к БД)
   - data/
     - `db.json`  
       Файл для хранения данных (шаблонов, списков чатов, аккаунтов и т. д.), если используется JSON

2. handlers/
   - `callback-handler.py`  
     Код, обрабатывающий инлайн-коллбеки (нажатия на инлайн-кнопки) 
   - `message-handler.py`  
     Обработка входящих текстовых сообщений  
   - `start-handler.py`  
     Логика, вызываемая при запуске команды /start (приветствие, главное меню)

3. keyboards/ 
   - `inline-keyboard.py`  
     Описание инлайн-клавиатур (кнопок, которые появляются под сообщением)
   - `reply-keyboard.py`  
     Описание reply-клавиатур, если бот их использует (обычные кнопки в месте ввода текста)

4. logs/  
   - `bot.log`  
     Лог-файл для записи событий бота, возможных ошибок и другой технической информации

5. utils/ 
   - `helpers.py`  
     Вспомогательные функции, которые могут использоваться в разных частях бота (например, форматирование сообщений, валидация данных)

6. main.py  
   Главный скрипт для запуска бота. Как правило, здесь находится точка входа (например, инициализация хэндлеров, запуск polling или webhook)

7. README.md  
   Документация проекта (текущий файл)

8. requirements.txt  
   Список всех необходимых библиотек для установки через `pip install -r requirements.txt`

--------------------------------------------------------------------------------

### Дополнительно (рекомендации):

# Шаблоны и сохранение данных
   При работе с шаблонами (списки чатов, аккаунтов) данные обычно хранятся либо в `db.json`, либо в базе данных. Убедитесь, что формат структуры в `db.json` вам удобен, чтобы бот мог легко читать и обновлять нужные поля

# FAQ
   - Что делать, если бот не отвечает? 
     Убедитесь, что ваш токен правильный, и у бота есть доступ к интернету. Проверьте логи (`bot.log`) на наличие ошибок 
   - Как добавить новую функцию?
     Создайте новый хэндлер в папке `handlers` и опишите в нём нужную логику. Если понадобится новая клавиатура, оформите её в папке `keyboards`
   - Можно ли запускать несколько функций параллельно? 
     В дальнейшем собираемся сделать такой функционал, но на данный момент нет

# Управление логами  
   Для удобной отладки и мониторинга работы бота используйте `bot.log`. В случае необходимости можно разделить логи на несколько файлов (например, `error.log` и `info.log`)

### Контакты
   - Автор: kalada ybt  
   - Telegram: @kaladaq  
   - GitHub: @kaladaybt
