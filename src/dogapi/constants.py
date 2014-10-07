
class MetricType(object):
    Gauge = "gauge"
    Counter = "counter"
    Histogram = "histogram"


class CheckStatus(object):
    OK = 0
    WARNING = 1
    CRITICAL = 2
    UNKNOWN = 3
    ALL = (OK, WARNING, CRITICAL, UNKNOWN)
