from datetime import datetime
print(*datetime.utcnow().strftime('%Y-%m-%d').split('-'),sep="\n")