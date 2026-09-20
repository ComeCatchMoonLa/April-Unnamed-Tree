# 首章全文。BGM/SE 只留标记。每句 label 供 jump_to_line。

label ch1_start:
    $ PlaySession.on_node_reached("ch1_start")
    $ script_restore_visuals("ch1_start")
    # 【BGM：钢琴独奏《四月，未命名的树》】
label ch1_start_0001:
    $ script_say("ch1_start:0001", None, "传说在这棵樱树下告白的人，一定会成功。")
label ch1_start_0002:
    $ script_say("ch1_start:0002", None, "校史馆的相册里，每一届毕业照都以它为背景。风一吹，粉色的雪就落满整个后院。")
label ch1_start_0003:
    $ script_say("ch1_start:0003", None, "放学后，弥生先到了。她站在树下仰着脸，裙摆被风掀起一个小小的弧度。")
label ch1_start_0004:
    $ script_say("ch1_start:0004", None, "我在三步之外停下。明明只是站着，却像闯进了什么了不得的场所。")
label ch1_start_0005:
    $ script_say("ch1_start:0005", CHAR_YAYOI, "「呐，」她突然开口，没有回头，「你说，今年的樱树，还是去年那一棵吗？」")
label ch1_start_0006:
    $ script_say("ch1_start:0006", CHAR_ME, "「……什么意思？」")
label ch1_start_0007:
    $ script_say("ch1_start:0007", CHAR_YAYOI, "「寒假里，园艺老师把枯枝全锯掉了。今年开花的每一根枝条，都是新的。」她伸出手，一片花瓣恰好停在指尖。「也就是说，我现在摸到的树，和去年在树下告白的那个人摸到的，是两个东西。」")
label ch1_start_0008:
    $ script_say("ch1_start:0008", None, "花瓣从她指尖滑走了。")
label ch1_start_0009:
    $ script_say("ch1_start:0009", CHAR_YAYOI, "「可大家还是叫它『那棵樱树』。校史、毕业照、『树下告白一定会成功』的传说……全都押在这棵明明已经不一样了的树上。」")
label ch1_start_0010:
    $ script_say("ch1_start:0010", None, "我想了想。")
label ch1_start_0011:
    $ script_say("ch1_start:0011", CHAR_ME, "「名字没变吧。树一直在换零件，但『樱树』这个名字，把所有瞬间缝在一起了。」")
label ch1_start_0012:
    $ script_say("ch1_start:0012", CHAR_YAYOI, "「哦——？」她回过头，眼睛亮得有点过分。「那，把名字也拿走呢？」")
label ch1_start_0013:
    $ script_say("ch1_start:0013", CHAR_ME, "「……」")
label ch1_start_0014:
    $ script_say("ch1_start:0014", CHAR_YAYOI, "「没有人喊它的名字，传说里删掉它，毕业照全部烧掉。那明年春天，它还会『开』吗？」")
    # 【SE：风】
label ch1_start_0015:
    $ script_say("ch1_start:0015", None, "整棵树哗啦一声，摇落一阵粉色的雨。")
label ch1_start_0016:
    $ script_say("ch1_start:0016", None, "我忽然明白，她问的根本不是树。")
label ch1_start_0017:
    $ script_say("ch1_start:0017", CHAR_ME, "「会开吧。花该开就开。只是，」")
label ch1_start_0018:
    $ script_say("ch1_start:0018", CHAR_YAYOI, "「只是？」")
label ch1_start_0019:
    $ script_say("ch1_start:0019", CHAR_ME, "「只是没有人的话，『盛开』就没了头尾。开了五天，落了，谁都不知道，那五天就像不存在一样。」")
label ch1_start_0020:
    $ script_say("ch1_start:0020", None, "弥生笑了，是那种夸奖一只终于肯跳上膝盖的猫的笑法。")
label ch1_start_0021:
    $ script_say("ch1_start:0021", CHAR_YAYOI, "「答对一半。你刚才说了『盛开』，却没说『颜色』。你想想，樱花的粉色，其实不在花瓣里哦。」")
label ch1_start_0022:
    $ script_say("ch1_start:0022", CHAR_ME, "「……哈？」")
label ch1_start_0023:
    $ script_say("ch1_start:0023", CHAR_YAYOI, "「花瓣只是一堆反射特定波长的细胞。波长冲进眼睛，视网膜把它翻译成信号，大脑再把它画出来。」她用指尖点了点自己的太阳穴。「全世界的粉色，都画在这里。花瓣只负责寄信，拆信的，是我们。」")
    jump ch1_cg_backlight

label ch1_cg_backlight:
    $ PlaySession.on_node_reached("ch1_cg_backlight")
    $ PlaySession.on_cg_shown("cg_yayoi_backlight")
    $ script_restore_visuals("ch1_cg_backlight")
label ch1_cg_backlight_0001:
    $ script_say("ch1_cg_backlight:0001", CHAR_YAYOI, "「所以这棵树自己，从来不知道自己是粉色的。」")
label ch1_cg_backlight_0002:
    $ script_say("ch1_cg_backlight:0002", None, "我抬头。阳光从花隙间漏下来，每一瓣都被照得半透明。明明是歪理，可我第一次觉得，这满树的粉色像是刚刚才被谁画上去的。")
label ch1_cg_backlight_0003:
    $ script_say("ch1_cg_backlight:0003", CHAR_ME, "「不对吧，」我抓住话缝，「照你这么说，花美不美全看人。那我看不到的背面那些花，不就白开了？」")
label ch1_cg_backlight_0004:
    $ script_say("ch1_cg_backlight:0004", CHAR_YAYOI, "「不是白开，是『还没开始』。」")
