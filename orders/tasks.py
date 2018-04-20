from celery import task
from celery.app import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    order.paid = True
    import time
    time.sleep(60)
    order.save()
    
    # subject = 'Order nr. {}'.format(order.id)
    # message = 'Dear {},\n\nYou have successfully placed an order.\
    #               Your order id is {}.'.format(order.first_name, order.id)
    # mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    # return mail_sent

    return True


logger = get_task_logger(__name__)

@shared_task
def debug_task(msg):
    import time
    time.sleep(10)
    logger.info("debug|msg=%s", msg)
