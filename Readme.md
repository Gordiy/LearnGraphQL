# To start project, execute next commands
1. docker-compose build
2. docker-compose up
3. docker exec file_storage_web bash -c "python manage.py migrate"
4. docker exec -it file_storage_web bash -c "python manage.py createsuperuser"
