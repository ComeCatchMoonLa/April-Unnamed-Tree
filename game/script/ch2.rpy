# 中章全文。BGM/SE 只留标记。每句 label 供 jump_to_line。

label ch2_start:
    $ PlaySession.on_node_reached("ch2_start")
    $ script_restore_visuals("ch2_start")
    # 【BGM：无（静音开场）】
label ch2_start_0001:
    $ script_say("ch2_start:0001", None, "四月八日。花苞鼓了，没开。")
label ch2_start_0002:
    $ script_say("ch2_start:0002", None, "弥生缺席第九天。")
label ch2_start_0003:
    $ script_say("ch2_start:0003", None, "班主任只说“请了一段时间的假”，语气像念天气预报。没人多问，她和谁都不熟，除了我。或者说，除了在她的问题里当过学生的人。")
label ch2_start_0004:
    $ script_say("ch2_start:0004", None, "放学后我照旧绕到后院。树下没人，花苞一粒一粒攥着，像憋了一整个冬天的话。")
label ch2_start_0005:
    $ script_say("ch2_start:0005", None, "今年的樱树，还是去年那一棵吗？")
label ch2_start_0006:
    $ script_say("ch2_start:0006", None, "没有人看，它还会“开”吗？")
label ch2_start_0007:
    $ script_say("ch2_start:0007", None, "我后颈一凉。我在用她的语法想问题。大概从她说“全世界的粉色都画在大脑里”那天起，我眼睛里就装了一台她的分机。")
label ch2_start_0008:
    $ script_say("ch2_start:0008", None, "今年最早来看这棵树的两个人：一个看不了，一个不敢看。")
    jump ch2_hospital

label ch2_hospital:
    $ PlaySession.on_node_reached("ch2_hospital")
    $ script_restore_visuals("ch2_hospital")
    # 【BGM：弦乐四重奏《探视时间》】
label ch2_hospital_0001:
    $ script_say("ch2_hospital:0001", None, "第十天，我翘了下午的课，拎着便利店最普通的草莓牛奶。上次她说想喝，说完自己先笑了——说这种甜味“只用舌头就能看，多划算”。")
label ch2_hospital_0002:
    $ script_say("ch2_hospital:0002", None, "当时没人听出，这句话是预告片。")
label ch2_hospital_0003:
    $ script_say("ch2_hospital:0003", None, "病房门开着。弥生坐在床上，脸朝着窗，阳光从正面照过来。听见动静，她没回头。")
label ch2_hospital_0004:
    $ script_say("ch2_hospital:0004", CHAR_YAYOI, "「你站在门缝的光里，」她说，「我只能听见你了。」")
label ch2_hospital_0005:
    $ script_say("ch2_hospital:0005", CHAR_ME, "「……什么意思？」")
label ch2_hospital_0006:
    $ script_say("ch2_hospital:0006", CHAR_YAYOI, "「视野缩了。中间还剩一小块，像手机取景框。」她转过脸，冲我晃了晃手里的视力检查表。「医生管这叫‘管状视野’。挺好听，自带剧场效果。」")
label ch2_hospital_0007:
    $ script_say("ch2_hospital:0007", None, "我张了张嘴，什么都没接住。")
label ch2_hospital_0008:
    $ script_say("ch2_hospital:0008", CHAR_YAYOI, "「先说好，探视规则——不准提樱花。」")
label ch2_hospital_0009:
    $ script_say("ch2_hospital:0009", CHAR_ME, "「花苞已经，」")
label ch2_hospital_0010:
    $ script_say("ch2_hospital:0010", CHAR_YAYOI, "「说了不准提。」她把吸管咬扁。「你每说一次，它就从『还没看』变成『看过了』。我亏一次。」")
label ch2_hospital_0011:
    $ script_say("ch2_hospital:0011", CHAR_ME, "「我不是来让你亏的。」")
