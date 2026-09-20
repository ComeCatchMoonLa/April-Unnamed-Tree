# 唯一写解锁点。关游戏仍在；不放进存档槽。

init python:
    from collections import namedtuple

    PersistentUnlocks = namedtuple(
        "PersistentUnlocks",
        ("after_unlocked", "inner_unlocked", "nodes", "cgs"),
    )

    class _UnlockStore(object):

        def get_all(self):
            data = self._load_raw()
            return PersistentUnlocks(
                data["after_unlocked"],
                data["inner_unlocked"],
                list(data["nodes"]),
                list(data["cgs"]),
            )

        def is_node_unlocked(self, node_id):
            return node_id in self._load_raw()["nodes"]

        def is_cg_unlocked(self, cg_id):
            return cg_id in self._load_raw()["cgs"]

        def is_after_unlocked(self):
            return self._load_raw()["after_unlocked"]

        def is_inner_unlocked(self):
            return self._load_raw()["inner_unlocked"]

        def unlock_node(self, node_id):
            if NodeCatalog.get_node(node_id) is None:
                return
            data = self._load_raw()
            if node_id in data["nodes"]:
                return
            data["nodes"] = data["nodes"] + [node_id]
            self._save_raw(data)

        def unlock_cg(self, cg_id):
            if NodeCatalog.get_cg(cg_id) is None:
                return
            data = self._load_raw()
            if cg_id in data["cgs"]:
                return
            data["cgs"] = data["cgs"] + [cg_id]
            self._save_raw(data)

        def unlock_after(self):
            data = self._load_raw()
            if data["after_unlocked"]:
                return
            data["after_unlocked"] = True
            self._save_raw(data)

        def unlock_inner(self):
            data = self._load_raw()
            if data["inner_unlocked"]:
                return
            data["inner_unlocked"] = True
            self._save_raw(data)

        def clear_all(self):
            self._save_raw(self._empty())

        def _load_raw(self):
            data = persistent.sakura_unlocks
            if not isinstance(data, dict):
                return self._empty()
            nodes = data.get("nodes")
            cgs = data.get("cgs")
            if not isinstance(nodes, list) or not isinstance(cgs, list):
                return self._empty()
            return {
                "after_unlocked": bool(data.get("after_unlocked")),
                "inner_unlocked": bool(data.get("inner_unlocked")),
                "nodes": list(nodes),
                "cgs": list(cgs),
            }

        def _save_raw(self, data):
            persistent.sakura_unlocks = {
                "after_unlocked": bool(data["after_unlocked"]),
                "inner_unlocked": bool(data["inner_unlocked"]),
                "nodes": list(data["nodes"]),
                "cgs": list(data["cgs"]),
            }
            renpy.save_persistent()

        def _empty(self):
            return {
                "after_unlocked": False,
                "inner_unlocked": False,
                "nodes": [],
                "cgs": [],
            }

    UnlockStore = _UnlockStore()
