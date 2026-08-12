===============================
Documentação de Exemplo Django
===============================

Bem-vindo a este exemplo de documentação utilizando o tema ``django-docs-theme``.

.. toctree::
   :maxdepth: 2
   :caption: Conteúdo Exemplo:

   installation
   tutorial
   reference

Visão Geral
------------

Este diretório ``docs/examples/`` serve como modelo para qualquer novo projeto Django que queira utilizar o ``django-docs-theme``.

Exemplo de Código
-----------------

.. code-block:: python

   from django.db import models

   class Project(models.Model):
       name = models.CharField(max_length=100)
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.name
