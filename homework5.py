immutable_var = 1, 3, 5, True, 'string'
print(immutable_var)
# immutable_var[1] = 35 # ВЫДАСТ ОШИБКУ, Т.К. кортеж используют в качестве хранилища, например для какого-нибудь списка, чтобы он оставался неизменным
mutable_list = [1, 2, 'a', 'b', True]
print(mutable_list)
print([mutable_list * 3])
mutable_list[1] = 35
print(mutable_list)