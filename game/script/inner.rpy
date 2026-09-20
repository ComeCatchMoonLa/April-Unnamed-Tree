# 里后日谈全文。旁白为主；他说才标「他」。BGM/SE 只留标记。

label inner_start:
    $ PlaySession.on_node_reached("inner_start")
    $ script_restore_visuals("inner_start")
    # ▎里·一
    # 【场景：厨房】
    # 【BGM：无。本线路不放音乐，音乐现场演奏：刀、汤勺、收音机、冰箱的电流。】
label inner_start_0001:
    $ script_say("inner_start:0001", None, "笃，笃，笃。")
label inner_start_0002:
    $ script_say("inner_start:0002", None, "刀不认识菜，刀认手感。萝卜的抵抗是钝的，姜的抵抗是滑的，今天这种软里带韧的，胡萝卜。切多细不看菜谱，看汤勺：他搅得慢，我就切得慢。他的手一慢，说明昨晚没睡踏实。")
label inner_start_0003:
    $ script_say("inner_start:0003", None, "收音机说降温。不必它说，凌晨被缝那一线凉，皮肤早表决过了。")
label inner_start_0004:
    $ script_say("inner_start:0004", None, "味噌多放了半勺。账面记在降温名下，实际记在另一个人名下，他一冷，话就少，汤倒喝得快。这半勺，是给那个速度备的。")
label inner_start_0005:
    $ script_say("inner_start:0005", CHAR_HE, "「味噌放多了吧。」")
label inner_start_0006:
    $ script_say("inner_start:0006", None, "看，眉毛来了。")
label inner_start_0007:
    $ script_say("inner_start:0007", None, "他的眉毛长在声音里，这件事，我失明后第三年确认的。声音会把脸带出来，「放多了吧」的尾音往上挑半度，眉梢就在那半度里。")
label inner_start_0008:
    $ script_say("inner_start:0008", None, "「收音机说今天降温。」")
label inner_start_0009:
    $ script_say("inner_start:0009", None, "译文：投诉不受理。他都懂，还年年问。这也是他的眉毛之一。")
label inner_start_0010:
    $ script_say("inner_start:0010", CHAR_HE, "「今天干什么？」")
label inner_start_0011:
    $ script_say("inner_start:0011", None, "「找缴费单。你上次乱塞的那个抽屉。」")
label inner_start_0012:
    $ script_say("inner_start:0012", None, "他喊冤。让他喊。")
label inner_start_0013:
    $ script_say("inner_start:0013", None, "那个抽屉，其实是我乱塞的。锅让他背了六年，冤案一桩，他年年上诉，年年懒得走流程。这样的案子我们家还有几件，都判给了岁月。")
label inner_start_0014:
    $ script_say("inner_start:0014", CHAR_HE, "「我什么时候乱塞，」")
label inner_start_0015:
    $ script_say("inner_start:0015", CHAR_HE, "「从哲学上讲——」")
label inner_start_0016:
    $ script_say("inner_start:0016", None, "「禁令。」")
label inner_start_0017:
    $ script_say("inner_start:0017", None, "这条禁令立法于六年前：那一个月，他用这四个字开了三次头，我们家凉了三顿晚饭。立法那天他投过反对票。现在我负责维护法律。")
label inner_start_0018:
    $ script_say("inner_start:0018", CHAR_HE, "「这条禁令执行六年了。」")
label inner_start_0019:
    $ script_say("inner_start:0019", None, "「有效期内。」")
    $ PlaySession.advance_replay()
    jump inner_mail

label inner_mail:
    $ PlaySession.on_node_reached("inner_mail")
    $ script_restore_visuals("inner_mail")
    # ▎里·二
    # 【SE：信封落桌。四封。有一封，落下去的声音比别的厚。】
label inner_mail_0001:
    $ script_say("inner_mail:0001", None, "他念信，是我这几年的广播电台。按规矩来，一个频道都不跳。")
label inner_mail_0002:
    $ script_say("inner_mail:0002", None, "水道费要涨——念得平，这种钱他心里早认了。")
label inner_mail_0003:
    $ script_say("inner_mail:0003", None, "健身房，慢了半拍。有人想办卡，又在算年费。")
label inner_mail_0004:
    $ script_say("inner_mail:0004", None, "区民合唱团，字正腔圆。他在等我笑。")
