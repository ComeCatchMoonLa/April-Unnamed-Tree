# 后日谈全文。BGM/SE 只留标记。每句 label 供 jump_to_line。

label after_start:
    $ PlaySession.on_node_reached("after_start")
    $ script_restore_visuals("after_start")
    # 【场景：公寓·周日早晨】
    # 【BGM：无。环境音：味噌汤的咕嘟声】
label after_start_0001:
    $ script_say("after_start:0001", None, "厨房里菜刀碰到砧板，笃、笃、笃，节奏很稳。")
label after_start_0002:
    $ script_say("after_start:0002", None, "他负责搅汤，她负责切东西。这套分工定下来很多年了，谁也不觉得亏欠谁，吵架的时候除外。")
label after_start_0003:
    $ script_say("after_start:0003", CHAR_HE, "「味噌放多了吧。」")
label after_start_0004:
    $ script_say("after_start:0004", CHAR_YAYOI, "「收音机说今天降温。」她说。意思是：多出来的那勺是给降温准备的，投诉不受理。")
label after_start_0005:
    $ script_say("after_start:0005", None, "他喝了一口。确实咸。他没说第二遍。")
label after_start_0006:
    $ script_say("after_start:0006", CHAR_HE, "「今天干什么？」")
label after_start_0007:
    $ script_say("after_start:0007", CHAR_YAYOI, "「找缴费单。你上次乱塞的那个抽屉。」")
label after_start_0008:
    $ script_say("after_start:0008", CHAR_HE, "「我什么时候乱塞，」")
label after_start_0009:
    $ script_say("after_start:0009", CHAR_HE, "「从哲学上讲，」")
label after_start_0010:
    $ script_say("after_start:0010", CHAR_YAYOI, "「禁令。」她说。")
label after_start_0011:
    $ script_say("after_start:0011", CHAR_HE, "「这条禁令执行六年了。」")
label after_start_0012:
    $ script_say("after_start:0012", CHAR_YAYOI, "「有效期内。」")
    # 【SE：纸袋窸窣】
label after_start_0013:
    $ script_say("after_start:0013", None, "信摊在餐桌上，他念给她听，这是规矩：水道费要涨，健身房传单，区民合唱团招募。")
label after_start_0014:
    $ script_say("after_start:0014", None, "然后是市役所的信。牛皮纸，很厚。")
label after_start_0015:
    $ script_say("after_start:0015", CHAR_HE, "「关于旧校舍樱树的老化与更新计划。因树龄逾五十年，根系……拟于近年，」")
label after_start_0016:
    $ script_say("after_start:0016", CHAR_YAYOI, "「跳过。」她说，「念吃的。」")
label after_start_0017:
    $ script_say("after_start:0017", None, "他把那张纸对折，又对折，塞进单据堆的最底下。")
label after_start_0018:
    $ script_say("after_start:0018", None, "压得很实。")
label after_start_0019:
    $ script_say("after_start:0019", None, "窗外的风把健身房传单吹得哗啦响。这件事，谁也没有再提。")
    # 【SE：抽屉、纸箱】
label after_start_0020:
    $ script_say("after_start:0020", None, "缴费单没找着。找出来一箱她学生时代的东西。最上面，牛皮纸包着一个本子，边角磨圆了。")
label after_start_0021:
    $ script_say("after_start:0021", CHAR_YAYOI, "「……那个啊。」她的手停了半拍，不注意就看不出。「扔了吧。」")
label after_start_0022:
    $ script_say("after_start:0022", CHAR_HE, "「里面是什么？」")
label after_start_0023:
    $ script_say("after_start:0023", CHAR_YAYOI, "「失败的实验记录。」")
label after_start_0024:
    $ script_say("after_start:0024", CHAR_HE, "「扔之前，」他解开牛皮纸，「验收一下？」")
label after_start_0025:
    $ script_say("after_start:0025", None, "她想了想，在椅子上坐正，像坐进很多年前的探视室。")
label after_start_0026:
    $ script_say("after_start:0026", CHAR_YAYOI, "「念。念错一个字我都听得出来。」")
    $ PlaySession.advance_replay()
    jump after_read

label after_read:
    $ PlaySession.on_node_reached("after_read")
    $ script_restore_visuals("after_read")
    # 【场景：餐桌·朗读】
    # 【BGM：无】
label after_read_0001:
    $ script_say("after_read:0001", None, "本子前半本，他认得那些记号。【场景】【BGM】【CG】。他人生里的一段，被另一个人拆成了脚本。")
label after_read_0002:
    $ script_say("after_read:0002", None, "页边全是补记。")
label after_read_0003:
    $ script_say("after_read:0003", None, "她写：「此处他应沉默三秒，然后给出漂亮的反驳。」")
