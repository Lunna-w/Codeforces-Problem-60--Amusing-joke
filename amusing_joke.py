from collections import Counter


guest = input().strip()
host = input().strip()
pile = input().strip()


guest_host_count = Counter(guest + host)
pile_count = Counter(pile)

if guest_host_count == pile_count:
    print("YES")
else:
    print("NO")