label inner_mail_0005:
    $ script_say("inner_mail:0005", None, "第四封。牛皮纸，厚。他拆它的手，比拆前三封慢。")
label inner_mail_0006:
    $ script_say("inner_mail:0006", CHAR_HE, "「关于旧校舍樱树的老化与更新计划。因树龄逾五十年，根系……拟于近年，」")
label inner_mail_0007:
    $ script_say("inner_mail:0007", None, "「跳过。」我说，「念吃的。」")
label inner_mail_0008:
    $ script_say("inner_mail:0008", None, "不是怕它。是这句话剩下的部分太长，长到他念完，声音会变。他声音一变，今天就被定了性。我今天不想被定性。")
label inner_mail_0009:
    $ script_say("inner_mail:0009", None, "念出声的东西才算送达。这一封，我要让它停在邮路上。")
label inner_mail_0010:
    $ script_say("inner_mail:0010", None, "他不争。对折，又对折。")
label inner_mail_0011:
    $ script_say("inner_mail:0011", None, "他害怕的时候把纸叠两折，这个毛病我收到第几年，忘了。纸落进单据堆最底下，上面压了厚厚一沓，压得很实——像给一句话捂住了嘴。")
label inner_mail_0012:
    $ script_say("inner_mail:0012", None, "我这边也入账：")
label inner_mail_0013:
    $ script_say("inner_mail:0013", None, "借：一句话，扣在途中。")
label inner_mail_0014:
    $ script_say("inner_mail:0014", None, "贷：两折纸，一份。")
label inner_mail_0015:
    $ script_say("inner_mail:0015", None, "树的事，到此为止。锯枯枝和锯一棵树算不算同一种手续，这道题今天不做。谁也没提。")
label inner_mail_0016:
    $ script_say("inner_mail:0016", None, "风大，就当刮过去了。")
    $ PlaySession.advance_replay()
    jump inner_note

label inner_note:
    $ PlaySession.on_node_reached("inner_note")
    $ script_restore_visuals("inner_note")
    # ▎里·三
    # 【SE：抽屉、纸箱。箱底被压得吱了一声。】
label inner_note_0001:
    $ script_say("inner_note:0001", None, "缴费单还是没找着。找出来一只纸箱，最上面，牛皮纸包着一个本子。不用摸，落桌那一下的轻响就告诉你：纸老得服帖了，边角全圆了。")
label inner_note_0002:
    $ script_say("inner_note:0002", None, "「……那个啊。」")
label inner_note_0003:
    $ script_say("inner_note:0003", None, "手停了半拍。明面上看不出。里子上是在盘点：接下来这句话，什么价钱，今天付不付得起。")
label inner_note_0004:
    $ script_say("inner_note:0004", None, "「扔了吧。」")
label inner_note_0005:
    $ script_say("inner_note:0005", None, "说出口，是为了听他接不接。")
label inner_note_0006:
    $ script_say("inner_note:0006", CHAR_HE, "「里面是什么？」")
label inner_note_0007:
    $ script_say("inner_note:0007", None, "「失败的实验记录。」")
label inner_note_0008:
    $ script_say("inner_note:0008", None, "不算撒谎。实验做过的，课题只有一行：把一个人提前写下来，现实肯不肯照着交卷。")
label inner_note_0009:
    $ script_say("inner_note:0009", None, "结论：交一半。剩下那一半，比写的强。")
label inner_note_0010:
    $ script_say("inner_note:0010", CHAR_HE, "「扔之前，」他解开牛皮纸，「验收一下？」")
label inner_note_0011:
    $ script_say("inner_note:0011", None, "我的词，他的嗓子。")
label inner_note_0012:
    $ script_say("inner_note:0012", None, "我那套语法在他身上装的分机，这些年一直没停机。分机响的时候，主线在偷偷高兴。")
label inner_note_0013:
    $ script_say("inner_note:0013", None, "我把椅子坐正。这个坐法是探视室教的：坐直，耳朵离人近半寸，气也顺。要听的东西，在这种姿势里不容易漏。")
label inner_note_0014:
    $ script_say("inner_note:0014", None, "「念。念错一个字我都听得出来。」")
