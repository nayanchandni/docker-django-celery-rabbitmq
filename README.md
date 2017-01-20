Every module runs as a container:
1.web - acts as the celery master here (also acts as the message broker and defines tasks)
2.worker - celery worker that picks up tasks
3.redis - result backend
4.rabbit - RabbitMQ the message queue

Running the containers:

$docker-compose up --build 
(by default brings up one worker)

To bring up more than one worker,use command - 

$docker-compose scale worker=4


Note : The flower folder contains the flower(celery monitoring tool) which can be integrated later.