label after_read_0004:
    $ script_say("after_read:0004", None, "页边小字：「实际：没沉默。打了个喷嚏。可恶。」")
label after_read_0005:
    $ script_say("after_read:0005", None, "她写：「他大概会生气。」")
label after_read_0006:
    $ script_say("after_read:0006", None, "页边：「判断失误。此人比我写的要好。」")
label after_read_0007:
    $ script_say("after_read:0007", CHAR_HE, "「我没这么说话。」他抗议。")
label after_read_0008:
    $ script_say("after_read:0008", CHAR_YAYOI, "「你就是这么说话的。」她把汤碗往他那边推了推，「我只是把废话删了。」")
label after_read_0009:
    $ script_say("after_read:0009", None, "翻页的手停住了。")
label after_read_0010:
    $ script_say("after_read:0010", None, "那一页只有一行对白，是他的声音：")
label after_read_0011:
    $ script_say("after_read:0011", None, "（他会说：「我喜欢你。」）")
label after_read_0012:
    $ script_say("after_read:0012", None, "四个字被一道铅笔线划掉。划得很用力，纸都快破了。页边补记：")
label after_read_0013:
    $ script_say("after_read:0013", None, "「编的。他没说过。一遍也没有。」")
label after_read_0014:
    $ script_say("after_read:0014", CHAR_HE, "「这页划掉了。」他说。")
label after_read_0015:
    $ script_say("after_read:0015", CHAR_YAYOI, "「划掉了也念。反正要扔了。」")
label after_read_0016:
    $ script_say("after_read:0016", None, "他念了一遍。平平的，像念别人的台词。")
    # 【SE：胶带撕开的声音，停了。】
label after_read_0017:
    $ script_say("after_read:0017", None, "厨房方向没有动静。冰箱的电流声忽然变得很大。")
label after_read_0018:
    $ script_say("after_read:0018", CHAR_YAYOI, "「语气不对。」她说。")
label after_read_0019:
    $ script_say("after_read:0019", CHAR_HE, "「他没说过这句话，哪来的对错。」")
label after_read_0020:
    $ script_say("after_read:0020", CHAR_YAYOI, "「没说过，才有对错。」她停了停。「念下一个吧。」")
label after_read_0021:
    $ script_say("after_read:0021", None, "他没念下一个。")
label after_read_0022:
    $ script_say("after_read:0022", None, "他清了清嗓子，把那一行重新念了一遍。这回不像念稿。像一件迟交了很多年的作业。")
label after_read_0023:
    $ script_say("after_read:0023", None, "他念的时候，拇指一直摩挲着这页的右下角。")
label after_read_0024:
    $ script_say("after_read:0024", None, "那个纸角是软的，起了毛。")
label after_read_0025:
    $ script_say("after_read:0025", None, "被同一根拇指，翻过很多很多次。")
label after_read_0026:
    $ script_say("after_read:0026", None, "她看不见这个。")
label after_read_0027:
    $ script_say("after_read:0027", None, "很久，胶带的声音都没有响起来。")
label after_read_0028:
    $ script_say("after_read:0028", CHAR_YAYOI, "「……过。」她说，「就这条过。」")
label after_read_0029:
    $ script_say("after_read:0029", CHAR_HE, "「就一条？」")
label after_read_0030:
    $ script_say("after_read:0030", CHAR_YAYOI, "「其余项目，」她说，「全部作废。」")
label after_read_0031:
    $ script_say("after_read:0031", None, "本子往后翻，全是空白。最后一页什么都没有，只夹着一支铅笔，笔杆的漆被咬掉了一小块。")
label after_read_0032:
    $ script_say("after_read:0032", CHAR_HE, "「后面怎么没了？」")
label after_read_0033:
    $ script_say("after_read:0033", CHAR_YAYOI, "「写不动了。」她站起来收碗，「水开了，让让。」")
    $ PlaySession.advance_replay()
    jump after_night

label after_night:
    $ PlaySession.on_node_reached("after_night")
    $ script_restore_visuals("after_night")
    # 【场景：卧室·夜】
    # 【BGM：无】
label after_night_0001:
    $ script_say("after_night:0001", None, "灯关了。黑下来的第一秒，谁都没说话。这个家的黑夜是她的主场，他从不僭越。")
label after_night_0002:
    $ script_say("after_night:0002", CHAR_YAYOI, "「把本子拿来。」她说。")
label after_night_0003:
    $ script_say("after_night:0003", None, "他摸黑递过去。她翻到最后，抽出那支铅笔。")
label after_night_0004:
    $ script_say("after_night:0004", CHAR_HE, "「你不看得见。」")
label after_night_0005:
    $ script_say("after_night:0005", CHAR_YAYOI, "「现在轮到你说蠢话了。」")
