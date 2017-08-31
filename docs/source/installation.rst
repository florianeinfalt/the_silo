Installation
------------

To install ``the_silo``, type:

.. code-block:: bash

    $ pip install the_silo

Open Nuke's ``init.py`` file and add:

.. code-block:: python

    nuke.pluginAddPath('/path/to/your/local/python/site-packages')

    import the_silo
    the_silo.init()

Open Nuke's ``menu.py`` file and add:

.. code-block:: python

    the_silo.build()
