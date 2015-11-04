FCSocial
========

.. contents:: :local:

Instalación
-----------

Configuración del ambiente de desarrollo

.. code:: bash

    $ virtualenv-3.4 fcsocial_dev
    $ source bin/activate
    (fcsocial_dev)$ git clone https://github.com/UNAM-FCiencias-TDI/FCsocial.git
    (fcsocial_dev)$ cd FCsocial
    (fcsocial_dev)$ pip install -r requirements.txt

Configuración de la base de datos (sqlite3)

.. code:: bash

    (fcsocial_dev)$ python manage.py migrate
    (fcsocial_dev)$ python manage.py createsuperuser

Ejecución
---------

.. code:: bash

    (fcsocial_dev)$ python manage.py runserver
