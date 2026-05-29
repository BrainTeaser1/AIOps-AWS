from clients.aws_clients import cloudwatch


def get_active_alarms():

    alarms = cloudwatch.describe_alarms()

    return [
        {
            "alarm_name": alarm["AlarmName"],
            "state": alarm["StateValue"],
            "reason": alarm["StateReason"]
        }
        for alarm in alarms["MetricAlarms"]
    ]
