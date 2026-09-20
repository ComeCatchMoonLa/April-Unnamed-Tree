# 尾章全文。BGM/SE 只留标记。每句 label 供 jump_to_line。

default _true_picked = None

label ch3_ledger:
    $ PlaySession.on_node_reached("ch3_ledger")
    $ PlaySession.apply_style("omote")
    $ script_restore_visuals("ch3_ledger")
    # 【开场·无画面】
    # 【BGM：无】
label ch3_ledger_0001:
    $ script_say("ch3_ledger:0001", None, "春天的账簿，第一页只有一行字：")
label ch3_ledger_0002:
    $ script_say("ch3_ledger:0002", None, "借：满开一场。")
label ch3_ledger_0003:
    $ script_say("ch3_ledger:0003", None, "贷：她的，余下的光。")
    $ PlaySession.advance_replay()
    jump ch3_omote1

label ch3_omote1:
    $ PlaySession.on_node_reached("ch3_omote1")
    $ PlaySession.apply_style("omote")
    $ script_restore_visuals("ch3_omote1")
    # 【场景：第二年四月·坡道→市立医院】
label ch3_omote1_0001:
    $ script_say("ch3_omote1:0001", None, "第二年，我们发明了一套电码。")
label ch3_omote1_0002:
    $ script_say("ch3_omote1:0002", None, "两指捏袖口：一次，台阶；两次，拐弯；攥住，停。")
label ch3_omote1_0003:
    $ script_say("ch3_omote1:0003", None, "没有名词。后来我才懂为什么——她不需要名词，她只要路。")
label ch3_omote1_0004:
    $ script_say("ch3_omote1:0004", None, "取景框又窄了。如今只剩巴掌大的一块天，悬在她视线的正前方。所以说话时，我总是悄悄挪，把自己校进那块天里。校了半年，自以为天衣无缝。")
label ch3_omote1_0005:
    $ script_say("ch3_omote1:0005", None, "那天下话说到一半，她忽然说：")
label ch3_omote1_0006:
    $ script_say("ch3_omote1:0006", CHAR_YAYOI, "「你往右了。」")
label ch3_omote1_0007:
    $ script_say("ch3_omote1:0007", None, "我僵住。")
label ch3_omote1_0008:
    $ script_say("ch3_omote1:0008", CHAR_ME, "「知道还校？」")
label ch3_omote1_0009:
    $ script_say("ch3_omote1:0009", CHAR_YAYOI, "「知道，才让你校。」她咬扁了吸管，「占领这种事，要双方签字。」")
label ch3_omote1_0010:
    $ script_say("ch3_omote1:0010", None, "候诊室里，陌生人的目光擦过她的侧脸，毫不停留。我竟然嫉妒一双路人的眼睛——嫉妒它随手挥霍的东西，是我用全部措辞也换不来的。羞耻来得很快，像冷水泼上烧红的铁。")
label ch3_omote1_0011:
    $ script_say("ch3_omote1:0011", None, "医生把片子夹上灯箱，声音放得很平：手术是唯一选项，结果，大概率是一片黑。")
label ch3_omote1_0012:
    $ script_say("ch3_omote1:0012", CHAR_YAYOI, "「排期放在满开之后。」她说。")
label ch3_omote1_0013:
    $ script_say("ch3_omote1:0013", None, "「为什么？」医生问。")
label ch3_omote1_0014:
    $ script_say("ch3_omote1:0014", CHAR_YAYOI, "「散场之前，观众有权看完。」她按上笔帽，像给这句话盖了章。")
    $ PlaySession.advance_replay()
    jump ch3_ura1

label ch3_ura1:
    $ PlaySession.on_node_reached("ch3_ura1")
    $ PlaySession.apply_style("ura")
    $ script_restore_visuals("ch3_ura1")
label ch3_ura1_0001:
    $ script_say("ch3_ura1:0001", None, "《颜色库存》·第九夜")
