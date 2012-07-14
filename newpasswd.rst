=========
newpasswd
=========

-----------------------------
generate a brand new password
-----------------------------

:Author: Written by Simonas Kazlauskas <https://github.com/simukis>.
:Date:   2012-07-11
:Copyright: Copyright © 2012 Simonas Kazlauskas. Licence: ICS.
:Version: 0.1
:Manual section: 1
:Manual group: User Commands

SYNOPSIS
========

::

    newpasswd [-h] [-l LEN] [-n N] [-r] [--extended] [--greek] [--cyrillic]

OPTIONS
=======

--help, -h              Show this help message and exit.
--length=LEN, -l LEN    Length of your password.
--count=N, -n N         Ammount of passwords to generate.
--random, -r            Use /dev/random as source of randomity.
--extended              Use characters from Latin Supplement, Extended-A and
                        Extended-B blocks in password.
--greek                 Use characters from Greek and Coptic block in
                        password.
--cyrillic              Use characters from Cyrillic and Cyrillic Supplement
                        blocks in password.

ISSUES
======

https://github.com/simukis/newpasswd/issues


