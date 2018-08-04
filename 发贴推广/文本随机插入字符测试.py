# -*- coding:utf-8

import re  # 正则式  [\u4e00-\u9fa5]{0,}$
import random

一楼内容 = r""" 
近几天拼多多成了各种绕不开的话题，突然之间很多人都没有用过也看不起的拼多多就成了中国第三大电商。目前拼多多年度活跃用户达3.44亿人。GMV超过千亿，京东用了10年，唯品会用了8年，淘宝用了5年，拼多多只用了2年11个月。不到3年时间成为国内电商行业第三。昨日收盘拼多多市值达到295.8亿美元，约等于半个京东，创始人黄铮身价达到138.5亿美元，超越了京东刘强东。
 
但是奇怪的是媒体上、朋友圈里对拼多多却大都表现出鄙夷的态度。很多人都在对拼多多的低价、假货口诛笔伐。怎么认识拼多多？拼多多其实就是淘宝的影子。当然新的淘宝不可能以原来的方式出现，在阿里掌控的范围也不允许有新的淘宝出现，所以杭州80后新首富借道腾讯微信社交，用淘宝+团购+社交在电商世界里抢到了跑道。
那些鄙视拼多多的人，装得好像自己没用过淘宝一样。康帅傅、娃娃哈、太白兔、必相印、abidas这样的产品我们在淘宝也没少见过。甚至你也不能说它们是假货。现在拼多多被批评的问题，淘宝也都经历过。对平台来说审核机制不可能完美，更多地也只能靠事后的惩罚机制。而拼多多对商家的惩罚机制是非常严的。要不然最近怎么有那么多商家去拼多多总部闹，还有商家去美国起诉拼多多处罚过严给拼多多上市添堵。
 
对于三亿多拼多多的用户，很多人不可理解，觉得这些人贪小便宜，上当受骗。先富起来的中国人，已经觉得没机会再富起来的中国人是怪物了。但是这个世界上只有一种病，那就是穷病。让人恶心的不是拼多多，而是穷这个字。
因为中国市场足够大，所以阿里战略放弃淘宝主推天猫也继续风光无限，但阿里当年之所以会成功，还不是靠淘宝服务穷人市场，中国那些成功的互联网公司也都是依靠屌丝经济起家的，这也是那些美国互联网公司雅虎、ebay们折戟中国的原因。自京东以后，中国电商开始走消费升级、高大上的道路，但也只有京东、天猫活得好，还有一些过得好的电商是转而去服务第三世界穷人了。
厉害了我的国只是幻象，当拼多多重走淘宝路时，黄铮两三年就赶超了刘强东的身价，已经很能说明问题了。虽然富人与中产看着拼多多觉得拉低了自己厉害的国，但是如果其他电商都还是去追求高大上，把电商穷人市场都留给拼多多，那么如果几年后阿里也压不住拼多多，也不用太惊讶。厉害的我的国就是天然出淘宝、拼多多这样的穷人商业奇迹。
黄铮说拼多多的模式北京五环以内的人看不懂，而北京五环以内的房价都在五万以上了。想必住在这么贵房子里的人连京东、天猫都会觉得low了。套用抖音流行的句式：你有你的可口可乐，我有我的可苦可乐，不是很有面子，但是也还能喝。你有你的苹果X，我有我的水果X，不是很酷，但是也还能用。
中国还是那个中国，一直都没有变，这些年的经济发展更多的是靠货币放水以及房价的高速上涨，居民收入的上涨都赶不上房价的上涨和通货膨胀，不存在什么消费降级，黄铮也不需要用消费均衡为拼多多辩护，我们还是社会主义初级阶段的发展中国家，只是先富起来的部分人甚至都已经觉得美帝的基础设施建设太落后，无法让他们在美利坚的豪宅享受国内一样的便利罢了。
中国太大，大到很多一线城市父母都在考虑送孩子去哪个世界名校留学深造才能不被社会淘汰，而全国的本科以上学历人口占比还不超过4%；银行存款50万以上的全国也不超过4%，A股账户资产10万以上的只占15%。中国按照每年2300元收入计算的贫困人口还有3046万人，是年收入2300元，不是月收入。
 
今天看到另一组数据，根据美国威廉玛丽学院的数据统计，从2000年到2014年，中国累计对外提供援助和贷款金额约3620亿美元，约2.4万亿元人民币。这也是美国人对中国贸易战的一个嘴上理由，他们认为中国每年的对外援助早都超过了美国，所以不能再在WTO里按发展中国家来看待。
 
拼多多的上市，更多的是一面镜子，我们以为自己应该消费升级，淘宝以后是天猫、京东、然后是网易严选，接下来应该是各种奢侈品电商的崛起，但是不好意思，我们还没有等到奢侈品电商，或者中国也很难等到像法国、意大利那样奢侈品品牌成为国家的形象企业（茅台除外），我们等到了自己都不想看到的---拼多多。
拼多多的上市，没有惊喜，或许都有了些许惊吓。拼多多自己都不好意思地反复辩解是消费均衡不是降级；穷人也不好意思地表示只是尝试去购买了下，买了就删了；中产愤怒地表示这样的“山寨”“假货”“骗子”怎么能让上市；富人看了莫名其妙。但这就是中国。
"""
#符号表 = random.choice('♪♩♭♪〡│╎╏┆┇┊┋↑↓↕↟↡↥↧↨⇑⇓↾↿⇂⇃⇞⇟⇡⇣⇧⇩「」´＇ˆˇ╎╏Ⅰ│')
正文 = 一楼内容

#正文='ᗱΕᗱ⒏ℂ○Ⅿ'  3e38、com丶

文本列表 = list(一楼内容)#转为列表
计数器=0
文本=''
for 每个字 in 文本列表:
    计数器 = 计数器+1
    if 计数器 ==12:
        符号表 = random.choice('↕↟↡↥↧↨↾↿⇂⇃⇞⇟⇡⇣´`ˆ')
        文本 =文本+符号表
        计数器 = 0
    文本 = 文本 + 每个字
print('文本', 文本)