label ch2_hospital_0012:
    $ script_say("ch2_hospital:0012", CHAR_YAYOI, "「那来干嘛？对账？」她笑了一下，很轻，落地就碎。「反正医生说，先没的是边上，再是夜里。最后……他没说最后。你自己查吧，查完也别告诉我。」")
label ch2_hospital_0013:
    $ script_say("ch2_hospital:0013", None, "那天的探视一共七分钟。是我先站起来的。")
    # 【SE：门轻轻合上】
label ch2_hospital_0014:
    $ script_say("ch2_hospital:0014", None, "出门时，我听见她在里面很小声说了句什么。没听清。也许是“慢走”，也许不是。")
    jump ch2_room

label ch2_room:
    $ PlaySession.on_node_reached("ch2_room")
    $ script_restore_visuals("ch2_room")
    # 【BGM：钢琴《反驳练习》】
label ch2_room_0001:
    $ script_say("ch2_room:0001", None, "睡不着。我把她这一年教我的东西全摆出来，一条一条，像拆弹。")
label ch2_room_0002:
    $ script_say("ch2_room:0002", None, "第一条：花瓣只负责寄信，拆信的是大脑。")
label ch2_room_0003:
    $ script_say("ch2_room:0003", None, "——那语言就是转寄。信到她手里皱一点，可邮戳还是今年的。转述不是赝品，是转寄。")
label ch2_room_0004:
    $ script_say("ch2_room:0004", None, "第二条：我们看到的一直是“刚才的樱花”，眼睛也永远迟到。")
label ch2_room_0005:
    $ script_say("ch2_room:0005", None, "——那她视网膜里那点残存视野，一样迟到。大家都迟到，凭什么她的迟到叫原版，我的转寄叫赝品？")
label ch2_room_0006:
    $ script_say("ch2_room:0006", None, "第三条：花期不是樱花的属性，是观看者的耐力比赛。")
label ch2_room_0007:
    $ script_say("ch2_room:0007", None, "这条不用反驳。这条是她答题时手滑，留的活口。")
    jump ch2_choice

label ch2_choice:
    $ PlaySession.on_node_reached("ch2_choice")
    $ script_restore_visuals("ch2_choice")
label ch2_choice_0001:
    $ script_say("ch2_choice:0001", None, "我坐起来。窗外没有月亮。樱花，就这几天。")
    $ PlaySession.run_choice_display(COPY_CHOICE_CH2_LEFT, COPY_CHOICE_CH2_RIGHT)
label ch2_choice_0002:
    $ script_say("ch2_choice:0002", None, "（两个按钮都亮着。我盯着看了很久，忽然想笑。")
label ch2_choice_0003:
    $ script_say("ch2_choice:0003", None, "这个游戏到今天还在维持它体面的假象——好像真的有得选。")
label ch2_choice_0004:
    $ script_say("ch2_choice:0004", None, "可是从她把“盛开”交给我保管那天起，")
label ch2_choice_0005:
    $ script_say("ch2_choice:0005", None, "剧本就已经换了作者。）")
label ch2_choice_0006:
    $ script_say("ch2_choice:0006", None, "（我哪个都没按。我按灭屏幕，在黑暗里听见了站起来的声音。）")
    jump ch2_fullbloom

label ch2_fullbloom:
    $ PlaySession.on_node_reached("ch2_fullbloom")
    $ PlaySession.on_cg_shown("cg_fullbloom_backlight")
    $ script_restore_visuals("ch2_fullbloom")
label ch2_fullbloom_0001:
    $ script_say("ch2_fullbloom:0001", None, "第十四天，十年一遇的满开。")
label ch2_fullbloom_0002:
    $ script_say("ch2_fullbloom:0002", None, "我没去树下。我去了医院，把她的外套塞进她怀里。")
label ch2_fullbloom_0003:
    $ script_say("ch2_fullbloom:0003", CHAR_YAYOI, "「我说了不准，」")
label ch2_fullbloom_0004:
    $ script_say("ch2_fullbloom:0004", CHAR_ME, "「规则作废。今天我出题。」")
