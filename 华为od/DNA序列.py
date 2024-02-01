def highest_gc_ratio_subsequence(dna_sequence, subsequence_length):
    max_ratio = 0
    max_subsequence = ""

    for i in range(len(dna_sequence) - subsequence_length + 1):
        subseq = dna_sequence[i : i + subsequence_length]
        gc_count = subseq.count("G") + subseq.count("C")
        ratio = gc_count / len(subseq)

        if ratio > max_ratio:
            max_ratio = ratio
            max_subsequence = subseq

    return max_subsequence


# 例子输入
sequence = "AACTGTGCACGACCTGA"
length = 5

result = highest_gc_ratio_subsequence(sequence, length)
print(result)
