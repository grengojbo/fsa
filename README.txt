# FreeSWITCH Admin v0.4.1  

FreeSWITCH Admin -это веб интерфейс для администрирования VoIp програмного коммутатора FreeSWITCH.  
В ближайшее время будет доступен видео ролик.  

## Установка FreeSWITCH Admin v0.4.1

### Установка  

1. Скачать установочный файл **wget http://github.com/grengojbo/fsa/raw/master/scripts/fsa-build**
2. Сделать его исполняемым **chmod 744 fsa-build**
3. Установите общие библиотеки **./fsa-build global** *(этот шаг можно делать один раз)*
4. Установка virtualenv и FreeSWITCH Admin (fsa) **./fsa-build stable fs_stable**
5. Переходим в виртуальное окружение workon fs_stable   

### Настройка FreeSWITCH Admin   

#### 1. В закладке FreeSWITCH Servers меняем  
1.1 Название сайта в *Начало › Sites › Сайты*  
1.2 Настраиваем Списки доступа *Начало › Acl › Acls* и *Начало › Acl › Acl Network Lists*  
1.3 Меняем и добавляем при необходимости синонимы для SIP *Начало › Server › SIP Alias*  
1.4 Настраиваем сервер *Начало › Server › Freeswitch Servers* подробнее в разделе Настраиваем сервер  
1.5 Добавляем Номерной план ./manage.py build_endpoint --number_start=1000 --number_end=1020 --site=1
    где number_start - с какого номера   
        number_end - по какой номер генерируется номерной план
        site - id сайта для которого будет использоватся номерной план
    далее переходим в раздел Управлени Номерным планом   
1.6 Настройка абонентов
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