label ch3_ura1_0002:
    $ script_say("ch3_ura1:0002", None, "颜色开始裁员。第一个走的是黄——校门口那张向日葵海报。走得很安静，没拿外套。")
label ch3_ura1_0003:
    $ script_say("ch3_ura1:0003", None, "第十一夜")
label ch3_ura1_0004:
    $ script_say("ch3_ura1:0004", None, "蓝也走了。没告别。它大概觉得，我们之间不需要客套。")
label ch3_ura1_0005:
    $ script_say("ch3_ura1:0005", None, "第十三夜")
label ch3_ura1_0006:
    $ script_say("ch3_ura1:0006", None, "绿是分批走的，先走浅的。树叶请撑住。不然他那套「只报实事」，会没素材。")
label ch3_ura1_0007:
    $ script_say("ch3_ura1:0007", None, "某夜，被夜班护士抓到")
label ch3_ura1_0008:
    $ script_say("ch3_ura1:0008", None, "蒙着眼在走廊练走。十七步一扇门，护士站的消毒水是路标。她说你梦游啊，我说不，我在预习。")
label ch3_ura1_0009:
    $ script_say("ch3_ura1:0009", None, "耳朵先上岗，眼睛才好退休。")
    $ PlaySession.advance_replay()
    jump ch3_omote2

label ch3_omote2:
    $ PlaySession.on_node_reached("ch3_omote2")
    $ PlaySession.apply_style("omote")
    $ PlaySession.on_cg_shown("cg_fullbloom_backlight")
    $ script_restore_visuals("ch3_omote2")
    # 【场景：满开日·旧校舍后·樱树】
    # 【CG：满开·逆光】
label ch3_omote2_0001:
    $ script_say("ch3_omote2:0001", None, "第十年的满开。她仰着脸，那块巴掌大的天空里，粉得几乎装不下。")
label ch3_omote2_0002:
    $ script_say("ch3_omote2:0002", CHAR_YAYOI, "「低头。」她说，「借你的瞳孔，用一下。」")
label ch3_omote2_0003:
    $ script_say("ch3_omote2:0003", None, "睫毛扫到睫毛。一年了，她的目光第一次不再偏移，笔直地，落在我脸上。落在更深处。虹膜的黑色里，烧着一粒极小的光。")
label ch3_omote2_0004:
    $ script_say("ch3_omote2:0004", CHAR_YAYOI, "「……看到了。」她说，「粉色。原来收存在你这里，是这个颜色。」")
label ch3_omote2_0005:
    $ script_say("ch3_omote2:0005", CHAR_ME, "「和花瓣上的一样吗？」")
label ch3_omote2_0006:
    $ script_say("ch3_omote2:0006", CHAR_YAYOI, "「不知道。原件我弄丢了。」她的声音很稳，「但这一滴，我在验收单上签字。认。」")
label ch3_omote2_0007:
    $ script_say("ch3_omote2:0007", None, "顿了顿，她补一句：")
label ch3_omote2_0008:
    $ script_say("ch3_omote2:0008", CHAR_YAYOI, "「顺便，你虹膜边上挂着张哭丧脸。让他笑一个再还我。」")
    $ PlaySession.advance_replay()
    jump ch3_ura2

label ch3_ura2:
    $ PlaySession.on_node_reached("ch3_ura2")
    $ PlaySession.apply_style("ura")
    $ script_restore_visuals("ch3_ura2")
label ch3_ura2_0001:
    $ script_say("ch3_ura2:0001", None, "第十夜")
label ch3_ura2_0002:
    $ script_say("ch3_ura2:0002", None, "他今天只坐了七分钟。第七分钟他站起来，膝盖响了一声。")
label ch3_ura2_0003:
    $ script_say("ch3_ura2:0003", None, "他走后，我对着门说了一句话。声音小得连我自己都想赖账。")
label ch3_ura2_0004:
    $ script_say("ch3_ura2:0004", None, "全文如下——")
label ch3_ura2_0005:
    $ script_say("ch3_ura2:0005", None, "「眼睛，再借我一年。利息随你开。」")
