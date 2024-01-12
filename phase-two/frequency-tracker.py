from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.counts = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number):
        prev_count = self.counts[number]
        self.counts[number] += 1
        self.freq[prev_count] -= 1
        self.freq[prev_count + 1] += 1

    def deleteOne(self, number):
        if self.counts[number] > 0:
            prev_count = self.counts[number]
            self.counts[number] -= 1
            self.freq[prev_count] -= 1
            self.freq[prev_count - 1] += 1

    def hasFrequency(self, frequency):
        return self.freq[frequency] > 0