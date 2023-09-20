def needleman_wunsch(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-2):
    n = len(seq1)
    m = len(seq2)
    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        score_matrix[i][0] = i * gap_penalty
    for j in range(m + 1):
        score_matrix[0][j] = j * gap_penalty

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score)
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(match, delete, insert)

    alignment_seq1 = []
    alignment_seq2 = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
            alignment_seq1.insert(0, seq1[i - 1])
            alignment_seq2.insert(0, '-')
            i -= 1
        elif j > 0 and score_matrix[i][j] == score_matrix[i][j - 1] + gap_penalty:
            alignment_seq1.insert(0, '-')
            alignment_seq2.insert(0, seq2[j - 1])
            j -= 1
        else:
            alignment_seq1.insert(0, seq1[i - 1])
            alignment_seq2.insert(0, seq2[j - 1])
            i -= 1
            j -= 1
    return ''.join(alignment_seq1), ''.join(alignment_seq2), score_matrix[n][m]

seq1 = "AGGCTAG"
seq2 = "AGCGA"
alignment1, alignment2, score = needleman_wunsch(seq1, seq2)
print("Sequence 1:", alignment1)
print("Sequence 2:", alignment2)
print("Alignment Score:", score)
