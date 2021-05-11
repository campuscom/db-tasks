from models.certificate.certificate import Certificate
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_all_certificate_with_careers():
    query = {'careers__exists': True}
    return Certificate.objects(**query)
