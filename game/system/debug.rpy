# 开发用。测继续/脏槽前把 RESET 改 False；正式解锁随 0.8，鉴赏可先全开。
define DEBUG_RESET_ON_BOOT = True
define DEBUG_UNLOCK_GALLERY = False

init python:
    def debug_apply_boot():
        if DEBUG_RESET_ON_BOOT:
            SaveStore.clear_slot(SLOT_MAIN)
            UnlockStore.clear_all()
        if DEBUG_UNLOCK_GALLERY:
            data = UnlockStore._load_raw()
            data["nodes"] = [node.node_id for node in NODE_DEFS]
            data["cgs"] = [cg.cg_id for cg in CG_DEFS]
            UnlockStore._save_raw(data)
