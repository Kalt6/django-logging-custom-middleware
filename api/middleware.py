import time
import logging

logger = logging.getLogger(__name__)


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        # Below are the requests
        method = request.method
        path = request.path

        # Calling the middleware
        response = self.get_response(request)

        # Response info to be logged
        duration = time.time() - start_time
        status_code = response.status_code


        # Logging the request info and the response info
        logger.info(
            f"Request handled | {method} {path} | status: {status_code} | duration: {round(duration*1000,2)}ms"
        )

        return response





