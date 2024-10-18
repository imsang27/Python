m_sum = 0
n_sum = 0

for m in range(100, 49, -1):
  m_sum += m
  print(f"m: {m:<3} m_sum: {m_sum:<3}")

for n in range(0, 51, 1):
  n_sum += n
  print(f"n: {n:<3} n_sum: {n_sum}")

mn = float(str(m_sum) + "." + str(n_sum))

print(mn)