label inner_note_0015:
    $ script_say("inner_note:0015", None, "真话。那些字写的时候念过，改的时候念过，定稿前通读时念过；后来眼睛不够用，全数换成耳朵存档。每个字几钱几两，耳朵里有一杆秤。")
label inner_note_0016:
    $ script_say("inner_note:0016", None, "他念。页边的补记也念。")
label inner_note_0017:
    $ script_say("inner_note:0017", None, "第一条：「此处他应沉默三秒，然后给出漂亮的反驳」——「实际：没沉默。打了个喷嚏。可恶。」")
label inner_note_0018:
    $ script_say("inner_note:0018", None, "可恶是真的。那个喷嚏毁了我排练三天的节奏。可毁掉的节奏里长出来的那句反驳，比我写的版本好。第二条判词就是为它写的：「判断失误。此人比我写的要好。」——我手记里最老实的九个字。")
label inner_note_0019:
    $ script_say("inner_note:0019", CHAR_HE, "「我没这么说话。」他抗议。")
label inner_note_0020:
    $ script_say("inner_note:0020", None, "你就是这么说话的，我只是把废话删了，这话我说了一半。删掉的废话里，有一半是我自己的。")
label inner_note_0021:
    $ script_say("inner_note:0021", None, "汤碗往他那边推了推。桌上的疆域，我闭着眼也画得出来。")
label inner_note_0022:
    $ script_say("inner_note:0022", None, "然后，他翻页的手指停了一下。很短。我听见了。")
label inner_note_0023:
    $ script_say("inner_note:0023", None, "那一页只有一行对白，四个字，被铅笔划掉。划的时候笔尖断过两次，断芯的声音我还收着。页边小字也是我写的：「编的。他没说过。一遍也没有。」，写下它的那天，三个分句，句句属实。")
label inner_note_0024:
    $ script_say("inner_note:0024", CHAR_HE, "「这页划掉了。」他说。")
label inner_note_0025:
    $ script_say("inner_note:0025", None, "他在递台阶。意思是：可以跳过，不算数。")
label inner_note_0026:
    $ script_say("inner_note:0026", None, "「划掉了也念。反正要扔了。」")
label inner_note_0027:
    $ script_say("inner_note:0027", None, "台阶我不下。要扔的东西，扔之前也得点清数。划掉的也是一行。")
label inner_note_0028:
    $ script_say("inner_note:0028", None, "他念了第一遍。平平的，每个字都端着，像替别人值班。")
    # 【SE：胶带撕开的声音，停了。】
label inner_note_0029:
    $ script_say("inner_note:0029", None, "我手里正撕着胶带，在那一下停住。原因有二。小的：胶带一响，等于催他。大的：他念得太平，太平，说明这行字到今天还是台词。")
label inner_note_0030:
    $ script_say("inner_note:0030", None, "台词我不收。")
label inner_note_0031:
    $ script_say("inner_note:0031", None, "「语气不对。」")
label inner_note_0032:
    $ script_say("inner_note:0032", None, "明面上是导演挑戏。里子上是：再来一遍。像你一个人时那样念。一个人时的那种念法，收件人才在场。")
label inner_note_0033:
    $ script_say("inner_note:0033", CHAR_HE, "「他没说过这句话，哪来的对错。」")
label inner_note_0034:
    $ script_say("inner_note:0034", None, "「没说过，才有对错。」")
label inner_note_0035:
    $ script_say("inner_note:0035", None, "说出口的话都会走样。没说出口的，才有标准答案，这句当时随口，现在想来，够我用很多年。")
label inner_note_0036:
    $ script_say("inner_note:0036", None, "我停了停。「念下一个吧。」")
label inner_note_0037:
    $ script_say("inner_note:0037", None, "我给的台阶。他没下。他把本子拿正，回头重新念那一行。")
label inner_note_0038:
    $ script_say("inner_note:0038", None, "就在第二遍里，多出来一个很轻的声音：")
label inner_note_0039:
    $ script_say("inner_note:0039", None, "指腹蹭过纸角。起毛的纸特有的那种沙沙，像雪落在雪上。")
label inner_note_0040:
    $ script_say("inner_note:0040", None, "一下是偶然。这个密度，是很多年。")
