.. _macro_lightning-test:

=================
Running the tests
=================

The tests are written assuming they will be run with `pytest <http://doc.pytest.org/>`_ using the Astropy `custom test runner <http://docs.astropy.org/en/stable/development/testguide.html>`_. To set up a Conda environment to run the full set of tests, install ``macro_lightning`` or see the setup.cfg file for dependencies. Once the dependencies are installed, you can run the tests two ways:

1. By importing ``macro_lightning``::

    import macro_lightning
    macro_lightning.test()

2. By cloning the ``macro_lightning`` repository and running::

    tox -e test


Reference/API
=============

The test functions.

.. currentmodule:: macro_lightning.tests

.. automodapi:: macro_lightning.tests.test_parameters


.. automodapi:: macro_lightning.tests.test_plot


.. automodapi:: macro_lightning.tests.test_utils
