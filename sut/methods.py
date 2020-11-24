def remove_zeros_from(text):
    return text.replace('0', '')


def get_positives(items):
    return [item for item in items if item > 0]
