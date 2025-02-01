import hashlib

def generate_hash(name, date, time, price) -> str:
    data = f"{name}{time}{price}{date}"
    hash_id = hashlib.sha256(data.encode()).hexdigest()
    return hash_id[:16]
    