label ch1_cg_backlight_0005:
    $ script_say("ch1_cg_backlight:0005", None, "她转过身，背靠着树干。一缕头发被风吹到嘴角，她也不去拨。")
label ch1_cg_backlight_0006:
    $ script_say("ch1_cg_backlight:0006", CHAR_YAYOI, "「再告诉你一件事。光从花瓣跑到眼睛，再被大脑处理完，是需要时间的。虽然只有零点几秒——但严格来说，我们看到的一直是『刚才的樱花』。」")
label ch1_cg_backlight_0007:
    $ script_say("ch1_cg_backlight:0007", CHAR_ME, "「追不上的……『现在』。」")
label ch1_cg_backlight_0008:
    $ script_say("ch1_cg_backlight:0008", CHAR_YAYOI, "「对。你每说一次『真美』，被夸的那朵早就落了。语言永远迟到，眼睛也是。」她微微歪头。「所以在树下的人，一直被『过去』包围着哦。——很浪漫吧？」")
label ch1_cg_backlight_0009:
    $ script_say("ch1_cg_backlight:0009", None, "狡猾。这种话题由她说出来，就像撒娇。")
label ch1_cg_backlight_0010:
    $ script_say("ch1_cg_backlight:0010", CHAR_ME, "「浪漫什么啊。照你说的，全世界都在迟到。」")
label ch1_cg_backlight_0011:
    $ script_say("ch1_cg_backlight:0011", CHAR_YAYOI, "「本来就是这么回事。」她轻轻踢了踢脚下的花瓣。「但我找到了一个漏洞。」")
label ch1_cg_backlight_0012:
    $ script_say("ch1_cg_backlight:0012", CHAR_ME, "「漏洞？」")
label ch1_cg_backlight_0013:
    $ script_say("ch1_cg_backlight:0013", CHAR_YAYOI, "「『盛开』这个词，我想了很久，它不是树的状态，是看的人的状态。花开五天，是树自己的日程表；可『盛开』能持续多久，取决于有没有人一直看着。」")
label ch1_cg_backlight_0014:
    $ script_say("ch1_cg_backlight:0014", None, "弥生抬起手，隔着纷纷扬扬的花瓣，指向我。")
    jump ch1_choice

label ch1_choice:
    $ PlaySession.on_node_reached("ch1_choice")
    $ script_restore_visuals("ch1_choice")
label ch1_choice_0001:
    $ script_say("ch1_choice:0001", CHAR_YAYOI, "「所以花期不是樱花的属性，是观看者的耐力比赛。」")
    $ PlaySession.run_choice_fake(COPY_CHOICE_CH1_LEFT, COPY_CHOICE_CH1_RIGHT)
label ch1_choice_0002:
    $ script_say("ch1_choice:0002", None, "（无论按下哪一个，接下来的演出都相同——")
label ch1_choice_0003:
    $ script_say("ch1_choice:0003", None, "这个游戏从来没给过真正的选项。")
label ch1_choice_0004:
    $ script_say("ch1_choice:0004", None, "所有岔路，最终都通向她。）")
label ch1_choice_0005:
    $ script_say("ch1_choice:0005", None, "弥生收回手，把手掌贴在胸口，像是在确认心跳还在。")
label ch1_choice_0006:
    $ script_say("ch1_choice:0006", CHAR_YAYOI, "「看到我再也睁不开眼睛为止。」")
label ch1_choice_0007:
    $ script_say("ch1_choice:0007", None, "一片花瓣恰好在此时落进我们之间，慢得几乎要在空中停住。")
label ch1_choice_0008:
    $ script_say("ch1_choice:0008", CHAR_YAYOI, "「你说过，粉色是大脑画出来的。那从今天起，」她笑了，眉眼弯起来，「你眼睛里的粉色，就有一半是我了。」")
    jump ch1_cg_blizzard

label ch1_cg_blizzard:
    $ PlaySession.on_node_reached("ch1_cg_blizzard")
    $ PlaySession.on_cg_shown("cg_sakura_blizzard")
    $ script_restore_visuals("ch1_cg_blizzard")
label ch1_cg_blizzard_0001:
    $ script_say("ch1_cg_blizzard:0001", None, "回去的路上，我一直在想，到底是从哪一句开始跑偏的。")
label ch1_cg_blizzard_0002:
    $ script_say("ch1_cg_blizzard:0002", None, "明明在讨论树、名字、波长和迟到的时间。等回过神来，我们已经并排走在回家的坡道上，我的心脏敲得比上课铃还响。")
label ch1_cg_blizzard_0003:
    $ script_say("ch1_cg_blizzard:0003", None, "传说，在樱树下告白的人一定能成功。")
label ch1_cg_blizzard_0004:
    $ script_say("ch1_cg_blizzard:0004", None, "可我们从头到尾，谁也没说那两个字。")
label ch1_cg_blizzard_0005:
    $ script_say("ch1_cg_blizzard:0005", None, "只是互相看着，又被互相看着，把彼此的『盛开』交给了对方保管。")
label ch1_cg_blizzard_0006:
    $ script_say("ch1_cg_blizzard:0006", None, "有位哲学家说过：存在，就是被感知。")
label ch1_cg_blizzard_0007:
    $ script_say("ch1_cg_blizzard:0007", None, "那么今天，在这棵『已经不是去年那棵』的树下——")
label ch1_cg_blizzard_0008:
    $ script_say("ch1_cg_blizzard:0008", None, "至少有一点可以确定：")
label ch1_cg_blizzard_0009:
    $ script_say("ch1_cg_blizzard:0009", None, "我被她看见了。")
label ch1_cg_blizzard_0010:
    $ script_say("ch1_cg_blizzard:0010", None, "所以，今天的我，存在过。")
    $ PlaySession.advance_replay()
    jump ch2_start
