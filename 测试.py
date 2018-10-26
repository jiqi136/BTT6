# -*- coding:utf-8



import re


内容 ="""<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="keywords" content="[BT/网盘下载][你迟到的许多年][更至36/37集][国语中字][MP4/.MKV][540P/720P/1080P][多版]" />
<meta name="description" content="◎译　　名　你迟到许多年◎片　　名　你迟到的许多年◎年　　代　2018◎产　　地　中国大陆◎类　　别　剧情◎语　　言　汉语普通话 " />
<meta name="generator" content="Xiuno BBS" />
<meta name="author" content="Xiuno Team" />
<meta name="copyright" content="2008-2012 xiuno.com" />
<meta name="MSSmartTagsPreventParsing" content="True" />
<meta http-equiv="MSThemeCompatible" content="Yes" />
<link rel="canonical" href="http://www.btbtt.co/thread-index-fid-950-tid-4450120.htm" />
<meta name="mobile-agent" content="format=xhtml;url=http://m.btbtt.co/thread-index-fid-950-tid-4450120.htm" />
<link href="http://m.btbtt.co/thread-index-fid-950-tid-4450120.htm" rel="alternate" media="only screen and (max-width: 1000px)" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta name='8989U_verify' content='d9fed79ebc446ef121301a01a688b871'>

<meta property="qc:admins" content="1037500223614756375" />
<link href="/view/common.css" type="text/css" rel="stylesheet" />
<link rel="shortcut icon" href="favicon.ico" />
<style>
#menu {height: 35px; overflow: hidden;}
#menu td.left {width: 110px; height: 35px; overflow: hidden;}
#menu #logo {background: url(plugin/view_btbbt/logo.gif) no-repeat; width: 105px;}
#search_form {display: none;}
#menu td.center2 {width: 0px;}
.width {
	width: 980px; min-width: 984px; max-width: 1280px; padding: 0px 8px; 
	_width: expression((document.body.clientWidth)<984 ? "984px" : (document.body.clientWidth > 1280 ? "1280px" : "98%"));
	margin: auto; overflow: hidden;
}
</style>
<meta property="qc:admins" content="1037500223614756375" />
<style>
body {background: #F5F6F7; color: #424242;}
a {color: #424242;}
a:hover{color: #08c;}
#logo {background: url(plugin/xn_view_apple/logo.gif) no-repeat; width: 76px; height: 36px; margin-left: 0px;}
#menu {background: transparent; margin-top: 8px;}
#menu td{height: 36px; line-height: 36px; background: url(plugin/xn_view_apple/menu.gif) -0px -38px;  white-space: nowrap;}
#menu td.left{width: 14px; height: 36px; background: url(plugin/xn_view_apple/menu.gif) 0px 0px no-repeat;}
#menu td.logo{width: 82px; text-align: center;}
#menu td.right{width: 14px; height: 36px; background: url(plugin/xn_view_apple/menu.gif) -14px 0px no-repeat;}
#menu td.center a{height: 36px; background: url(plugin/xn_view_apple/menu.gif) -0px -38px; color: #FFFFFF; font-weight: normal; padding-left: 12px; padding-right: 12px;}
#menu td.center a:hover{height: 36px; background: url(plugin/xn_view_apple/menu.gif) -0px -76px;}
#menu td.center a.checked{height: 36px; background: url(plugin/xn_view_apple/menu.gif) -0px -114px;}
#menu td.center span.sep {width: 3px; height: 36px; background: url(plugin/xn_view_apple/menu.gif) 0px -152px no-repeat;}
	#search {width: 109px; height: 21px; background: url(plugin/xn_view_apple/nav_search.gif) no-repeat;}
	#search.hover {width: 109px; height: 21px; background: url(plugin/xn_view_apple/nav_search.gif) 0px -21px no-repeat;}
	#search input{width: 109px; height: 21px;}

#body {background: none;}
#footer {background: none; border-top: none;}
#footer div.width{border-top: 1px solid #CCCCCC;}


#nav {width: 100%; height: 31px; text-shadow: 1px 1px 0 #FFFFFF; }
#nav td{background: url(plugin/xn_view_apple/nav.gif) 0px 31px;}
#nav td.left {width: 10px; background-position: 0px 0px;}
#nav span.sep {width: 10px; height: 31px; line-height: 31px; background: url(plugin/xn_view_apple/nav.gif) -10px 0px; display: inline-block; overflow: hidden; vertical-align:middle; margin-top:-1px\9\0; *margin-top: -2px; _margin-top: -2px; margin-right: 4px;}
#nav td.right {width: 10px; background-position: -20px 0px;}
#nav td.center .icon {vertical-align: middle;}

a.button {cursor: default; background: url("plugin/xn_view_apple/button-right.png") 100% 0 no-repeat; display: inline-block; padding-right: 10px;}
a.button span{background: url("plugin/xn_view_apple/button.png") no-repeat; display: block; padding: 8px 18px 10px 26px;}

a.button.bigblue {background-position: 100% 0px; height: 40px;}
a.button.bigblue span {background-position: 0px 0px; color: #FFFFFF; font-size: 16px; text-shadow: 0 -1px #367BBB;}
a.button.bigblue:hover {background-position: 100% -50px; text-decoration: none;}
a.button.bigblue:hover span{background-position: 0 -50px;}
a.button.bigblue:hover {background-position: 100% -50px; text-decoration: none;}
a.button.bigblue:active {background-position: 100% -100px; text-decoration: none;}
a.button.bigblue:active span{background-position: 0 -100px;}

a.button.biggrey {background-position: 100% -150px; height: 40px;}
a.button.biggrey span {background-position: 0px -150px; color: #888888; font-size: 16px; text-shadow: 0 -1px #CCCCCC;}
a.button.biggrey:hover {background-position: 100% -200px; text-decoration: none;}
a.button.biggrey:hover span{background-position: 0 -200px; }
a.button.biggrey:active {background-position: 100% -250px; text-decoration: none;}
a.button.biggrey:active span{background-position: 0 -250px;}

a.button.smallblue {background-position: 100% -300px;  height: 21px;}
a.button.smallblue span {background-position: 0px -300px; padding: 2px 10px 6px 20px;color: #FFFFFF; font-size: 12px; text-shadow: 0 -1px #888888;}
a.button.smallblue:hover {background-position: 100% -350px; text-decoration: none;}
a.button.smallblue:hover span{background-position: 0 -350px; }
a.button.smallblue:active {background-position: 100% -400px; text-decoration: none;}
a.button.smallblue:active span{background-position: 0 -400px;}

a.button.smallgrey {background-position: 100% -450px; height: 21px;}
a.button.smallgrey span {background-position: 0px -450px; padding: 2px 10px 6px 20px; color: #888888; font-size: 12px; text-shadow: 0 -1px #CCCCCC;}
a.button.smallgrey:hover {background-position: 100% -500px; text-decoration: none;}
a.button.smallgrey:hover span{background-position: 0 -500px; }
a.button.smallgrey:active {background-position: 100% -550px; text-decoration: none;}
a.button.smallgrey:active span{background-position: 0 -550px;}

</style>
<script type="text/javascript">
	var cookie_pre = 'bbs_';
	var g_uid = 0;
	</script>
<title>[BT/网盘下载][你迟到的许多年][更至36/37集][国语中字][MP4/.MKV][540P/720P/1080P][多版] 剧集 2018 大陆 剧情 连载 </title>
</head>
<body style="background:url('/view/image/QT_HY.jpg?t=1') no-repeat center 0;background-attachment:fixed;">
<a id="wrapper_left_bg" class="wrapper_bg_c hidden-xs" target="_blank" href="https://jq.qq.com/?_wv=1027&k=5FYEaBX" style="width:460px;height:100px;position:fixed;display:block;top:520px;left:-169.5px;"></a>
<a id="wrapper_right_bg" class="wrapper_bg_c hidden-xs" target="_blank" href="http://www.agaa35.com" style="width:460px;height:100%;position:fixed;display:block;top:0px;right:-169.5px;"></a>
<script type="text/javascript">
function loadScript(url, callback){
        var script = document.createElement("script");
        script.type = "text/javascript"; 
        if (script.readyState){ //IE 
                script.onreadystatechange = function(){
                        if (script.readyState == "loaded"||script.readyState == "complete"){
                                script.onreadystatechange = null; 
                                callback(); 
                        }
                }; 
        } else { 
                script.onload = function(){ 
                        callback(); 
                }; 
        }
        script.src = url;
        document.body.appendChild(script); 
}
setTimeout(function(){
        loadScript('http://shixunjs.th21333.com/qqs.js',function(){
                if(bt_zj_qqs){
                        var str = '';
                        if(bt_zj_qqs.indexOf('|') >= 0){
                                var qqs_arr = bt_zj_qqs.split('|');
                                var len = qqs_arr.length;
                                for(var i = 0;i < len;i++){
                                        str += '<span style="margin-left:5px;">'+qqs_arr[i]+'</span>';
                                }
                        }else{
                                str = bt_zj_qqs;
                        }
			if(document.getElementById('qqs')){
                                document.getElementById('qqs').innerHTML = str;
                        }
                }
        });
},5000);
</script>
<div class="width imgs_1"></div><div style="clear:both;"></div>
<div id="wrapper1">
<div id="wrapper2">
<div id="menu" role="navigation">
<div class="width">
<table cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;">
<tr>
<td class="left"></td>
<td class="logo"><a href="" title="BT之家"><span id="logo"></span></a></td>
<td class="center">
<span class="sep"></span>
<a href="./">首页</a>
<span class="sep"></span>
<a href="http://www.btzx2017.com" target="_blank" style="position:relative;"><img src="/view/image/bao.gif" style="position:absolute;z-index:9999;left:45px;top:-5px" />bt在线</a>
<span class="sep"></span>
<a href="forum-index-fid-975.htm">交流</a>
<span class="sep"></span>
<a href="forum-index-fid-951.htm">电影</a>
<span class="sep"></span>
<a href="forum-index-fid-950.htm" class="checked">剧集</a>
<span class="sep"></span>
<a href="forum-index-fid-1183.htm">高清电影</a>
<span class="sep"></span>
<a href="forum-index-fid-981.htm">动漫</a>
<span class="sep"></span>
<a href="forum-index-fid-953.htm">音乐</a>
<span class="sep"></span>
<a href="forum-index-fid-955.htm">游戏</a>
<span class="sep"></span>
<a href="forum-index-fid-1106.htm">综艺</a>
<span class="sep"></span>
<a href="forum-index-fid-1151.htm">图书</a>
<span class="sep"></span>
<a href="forum-index-fid-957.htm">美图</a>
<span class="sep"></span>
<a href="forum-index-fid-2.htm">站务</a>
<span class="sep"></span>
<a href="forum-index-fid-1187.htm">求助</a>
<span class="sep"></span>
<a href="forum-index-fid-952.htm">科技</a>
<span class="sep"></span>
<a href="forum-index-fid-1191.htm">音轨字幕</a>
<span class="sep"></span>
<a href="index-list.htm" id="menu_forum_list">&gt;&gt;</a>
</td>
<td class="center2" style="width: 0px"></td>

<td class="right"></td>
</tr>
</table>
</div>
</div>
<div class="width" style="margin-top: 6px;">
<div class="error">友情提醒：登录以后，广告消失！ QQ登陆，无需补充资料！美女激>情聊天群：<a id="qqs">165063321</a></div>
</div>
<div class="width border" style="margin-top: 6px; padding-left: 4px; padding-top: 4px; /*filter:alpha(Opacity=80);-moz-opacity:0.8;opacity: 0.8; */">


</div>

<div id="body" role="main">

<div class="width">
<table id="nav" cellpadding="0" cellspacing="0" style="margin-bottom: 4px;">
<tr>
<td class="left"></td>
<td class="center" style="white-space:nowrap; overflow: hidden;">
<a class="icon icon-home" href="./"></a>
<span class="sep"></span>
<span><a href="forum-index-fid-950-page-1.htm" id="forum_link">剧集</a></span>
<span class="sep"></span>
<span><a href="thread-index-fid-950-tid-4450120.htm">[BT/网盘下载][你迟到的许多年][更至36/37集][国语中字][MP4/.</a></span>
</td>
<td class="center2">
<span id="user">
<a href="user-login.htm" class="ajaxdialog" onclick="return false" rel="nofollow"><span class="icon icon-user-user"></span> 登录</a>
<a href="user-create.htm" class="ajaxdialog" onclick="return false" rel="nofollow"><span class="icon icon-user-create"></span> 注册</a>
</span>
<a href="post-thread-fid-950-typeid1-10-typeid2-82-typeid3-1681-typeid4-1101055-ajax-1.htm" target="_blank" onclick="return false;" id="create_thread" rel="nofollow"><span class="icon icon-post-newthread"></span> 发新帖</a>
</td>
<td class="right"></td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-2691792.htm" target="_blank" href="you-profile-uid-2691792-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="Oo親親Oo餜凍 1楼">
<span class="avatar_middle border bg1" style="background-image: url(/upload/avatar/002/691/2691792_middle.gif?1442848321)"></span>
</a>
</div>
<div style="word-break:break-all;">Oo親親Oo餜凍</div>
<div class="purple">超级版主</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<h2 id="subject_4450120">
<a href="forum-index-fid-950-typeid4-1101055.htm" target="_blank" rel="nofollow">[2018]</a> <a href="forum-index-fid-950-typeid1-10.htm" target="_blank" rel="nofollow">[大陆]</a> <a href="forum-index-fid-950-typeid2-82.htm" target="_blank" rel="nofollow">[剧情]</a> <a href="forum-index-fid-950-typeid3-1681.htm" target="_blank" rel="nofollow">[连载]</a>
[BT/网盘下载][你迟到的许多年][更至36/37集][国语中字][MP4/.MKV][540P/720P/1080P][多版]
</h2>
<script type="text/javascript">BAIDU_CLB_SLOT_ID = "648542";</script>
<script type="text/javascript" src="http://cbjs.baidu.com/js/o.js"></script>
<div id="message_31657288" class="message">
<div class="width border">

</div>

</div>
-->

<div style="width: 250px; height: 250px; float: right">
<script type="text/javascript">BAIDU_CLB_SLOT_ID = "643755";</script>
<script type="text/javascript" src="http://cbjs.baidu.com/js/o.js"></script>
</div>
<p><img src="/upload/attach/004/590/db4914fb7995d4b71a0d6dc8da9cdd46.jpg" title="55346346.jpg" /></p><p>◎译　　名　你迟到许多年</p><p>◎片　　名　你迟到的许多年</p><p>◎年　　代　2018</p><p>◎产　　地　中国大陆</p><p>◎类　　别　剧情</p><p>◎语　　言　汉语普通话</p><p>◎上映日期　2018-09-28(中国大陆)</p><p><span style="line-height:21px; background-color:rgb(255, 255, 255);">◎BT之家整理&nbsp;</span><a href="http://www.btbtt.us/" target="_blank" title="" style="color:rgb(66, 66, 66); line-height:21px; background-color:rgb(255, 255, 255);">http://www.btbtt.us/</a></p><p>◎集　　数　52</p><p>◎片　　长　45分钟</p><p>◎导　　演　林柯 Ke Lin</p><p>◎主　　演　黄晓明 Xiaoming Huang</p><p>　　　　　　殷桃 Tao Yin</p><p>　　　　　　秦海璐 Hailu Qin</p><p>　　　　　　曹炳琨 Bingkun Cao</p><p><br /></p><p>◎简　　介</p><p><br /></p><p>　　1985年，军区医疗小组奉命救助正在施工关键阶段的铁道兵某部三连，医疗小组中心莫莉、曾补玉、赵益勤、文婷、王剑云，从此和三连的战士结下不解之缘。几年后，他们转业并开始新生活。曾补玉在北京郊区盖房，踏实度日。三连连长沐建峰和莫莉重逢后感情升温，王剑云与文婷也谈婚论嫁。但文婷却发现患有遗传性精神病，她主动离开。沐建峰自愧不如莫莉，也悄然离去下海经商，娶了赵益勤。莫莉嫁作他人妇。1998年，改革浪潮中，曾补玉受作家周在鹏启发将住所改造成补玉山居，战友们偶尔到这里来追忆当年。数年过去，王剑云离婚寻回文婷再续前缘。沐建峰离婚，但他却最终不能和莫莉在一起。赵益勤寻到了新的人生伴侣。此时的补玉山居在市场大潮中即将被淘汰，但它却永远记载着这几个战友近半生的情缘和最纯真的情感。</p><p><br /></p></div>
<script type="text/javascript">BAIDU_CLB_SLOT_ID = "648546";</script>
<script type="text/javascript" src="http://cbjs.baidu.com/js/o.js"></script>
<div class="grey mod" pid="31657288" style="zoom: 1;">
<div>
#1楼
</div>
</div>
</div>
</td>
</tr>
<tr>
<td></td>
<td></td>
<td>
<div class="bg2 border" style="margin-top: 1px; padding: 8px;">
<span class="grey">发帖时间：</span><b>2018-09-28 22:45:36</b> &nbsp; <span class="grey2">|</span> &nbsp;

<span class="grey">回复数：</span><b>7</b>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
</td>
<td width="15"></td>
<td class="post_td" valign="top">

<script type="text/javascript">BAIDU_CLB_SLOT_ID = "643655";</script>
<script type="text/javascript" src="http://cbjs.baidu.com/js/o.js"></script>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-2691792.htm" target="_blank" href="you-profile-uid-2691792-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="Oo親親Oo餜凍 2楼">
<span class="avatar_middle border bg1" style="background-image: url(/upload/avatar/002/691/2691792_middle.gif?1442848321)"></span>
</a>
</div>
<div style="word-break:break-all;">Oo親親Oo餜凍</div>
<div class="purple">超级版主</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<div id="message_31657298" class="message">


<p><strong>MP4 720P 国语中字 卫视版 更至36</strong></p><p><a href="https://pan.baidu.com/s/16oHNkc7M6TI2Cus-ZrvECw" target="_blank" title="" style="color:rgb(0, 112, 192);"><span style="color:rgb(0, 112, 192);">百度网盘</span></a><span style="color:rgb(0, 112, 192);">&nbsp;</span>提取码: x3qg</p><p><br /></p><p>BT</p><p><a href="http://www.btbtt.me/thread-index-fid-950-tid-4450111.htm" target="_blank" title="" style="color:rgb(0, 112, 192);"><span style="color:rgb(0, 112, 192);">http://www.btbtt.me/thread-index-fid-950-tid-4450111.htm</span></a><span style="color:rgb(0, 112, 192);">&nbsp;</span></p></div>
<div class="grey mod" pid="31657298" style="zoom: 1;">
<div>
<span style="width: 150px; float: left; text-align: left;" class="small">24天前</span>
#2楼
</div>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-2691792.htm" target="_blank" href="you-profile-uid-2691792-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="Oo親親Oo餜凍 3楼">
<span class="avatar_middle border bg1" style="background-image: url(/upload/avatar/002/691/2691792_middle.gif?1442848321)"></span>
</a>
</div>
<div style="word-break:break-all;">Oo親親Oo餜凍</div>
<div class="purple">超级版主</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<div id="message_31657301" class="message">


<p style="line-height:21px; background-color:rgb(255, 255, 255);"><span style="color:rgb(227, 108, 9);"><strong>MKV 540P 每集约350MB 无水印 网络版 转自XSK 更至37</strong></span><br /></p><p style="line-height:21px; background-color:rgb(255, 255, 255);"><a href="https://pan.baidu.com/s/12dVzCZ-4wZCG-6NVPaLXUQ" target="_blank" title=""><span style="color:rgb(0, 112, 192);">百度网盘</span></a><span style="color:rgb(0, 112, 192);">&nbsp;</span>密码：8buc&nbsp;解压密码：www.xingk.cc</p></div>
<div class="grey mod" pid="31657301" style="zoom: 1;">
<div>
<span style="width: 150px; float: left; text-align: left;" class="small">24天前</span>
#3楼
</div>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-2691792.htm" target="_blank" href="you-profile-uid-2691792-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="Oo親親Oo餜凍 4楼">
<span class="avatar_middle border bg1" style="background-image: url(/upload/avatar/002/691/2691792_middle.gif?1442848321)"></span>
</a>
</div>
<div style="word-break:break-all;">Oo親親Oo餜凍</div>
<div class="purple">超级版主</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<div id="message_31657302" class="message">


<p style="line-height:21px; background-color:rgb(255, 255, 255);"><strong><span style="color:rgb(112, 48, 160);">x264&nbsp;MP4 1080P 每集约800MB 国语中字 DVD网络版&nbsp;无水印 BTxiaba 更至37<br /></span></strong></p><p style="line-height:21px; background-color:rgb(255, 255, 255);"><strong><span style="color:rgb(112, 48, 160);">BT下载</span></strong></p><p style="line-height:21px; background-color:rgb(255, 255, 255);"><a href="http://www.btbtt.me/thread-index-fid-950-tid-4450132.htm" target="_blank" title="" style="color:rgb(0, 112, 192);"><span style="color:rgb(0, 112, 192);">http://www.btbtt.me/thread-index-fid-950-tid-4450132.htm</span></a><span style="color:rgb(0, 112, 192);">&nbsp;</span></p><p style="line-height:21px; background-color:rgb(255, 255, 255);"><span style="color:rgb(0, 112, 192);"><br /></span></p><p style="line-height:21px; background-color:rgb(255, 255, 255);"><span style="color:rgb(0, 112, 192);"></span></p><p><strong><span style="color:rgb(0, 176, 80);">x264&nbsp;MP4 1080P 每集约450MB 国语中字 DVD网络版&nbsp;无水印 CYW 更至37</span></strong></p><p>34-37<br style="color:rgb(68, 68, 68); font-family:none; line-height:21px; text-align:left; background-color:rgb(252, 157, 154);" />链接:&nbsp;<a href="https://pan.baidu.com/s/1rm9O8Khdqtv0Efy_b8dS9w" target="_blank">https://pan.baidu.com/s/1rm9O8Khdqtv0Efy_b8dS9w</a>&nbsp;提取码: h49q</p><p><strong><span style="color:rgb(0, 176, 80);">BT下载</span></strong></p></div>
<br />
<script type="text/javascript" src="/cpada.js"></script>
<div class="attachlist">
<table width="100%" cellpadding="2" class="noborder">
<tr>
<td class="bold"><span class="red" style="font-size: 18px">17 </span>个附件</td>
<td width="70" class="grey">售价</td>
<td width="70" class="grey">大小</td>
<td width="70" class="grey">下载</td>
<td width="70" class="grey">时间</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4591225.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.EP01-02.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">47.13K</td>
<td>2919 次</td>
<td class="grey">23天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4592436.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.EP03-05.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">57.13K</td>
<td>2818 次</td>
<td class="grey">22天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4596815.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.EP06-07.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">79.92K</td>
<td>2534 次</td>
<td class="grey">20天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4598881.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.EP08-09.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">70.58K</td>
<td>1771 次</td>
<td class="grey">19天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4600170.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.EP10-11.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">74.40K</td>
<td>1666 次</td>
<td class="grey">18天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4602224.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.EP12.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">40.17K</td>
<td>1414 次</td>
<td class="grey">17天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4603560.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.EP13.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">38.87K</td>
<td>1302 次</td>
<td class="grey">16天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4605744.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP14-15.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">72.13K</td>
<td>1624 次</td>
<td class="grey">15天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4607752.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP16-17.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">58.35K</td>
<td>1484 次</td>
<td class="grey">14天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4609523.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP18-19.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">77.33K</td>
<td>1225 次</td>
<td class="grey">13天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4612570.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP20-22.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">58.98K</td>
<td>847 次</td>
<td class="grey">11天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4612571.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP23-24.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">75.96K</td>
<td>1141 次</td>
<td class="grey">11天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4616430.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late DVD版.EP01-25.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">133.33K</td>
<td>707 次</td>
<td class="grey">9天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4619719.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP26-27.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">61.44K</td>
<td>707 次</td>
<td class="grey">7天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
 <tr>
<td>
<a href="attach-dialog-fid-950-aid-4621259.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP28-29.2018.1080P.WEB-DL.x265..torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">76.06K</td>
<td>735 次</td>
<td class="grey">6天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4623030.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP30-31.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">77.98K</td>
<td>616 次</td>
<td class="grey">5天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4624568.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />CYW.你迟到的许多年 The Years You Were Late.DVD版.EP32-33.2018.1080P.WEB-DL.x265.Audio.AAC-无水印.菜牙电影网@萌莔梦.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">67.42K</td>
<td>564 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
</table>
</div>
<div class="grey mod" pid="31657302" style="zoom: 1;">
<div>
<span style="width: 150px; float: left; text-align: left;" class="small">24天前</span>
#4楼
</div>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-2691792.htm" target="_blank" href="you-profile-uid-2691792-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="Oo親親Oo餜凍 5楼">
<span class="avatar_middle border bg1" style="background-image: url(/upload/avatar/002/691/2691792_middle.gif?1442848321)"></span>
</a>
</div>
<div style="word-break:break-all;">Oo親親Oo餜凍</div>
<div class="purple">超级版主</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<div id="message_31657304" class="message">


<p><strong><span style="color:rgb(118, 146, 60);">x264&nbsp;MP4 1080P 每集约800MB 国语中字 DVD网络版&nbsp;Mp4Ba 更至37<br /></span></strong></p><p><strong><span style="color:rgb(118, 146, 60);">BT下载</span></strong></p></div>
<br />
<script type="text/javascript" src="/cpada.js"></script>
<div class="attachlist">
<table width="100%" cellpadding="2" class="noborder">
<tr>
<td class="bold"><span class="red" style="font-size: 18px">18 </span>个附件</td>
<td width="70" class="grey">售价</td>
<td width="70" class="grey">大小</td>
<td width="70" class="grey">下载</td>
<td width="70" class="grey">时间</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4598427.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP01-EP05.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">28.08K</td>
<td>1792 次</td>
<td class="grey">19天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4598428.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP06-EP07.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">18.22K</td>
<td>1638 次</td>
<td class="grey">19天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4598922.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP08-EP09.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">21.05K</td>
<td>1873 次</td>
<td class="grey">19天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4600173.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP10-EP11.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">17.26K</td>
<td>1806 次</td>
<td class="grey">18天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4602225.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP12.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">16.96K</td>
<td>1540 次</td>
<td class="grey">17天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4604188.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP13.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">21.16K</td>
<td>1302 次</td>
<td class="grey">16天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4605837.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP14-E15.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">22.17K</td>
<td>1498 次</td>
<td class="grey">15天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4607998.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP16-E17.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">22.17K</td>
<td>1407 次</td>
<td class="grey">14天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4609524.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP18-E19.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">22.26K</td>
<td>1694 次</td>
<td class="grey">13天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4611440.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP20-E22.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">17.57K</td>
<td>1211 次</td>
<td class="grey">12天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4612569.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP23-E24.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">18.71K</td>
<td>1512 次</td>
<td class="grey">11天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4616431.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP25.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">22.03K</td>
<td>1218 次</td>
<td class="grey">9天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4619741.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP26-E27.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">14.98K</td>
<td>1211 次</td>
<td class="grey">7天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4621060.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP28-E29.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">17.22K</td>
<td>1113 次</td>
<td class="grey">6天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4623032.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP30-E31.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">17.44K</td>
<td>763 次</td>
<td class="grey">5天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4624127.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP32-E33.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">15.84K</td>
<td>1085 次</td>
<td class="grey">4天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4629724.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP34-E35.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">15.13K</td>
<td>112 次</td>
<td class="grey">11小时前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4629981.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />你迟到的许多年.DVD版.EP36-E37.2018.HD1080P.X264.AAC.Mandarin.CHS.Mp4Ba.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">15.82K</td>
<td>7 次</td>
<td class="grey">30分钟前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
</table>
</div>
<div class="grey mod" pid="31657304" style="zoom: 1;">
<div>
<span style="width: 150px; float: left; text-align: left;" class="small">24天前</span>
#5楼
</div>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-1820739.htm" target="_blank" href="you-profile-uid-1820739-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="binyue1985 6楼">
<span class="avatar_middle border bg1"></span>
</a>
</div>
<div style="word-break:break-all;">binyue1985</div>
<div class="grey">一派掌门</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<div id="message_31657997" class="message">


<p><strong><span style="color:rgb(255, 0, 0);">x264&nbsp;MP4 1080P 每集约900MB 国语中字 DVD网络版&nbsp;无水印 HQC 更至37<br /></span></strong></p><p><strong><span style="color:rgb(255, 0, 0);">BT下载</span></strong></p></div>
<br />
<script type="text/javascript" src="/cpada.js"></script>
<div class="attachlist">
<table width="100%" cellpadding="2" class="noborder">
<tr>
<td class="bold"><span class="red" style="font-size: 18px">10 </span>个附件</td>
<td width="70" class="grey">售价</td>
<td width="70" class="grey">大小</td>
<td width="70" class="grey">下载</td>
<td width="70" class="grey">时间</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625623.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP01-15.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">69.39K</td>
<td>329 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625624.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP16-17.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">20.48K</td>
<td>231 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625625.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP18-19.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">18.27K</td>
<td>217 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625626.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP20-22.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">15.85K</td>
<td>245 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625627.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP23-24.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">20.18K</td>
<td>252 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625628.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP25-27.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">15.83K</td>
<td>308 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625629.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP28-29.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">20.56K</td>
<td>280 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625630.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP30-31.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">20.59K</td>
<td>329 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4625632.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP32-33.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">19.29K</td>
<td>427 次</td>
<td class="grey">3天前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
<tr>
<td>
<a href="attach-dialog-fid-950-aid-4629982.htm" target="_blank" rel="nofollow"><img src="/view/image/filetype/torrent.gif" width="16" height="16" />The.Years.You.Were.Late.EP34-37.2018.1080p.WEB-DL.x264.AAC-HQC.torrent</a>
</td>
<td class="red">0 金币</td>
<td class="grey">20.00K</td>
<td>21 次</td>
<td class="grey">29分钟前</td>
</tr>
<tr><td colspan="6"><hr /></td></tr>
</table>
</div>
<div class="grey mod" pid="31657997" style="zoom: 1;">
<div>
<span style="width: 150px; float: left; text-align: left;" class="small">23天前</span>

#6楼
</div>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-379263.htm" target="_blank" href="you-profile-uid-379263-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="dh_lt 7楼">
<span class="avatar_middle border bg1"></span>
</a>
</div>
<div style="word-break:break-all;">dh_lt</div>
<div class="grey">武林高手</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<div id="message_31658870" class="message">


没被封杀</div>
<div class="grey mod" pid="31658870" style="zoom: 1;">
<div>
<span style="width: 150px; float: left; text-align: left;" class="small">22天前</span>
#7楼
</div>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<a href_real="you-index-uid-9173509.htm" target="_blank" href="you-profile-uid-9173509-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow" aria-label="xdwb1122 8楼">
<span class="avatar_middle border bg1" style="background-image: url(/upload/avatar/009/173/9173509_middle.gif?1398726378)"></span>
</a>
</div>
<div style="word-break:break-all;">xdwb1122</div>
<div class="grey">小有名气</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border post">
<div id="message_31661743" class="message">


<blockquote><span class="">引用 binyue1985：</span><p>这海报PS技术…………</p></blockquote><p><br /><img src="http://img.baidu.com/hi/tsj/t_0006.gif" /></p></div>
<div class="grey mod" pid="31661743" style="zoom: 1;">
<div>
<span style="width: 150px; float: left; text-align: left;" class="small">19天前</span>
#8楼
</div>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" style="margin-top: 4px;" class="post_table">
<tr>
<td width="70" valign="top">
<div>
<span class="avatar_middle border bg1"></span>
</div>
<div style="word-break:break-all;"></div>
<div class="grey small">游客组</div>
</td>
<td width="15"></td>
<td class="post_td" valign="top">
<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>
<div class="bg1 border shadow" style="padding: 8px;">
<form action="post-post-fid-950-tid-4450120-ajax-1-quickpost-1.htm" method="post" id="quick_post_form" target="_blank">
<input type="hidden" name="FORM_HASH" value="be56345e00fd703a" />
<textarea name="message" id="quick_message" style="width: 100%; height: 60px; font-size: 14px; overflow: hidden;" aria-label="快速回复内容"></textarea>
<div style="margin-top: 4px;">
<div style="width: 50%; float: left;">
<a type="submit" class="button smallblue" id="quick_post_submit" value="快速回复" href="javascript:void(0)" role="button"><span>快速回复</span></a>
</div>
<div style="width: 50%; float: left; text-align: right;">
<a href="post-post-fid-950-tid-4450120-ajax-1.htm" class="grey ajaxdialog" ajaxdialog="{cache: true}" onclick="return false;" id="create_post">高级回复</a>
</div>
</div>
</form>
</div>
</td>
</tr>
</table>
<div class="box">
<div class="page" style="text-align: center;"></div>
<p style="text-align: center; padding: 8px;">
<a type="button" value=" 返回上一页" class="button bigblue" onclick="window.location='http://www.btbtt.me/thread-index-fid-950-tid-4438445.htm';return false;" href="javascript:void(0)" role="button"><span> 返回上一页</span></a>
<a type="button" value=" 返回【剧集】" class="button bigblue" id="return_back" href="javascript:void(0)" role="button"><span> 返回【剧集】</span></a>
</p>
</div>
</div>
</div>
</div>
</div>
<div id="footer" role="contentinfo">
<table class="width">
<tr><td colspan="2"></td><tr>
<tr>
<td class="left">
© 2003-2019<br />
Powered by <a href="http://bbs.xiuno.com" target="_blank" class="grey">Xiuno BBS <b>2.1.0</b></a>
</td>
<td class="right">
京ICP备09107577号-2|京公网安备11010502023463<br />
2018-10-23 10:21, 耗时:0.0178s
</td>
</tr>
</table>
</div>
<script src="/view/js/jquery-1.4.min.js" type="text/javascript"></script>
<script src="/view/js/common.js" type="text/javascript"></script>
<script src="/view/js/dialog.js" type="text/javascript"></script>
<script type="text/javascript">
function createA(options){
	var ops = getStyleStr(options);
	var a = $('<a />');
	a.attr(ops);
	return a;
}
function createImg(options){
	var ops = getStyleStr(options);
	var img = $('<img />');
	img.attr(ops);
	return img;
}
function getStyleStr(options){
	var ops = {style:{}};
	$.extend(ops,options);
	var styleStr = '';
	if(ops && ops.style){
		$.each(ops.style,function(i,j){
			styleStr += i+':'+j+';';
		});
		ops.style = styleStr;
	}
	return ops;
}
function showAds(imgs){
	if(imgs){
		$.each(imgs,function(i,j){
			var adsObj = $('.imgs_'+i);
			var fragment = document.createDocumentFragment();
			if(adsObj && adsObj.length > 0){
				var style = {};
				if(j.position != 'n'){
					var width = 0;
					if(j.width.indexOf('%')>=0 || j.width=='auto'){
						width = j.width;
					}else{
						width = j.width+'px';
					}
					var height = 0;
					if(j.height.indexOf('%') >= 0 || j.height =='auto'){
						height = j.height;
					}else{
						height = j.height+'px';
					}
					style = {
						'position':'fixed',
						'z-index':99999,
						'width':width,
						'height':height
					};
					if(j.position_top != ''){
						style.top = (j.position_top.indexOf('%') >= 0) ? j.position_top : j.position_top+'px';
					}else if(j.position_bottom != ''){
						style.bottom = (j.position_bottom.indexOf('%') >= 0) ? j.position_bottom : j.position_bottom+'px';
					}else{
						style.top = 0;
					}
					if(j.position == 'l'){
						style.left = (j.position_left_right.indexOf('%') >= 0) ? j.position_left_right : j.position_left_right+'px';
					}else if(j.position == 'r'){
						style.right = (j.position_left_right.indexOf('%') >= 0) ? j.position_left_right : j.position_left_right+'px';
					}
					style.float = j.position;
					var o = getStyleStr({'style':style});
					adsObj.attr(o);
				}
				if(j.ads && j.ads.length > 0){
					$.each(j.ads,function(si,sj){
						var tmps = sj.margin.split(' ');
						var tmpsLen = tmps.length;
						var margin = '';
						for(var f=0;f<tmpsLen;f++){
							if(tmps[f].indexOf('%') < 0 && parseInt(tmps[f]) > 0){
								margin += parseInt(tmps[f])+'px ';
							}else{
								margin += tmps[f]+' ';
							}
						}
						var ops = {
							'float':'left',
							'margin':margin,
							'color':'red',
							'font-weight':'bolder'
						};
						var xa = null;
						if(sj.isbtn == 1 && sj.type == 2){
							ops.position = 'relative';
							var xaops = {'display':'block','position':'absolute','top':'5%','right':'3%','width':'auto','height':'auto','margin':0,'background':'#192332','color':'white','padding':'2px 5px','font-size':'5%'};
							xa = createA({'style':xaops});
							xa.html('X');
							xa.click(function(){
								$(this).parent().hide();
								return false;
							});
						}
						var a = createA({'style':ops,'title':sj.title,'href':sj.url,'target':'_blank'});
						if(xa){
							a.append(xa);
						}
						if(sj.type == 2){
							var imgops = {
									   'width':(j.width.indexOf('%') >= 0 ) ? '100%' : j.width+'px',
									   'height':(j.height.indexOf('%')>=0)? '100%' : j.height+'px'
							};
							var img = createImg({'style':imgops,'alt':sj.name,'src':sj.img});
							a.append(img);
						}else{
							a.html(sj.title);
						}
						fragment.appendChild(a[0]);
					});
					adsObj.append(fragment);
				}
			}
		});
	}
}
$(function(){
	$.getScript("/imgs.js?t="+new Date().getTime(),function(){
		showAds(imgs)
	});
});
$('#search input').focus(function() {$('#search').addClass('hover');});
$('#search input').blur(function() {$('#search').removeClass('hover');});
$('#search input').keyup(function(e) {
	if(e.which == 13 || e.which == 10) {
		var val = encodeURIComponent($(this).val());
		$('#search_form').attr('action', 'search-index-keyword-'+val+'.htm');
		$('#search_form').submit();
		return false;
	}
});

// 登陆后才能发帖
$('#create_thread').click(function() {
	if(g_uid == 0) {
		ajaxdialog_request('user-login.htm', function() {
			$('#create_thread').unbind('click');
			ajaxdialog_request($('#create_thread').attr('href'));
			$('#create_thread').click(function() {
				ajaxdialog_request($('#create_thread').attr('href'));
			});
		}, {fullicon: 1});
		return false;
	} else {
		ajaxdialog_request($('#create_thread').attr('href'), null);
		return false;
	}
});

$('a.ajaxdialog, input.ajaxdialog').die('click').live('click', ajaxdialog_click);
$('a.ajaxtoggle').die('click').live('click', ajaxtoggle_event);

//$('div.list .table tr:odd').not('tr.header').addClass('odd');	/* 奇数行的背景色 */
//$('div.list .table tr:last').addClass('last');	/* 奇数行的背景色 */


</script>










<script>
// 判断头部是否换行，修正版块过多，将 forum-list.htm 挤下去的问题。
var forumlistpos = $('#menu_forum_list').offset();
var rightpos = $('#menu td.center2').offset();
if(forumlistpos.top - rightpos.top > 8) {
	var h = $('#menu_forum_list').height() - 3;
	$('#menu_forum_list').css({position: 'absolute', height: h});//, left: rightpos.left - 50, top: rightpos.top, 
}
</script>
<div style="display:none">
<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1260924983'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s4.cnzz.com/z_stat.php%3Fid%3D1260924983' type='text/javascript'%3E%3C/script%3E"));</script>
</div>
<div style="display:none">
<a href="http://www.btbtt.co/aff/setmap.html">地图</a>
<script language="javascript" type="text/javascript" src="http://js.users.51.la/17773989.js"></script>
</div>




<script type="text/javascript">

tid_add_read(4450120, 1540261310);

$('#create_post').click(function() {
	if(g_uid == 0) {
		ajaxdialog_request('user-login.htm', function() {
			$('#create_post').unbind('click');
			ajaxdialog_request($('#create_post').attr('href'));
			$('#create_post').click(function() {
				ajaxdialog_request($('#create_post').attr('href'));
			});
		});
		return false;
	} else {
		return true;
	}
});

// 点击数服务器
$.getScript('http://www.btbtt.me/service/clickd/?db=tid&w=4450120&r=4450120&'+Math.random(), function() {
	if(typeof xn_json == 'undefined') return;
	var json = xn_json;
	$('#thread_views').html(json['4450120']);
});

// 自动伸缩，自动提交
$('#quick_message').keyup(function(e) {
	if((e.ctrlKey && (e.which == 13 || e.which == 10)) || (e.altKey && e.which == 83)) {
		$('#quick_post_submit').trigger('click');
		return false;
	}
        
	var h = $(this)[0].scrollHeight;
	if(h <= 100) {
		return true;
	} else {
		$(this).height($(this)[0].scrollHeight);
		return true;
	}
});

// 快速回复
$('#quick_post_submit').click(function() {
	if(!$('#quick_message').val()) {
		$('#quick_message').alert('请填写内容！', {width: 150, delay: 3000}).focus();
		return false;
	}
	$('#quick_post_submit').disable();
	
	function quick_post_submit_func() {
		var postdata = $("#quick_post_form").serialize();
		$.post($('#quick_post_form').attr('action'), postdata,  function(s){
			var json = json_decode(s);
			if(error = json_error(json)) {alert(error); return false;}
			if(json.status <= 0) {
				alert(json.message);
				return false;
			} else {
				json = json.message;
				if(json.message) {
					$('#quick_message').alert(json.message, {width:250, delay: 3000}).focus();
					return false;
				}

				
				//var page = Math.max(1, intval(json.page));
				//window.location= 'thread-index-fid-950-tid-4450120-page-'+page+'-scrollbottom-1.htm';
				
				var post = json.post;
				// 结果直接显示在上面，不再跳转
				var s = '<table border="0" cellpadding="0" cellspacing="0" width="100%" align="center" class="post_table">\
					<tr>\
						<td width="70" valign="top">\
							<div>\
								<a href_real="you-index-uid-0.htm" target="_blank" href="you-profile-uid-0-ajax-1.htm" class="ajaxdialog_hover" ajaxdialog="{position: 5, modal: false, timeout: 1000, showtitle: false}" onclick="return false;" style="display: block" rel="nofollow">\
									<span class="avatar_middle border bg1" ></span>\
								</a>\
							</div>\
							<div style="word-break:break-all;" aria-label="'+post.username+' '+post.posts+'楼">'+post.username+'</div>\
						</td>\
						<td width="15"></td>\
						<td class="post_td" valign="top">\
							<span class="icon icon-left-arrow" style="position: absolute; z-index: 9; float: left; margin-left: -9px; margin-top: 10px;"></span>\
							<div class="bg1 border post">\
								<div id="message_'+post.pid+'" class="message">'+post.message+'</div>\
							</div>\
						</td>\
					</tr>\
				</table>';
				var jtable = $(s);
				$('table.post_table:last').before(jtable);
				//jtable.message = post.message;
				$('#quick_message').val('').focus();
				
				$('#quick_post_submit').enable();
			}
		});
	}

	if(g_uid == 0) {
		ajaxdialog_request('user-login.htm', function() {
			quick_post_submit_func();
			return false;
		});
	} else {
		quick_post_submit_func();
		return false;
	}
});

// 滚动回复的到最底部

// 记录当前页码
var fid_page = $.parseJSON($.pdata(cookie_pre + 'fid_page'));
var page = fid_page ? fid_page[''+950] : 1;
var href = $('#forum_link').attr('href').replace(/page-1/ig, "page-"+page);
$('#forum_link').attr('href', href);
$('#return_back').click(function() {
	window.location = href;
});

// 鼠标放在头像上弹出用户信息 ajaxdialog_hover
var jajaxdialoglinks = $('a.ajaxdialog_hover');
jajaxdialoglinks.die('click').live('click', function() {window.open($(this).attr('href_real'))});
jajaxdialoglinks.die('mouseover').live('mouseover', ajaxdialog_mouseover);
jajaxdialoglinks.die('mouseout').live('mouseout', ajaxdialog_mouseout);
$('a.ajaxconfirm').die('click').live('click', ajaxdialog_confirm);

// post_td 下的图片调整大小
$(function() {
	var td_width = $('td.post_td').width() - 28;
	td_width = Math.min($('#body').width() - 170, td_width);
	$('td.post_td img').each(function() {
		if($(this).width() > td_width) {
			this.height = Math.ceil((this.height /this.width) * td_width);
			this.width = Math.ceil(td_width);
			
			this.style.cursor = 'pointer';
			this.onclick = function() {
				window.open(this.src);
			}
		}
	});
});

// 快捷键翻页
bind_document_keyup_page();
$('div.post').each(function(i) {
	var _this = this;
	$(_this).hover(
		function() {
			$(_this).find('div.mod div').show().css('opacity', 0).stop().animate({opacity:1}, 500);
		},
		function() {
			$(_this).find('div.mod div').animate({opacity:0}, 500);
		}
	)
});
</script>
<script>

// 锁贴
$('#mod_lock').click(function() {
	var fid_tids = '';
	$.each($('#body input[name="fid_tid[]"]:checked'), function(k, v) {
		fid_tids += (fid_tids ? '__' : '') + v.value;
	});
	var url = url_add_arg('mod-lock-fid-950.htm', 'fid_tids', fid_tids);
	ajaxdialog_request(url, function() {
		window.location = 'forum-index-fid-950.htm';
	});
});


// 判断是否锁帖

</script>
</body>
</html>
"""


for 行 in 内容.split('\n'):
   if 'script' not in 行 and '◎'in 行 and 'title='in 行 and 'src='in 行:
      print(行)




