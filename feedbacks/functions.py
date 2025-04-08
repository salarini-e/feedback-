from collections import Counter
from .models import Feedback
import statistics

def get_feedback_distribution(feedbacks, field):
    values = feedbacks.values_list(field, flat=True)
    counter = Counter(values)
    total = sum(counter.values())
    return {
        i: {
            'count': counter.get(i, 0),
            'percent': round((counter.get(i, 0) / total) * 100, 2) if total else 0
        }
        for i in range(1, 6)
    }

RATING_CHOICES = dict(Feedback.RATING_CHOICES)

def get_frequencies(feedbacks, field):
    values = list(feedbacks.values_list(field, flat=True))
    count = {}
    for v in values:
        count[v] = count.get(v, 0) + 1

    total = len(values)
    freq = [
        {
            'valor': RATING_CHOICES.get(k, k),
            'numero': v,
            'porcentagem': round((v / total) * 100, 1)
        }
        for k, v in sorted(count.items())
    ]

    moda = statistics.mode(values) if values else None
    mediana = statistics.median(values) if values else None

    return {
        'frequencias': freq,
        'moda': RATING_CHOICES.get(moda, moda),
        'mediana': RATING_CHOICES.get(mediana, mediana),
        'total': total
    }