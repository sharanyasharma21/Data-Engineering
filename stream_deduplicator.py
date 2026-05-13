# Implement a streaming deduplicator for records with:
# {"id": str, "timestamp": int, "payload": dict}

import random
import time
from pprint import pprint


def generate_fake_stream(n=20, unique_ids=5):
    records = []

    for _ in range(n):
        record_id = f"user_{random.randint(1, unique_ids)}"

        record = {
            "id": record_id,
            "timestamp": int(time.time()) + random.randint(-100, 100),
            "payload": {
                "event_type": random.choice(["click", "view", "purchase"]),
                "text": random.choice([
                    "Hello World",
                    "hello world",
                    "HELLO WORLD",
                    "Data Engineering",
                    "data engineering",
                    "Python practice"
                ]),
                "quality_score": random.randint(1, 100)
            }
        }

        records.append(record)

    return records


records = generate_fake_stream(n=20, unique_ids=5)

# pprint(records)

# dedup only by ID
def dedup_by_id(records):
    # return unique IDs
    seen = set()
    for record in records:
        # print(record["id"])
        seen.add(record["id"])
    return seen
# print(dedup_by_id(generate_fake_stream(n=20, unique_ids=5)))    

# count how many times each ID appears
def counts_by_id(records):
    id_counts = {}
    for record in records:
        record_id = record["id"]

        if record_id not in id_counts:
            id_counts[record_id] = 0
        id_counts[record_id] += 1 
    
    return id_counts
# print(counts_by_id(generate_fake_stream(n=20, unique_ids=5)))    


# dedup by ID, keep newest timestamp
def dedup_by_id_and_timestamp(records):
    best_records = {}

    for record in records:
        record_id = record["id"]

        if record_id not in best_records:
            best_records[record_id] = record

        else:
            if record["timestamp"] > best_records[record_id]["timestamp"]:
                best_records[record_id] = record
    return best_records
# print(dedup_by_id_and_timestamp(generate_fake_stream(n=20, unique_ids=5)))  

# dedup ID by keeping highest quality_score
def highest_quality_score(records):
    best_records = {}

    for record in records:
        record_id = record["id"]

        if record_id not in best_records:
            best_records[record_id] = record
        else:
            if record["payload"]["quality_score"] > best_records[record_id]["payload"]["quality_score"]:
                best_records[record_id] = record

    return best_records
# pprint(records)
# print(highest_quality_score(generate_fake_stream(n=20, unique_ids=5)))  

# get record with highest quality score deduped by normalized text hash
import hashlib

def normalize_and_hash(text):
    normalized = text.strip().lower()         
    return hashlib.md5(normalized.encode()).hexdigest()

def highest_quality_score_by_normalized_text(records):
    best_records = {}

    for record in records:
        record_id = record["id"]
        text_hash = normalize_and_hash(record["payload"]["text"])
        key = (record_id, text_hash)  # composite key

        if key not in best_records:
            best_records[key] = record
        else:
            if record["payload"]["quality_score"] > best_records[key]["payload"]["quality_score"]:
                best_records[key] = record

    return best_records

# Windowed dedup record with TTL
# return non duplicate customer_ids in a 60 second interval

import time

def windowed_dedup_with_ttl(records, ttl_seconds=60):
    best_records = {}   # key -> record
    expiry_times = {}   # key -> unix timestamp when this entry expires

    now = int(time.time())

    for record in records:
        record_id = record["id"]
        record_ts = record["timestamp"]

        # evict expired entries before processing
        expired_keys = [k for k, exp in expiry_times.items() if now > exp]
        for k in expired_keys:
            del best_records[k]
            del expiry_times[k]

        if record_id not in best_records:
            best_records[record_id] = record
            expiry_times[record_id] = record_ts + ttl_seconds  # TTL anchored to record time
        else:
            if record["payload"]["quality_score"] > best_records[record_id]["payload"]["quality_score"]:
                best_records[record_id] = record
                expiry_times[record_id] = record_ts + ttl_seconds  # reset TTL on update

    return best_records

