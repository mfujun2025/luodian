# -*- coding: utf-8 -*-
"""GitHub Actions：审核通过的商家自动追加到 shops-data.json（幂等）"""
import json, os, sys

CWD = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 仓库根
DATA = os.path.join(CWD, "assets", "data", "shops-data.json")

payload_raw = os.environ.get("PAYLOAD", "")
if not payload_raw:
    print("NO_PAYLOAD")
    sys.exit(0)

try:
    payload = json.loads(payload_raw)
except Exception as e:
    print("BAD_PAYLOAD", e)
    sys.exit(1)

record_id = str(payload.get("record_id", "")).strip()
if not record_id:
    print("NO_RECORD_ID")
    sys.exit(1)

with open(DATA, "r", encoding="utf-8") as f:
    shops = json.load(f)

# 幂等：同一 record_id 已存在则跳过
if any(s.get("record_id") == record_id for s in shops):
    print("ALREADY_EXISTS", record_id)
    sys.exit(0)

shops.append({
    "record_id": record_id,
    "type": str(payload.get("type", "")).strip(),
    "name": str(payload.get("name", "")).strip(),
    "phone": str(payload.get("phone", "")).strip(),
    "addr": str(payload.get("addr", "")).strip(),
    "intro": str(payload.get("intro", "")).strip(),
})

with open(DATA, "w", encoding="utf-8") as f:
    json.dump(shops, f, ensure_ascii=False, indent=2)

print("APPENDED", record_id, "total", len(shops))
