Benolot's cookie API, python version
------------------------------------

This package gives you two functions, add and gib, explained below:

add
  The 'add' function takes a cookie image url as argument and saves that image to a database folder.
gib
  The 'gib' function takes no argumens and returns the path to one of the images in the previously mentioned databse folder, randomely picked. 


To use, simply do::

    >>> import realcookie
    >>> a = realcookie.cookie()
    >>> a.add('some cookie image url')
    >>> a.gib()