label inner_note_0041:
    $ script_say("inner_note:0041", None, "我在心里算了笔算不出来的账：一个纸角，从平整到起毛，要翻多少次。一千次？两千次？摊到年头里，摊到没人看见的晚上：")
label inner_note_0042:
    $ script_say("inner_note:0042", None, "原来这一页，划掉的是一行字，养着的是另一行。")
label inner_note_0043:
    $ script_say("inner_note:0043", None, "那阵酸从胃里往上走。失明以后我练得最熟的就是这一口：把哭压成一次深呼吸，再压成一次吞咽。")
label inner_note_0044:
    $ script_say("inner_note:0044", None, "眼泪需要脸。我的脸现在归声音管。声音不能漏水。")
label inner_note_0045:
    $ script_say("inner_note:0045", None, "「……过。」我说，「就这条过。」")
label inner_note_0046:
    $ script_say("inner_note:0046", None, "声音平得我自己都满意。")
label inner_note_0047:
    $ script_say("inner_note:0047", CHAR_HE, "「就一条？」")
label inner_note_0048:
    $ script_say("inner_note:0048", None, "「其余项目，全部作废。」")
label inner_note_0049:
    $ script_say("inner_note:0049", None, "作废是个好词，像盖章。有些章盖下去不是为了否掉别的，是为了把值得的那一条，单独护送出这一页。")
label inner_note_0050:
    $ script_say("inner_note:0050", None, "后来他翻到后半本。")
label inner_note_0051:
    $ script_say("inner_note:0051", CHAR_HE, "「后面怎么没了？」")
label inner_note_0052:
    $ script_say("inner_note:0052", None, "「写不动了。」我说，「水开了，让让。」")
label inner_note_0053:
    $ script_say("inner_note:0053", None, "水没开。那是我的台阶。")
label inner_note_0054:
    $ script_say("inner_note:0054", None, "后半本不是写不动，是不敢往下写，再写，就该写结局了。脚本写到「他会说」为止，剩下的归即兴。即兴这种东西，不能有作者在场。我在场，他们放不开。")
label inner_note_0055:
    $ script_say("inner_note:0055", None, "那支铅笔还别在封皮上，笔杆一个牙印，我咬的。它被咬的年头，比被削的多。")
    $ PlaySession.advance_replay()
    jump inner_night

label inner_night:
    $ PlaySession.on_node_reached("inner_night")
    $ script_restore_visuals("inner_night")
    # ▎里·四
    # 【场景：卧室。声道：被褥、呼吸、一支很短的铅笔。】
label inner_night_0001:
    $ script_say("inner_night:0001", None, "「把本子拿来。」")
label inner_night_0002:
    $ script_say("inner_night:0002", None, "他摸黑递来。本子角先到，手后到——他递东西永远这样，怕角碰着我的脸。")
label inner_night_0003:
    $ script_say("inner_night:0003", CHAR_HE, "「你不看得见。」")
label inner_night_0004:
    $ script_say("inner_night:0004", None, "心疼话。心疼话也要回：")
label inner_night_0005:
    $ script_say("inner_night:0005", None, "「现在轮到你说蠢话了。」")
label inner_night_0006:
    $ script_say("inner_night:0006", None, "被子那边动了一下，肩膀先起的那种动。他要开灯。他开灯前有个预备动作，跟叹气是同一个。很多年了，我没提醒过他。")
label inner_night_0007:
    $ script_say("inner_night:0007", None, "「别开。」")
label inner_night_0008:
    $ script_say("inner_night:0008", None, "那只手在半路停住。停得好。")
label inner_night_0009:
    $ script_say("inner_night:0009", None, "开灯写出来的字，给眼睛。")
label inner_night_0010:
    $ script_say("inner_night:0010", None, "黑着写，给时间。")
label inner_night_0011:
    $ script_say("inner_night:0011", None, "左手压住本子的脊，右手小指抵住页边当轨道。铅笔要短，长的会颤。下笔不能想字形，要想笔画，字是手替眼睛养大的孩子，眼睛不在，孩子也认得回家。")
label inner_night_0012:
    $ script_say("inner_night:0012", None, "先来了三句，都在心里划掉了。")
label inner_night_0013:
    $ script_say("inner_night:0013", None, "第一句是账。白天平过了。")
