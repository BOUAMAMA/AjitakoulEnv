web: gunicorn dj-project.wsgi
web: gunicorn application:app
web: bundle exec puma start -p $PORT $RAILS_ENV -C config/puma.rb