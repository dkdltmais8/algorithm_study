def solution(id_list, report, k):
    answer = []
    #똑같은 사람이 똑같은 사람을 신고한 내역을 제외한 신고자들 모임
    s1 = [s.split()[1] for s in set(report)]
    #중복을 제거해서 신고 받은 사람을 1번씩 검사 -> 제제 당할 만큼 신고당했는지 확인해서 맞다면 저장
    s2 = [s for s in set(s1) if s1.count(s)>=k]
    #제제당할 사람들을 신고한 사람들의 정보 저장
    s3 = [s.split()[0] for s in set(report) if s.split()[1] in s2]
    #id_list를 돌면서 각 사람들이 s3에 몇 번 있는지 확인해서 저장
    s4 = [s3.count(i) for i in id_list]
    return s4
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)