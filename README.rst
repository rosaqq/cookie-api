Benolot's cookie API, python version
------------------------------------

This package gives you 2 functions, "add" and "gib"::
	add('http://someRandomImageUrl.com') saves that image to a databse folder
	gib() returns the path to one of the images inside that folder, randomly picked

To use, simply do::

    >>> import realcookie
    >>> a = realcookie.cookie()
	>>> a.add('some cookie image url')
	>>> a.gib()