label after_night_0006:
    $ script_say("after_night:0006", None, "他的手伸向床头灯的开关。")
label after_night_0007:
    $ script_say("after_night:0007", CHAR_YAYOI, "「别开。」")
label after_night_0008:
    $ script_say("after_night:0008", None, "指尖停住。黑暗里只有铅笔走在纸上的声音，很慢。一行，只一行。字大概全叠在了一起，像一排淋过雨的人。")
label after_night_0009:
    $ script_say("after_night:0009", None, "她合上本子递还给他，把铅笔别回封皮。")
label after_night_0010:
    $ script_say("after_night:0010", CHAR_HE, "「写了什么？」")
label after_night_0011:
    $ script_say("after_night:0011", CHAR_YAYOI, "「验收结果。」她躺下来，拉了拉被子，「睡了。」")
label after_night_0012:
    $ script_say("after_night:0012", None, "那行字从此存在。")
label after_night_0013:
    $ script_say("after_night:0013", None, "写它的人读不了它，收下的人没读过它。")
label after_night_0014:
    $ script_say("after_night:0014", None, "这个家里，它是唯一的原件。")
    $ PlaySession.advance_replay()
    jump after_tree

label after_tree:
    $ PlaySession.on_node_reached("after_tree")
    $ script_restore_visuals("after_tree")
    # 【场景：坡道·樱树】
    # 【BGM：《四月，未命名的树》（极慢，若有若无）】
label after_tree_0001:
    $ script_say("after_tree:0001", None, "第二天他们上了坡。第三十块石板照例响了一声。")
label after_tree_0002:
    $ script_say("after_tree:0002", None, "花已经落完了。满树新叶，绿得乱七八糟，风一过，哗啦哗啦，像很小很碎的掌声。")
label after_tree_0003:
    $ script_say("after_tree:0003", None, "树下站着个一年级的女生，举着手机，对着一棵没有花的树，认认真真地找角度。")
label after_tree_0004:
    $ script_say("after_tree:0004", None, "弥生在十几步外停住，鼻子朝那边偏了偏。")
label after_tree_0005:
    $ script_say("after_tree:0005", CHAR_YAYOI, "「有人？」")
label after_tree_0006:
    $ script_say("after_tree:0006", CHAR_HE, "「有。校服。在拍树。」")
label after_tree_0007:
    $ script_say("after_tree:0007", CHAR_YAYOI, "「花都没了，拍什么？」")
label after_tree_0008:
    $ script_say("after_tree:0008", CHAR_HE, "「拍叶子。」")
label after_tree_0009:
    $ script_say("after_tree:0009", CHAR_YAYOI, "「……哦。」")
label after_tree_0010:
    $ script_say("after_tree:0010", None, "女生发觉有人，朝这边微微欠了欠身，又转回去，继续拍那张绿得毫无道理的照片。")
label after_tree_0011:
    $ script_say("after_tree:0011", CHAR_YAYOI, "「第几年了？」弥生忽然问。")
label after_tree_0012:
    $ script_say("after_tree:0012", CHAR_HE, "「忘了数。」")
label after_tree_0013:
    $ script_say("after_tree:0013", CHAR_YAYOI, "「我也忘了。」她把手插进他外套的口袋。「那正好。谁也不用负责。」")
label after_tree_0014:
    $ script_say("after_tree:0014", None, "回去的路上，她一直走在他左边，让耳朵朝着那棵树的方向。快到家门口，她开口：")
label after_tree_0015:
    $ script_say("after_tree:0015", CHAR_YAYOI, "「晚饭想吃什么？」")
label after_tree_0016:
    $ script_say("after_tree:0016", CHAR_HE, "「都行。别太咸。」")
label after_tree_0017:
    $ script_say("after_tree:0017", CHAR_YAYOI, "「你眉毛又开始了。」")
    # 【SE：门关上】
    # 【画面：黑】不要做黑屏两秒转场
    $ renpy.scene()
    $ renpy.show("bg_black")
label after_tree_0018:
    $ script_say("after_tree:0018", None, "树的那边，风还在响。")
label after_tree_0019:
    $ script_say("after_tree:0019", None, "花要等明年四月才开。开了，会有人来看；")
label after_tree_0020:
    $ script_say("after_tree:0020", None, "落了，现在也正有人看。")
label after_tree_0021:
    $ script_say("after_tree:0021", None, "而标题画面上的那棵树，用的是你机器里的日历。")
label after_tree_0022:
    $ script_say("after_tree:0022", None, "多年以后你再打开，它不会问你去了哪里。")
label after_tree_0023:
    $ script_say("after_tree:0023", None, "它只是接上你离开的那一天，")
label after_tree_0024:
    $ script_say("after_tree:0024", None, "继续开。")
    $ PlaySession.complete_after_chapter()
