Lumbergh
=======

Lumbergh is the Mozilla careers website. It is a [playdoh][gh-playdoh]-based site
that displays open jobs.

[gh-playdoh]: https://github.com/mozilla/playdoh

Setup
-----
These instructions assume you have [git][], [python][], and `pip` installed. If
you don't have `pip` installed, you can install it with `easy_install pip`.


1. Start by getting the source:

   ```sh
   $ git clone --recursive git@github.com:mozilla/lumbergh.git
   $ cd lumbergh
   ```
   Note you may want to fork and clone the repo as described in the
   [github docs][git-clone] if you are doing active development.

2. Create a virtualenv for Lumbergh. Skip the first step if you already have
   `virtualenv` installed.

   ```sh
   $ pip install virtualenv
   $ virtualenv venv
   $ source venv/bin/activate
   ```

3. Install the compiled requirements:

   ```sh
   $ pip install -r requirements/compiled.txt
   ```

4. Set up a local MySQL database. The [MySQL Installation Documentation][mysql]
   explains how to do this. Make sure your DB is utf8.

5. Configure your local settings by copying `careers/settings/local.py-dist` to
   `careers/settings/local.py` and customizing the settings in it:

   ```sh
   $ cp settings/local.py-dist settings/local.py
   ```

   The file is commented to explain what each setting does and how to customize
   them.

   If you wish to have jobs appear locally make sure JOBVITE_URI is set.

6. Initialize your database structure:

   ```sh
   $ python manage.py syncdb
   $ python manage.py migrate
   ```

Running the Development Server
------------------------------
You can launch the development server like so:

```sh
$ python manage.py runserver
```

Updating Jobs
------------------------------
You can update jobs so they appear locally by running:

```sh
$ python manage.py syncjobvite
```


[git]: http://git-scm.com/
[git-clone]: https://help.github.com/articles/fork-a-repo
[python]: http://www.python.org/
[mysql]: http://dev.mysql.com/doc/refman/5.6/en/installing.html
[gh-playdoh]: https://github.com/mozilla/playdoh


License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://creativecommons.org/licenses/BSD/