label ch2_fullbloom_0005:
    $ script_say("ch2_fullbloom:0005", CHAR_YAYOI, "「你算老几？」")
label ch2_fullbloom_0006:
    $ script_say("ch2_fullbloom:0006", CHAR_ME, "「观看者。」我说，「你亲口定的，花期是观看者的耐力比赛。你弃赛，只好我替你跑。」")
label ch2_fullbloom_0007:
    $ script_say("ch2_fullbloom:0007", None, "她抱着外套，很久没动。走廊尽头的窗白得晃眼。")
label ch2_fullbloom_0008:
    $ script_say("ch2_fullbloom:0008", CHAR_YAYOI, "「……路我说好了，」她的声音忽然矮下去，「你挽着我。别让护士看见，看见要登记的。」")
label ch2_fullbloom_0009:
    $ script_say("ch2_fullbloom:0009", None, "路上她一直很安静。路过花坛，她停了半秒——取景框里那一小块，大概正停在一朵郁金香上。她没说话，我也没出声。有些东西，看见了就别惊动它。")
label ch2_fullbloom_0010:
    $ script_say("ch2_fullbloom:0010", None, "树下很亮。她仰起脸。")
label ch2_fullbloom_0011:
    $ script_say("ch2_fullbloom:0011", CHAR_ME, "「怎么样？」")
label ch2_fullbloom_0012:
    $ script_say("ch2_fullbloom:0012", CHAR_YAYOI, "「很挤。」她说，「粉色全往取景框外面漏。以前是花在里面、世界在外面，现在中间只有一小块是『我的』。……贪婪吧。明明只剩这么点，还想全要。」")
label ch2_fullbloom_0013:
    $ script_say("ch2_fullbloom:0013", CHAR_ME, "「那就全给你。」我说，「贝克莱怕‘闭上眼世界就消失’，你猜他怎么办？他搬了个上帝，说神永远替所有人看着。我不搬上帝，太远，而且神明才没空替你看樱花。」")
label ch2_fullbloom_0014:
    $ script_say("ch2_fullbloom:0014", CHAR_YAYOI, "「那你想，」")
label ch2_fullbloom_0015:
    $ script_say("ch2_fullbloom:0015", CHAR_ME, "「我搬我自己。」")
label ch2_fullbloom_0016:
    $ script_say("ch2_fullbloom:0016", None, "她的表情第一次裂开。不是被逗笑的裂法。")
label ch2_fullbloom_0017:
    $ script_say("ch2_fullbloom:0017", CHAR_YAYOI, "「不行。转述的不算。」她说得很快。「你说的粉和你眼睛的粉，本来就是两种粉。私人订制，概不通兑。我收了，也只收到一张赝品。」")
label ch2_fullbloom_0018:
    $ script_say("ch2_fullbloom:0018", CHAR_ME, "「那你的原版呢？！」")
label ch2_fullbloom_0019:
    $ script_say("ch2_fullbloom:0019", None, "我的声音在院子里炸开，惊起两只鸟。")
label ch2_fullbloom_0020:
    $ script_say("ch2_fullbloom:0020", CHAR_ME, "「你自己说的，全世界的粉色都画在大脑里——那你取景框里那点颜色，是大脑拿旧墨水补的画！你的原版去年就停产了！大家都在迟到，大家都在补画，凭什么你是原版，我是赝品？！」")
label ch2_fullbloom_0021:
    $ script_say("ch2_fullbloom:0021", CHAR_YAYOI, "「因为我看得见，」")
label ch2_fullbloom_0022:
    $ script_say("ch2_fullbloom:0022", CHAR_ME, "「你看得见多少？！」")
    # 【SE：风，停了。】
label ch2_fullbloom_0023:
    $ script_say("ch2_fullbloom:0023", None, "死寂。静得能听见花瓣离开花梗的声音。")
