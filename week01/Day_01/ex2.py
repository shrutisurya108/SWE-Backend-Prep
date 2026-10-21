# Log parser (real backend task): given line = "2026-10-19 15:37:02 ERROR [payment-service] Card declined for user_id=4821"
# extract and print date, level, service (without brackets) and user_id as an int. Use split and slicing only.

logline = "2026-10-19 15:37:02 ERROR [payment-service] Card declined for user_id=4821"
log_details = logline.split(' ')
date_val=log_details[0]
level=log_details[2]
service=log_details[3][1:-1]
user_id=int(log_details[-1].split('=')[1])
print(f"date: {date_val}, level: {level}, service: {service}, user_id: {user_id}, type_user_id: {type(user_id)}")