label ch3_ura2_0006:
    $ script_say("ch3_ura2:0006", None, "如今催款单到了。利息我点过了：黄，蓝，绿，以及今天下午的粉，四分之三。")
label ch3_ura2_0007:
    $ script_say("ch3_ura2:0007", None, "剩下的四分之一，不在单子上。")
label ch3_ura2_0008:
    $ script_say("ch3_ura2:0008", None, "我查了合同。它早被转存了，活期。")
label ch3_ura2_0009:
    $ script_say("ch3_ura2:0009", None, "户名：他。")
label ch3_ura2_0010:
    $ script_say("ch3_ura2:0010", None, "附页")
label ch3_ura2_0011:
    $ script_say("ch3_ura2:0011", None, "他的转述是乐谱。乐谱不是音乐，这是事实。")
label ch3_ura2_0012:
    $ script_say("ch3_ura2:0012", None, "可贝多芬没退票。我也不退。")
    $ PlaySession.advance_replay()
    jump ch3_omote3

label ch3_omote3:
    $ PlaySession.on_node_reached("ch3_omote3")
    $ PlaySession.apply_style("omote")
    $ script_restore_visuals("ch3_omote3")
    # 【场景：手术日·医院】
label ch3_omote3_0001:
    $ script_say("ch3_omote3:0001", None, "手术前，我在楼梯间把脸洗了三遍。凉水。让红退下去，让手学会不动。")
label ch3_omote3_0002:
    $ script_say("ch3_omote3:0002", None, "推床到了门口。她两指捏住我的袖口——")
label ch3_omote3_0003:
    $ script_say("ch3_omote3:0003", None, "然后攥住了。")
label ch3_omote3_0004:
    $ script_say("ch3_omote3:0004", None, "攥住，是「停」。这套电码里唯一用得上力气的一条。她什么也没说，就那么攥着，三秒，五秒。我把自己的心跳调成秒针，陪她走完这三格。")
label ch3_omote3_0005:
    $ script_say("ch3_omote3:0005", None, "她松手，指钩在我袖口多挂了一瞬，才收回去。")
label ch3_omote3_0006:
    $ script_say("ch3_omote3:0006", CHAR_YAYOI, "「你脸洗过了。」躺上推床前，她忽然说，「水是凉的。」")
label ch3_omote3_0007:
    $ script_say("ch3_omote3:0007", None, "她把一样东西塞进我怀里。旧笔记本，牛皮纸包着。")
label ch3_omote3_0008:
    $ script_say("ch3_omote3:0008", CHAR_YAYOI, "「结束后再拆。念给我听，差一个字我都听得出来。」")
    # 【SE：门，轻轻合上。】
label ch3_omote3_0009:
    $ script_say("ch3_omote3:0009", None, "和上一次那扇门，是同一种声音。")
    $ PlaySession.advance_replay()
    jump ch3_black

label ch3_black:
    $ PlaySession.on_node_reached("ch3_black")
    $ PlaySession.apply_style("ura")
    $ script_restore_visuals("ch3_black")
    # 【画面：黑】
    # 【BGM：无】
label ch3_black_0001:
    $ script_say("ch3_black:0001", None, "（黑屏不是没有画面。")
label ch3_black_0002:
    $ script_say("ch3_black:0002", None, "黑屏，是她的画面。）")
label ch3_black_0003:
    $ script_say("ch3_black:0003", None, "……")
label ch3_black_0004:
    $ script_say("ch3_black:0004", None, "麻药退去的时候，我先听见了海。")
label ch3_black_0005:
    $ script_say("ch3_black:0005", None, "不是海。是自己的呼吸。")
label ch3_black_0006:
    $ script_say("ch3_black:0006", None, "世界瘦成一条走廊，走廊瘦成一根声带。")
label ch3_black_0007:
    $ script_say("ch3_black:0007", None, "「还在？」我问。")
