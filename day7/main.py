# khai bao
tap_hop_a = set()

# tap_hop = {1,2,9,10} # so, chu, dic, list

#  ham len 
# print(len(tap_hop))

#  toán tư in 
# print(1 not in tap_hop)

# thêm vào 1 tập hơp mình có syntax
# tap_hop.add(1)

# tap_hop = {"pt1","pt2","pt3","pt4"}
# print(tap_hop) # 

#  tap hop la ds khong trung
#  de them nhiu tap hop
# update
tap_hop_a = {1,2,9,10}
# tap_hop_b = {5,6,7}
# print(tap_hop_a.union(tap_hop_b))
# tap_hop.update({5,6,7})
# print(tap_hop_a)

# print(tap_hop_b)
# union

tap_hop_a = {5,2,3,1,6,7, 10}
# remove neu khong co thi bao loi
# tap_hop_a.remove(10)
# discard neu khong co thi ko lam j het
# tap_hop_a.discard(11)
# xoa phan tu ngau nhiên 
# tap_hop_a.pop()

# 1 > 5 > 2 < 3 > 6 < 7

# print(tap_hop_a.remove(10))
# print(tap_hop_a)

# tap_hop_a.clear()
# clear vs del
# clear la gan lai tap hơp rỗng
# del xoá luôn biên

# print(tap_hop_a)

# ds = [1,2,2,3]
# tap_hop_a = set(ds)
# print(tap_hop_a)

# tap_hop_a = {5,2,3,1,6,7, 10}

# ds = list(tap_hop_a)
# print(ds)

# tpa = {1,2,3,4}
# tpb = {3,2,10}

# print(tpa.intersection(tpb))

# tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
# tap2 = {'pt2', 'pt3'}
# print(tap2.issubset(tap1))    # True  — tap2 ⊆ tap1
# print(tap2.issuperset(tap1))  #  True  — tap1 ⊇ tap2
# tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
# tap2 = {'pt2', 'pt3'}
# print(tap2.issuperset(tap1))  

# hiệu
# print(tap2.difference(tap1))    
# hiệu đối xứng
# cú pháp
# tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
# tap2 = {'pt2', 'pt3'}
# print(tap2.symmetric_difference(tap1))

# tap hơp rời nhau

# xem thằng 2 có khác thằng 1 hay không
# tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
# tap2 = {'pt6', 'pt5'}
# print(tap2.isdisjoint(tap1))

# tap1 = {'pt1', 'pt2', 'pt3', 'pt4'}
# tap2 = {'pt3', 'pt5'}

# # in pt3 
# print(tap1.intersection(tap2))
# # in 'pt1', 'pt2', 'pt4' 
# print(tap1.difference(tap2))
# # in 'pt1', 'pt2', 'pt4' , 'pt5' 
# print(tap1.symmetric_difference(tap2))
# # in 'pt1', 'pt2','pt3', 'pt4' , 'pt5' 
# print(tap1.union(tap2))
# # in 'pt5' 
# print(tap2.difference(tap1))

# Kiêu từ điển

tu_dien_rong = {}
# Từ điển có dữ liệu
dct = {
    'key1':'value1', 
    'key2':'value2', 
    'key3':'value3', 
    'key4':'value4'
}

# nguoi = {
#     'ten': 'Asabeneh',
#     'ho': 'Yetayeh',
#     'tuoi': 250,
#     'quoc_gia': 'Phần Lan',
#     'da_ket_hon': True,
#     'ky_nang': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'dia_chi': {
#         'duong': 'Space street',
#         'ma_buu_dien': '02210'
#     }
# }


# print(nguoi['tuoi'])

# print(len(nguoi))

# print(nguoi['dia_chi']['duong'])
# print(nguoi['ky_nang'][2])
# print(nguoi.get('tuoi'))
# print(nguoi.get('dia_chi'))

# nguoi['ten'] = "thai"
# nguoi['ky_nang'].append('CSS')
# in ben dic la tim key
# print('ky_nang_1' in nguoi)
# nguoi.pop()
# nguoi.popitem()


# del nguoi['ten']
# nguoi.pop('ten')
# nguoi['ten'] = None
# nguoi.clear()
# print(nguoi)

# nguoi1 = {
#     'ten': 'thai',
#     'ho': 'huynh',
# }

# nguoi2 = nguoi1.copy()

# nguoi1['ten'] = 'thanh' 

# print(nguoi2)

# nguoi1 = {
#     'ten': 'thai',
#     'ho': 'huynh',
# }

# print(nguoi1.values())

# nhập n = 3 => "***", n = 10 => "**********", n thuộc (1,10)

dau_vao = int(input())
kt = {
    '1': "*",
    '2': "**",
    '3': "***"
}

print(list(kt.values())[dau_vao - 1])