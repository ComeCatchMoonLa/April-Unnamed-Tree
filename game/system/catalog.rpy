# 只读节点 / CG 查询。未知 ID 记日志并返回 None，不抛给 UI。

init python:
    class _NodeCatalog(object):

        def get_node(self, node_id):
            node = NODE_BY_ID.get(node_id)
            if node is None:
                renpy.log("NodeCatalog: unknown node_id %r" % (node_id,))
            return node

        def nodes_in_chapter(self, chapter_id):
            if chapter_id not in CHAPTER_IDS:
                renpy.log("NodeCatalog: unknown chapter_id %r" % (chapter_id,))
                return []
            return [node for node in NODE_DEFS if node.chapter_id == chapter_id]

        def all_nodes(self):
            return list(NODE_DEFS)

        def chapter_of(self, node_id):
            node = self.get_node(node_id)
            if node is None:
                return None
            return node.chapter_id

        def first_line_id(self, node_id):
            if self.get_node(node_id) is None:
                return None
            # 章脚本尚未标注句号时的约定；0.8 必须以实际首句为准。
            return "%s:0001" % node_id

        def chapter_last_line_id(self, chapter_id):
            nodes = self.nodes_in_chapter(chapter_id)
            if not nodes:
                return None
            # 暂用该章末节点首句；0.8 有真实末句后再改，不另加字段。
            return self.first_line_id(nodes[-1].node_id)

        def get_cg(self, cg_id):
            cg = CG_BY_ID.get(cg_id)
            if cg is None:
                renpy.log("NodeCatalog: unknown cg_id %r" % (cg_id,))
            return cg

        def all_cgs(self):
            return list(CG_DEFS)

        def route_of_chapter(self, chapter_id):
            route = ROUTE_BY_CHAPTER.get(chapter_id)
            if route is None:
                renpy.log("NodeCatalog: unknown chapter_id %r" % (chapter_id,))
            return route

    NodeCatalog = _NodeCatalog()


init 1 python:
    def _log_catalog():
        nodes = NodeCatalog.all_nodes()
        cgs = NodeCatalog.all_cgs()
        renpy.log("NodeCatalog: %d nodes, %d cgs" % (len(nodes), len(cgs)))
        for node in nodes:
            renpy.log("  node %s" % node.node_id)
        for cg in cgs:
            renpy.log("  cg %s" % cg.cg_id)

    _log_catalog()


# 不挂启动路径。控制台：jump catalog_probe
label catalog_probe:
    $ ncount = len(NodeCatalog.all_nodes())
    $ ccount = len(NodeCatalog.all_cgs())
    $ unknown_none = NodeCatalog.get_node("no_such_node") is None
    "目录：[ncount] 节点 / [ccount] CG；未知 ID 为 None：[unknown_none]"
    jump boot