label ch3_black_0008:
    $ script_say("ch3_black:0008", CHAR_HE, "「在。」他说。")
label ch3_black_0009:
    $ script_say("ch3_black:0009", None, "他的声音，大约四十瓦。够用。")
label ch3_black_0010:
    $ script_say("ch3_black:0010", None, "第五天，我数清了走廊：十七步一扇门，和预习的分毫不差。世界没有骗我，它只是换了频道。")
label ch3_black_0011:
    $ script_say("ch3_black:0011", None, "现在，我见过最粉的东西，是草莓牛奶。护士不信。")
label ch3_black_0012:
    $ script_say("ch3_black:0012", None, "信不信，舌头说了算。")
    # 【CG：黑·一粒粉】白图，不做像素点
    $ PlaySession.on_cg_shown("cg_black_pink")
    $ renpy.scene()
    $ renpy.show("cg_black_pink")
label ch3_black_0013:
    $ script_say("ch3_black:0013", None, "（他描述到满开的那一晚，黑屏正中，亮起一个像素点。")
label ch3_black_0014:
    $ script_say("ch3_black:0014", None, "她说：那一粒，就是全部。")
label ch3_black_0015:
    $ script_say("ch3_black:0015", None, "我说：那今年的盛开，是省着开的。")
label ch3_black_0016:
    $ script_say("ch3_black:0016", None, "她说：不。是攒着开的。）")
    $ PlaySession.advance_replay()
    jump ch3_ura3

label ch3_ura3:
    $ PlaySession.on_node_reached("ch3_ura3")
    $ PlaySession.apply_style("ura")
    $ script_restore_visuals("ch3_ura3")
label ch3_ura3_0001:
    $ script_say("ch3_ura3:0001", None, "第七夜，我拆开牛皮纸。")
label ch3_ura3_0002:
    $ script_say("ch3_ura3:0002", None, "前半本是库存，是利息，是预习。翻到后半，纸的脾气忽然变了。没有日期，没有颜色。取而代之的是——")
    # 【场景：旧校舍后·樱树】
    # 【BGM：钢琴独奏《四月，未命名的树》】
    $ PlaySession.run_choice_display(COPY_CHOICE_CH3_URA3, COPY_CHOICE_CH3_URA3)
label ch3_ura3_0003:
    $ script_say("ch3_ura3:0003", None, "我的手指停在纸上。这套记号，我认得。")
label ch3_ura3_0004:
    $ script_say("ch3_ura3:0004", None, "这个游戏，从头到尾，用的就是这套记号。")
label ch3_ura3_0005:
    $ script_say("ch3_ura3:0005", None, "扉页背面，一行小字：")
label ch3_ura3_0006:
    $ script_say("ch3_ura3:0006", None, "《四月，未命名的树》——脚本。作者：弥生。")
label ch3_ura3_0007:
    $ script_say("ch3_ura3:0007", None, "连表和里的顺序，连「我」的心里话，连「什么时候让读者读到什么」——都排好了。原来这条时间线本身，就是她的台词。")
label ch3_ura3_0008:
    $ script_say("ch3_ura3:0008", None, "「未命名」不是没来得及取名。是她不肯。有些东西一旦命名，就只属于某一个人。她要让这棵树，永远属于所有四月。")
label ch3_ura3_0009:
    $ script_say("ch3_ura3:0009", None, "最后一页，字迹换了支笔，用力许多：")
label ch3_ura3_0010:
    $ script_say("ch3_ura3:0010", None, "写在最后，致玩家：")
label ch3_ura3_0011:
    $ script_say("ch3_ura3:0011", None, "你翻到这里，大概全明白了。选项是假的，BGM是我挑的，「他」的心里话，一半是我猜的。抱歉。「存在即被感知」——我只是想知道，被人看着的时候，我到底是什么形状。只好亲自动手。")
label ch3_ura3_0012:
    $ script_say("ch3_ura3:0012", None, "现在，新的人来了。")