label inner_night_0014:
    $ script_say("inner_night:0014", None, "第二句太重，怕压坏本子。")
label inner_night_0015:
    $ script_say("inner_night:0015", None, "第三句，他今天已经用嗓子领走了。再写一遍，是复写本。复写本不值钱。")
label inner_night_0016:
    $ script_say("inner_night:0016", None, "第四句来的时候没敲门。我照着写。写完，那行字多半在纸上站成淋过雨的一排，挤就挤点，挤着暖和。")
label inner_night_0017:
    $ script_say("inner_night:0017", None, "合上。递还。铅笔别回封皮。")
label inner_night_0018:
    $ script_say("inner_night:0018", CHAR_HE, "「写了什么？」")
label inner_night_0019:
    $ script_say("inner_night:0019", None, "「验收结果。」我说，「睡了。」")
label inner_night_0020:
    $ script_say("inner_night:0020", None, "他没追问。这个人花了很多年，学会我最难的功课：不问，也是一种念法。")
label inner_night_0021:
    $ script_say("inner_night:0021", None, "那行字从此是这个家唯一的原件。")
label inner_night_0022:
    $ script_say("inner_night:0022", None, "原件的意思是：连作者引用，也只能凭记忆。")
label inner_night_0023:
    $ script_say("inner_night:0023", None, "我老得很慢。记得住。")
    $ PlaySession.advance_replay()
    jump inner_slope

label inner_slope:
    $ PlaySession.on_node_reached("inner_slope")
    $ script_restore_visuals("inner_slope")
    # ▎里·五
    # 【场景：坡道。声道：石板、风、叶子、一部手机的假快门。】
label inner_slope_0001:
    $ script_say("inner_slope:0001", None, "第二天，上坡。")
label inner_slope_0002:
    $ script_say("inner_slope:0002", None, "四十一块石板，第三十块会响。照例踩响它，跟这条坡道个早，坡也应一声，一天就算开张。")
label inner_slope_0003:
    $ script_say("inner_slope:0003", None, "他走外侧，步幅悄悄收半格。收得很隐蔽，自以为没被发现。这半格我收了很多年，没退过货。")
label inner_slope_0004:
    $ script_say("inner_slope:0004", None, "树下有风。叶子比花诚实：花落得悲壮，叶子响得琐碎，哗啦哗啦，满树没排练过的小掌声。")
label inner_slope_0005:
    $ script_say("inner_slope:0005", None, "十几步外，快门响。")
label inner_slope_0006:
    $ script_say("inner_slope:0006", None, "「有人？」鼻子先报到。")
label inner_slope_0007:
    $ script_say("inner_slope:0007", CHAR_HE, "「有。校服。在拍树。」")
label inner_slope_0008:
    $ script_say("inner_slope:0008", None, "咔嚓。停。挪半步。咔嚓。")
label inner_slope_0009:
    $ script_say("inner_slope:0009", None, "手机那个快门是假的，机器里造出来哄耳朵的。可哄耳朵的也是声音，落到我这儿一样作数，这世上本来也没多少声音是真材实料。作数与否，从来不在原料，在听的人当不当真。")
label inner_slope_0010:
    $ script_say("inner_slope:0010", None, "「花都没了，拍什么？」")
label inner_slope_0011:
    $ script_say("inner_slope:0011", CHAR_HE, "「拍叶子。」")
label inner_slope_0012:
    $ script_say("inner_slope:0012", None, "「……哦。」")
label inner_slope_0013:
    $ script_say("inner_slope:0013", None, "心里那本册子记下一笔：花是预告，叶子是正篇。预告谁都会拍；肯对着一树绿按快门的人，跟我们是一路的。她的耐力比赛，今天开赛。祝她跑得久。")
label inner_slope_0014:
    $ script_say("inner_slope:0014", None, "那孩子发觉我们，衣料朝这边欠了欠。礼数教得好。后来脚步跑起来，远处的上课铃帮了忙。年轻真好，铃一响，就有地方要去。")
label inner_slope_0015:
    $ script_say("inner_slope:0015", None, "「第几年了？」")
label inner_slope_0016:
    $ script_say("inner_slope:0016", CHAR_HE, "「忘了数。」")
label inner_slope_0017:
    $ script_say("inner_slope:0017", None, "「我也忘了。」")