label ch2_fullbloom_0024:
    $ script_say("ch2_fullbloom:0024", None, "她慢慢坐下去，坐在树根隆起的地方，像被抽掉了一个零件。")
label ch2_fullbloom_0025:
    $ script_say("ch2_fullbloom:0025", CHAR_YAYOI, "「……我怕的不是黑。」每个字都像从取景框最边上抠出来的。「黑我可以背下来。哪级台阶，哪棵树，哪段坡。我怕的是，我这边的灯灭了以后，你们那边的樱花，连『亮过』都不算了。」")
label ch2_fullbloom_0026:
    $ script_say("ch2_fullbloom:0026", None, "她仰起头。取景框里第一次有了水光。")
label ch2_fullbloom_0027:
    $ script_say("ch2_fullbloom:0027", CHAR_YAYOI, "「存在就是被感知，对吧。那我这个感知者一注销，去年的满开、前年的、我们在树下说的废话，是不是就等于，没开过？」")
label ch2_fullbloom_0028:
    $ script_say("ch2_fullbloom:0028", None, "我在她旁边坐下。树根硌人，谁也没挪。")
label ch2_fullbloom_0029:
    $ script_say("ch2_fullbloom:0029", CHAR_ME, "「不会被注销。去年那场花开过了，它落进过你的眼睛、画进过你的大脑，它就『发生』了。发生的事，不会因为放映机坏了就退回没发生。」我深吸一口气。「贝克莱漏了一条：被感知过，和正在被感知，是两种存在。后一种会灭。前一种，灭不掉。」")
label ch2_fullbloom_0030:
    $ script_say("ch2_fullbloom:0030", CHAR_YAYOI, "「……什么歪理。」")
label ch2_fullbloom_0031:
    $ script_say("ch2_fullbloom:0031", CHAR_ME, "「你的歪理，我现学的。老师名下，不许有歪理流失。」")
label ch2_fullbloom_0032:
    $ script_say("ch2_fullbloom:0032", None, "她愣了几秒，忽然笑出声。笑着笑着，眼泪砸在树根上，砸出很小的坑。")
label ch2_fullbloom_0033:
    $ script_say("ch2_fullbloom:0033", CHAR_YAYOI, "「狡猾。」她说，「这种话由你说出来，就像撒娇。」")
label ch2_fullbloom_0034:
    $ script_say("ch2_fullbloom:0034", None, "去年我就在心里这么说过她。原来这句词，谁用都一样。")
    # 【BGM：《四月，未命名的树》（副歌）】
label ch2_fullbloom_0035:
    $ script_say("ch2_fullbloom:0035", CHAR_ME, "「所以。」我伸出手，掌心向上，摆进她取景框正中央。「花期，轮到我的耐力比赛了。」")
label ch2_fullbloom_0036:
    $ script_say("ch2_fullbloom:0036", CHAR_ME, "「你眼睛里的份额，赊给我保管。我看一次，记一次；忘了，就再去看。今年替你看，明年替你看，往后每一场满开，我一朵一朵给你记账。」")
label ch2_fullbloom_0037:
    $ script_say("ch2_fullbloom:0037", CHAR_YAYOI, "「赝品呢？」她小声说，「你保证得了是原版吗？」")
label ch2_fullbloom_0038:
    $ script_say("ch2_fullbloom:0038", CHAR_ME, "「保证不了。这世上本来就没有两个人看过同一种粉。你要的那版原版，在我认识你之前就绝版了。」")
label ch2_fullbloom_0039:
    $ script_say("ch2_fullbloom:0039", CHAR_YAYOI, "「那我图什么？」")
label ch2_fullbloom_0040:
    $ script_say("ch2_fullbloom:0040", CHAR_ME, "「图绝版。」我说，「绝版的才值钱。」")
label ch2_fullbloom_0041:
    $ script_say("ch2_fullbloom:0041", None, "她把手放上来。很轻，像一片花瓣自己挑了个落脚点。")