label ch3_ura3_0013:
    $ script_say("ch3_ura3:0013", None, "规则不变：花期，是观看者的耐力比赛。神明必须一直看着。一个神明不够用。")
label ch3_ura3_0014:
    $ script_say("ch3_ura3:0014", None, "所以——你好。工资是四月，日结。不许旷工，不许代哭。")
label ch3_ura3_0015:
    $ script_say("ch3_ura3:0015", None, "按「结束」也不要紧。被感知过的，灭不掉。这是他的歪理，我盖过章了。")
label ch3_ura3_0016:
    $ script_say("ch3_ura3:0016", None, "那么，关掉我之后：")
label ch3_ura3_0017:
    $ script_say("ch3_ura3:0017", None, "回到你自己的四月去。那里总有个没被好好看过的家伙，等你看到盛开。")
label ch3_ura3_0018:
    $ script_say("ch3_ura3:0018", None, "轮到你了。")
    $ PlaySession.advance_replay()
    jump ch3_omote5

label ch3_omote5:
    $ PlaySession.on_node_reached("ch3_omote5")
    $ PlaySession.apply_style("omote")
    $ script_restore_visuals("ch3_omote5")
    # 【场景：第九个春天·坡道→樱树下】
    # 【BGM：《四月，未命名的树》（钢琴，极慢）】
label ch3_omote5_0001:
    $ script_say("ch3_omote5:0001", None, "第九个春天。她拄着白杖，自己走上坡道。")
label ch3_omote5_0002:
    $ script_say("ch3_omote5:0002", None, "这条坡，四十一块石板，第三十块会响。她踩上去的时候，我在树下数完了最后一次心跳。")
label ch3_omote5_0003:
    $ script_say("ch3_omote5:0003", CHAR_YAYOI, "「站哪儿了？」她问。")
label ch3_omote5_0004:
    $ script_say("ch3_omote5:0004", CHAR_ME, "「正中央。」")
label ch3_omote5_0005:
    $ script_say("ch3_omote5:0005", CHAR_YAYOI, "「验收合格。」她口袋里插着一盒草莓牛奶，吸管咬扁了一半。「上市第九年了，还没褪色。全世界就它守约。」")
label ch3_omote5_0006:
    $ script_say("ch3_omote5:0006", None, "账本摊开。我念：今日晴，东南风二级，满开。你的那一份，一朵不少。")
label ch3_omote5_0007:
    $ script_say("ch3_omote5:0007", CHAR_YAYOI, "「有笔错账。」她说，「前天那场雨，你记成了阴。雨里的花瓣贴着枝，声音是闷的——我那本账上记着呢。用耳朵。」")
label ch3_omote5_0008:
    $ script_say("ch3_omote5:0008", CHAR_ME, "「你那本，记的是什么？」")
label ch3_omote5_0009:
    $ script_say("ch3_omote5:0009", CHAR_YAYOI, "「同一棵树。」她说，「你记借方，我记贷方。春天平账，谁也不欠谁。」")
label ch3_omote5_0010:
    $ script_say("ch3_omote5:0010", None, "风来了。花从顶往底落，像谁倒了一筛子的光。")
label ch3_omote5_0011:
    $ script_say("ch3_omote5:0011", CHAR_YAYOI, "「还在落？」她问。")
label ch3_omote5_0012:
    $ script_say("ch3_omote5:0012", CHAR_ME, "「还在落。」")
label ch3_omote5_0013:
    $ script_say("ch3_omote5:0013", CHAR_YAYOI, "「……我问你，」她忽然说，「今天这一场，和去年那一场，是同一场花吗？」")
label ch3_omote5_0014:
    $ script_say("ch3_omote5:0014", CHAR_ME, "「账上，是。」")
label ch3_omote5_0015:
    $ script_say("ch3_omote5:0015", CHAR_YAYOI, "「账是你记的。」")
label ch3_omote5_0016:
    $ script_say("ch3_omote5:0016", CHAR_ME, "「嗯。」")
