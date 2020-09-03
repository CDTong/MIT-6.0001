def get_permutations(sequence):
    if len(sequence) == 0:
        print('empty sequence')
    if len(sequence) == 1:
        return[sequence]
    result = []
    for i, let in enumerate(sequence):
        for p in get_permutations(sequence[:i]+sequence[i+1:]):
            result = result+[let+p]
    return result


if __name__ == '__main__':
    example_input = 'cde'
    print('Input is: cde')
    print('Expected Output:', ['cde', 'ced', 'dce', 'dec', 'ecd', 'edc'])
    print('Actual Output:', get_permutations(example_input))