label inner_slope_0018:
    $ script_say("inner_slope:0018", None, "实话。数字用完就还回去了。还回去不叫丢，叫存成了别的，存成每年四月他的心跳，存成第三十块石板那一声。要那么多数字做什么。")
label inner_slope_0019:
    $ script_say("inner_slope:0019", None, "「那正好。」我把手插进他外套的口袋。「谁也不用负责。」")
label inner_slope_0020:
    $ script_say("inner_slope:0020", None, "口袋很暖。口袋这种地方，是失明以后新划进来的国土。面积不大，主权清楚。")
label inner_slope_0021:
    $ script_say("inner_slope:0021", None, "回去走他左边，耳朵借给树。它今天不说话，只摇叶子。")
label inner_slope_0022:
    $ script_say("inner_slope:0022", None, "不说话也是一种说话。这个道理，树比人懂得早。")
    $ PlaySession.advance_replay()
    jump inner_end

label inner_end:
    $ PlaySession.on_node_reached("inner_end")
    $ script_restore_visuals("inner_end")
    # ▎里·六
    # 【SE：钥匙、门、拖鞋。】
label inner_end_0001:
    $ script_say("inner_end:0001", None, "快到家门口。")
label inner_end_0002:
    $ script_say("inner_end:0002", None, "「晚饭想吃什么？」")
label inner_end_0003:
    $ script_say("inner_end:0003", CHAR_HE, "「都行。别太咸。」")
label inner_end_0004:
    $ script_say("inner_end:0004", None, "早上那半勺是给降温的，说辞我都替他想好了，他到嘴边只剩一个咸字。味噌和天气这门课，他很多年没及格。")
label inner_end_0005:
    $ script_say("inner_end:0005", None, "也好。全及格，日子就成了考试。")
label inner_end_0006:
    $ script_say("inner_end:0006", None, "「你眉毛又开始了。」")
label inner_end_0007:
    $ script_say("inner_end:0007", None, "他大概又在想，我怎么知道。")
label inner_end_0008:
    $ script_say("inner_end:0008", None, "不告诉你。总得留一桩他破不了的案。")
    # 【SE：门关上。】
label inner_end_0009:
    $ script_say("inner_end:0009", None, "门在我们家不是句号，是下一句的抬手。")
    # ▎里·尾声
    $ renpy.scene()
    $ renpy.show("bg_bedroom_inner")
label inner_end_0010:
    $ script_say("inner_end:0010", None, "睡前记账，只记这一页：")
label inner_end_0011:
    $ script_say("inner_end:0011", None, "本日。据他的频道：晴，无事。")
label inner_end_0012:
    $ script_say("inner_end:0012", None, "据我的频道：有事。清单如下：")
label inner_end_0013:
    $ script_say("inner_end:0013", None, "一、一句话，扣在邮路上，改判两折纸，押于单据堆最底层。")
label inner_end_0014:
    $ script_say("inner_end:0014", None, "二、四个字，念了两遍。第一遍是台词，退回。第二遍带着纸角的年轮，签收。")
label inner_end_0015:
    $ script_say("inner_end:0015", None, "三、一行字，写进黑里，无收件人。作数。")
label inner_end_0016:
    $ script_say("inner_end:0016", None, "四、一棵树，把花收进仓库，换一身叶子，原地营业。")
label inner_end_0017:
    $ script_say("inner_end:0017", None, "五、一个孩子，对着满树的绿，按了七次假快门。我听见了。")
label inner_end_0018:
    $ script_say("inner_end:0018", None, "都记下了。用耳朵。")
label inner_end_0019:
    $ script_say("inner_end:0019", None, "这本账不平。不平就对了——平了就得结。我们家不结账。")
label inner_end_0020:
    $ script_say("inner_end:0020", None, "灯黑着。他先睡着，呼吸一格一格落下去，像那条坡的石板。")
label inner_end_0021:
    $ script_say("inner_end:0021", None, "数到第三十块，我也睡了。")
label inner_end_0022:
    $ script_say("inner_end:0022", None, "（读完了，请把亮度调回去。")
label inner_end_0023:
    $ script_say("inner_end:0023", None, "你那边的颜色，也是替谁收着的。别亏待它。）")
    $ PlaySession.complete_inner_chapter()
