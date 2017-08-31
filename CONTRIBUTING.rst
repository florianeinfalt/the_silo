Contributing
============

All useful additions to The Silo are welcome.

To contribute to the project please do the following:

1. Fork the project

Add gizmos
----------

2. Add gizmos to ``/the_silo/gizmos``

    Gizmo names should be all lowercase and separated by underscores

3. Register the new gizmo in ``/the_silo/silo_data.json``

    Gizmos are described in a list of lists under the key ``gizmos``.
    To extend the list of gizmos, create a new list with the format [nice name, gizmo_name]

4. Test the changes work

5. Create a pull request

Add scripts
-----------

2. Add scripts to ``/the_silo/scripts``

    Module names should be all lowercase and separated by underscores

3. Register the new script in ``/the_silo/silo_data.json``

    Scripts are described in a list of lists under the key ``scripts``.
    To extend the list of scripts, create a new list with the format [nice name, module_name, function_name, shortcut]

4. Test the changes work

5. Create a pull request
