# Shard router: given user_id and num_servers = 4, print which server (0–3) stores that user.
# Then print the server for user IDs 1 to 10 in a loop.

num_servers=4
server=None
for u_id in range(1,11):
    print(f"uid: {u_id}, server: {u_id % num_servers}")