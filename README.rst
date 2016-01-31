Benolot's cookie API, python version
------------------------------------

This package gives you three functions, add, gib, count, and rm, explained below:

add
  The 'add' function takes a cookie image url as argument and saves that image to a database folder.
gib
  The 'gib' function takes no argumens and returns the path to one of the images in the previously mentioned databse folder, randomely picked.
count
  The 'count' function returns the number of images currently in the database folder.
rm
  The 'rm' function deletes the database folder and all the images in it.


To install, simply do::
    pip install realcookie

  

To use, simply do::

    >>> import realcookie
    >>> a = realcookie.cookie()
    >>> a.add('some cookie image url')
    >>> a.gib()