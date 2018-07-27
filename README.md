# flask_plot
<img src="https://raw.githubusercontent.com/xaratustrah/flask_plot_docker/master/screenshot.png" width="512">

This is the dockerized version of [this repository](https://github.com/xaratustrah/flask_plot). I have learned a lot and used code snippets from [Patrick Kennedy's blog post](http://www.patricksoftwareblog.com/how-to-use-docker-and-docker-compose-to-create-a-flask-application/) and [Maksym Sladkov' project](https://github.com/sladkovm/docker-flask-gunicorn-nginx/blob/master/docker-compose.yml). Patrick has many other blog posts the topic of `docker`.

For this project, I have tried to maintain the recommanded directory structure on [flask's official docs](http://flask.pocoo.org/docs/1.0/patterns/packages/), mixed with suggestions in above posts.

The above posts use `docker-compose up --build -d`. While this is still OK, meanwhile the official docker docs recommend using the new syntax `docker stack deploy -c docker-compose.yml somestackname` which is swarm compatible. So I tried to change the syntax accordingly.

For completeness, a `setup.py` file has been provided. In order to avoid duplicating, including the `requirements.txt` in `setup.py` was inspired by [Karol Kuczmarski's blog post](http://xion.io/post/code/python-pip-requirements.html).

You can run this code in several ways. At the top level directory run:

    python flask_plot/run.py

or you can install using `pip`. But that is not the whole idea. Better is docker of course.
