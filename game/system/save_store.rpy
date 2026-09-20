# 唯一写槽点。load_slot 只读记录，不整局 renpy.load。

init python:
    from collections import namedtuple
    import datetime
    import re

    SLOT_MAIN = "0"
    SCHEMA_VERSION = 1
    STYLES = ("omote", "ura")
    ROUTES = ("main", "after", "inner")
    PLAY_MODES = ("play", "replay")
    LINE_ID_RE = re.compile(r"^[a-z0-9_]+:[0-9]{4}$")
    _SAVE_RECORD_KEYS = (
        "slot_id",
        "updated_at",
        "chapter_id",
        "node_id",
        "line_id",
        "style",
        "route",
        "play_mode",
        "reserved",
    )

    SaveRecord = namedtuple(
        "SaveRecord",
        (
            "slot_id",
            "updated_at",
            "chapter_id",
            "node_id",
            "line_id",
            "style",
            "route",
            "play_mode",
            "reserved",
        ),
    )
    LineRef = namedtuple(
        "LineRef",
        ("chapter_id", "node_id", "line_id", "style", "route"),
    )

    class _SaveStore(object):

        def has_slot(self, slot_id):
            return self.load_slot(slot_id) is not None

        def load_slot(self, slot_id):
            slots = persistent.sakura_save_slots
            if not isinstance(slots, dict):
                return None
            payload = slots.get(slot_id)
            return self._record_from_payload(payload)

        def write_record(self, record):
            if record.play_mode != "play":
                return False
            cleaned = record._replace(reserved={})
            if not self._record_writable(cleaned):
                return False
            slots = persistent.sakura_save_slots
            if not isinstance(slots, dict):
                slots = {}
            else:
                slots = dict(slots)
            slots[cleaned.slot_id] = self._payload_from_record(cleaned)
            persistent.sakura_save_slots = slots
            # 立刻落盘，避免只杀进程时 persistent 还停在内存。
            renpy.save_persistent()
            return True

        def write_line(self, slot_id, line):
            record = SaveRecord(
                slot_id,
                datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                line.chapter_id,
                line.node_id,
                line.line_id,
                line.style,
                line.route,
                "play",
                {},
            )
            return self.write_record(record)

        def clear_slot(self, slot_id):
            slots = persistent.sakura_save_slots
            if not isinstance(slots, dict):
                slots = {}
            else:
                slots = dict(slots)
            if slot_id in slots:
                del slots[slot_id]
            persistent.sakura_save_slots = slots
            renpy.save_persistent()
            return True

        def _record_writable(self, record):
            if not LINE_ID_RE.match(record.line_id):
                renpy.log("SaveStore: bad line_id %r" % (record.line_id,))
                return False
            if record.style not in STYLES or record.route not in ROUTES:
                renpy.log("SaveStore: bad style/route")
                return False
            node = NodeCatalog.get_node(record.node_id)
            if node is None:
                return False
            if node.chapter_id != record.chapter_id:
                renpy.log("SaveStore: node/chapter mismatch")
                return False
            if NodeCatalog.route_of_chapter(record.chapter_id) is None:
                return False
            return True

        def _payload_from_record(self, record):
            payload = {"schema_version": SCHEMA_VERSION}
            for key in _SAVE_RECORD_KEYS:
                payload[key] = getattr(record, key)
            payload["reserved"] = {}
            return payload

        def _record_from_payload(self, payload):
            if not isinstance(payload, dict):
                return None
            if payload.get("schema_version") != SCHEMA_VERSION:
                return None
            try:
                values = [payload[key] for key in _SAVE_RECORD_KEYS]
            except KeyError:
                return None
            record = SaveRecord(*values)
            if record.play_mode != "play":
                return None
            if not isinstance(record.reserved, dict):
                return None
            if record.style not in STYLES or record.route not in ROUTES:
                return None
            if not LINE_ID_RE.match(record.line_id):
                return None
            return record._replace(reserved={})

    SaveStore = _SaveStore()
