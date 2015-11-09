FCSocial
========

.. contents:: :local:

.. image:: https://travis-ci.org/UNAM-FCiencias-TDI/FCsocial.svg
    :target: https://travis-ci.org/UNAM-FCiencias-TDI/FCsocial

Instalación
-----------

Configuración del ambiente de desarrollo

.. code:: bash

    $ virtualenv-3.4 fcsocial_dev
    $ cd fcsocial_dev
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


Pruebas
-------

Para ejecutar las pruebas funcionales levantamos el servidor

.. code:: bash

    (fcsocial_dev)$ python manage.py runserver


y en otra cosnola ejecutamos

.. code:: bash

    (fcsocial_dev)$ python functional_tests/fcsocial_test.py