label ch3_omote5_0017:
    $ script_say("ch3_omote5:0017", CHAR_YAYOI, "「那就是你说了算？」")
label ch3_omote5_0018:
    $ script_say("ch3_omote5:0018", CHAR_ME, "「不。」我说，「是你认的。」")
label ch3_omote5_0019:
    $ script_say("ch3_omote5:0019", None, "她想了很久。久到新的一阵花瓣落满了她的肩。")
label ch3_omote5_0020:
    $ script_say("ch3_omote5:0020", CHAR_YAYOI, "「……我认。」")
label ch3_omote5_0021:
    $ script_say("ch3_omote5:0021", None, "这本账没有「结清」那一栏。挺好。")
label ch3_omote5_0022:
    $ script_say("ch3_omote5:0022", None, "没结清，就得一直对账。")
label ch3_omote5_0023:
    $ script_say("ch3_omote5:0023", None, "一直对账，就得一直见面。")
    # ▎升华（无独立节点）
label ch3_omote5_0024:
    $ script_say("ch3_omote5:0024", None, "后来，我常常在黄昏想，「盛开」到底是什么。")
label ch3_omote5_0025:
    $ script_say("ch3_omote5:0025", None, "树不知道自己开过。宇宙从不点收春天的货物。无人的山谷里，花开了又落，按宇宙的记账法，那叫「没有发生」。")
label ch3_omote5_0026:
    $ script_say("ch3_omote5:0026", None, "可是只要有一个肯停下脚步的东西，一只眼睛，一段被保存的三十秒，「开过」就被签收了，从此赖不掉。")
label ch3_omote5_0027:
    $ script_say("ch3_omote5:0027", None, "神明未必全能。神明只是不肯走。")
label ch3_omote5_0028:
    $ script_say("ch3_omote5:0028", None, "所谓永恒，不是不灭，是不断有人肯替它记下去。")
label ch3_omote5_0029:
    $ script_say("ch3_omote5:0029", None, "此刻，这棵树开在纸上，开在光里，开在你的眼睛后面。")
label ch3_omote5_0030:
    $ script_say("ch3_omote5:0030", None, "它的第十年，也是你的，这一分钟。")
    $ PlaySession.advance_replay()
    jump ch3_staff

label ch3_staff:
    $ PlaySession.on_node_reached("ch3_staff")
    $ PlaySession.apply_style("omote")
    $ script_restore_visuals("ch3_staff")
    $ _true_picked = None
    # 【STAFF ROLL】与标题「制作名单」不是同一入口
label ch3_staff_0001:
    $ script_say("ch3_staff:0001", None, "脚本：弥生 / 演出：四月 / 校对：他的耳朵 / 原谅：彼此")
    $ _true_picked = PlaySession.run_choice_true()
label ch3_staff_0002:
    if _true_picked is None:
        $ _true_picked = PlaySession.run_choice_true()
    $ script_say("ch3_staff:0002", None, "（这一次，选项是真的。按哪个都对。）")
label ch3_staff_0003:
    $ script_say("ch3_staff:0003", None, "（屏幕暗下去的时候，别难过。那只是放映机在换电池。")
label ch3_staff_0004:
    $ script_say("ch3_staff:0004", None, "黑屏从来不是没有画面：")
label ch3_staff_0005:
    $ script_say("ch3_staff:0005", None, "它是某人画完了，把画笔，递给你。）")
label ch3_staff_0006:
    $ script_say("ch3_staff:0006", None, "（现在，窗外如果正好是春天，请开窗。")
label ch3_staff_0007:
    $ script_say("ch3_staff:0007", None, "如果不是，也无妨。")
label ch3_staff_0008:
    $ script_say("ch3_staff:0008", None, "你的四月，不归我写。")
label ch3_staff_0009:
    $ script_say("ch3_staff:0009", None, "该你了。）")
    # 共同散场之后才分去向；回放 complete 无副作用。
    $ PlaySession.complete_true_choice(_true_picked)
    $ PlaySession.advance_replay()
