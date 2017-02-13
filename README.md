Link Check
==========

This is a simple function that takes a list of URLs
and verifies each one. Bad URLs are returned with a
reason for failure (bad format and/or unable to locate
the requested service).

Command Line
------------

    python3 linkcheck.py <link1> <link2> ... <linkn>

From Python
-----------

    from linkcheck import check_links
    
    results = check_links(['link1', 'link2', ..., 'linkn'])

Running Tests
-------------

    $ python3 test_linkcheck.py