label ch2_fullbloom_0042:
    $ script_say("ch2_fullbloom:0042", None, "那天下午，我给她描述今年的满开。她说形容词免了，“那是滤镜。说实事。”")
label ch2_fullbloom_0043:
    $ script_say("ch2_fullbloom:0043", None, "于是我说：东边第三根枝是去年锯掉枯枝后新发的，今年的花是头一茬，开得最疯，太阳一穿就透，粉里透着一点没道理的白。我说：风从操场那边来时，整棵树先晃后落，从顶往底，像谁倒了一筛子的光。我说：有一片落在你手背上了。现在还没走。")
label ch2_fullbloom_0044:
    $ script_say("ch2_fullbloom:0044", None, "她一动不动地听。忽然说：")
label ch2_fullbloom_0045:
    $ script_say("ch2_fullbloom:0045", CHAR_YAYOI, "「别说了。」")
label ch2_fullbloom_0046:
    $ script_say("ch2_fullbloom:0046", CHAR_ME, "「……停哪了？」")
label ch2_fullbloom_0047:
    $ script_say("ch2_fullbloom:0047", CHAR_YAYOI, "「停这儿挺好。」她把手背翻过来，花瓣还在。「剩下的留到明年。转寄太满，会腻。」")
    # 【SE：风。花落。】
label ch2_fullbloom_0048:
    $ script_say("ch2_fullbloom:0048", None, "很久之后，她开口，轻得像自言自语：")
label ch2_fullbloom_0049:
    $ script_say("ch2_fullbloom:0049", CHAR_YAYOI, "「……今年的，比去年淡。」")
label ch2_fullbloom_0050:
    $ script_say("ch2_fullbloom:0050", None, "我心口一紧。我没说过淡，一个字都没说。")
label ch2_fullbloom_0051:
    $ script_say("ch2_fullbloom:0051", None, "是她那一小块取景框真的在掉色，还是她的大脑，已经开始拿旧墨水补画新信？")
label ch2_fullbloom_0052:
    $ script_say("ch2_fullbloom:0052", None, "我不知道。也许连她自己也不知道。")
label ch2_fullbloom_0053:
    $ script_say("ch2_fullbloom:0053", CHAR_YAYOI, "「不许问。」她抢在我前面，唇角翘着。「有些验收结果，一问出口，作废。」")
label ch2_fullbloom_0054:
    $ script_say("ch2_fullbloom:0054", None, "我闭嘴。花继续落。")
label ch2_fullbloom_0055:
    $ script_say("ch2_fullbloom:0055", CHAR_YAYOI, "「……还在落？」她问。")
label ch2_fullbloom_0056:
    $ script_say("ch2_fullbloom:0056", CHAR_ME, "「还在落。」")
label ch2_fullbloom_0057:
    $ script_say("ch2_fullbloom:0057", CHAR_YAYOI, "「那就好。」她把手背上那片花瓣拈起来，举高，举进她那一小块天空里。")
label ch2_fullbloom_0058:
    $ script_say("ch2_fullbloom:0058", CHAR_YAYOI, "「落着，就说明还开着。」")
label ch2_fullbloom_0059:
    $ script_say("ch2_fullbloom:0059", None, "这句话算不算“看见”，我没问，她也没说。")
label ch2_fullbloom_0060:
    $ script_say("ch2_fullbloom:0060", None, "这个问题，大概会活得比我们两个都久。")
label ch2_fullbloom_0061:
    $ script_say("ch2_fullbloom:0061", None, "而那棵换过新枝的树站在暮色里，明天照样开它的花。它不会回答任何人。")
label ch2_fullbloom_0062:
    $ script_say("ch2_fullbloom:0062", None, "只是从此以后，每年四月，人群里会有一个人看得特别用力——")
label ch2_fullbloom_0063:
    $ script_say("ch2_fullbloom:0063", None, "像替两个人看。")
    $ PlaySession.advance_replay()
    jump ch3_ledger
