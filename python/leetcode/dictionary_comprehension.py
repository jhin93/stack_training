
squares = {x: x**2 for x in range(1, 5)}
print(squares)

even_squares = {x: x**2 for x in range(1, 10) if x % 2 == 0}
print(even_squares)

servers = ["server1", "server2", "server3", "server4"]
statuses = ["active", "inactive", "active", "maintenance"]

active_servers = {server: status for server, status in zip(servers, statuses) if status == "active" }
print(active_servers)

names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 90, 78, 88]

over_80 = {name[:3].upper(): score for name, score in zip(names, scores) if score > 80}
print(over_80)
