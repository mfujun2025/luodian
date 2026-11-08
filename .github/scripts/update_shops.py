# -*- coding: utf-8 -*-
"""GitHub Actions：同步飞书审核结果到 shops-data.json

EVENT=merchant-approved  → 审核通过，幂等追加
EVENT=merchant-rejected  → 审核驳回，按 record_id 下架（不存在则什么都不做）
"""
import json, os, sys

CWD = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 仓库根
DATA = os.path.join(CWD, "assets", "data", "shops-data.json")

# 只有这两类申请会上网站；其他咨询类审核通过也不收录
ALLOWED_TYPES = {"商家收录", "厂房房源"}


def pick(value):
    """把飞书传过来的值规整成字符串：选项字段可能给数组，空值给 None"""
    if value is None:
        return ""
    if isinstance(value, list):
        value = value[0] if value else ""
    if isinstance(value, dict):
        value = value.get("name") or value.get("text") or ""
    return str(value).strip()


def save(shops):
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(shops, f, ensure_ascii=False, indent=2)
        f.write("\n")


event = pick(os.environ.get("EVENT", "merchant-approved"))
payload_raw = os.environ.get("PAYLOAD", "")
if not payload_raw:
    print("NO_PAYLOAD")
    sys.exit(0)

try:
    payload = json.loads(payload_raw)
except Exception as e:
    print("BAD_PAYLOAD", e)
    sys.exit(1)

record_id = pick(payload.get("record_id"))
if not record_id:
    print("NO_RECORD_ID")
    sys.exit(1)

with open(DATA, "r", encoding="utf-8-sig") as f:   # 兼容带 BOM 的文件
    shops = json.load(f)

if event == "merchant-rejected":
    remain = [s for s in shops if s.get("record_id") != record_id]
    if len(remain) == len(shops):
        print("NOT_FOUND", record_id, "nothing to remove")
        sys.exit(0)
    save(remain)
    print("REMOVED", record_id, "total", len(remain))
    sys.exit(0)

biz_type = pick(payload.get("type"))
if biz_type not in ALLOWED_TYPES:
    print("SKIP_TYPE", record_id, biz_type)
    sys.exit(0)

# 幂等：同一 record_id 已存在则跳过
if any(s.get("record_id") == record_id for s in shops):
    print("ALREADY_EXISTS", record_id)
    sys.exit(0)

shops.append({
    "record_id": record_id,
    "type": biz_type,
    "name": pick(payload.get("name")),
    "phone": pick(payload.get("phone")),
    "addr": pick(payload.get("addr")),
    "intro": pick(payload.get("intro")),
})

save(shops)
print("APPENDED", record_id, biz_type, "total", len(shops))
