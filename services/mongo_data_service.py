from models.certificate.certificate import Certificate
from models.course.course import Course
from mongoengine import DoesNotExist, NotUniqueError
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_all_certificate_with_careers():
    query = {'careers__exists': True}
    return Certificate.objects(**query)
