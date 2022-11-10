from collections import defaultdict


def solution(s1, s2, k):
    all_subjects = set()
    visitable_by_subject = defaultdict(set)
    come_in_by_subject = defaultdict(set)

    for subject_from, subject_to in zip(s1, s2):
        all_subjects.update([subject_from, subject_to])
        visitable_by_subject[subject_from].add(subject_to)
        come_in_by_subject[subject_to].add(subject_from)

    answer = []
    while True:
        zero_come_in_subjects = set()
        for subject in all_subjects:
            come_in_subjects = come_in_by_subject[subject]
            if len(come_in_subjects) == 0:
                zero_come_in_subjects.add(subject)
        if k in zero_come_in_subjects:
            answer.append(k)
            break
        zero_come_in_subjects = sorted(list(zero_come_in_subjects))
        for zero_subject in zero_come_in_subjects:
            answer.append(zero_subject)
            all_subjects.remove(zero_subject)
            zero_subject_visitable_list = visitable_by_subject[zero_subject]
            for zero_subject_visitable in zero_subject_visitable_list:
                come_in_by_subject[zero_subject_visitable].remove(zero_subject)


    return answer

