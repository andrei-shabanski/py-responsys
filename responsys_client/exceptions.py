class ResponsysClientError(Exception):
    pass


class ResponsysLimitError(ResponsysClientError):
    pass


class ResponsysTimeoutError(ResponsysClientError):
    message = 'There was a timeout error sending a request to Responsys'

    def __init__(self, method, url):
        super(ResponsysTimeoutError, self).__init__(method, url)

        self.method = method
        self.url = url

    def __str__(self):
        return '{message}. Method: {method}, URL: {url}'.format(message=self.message,
                                                                method=self.method,
                                                                url=self.url)


class ResponsysHTTPError(ResponsysClientError):

    def __init__(self, message, response):
        super(ResponsysHTTPError, self).__init__(message, response)

        self.message = message
        self.response = response

    def __str__(self):
        request = self.response.request

        return ('{message}. Request Method: {method}. Request Path: {path}. '
                'Request Body: {request}. Response Status Code: {status}. '
                'Response Text: {response}.'
                .format(message=self.message,
                        method=request.method,
                        path=request.path_url,
                        request=request.body,
                        status=self.response.status_code,
                        response=self.response.text))


class ResponsysAuthError(ResponsysHTTPError):
    message = 'There was an issue sending a login request to Responsys'

    def __init__(self, response):
        super(ResponsysAuthError, self).__init__(self.message, response)
