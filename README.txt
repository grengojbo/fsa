# FreeSWITCH Admin v0.4.1  

FreeSWITCH Admin -это веб интерфейс для администрирования VoIp програмного коммутатора FreeSWITCH.  
В ближайшее время будет доступен видео ролик.  

## Установка FreeSWITCH Admin

###Установка необходимых библиотек

Сперва устанавливаем необходимые библиотеки для всей системы
sudo su -
add-apt-repository ppa:linktel/ppa
wget -O- http://ourdelta.org/deb/ourdelta.gpg | sudo apt-key add -
wget http://ourdelta.org/deb/sources/lucid-mariadb-ourdelta.list \
      -O /etc/apt/sources.list.d/ourdelta.list
aptitude update
aptitude safe-upgrade
aptitude install -y language-pack-ru language-pack-ru-base language-support-extra-ru language-support-input-ru language-support-ru language-support-translations-ru manpages-ru
aptitude install -y gcc build-essential libc6-dev
aptitude install -y curl wget python-setuptools python-dev libevent-dev screen
aptitude install -y mariadb-client-5.1 libmemcached2 libmemcached-tools libmemcache-dev

aptitude install -y python-cjson python-crypto python-docutils python-geoip python-git python-httplib2 python-html5lib
aptitude install -y python-imaging python-lxml python-mysqldb python-pam python-pycurl python-sphinx python-tz python-yaml
aptitude install -y python-pyrex python-rdflib python-rdflib python-openssl

easy_install -U mercurial
easy_install -U pip
pip install ipython virtualenv virtualenvwrapper

pip install hg-git setuptools_hg setuptools_git Fabric
pip install greenlet
easy_install concurrence

pip install django
easy_install jinja2 python-memcached
aptitude install uwsgi runit

Добавляем группу и пользователя от которого будет запускатся веб интерфейс
/usr/sbin/groupadd fsweb
/usr/sbin/useradd -g fsweb -m --shell /bin/bash -d /home/fsweb fsweb
Добавляем пароль
passwd fsweb
Затем устанавливам виртуальное окружения для нашей программы
mkvirtualenv <name>
cd <name>
workon <name>

pip install -r http://github.com/grengojbo/fsa/raw/master/scripts/requirements-dev.txt
./manage.py syncdb
./manage.py migrate
./manage.py loaddata l10n_data
pip install -e git+http://github.com/grengojbo/fsa.git#egg=fsa
./manage.py syncdb
./manage.py migrate
./manage.py loaddata  currency_default
pip install -e git+http://github.com/grengojbo/fsb.git#egg=fsb
pip install -e git+http://github.com/grengojbo/fsc.git#egg=fsc
./manage.py syncdb
./manage.py migrate
./manage.py loaddata tariffplan --settings=settings


Для удаленного обновления и перезагрузки uwsgi в файл /etc/sudoers добавьте сторки
fsweb ALL= NOPASSWD:/usr/bin/rsync
fsweb ALL= NOPASSWD:/usr/bin/sv

### Настройка FreeSWITCH Admin

#### 1. В закладке FreeSWITCH Servers меняем  
1.1 Название сайта в *Начало › Sites › Сайты*  
1.2 Настраиваем Списки доступа *Начало › Acl › Acls* и *Начало › Acl › Acl Network Lists*  
1.3 Меняем и добавляем при необходимости синонимы для SIP *Начало › Server › SIP Alias*  
1.4 Настраиваем сервер *Начало › Server › Freeswitch Servers* подробнее в разделе Настраиваем сервер  
1.5 Добавляем Номерной план ./manage.py build_endpoint --number_start=1000 --number_end=1020 --site=1 --nt=1
    где number_start - с какого номера   
        number_end - по какой номер генерируется номерной план
        site - id сайта для которого будет использоватся номерной план
        nt - Тип номера 1-Default, 2-Silver, 3-Gold, 4-Starting packet
    далее переходим в раздел Управлени Номерным планом   
1.6 Настройка абонентов
Добавте группы Начало › Auth › Группы
server
support
user - это группа в которую добавляются обычные пользователи

Если Вы хотите что бы при активации новой учетной записи создавался SIP ID
то перейдите в раздел Site Setting и активируйте  *Endpoint Module Settings > Auto create endpoint*

#### 2. Настраиваем сервер  
*Начало › Server › SIP Profiles* установите профиль по умолчанию  
*Начало › Dialplan › Dialplan Contexts* установите контекст по умолчанию

#### 3. Управлени Номерным планом  
Переходим в *Начало › Numberplan › Number Plans*
Номера в номерном плане делятся на такие типы    
1. Default - все номера после их создания (из этого пула номеров берутся автоматически для новых клиентов)   
2. Silver и Gold - эти номера клиентам может присвоить только администратор   
Для груповой обработки номерного плана воспользуйтесь *Mark selected type as Silver* и т.д.   
Выбрать можно только номера с статусом Free и Disable.

#### 3. Маршруты LCR
Подготовка CSV файла
Для добавления маршрута необходимо в начале добавить формат загружаемого файла в таблицу
*Начало › Server › Format loads csv files* напрмер в таком формате
delimiter=';'time_format='%d.%m.%Y 00:00'country_code|name|digits|price|rate|currency|weeks|time_start|time_end
где 
country_code - код страны например 380 для Украины
name - название (Ukraine-Mobile KYIV STAR)
rate - цена (0.01) переведенная в валюту системы
price - цена в валюте оригинала
currency - тип валюты (USD)
other - любая колонка которую необходимо пропустить
date_start - дата начала периода (31.12.2009) если неуказано то текущая дата, в xls формат колонки текстовый
date_end - дата окончания, в xls формат колонки текстовый
weeks - день недели начало с воскресенья (2,4 - поонедельник среда) all-любой день
time_start time_end - период времент (с 00:00	до 23:59)
operator_type - Тип оератора: F - фиксированая связь, M - мобильная,S - спутниковая, N - неопределен
digits - код страны + код оператора (38044 - Украина Киев)
pref_digits - обрабатывает шаблоны
7 (495, 499) => 7495, 7499
61 (15-17, 4) = > 6115, 6116, 6117, 614 
98170-98172;9213; 9219; => 98170, 98171, 98172, 9213, 9219
Обязательно должны быть поля digits или pref_digits
quality - приоретет при выборе маршрута определяется по rate и если rate одинаково то тогда то у кого больше quality по умолчанию 0
Если в CSV файле используется кирилица конвертируйте ее в utf8 *iconv -f CP1251 -t UTF-8 works/lcr_ukr.csv > works/lcr_ukr_utf8.csv*

Добавляем маршрут
./manage.py load_lcr --gw=3 --site=1 --format_csv=1 /fsa/lcr/fixtures/test-lcr.csv
gw - ID шлюза смотреть в таблице Начало › Gateway › Gateways
site - ID сайта смотреть в Начало › Sites › Сайты 
format_csv - смотреть в Начало › Server › Format loads csv files 

