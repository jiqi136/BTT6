# -*- coding:utf-8

import re  # 正则式

文本="""
E:\python3an\an\python.exe E:/PY学习文件/BTT影视剧/测试.py
{'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/666.3(KHTML,likeGecko)Chrome/79.0.1063.0Safari/536.3'}
成功采集网页： https://www.baidu.com/baidu?wd=ip&tn=monline_4_dg&ie=utf-8
网页采集,全部完成
返回网页内容
 <!DOCTYPE html>
<!--STATUS OK-->
























































	















<html>
	<head>
		
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<meta http-equiv="content-type" content="text/html;charset=utf-8">
		<meta content="always" name="referrer">
        <meta name="theme-color" content="#2932e1">
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
        <link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">
        <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" />
		
		
<title>ip_百度搜索</title>

		

		
<style data-for="result" type="text/css" id="css_newi_result">body{color:#333;background:#fff;padding:6px 0 0;margin:0;position:relative;min-width:900px}
body,th,td,.p1,.p2{font-family:arial}
p,form,ol,ul,li,dl,dt,dd,h3{margin:0;padding:0;list-style:none}
input{padding-top:0;padding-bottom:0;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;box-sizing:border-box}
table,img{border:0}
td{font-size:9pt;line-height:18px}
em{font-style:normal;color:#c00}
a em{text-decoration:underline}
cite{font-style:normal;color:green}
.m,a.m{color:#666}
a.m:visited{color:#606}
.g,a.g{color:green}
.c{color:#77c}
.f14{font-size:14px}
.f10{font-size:10.5pt}
.f16{font-size:16px}
.f13{font-size:13px}
.bg{background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_5859e57.png);_background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_d5b04cc.gif);background-repeat:no-repeat}
#u,#head,#tool,#search,#foot{font-size:12px}
.logo{width:117px;height:38px;cursor:pointer}
.p1{line-height:120%;margin-left:-12pt}
.p2{width:100%;line-height:120%;margin-left:-12pt}
#wrapper{_zoom:1}
#container{word-break:break-all;word-wrap:break-word;position:relative}
.container_s{width:1002px}
.container_l{width:1222px}
#content_left{width:636px;float:left;padding-left:35px}
#content_right{border-left:1px solid #e1e1e1;float:right}
.container_s #content_right{width:271px}
.container_l #content_right{width:434px}
.content_none{padding-left:35px}
#u{color:#999;white-space:nowrap;position:absolute;right:10px;top:4px;z-index:299}
#u a{color:#00c;margin:0 5px}
#u .reg{margin:0}
#u .last{margin-right:0}
#u .un{font-weight:700;margin-right:5px}
#u ul{width:100%;background:#fff;border:1px solid #9b9b9b}
#u li{height:25px}
#u li a{width:100%;height:25px;line-height:25px;display:block;text-align:left;text-decoration:none;text-indent:6px;margin:0;filter:none\9}
#u li a:hover{background:#ebebeb}
#u li.nl{border-top:1px solid #ebebeb}
#user{display:inline-block}
#user_center{position:relative;display:inline-block}
#user_center .user_center_btn{margin-right:5px}
.userMenu{width:64px;position:absolute;right:7px;_right:2px;top:15px;top:14px\9;*top:15px;padding-top:4px;display:none;*background:#fff}
#head{padding-left:35px;margin-bottom:20px;width:900px}
.fm{clear:both;position:relative;z-index:297}
.nv a,.nv b,.btn,#page,#more{font-size:14px}
.s_nav{height:45px}
.s_nav .s_logo{margin-right:20px;float:left}
.s_nav .s_logo img{border:0;display:block}
.s_tab{line-height:18px;padding:20px 0 0;float:left}
.s_nav a{color:#00c;font-size:14px}
.s_nav b{font-size:14px}
.s_ipt_wr{width:536px;height:30px;display:inline-block;margin-right:5px;background-position:0 -96px;border:1px solid #b6b6b6;border-color:#7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;vertical-align:top}
.s_ipt{width:523px;height:22px;font:16px/18px arial;line-height:22px;margin:5px 0 0 7px;padding:0;background:#fff;border:0;outline:0;-webkit-appearance:none}
.s_btn{width:95px;height:32px;padding-top:2px\9;font-size:14px;padding:0;background-color:#ddd;background-position:0 -48px;border:0;cursor:pointer}
.s_btn_h{background-position:-240px -48px}
.s_btn_wr{width:97px;height:34px;display:inline-block;background-position:-120px -48px;*position:relative;z-index:0;vertical-align:top}
.sethf{padding:0;margin:0;font-size:14px}
.set_h{display:none;behavior:url(#default#homepage)}
.set_f{display:none}
.shouji{margin-left:19px}
.shouji a{text-decoration:none}
#head .bdsug{top:33px}
#search form{position:relative}
#search form .bdsug{bottom:33px}
.bdsug{display:none;position:absolute;z-index:1;width:538px;background:#fff;border:1px solid #ccc;_overflow:hidden;box-shadow:1px 1px 3px #ededed;-webkit-box-shadow:1px 1px 3px #ededed;-moz-box-shadow:1px 1px 3px #ededed;-o-box-shadow:1px 1px 3px #ededed}
.bdsug.bdsugbg ul{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/sugbg_1762fe7.png) 100% 100% no-repeat;background-size:100px 110px;background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/sugbg_90fc9cf.gif)\9}
.bdsug li{width:522px;color:#000;font:14px arial;line-height:22px;padding:0 8px;position:relative;cursor:default}
.bdsug li.bdsug-s{background:#f0f0f0}
.bdsug-store span,.bdsug-store b{color:#7A77C8}
.bdsug-store-del{font-size:12px;color:#666;text-decoration:underline;position:absolute;right:8px;top:0;cursor:pointer;display:none}
.bdsug-s .bdsug-store-del{display:inline-block}
.bdsug-ala{display:inline-block;border-bottom:1px solid #e6e6e6}
.bdsug-ala h3{line-height:14px;background:url(//www.baidu.com/img/sug_bd.png) no-repeat left center;margin:8px 0 5px;font-size:12px;font-weight:400;color:#7B7B7B;padding-left:20px}
.bdsug-ala p{font-size:14px;font-weight:700;padding-left:20px}
.bdsug .bdsug-direct{width:auto;padding:0;border-bottom:1px solid #f1f1f1}
.bdsug .bdsug-direct p{color:#00c;font-weight:700;line-height:34px;padding:0 8px;cursor:pointer;white-space:nowrap;overflow:hidden}
.bdsug .bdsug-direct p img{width:16px;height:16px;margin:7px 6px 9px 0;vertical-align:middle}
.bdsug .bdsug-direct p span{margin-left:8px}
.bdsug .bdsug-direct p i{font-size:12px;line-height:100%;font-style:normal;font-weight:400;color:#fff;background-color:#2b99ff;display:inline;text-align:center;padding:1px 5px;*padding:2px 5px 0;margin-left:8px;overflow:hidden}
.bdsug .bdsug-pcDirect{color:#000;font-size:14px;line-height:30px;height:30px;background-color:#f8f8f8}
.bdsug .bdsug-pc-direct-tip{position:absolute;right:15px;top:8px;width:55px;height:15px;display:block;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/pc_direct_42d6311.png) no-repeat 0 0}
.bdsug li.bdsug-pcDirect-s{background-color:#f0f0f0}
.bdsug .bdsug-pcDirect-is{color:#000;font-size:14px;line-height:22px;background-color:#f8f8f8}
.bdsug .bdsug-pc-direct-tip-is{position:absolute;right:15px;top:3px;width:55px;height:15px;display:block;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/pc_direct_42d6311.png) no-repeat 0 0}
.bdsug li.bdsug-pcDirect-is-s{background-color:#f0f0f0}
.bdsug .bdsug-pcDirect-s .bdsug-pc-direct-tip,.bdsug .bdsug-pcDirect-is-s .bdsug-pc-direct-tip-is{background-position:0 -15px}
.bdsug .bdsug-newicon{color:#929292;opacity:.7;font-size:12px;display:inline-block;line-height:22px;letter-spacing:2px}
.bdsug .bdsug-s .bdsug-newicon{opacity:1}
.bdsug .bdsug-newicon i{letter-spacing:0;font-style:normal}
.bdsug .bdsug-feedback-wrap{text-align:right;background:#fafafa;color:#666;height:25px;line-height:27px}
.bdsug .bdsug-feedback{margin-right:10px;text-decoration:underline;color:#666}
.toggle-underline{text-decoration:none}
.toggle-underline:hover{text-decoration:underline}
#tb_mr{color:#00c;cursor:pointer;position:relative;z-index:298}
#tb_mr b{font-weight:400;text-decoration:underline}
#tb_mr small{font-size:11px}
#page{font:14px arial;white-space:nowrap;padding-left:35px}
#page a,#page strong{display:inline-block;vertical-align:text-bottom;height:66px;text-align:center;line-height:34px;text-decoration:none;overflow:hidden;margin-right:9px;background:#fff}
#page a{cursor:pointer}
#page a:hover{background:0 0}
#page .n:hover,#page a:hover .pc{background:#f2f8ff;border:1px solid #38f}
#page .n{height:34px;padding:0 18px;border:1px solid #e1e2e3}
#page span{display:block}
#page .pc{width:34px;height:34px;border:1px solid #e1e2e3;cursor:pointer}
#page .fk{width:24px;height:24px;margin-bottom:6px;margin-left:6px;cursor:pointer}
#page strong .fk,#page strong .pc{cursor:auto}
#page .fk .c-icon-bear-pn{top:-3px;position:relative}
#page .fkd .c-icon-bear-pn{top:3px;position:relative}
#page .fk_cur .c-icon-bear-p{top:-2px;position:relative}
#page strong .pc{border:0;width:36px;height:36px;line-height:36px}
#page .nums{display:inline-block;vertical-align:text-bottom;height:36px;line-height:36px;margin-left:10px}
#rs{width:900px;background:#fff;padding:8px 0;margin:20px 0 0 15px}
#rs td{width:5%}
#rs th{font-size:14px;font-weight:400;line-height:19px;white-space:nowrap;text-align:left;vertical-align:top}
#rs .tt{font-weight:700;padding:0 10px 0 20px}
#rs_top{font-size:14px;margin-bottom:22px}
#rs_top a{margin-right:18px}
#container .rs{margin:30px 0 20px;padding:5px 0 15px;font-size:14px;width:540px;padding-left:121px;position:relative;background-color:#fafafa}
#container .noback{background-color:#fff}
#content_left .rs{margin-left:-121px}
#container .rs table{width:540px}
#container .rs td{width:5px}
#container .rs th{font-size:14px;font-weight:400;white-space:nowrap;text-align:left;vertical-align:top;width:175px;line-height:22px}
#container .rs .tt{font-weight:700;padding:0 10px 0 20px;padding:0;line-height:30px;font-size:16px}
#container .rs a{margin:0;height:24px;width:173px;display:inline-block;line-height:25px;border:1px solid #ebebeb;text-align:center;vertical-align:middle;overflow:hidden;outline:0;color:#333;background-color:#fff;text-decoration:none}
#container .rs a:hover{border-color:#388bff}
.c-tip-con .c-tip-menu-b ul{width:100px}
.c-tip-con .c-tip-menu-b ul{text-align:center}
.c-tip-con .c-tip-menu-b li a{display:block;text-decoration:none;cursor:pointer;background-color:#fff;padding:3px 0;color:#666}
.c-tip-con .c-tip-menu-b li a:hover{display:block;background-color:#ebebeb}
#search{width:900px;padding:35px 0 16px 35px}
#search .s_help{position:relative;top:10px}
#foot{height:20px;line-height:20px;color:#77c;background:#e6e6e6;text-align:center}
#foot span{color:#666}
.site_tip{font-size:12px;margin-bottom:20px}
.site_tip_icon{width:56px;height:56px;background:url(//www.baidu.com/aladdin/img/tools/tools-3.png) -288px 0 no-repeat}
.to_zhidao,.to_tieba,.to_zhidao_bottom{font-size:16px;line-height:24px;margin:20px 0 0 35px}
.to_tieba .c-icon-tieba{float:left}
.f{line-height:115%;*line-height:120%;font-size:100%;width:33.7em;word-break:break-all;word-wrap:break-word}
.h{margin-left:8px;width:100%}
.r{word-break:break-all;cursor:hand;width:238px}
.t{font-weight:400;font-size:medium;margin-bottom:1px}
.pl{padding-left:3px;height:8px;padding-right:2px;font-size:14px}
.mo,a.mo:link,a.mo:visited{color:#666;font-size:100%;line-height:10px}
.htb{margin-bottom:5px}
.jc a{color:#c00}
a font[size="3"] font,font[size="3"] a font{text-decoration:underline}
div.blog,div.bbs{color:#707070;padding-top:2px;font-size:13px}
.result{width:33.7em;table-layout:fixed}
.result-op .f{word-wrap:normal}
.nums{font-size:12px;color:#999}
.tools{position:absolute;top:10px;white-space:nowrap}
#mHolder{width:62px;position:relative;z-index:296;top:-18px;margin-left:9px;margin-right:-12px;display:none}
#mCon{height:18px;position:absolute;top:3px;top:6px\9;cursor:pointer;line-height:18px}
.wrapper_l #mCon{right:7px}
#mCon span{color:#00c;display:block}
#mCon .hw{text-decoration:underline;cursor:pointer;display:inline-block}
#mCon .pinyin{display:inline-block}
#mCon .c-icon-chevron-unfold2{margin-left:5px}
#mMenu{width:56px;border:1px solid #9b9b9b;position:absolute;right:7px;top:23px;display:none;background:#fff}
#mMenu a{width:100%;height:100%;color:#00c;display:block;line-height:22px;text-indent:6px;text-decoration:none;filter:none\9}
#mMenu a:hover{background:#ebebeb}
#mMenu .ln{height:1px;background:#ebebeb;overflow:hidden;font-size:1px;line-height:1px;margin-top:-1px}
.op_LAMP{background:url(//www.baidu.com/cache/global/img/aladdinIcon-1.0.gif) no-repeat 0 2px;color:#77C;display:inline-block;font-size:13px;height:12px;*height:14px;width:16px;text-decoration:none;zoom:1}
.EC_mr15{margin-left:0}
.pd15{padding-left:0}
.map_1{width:30em;font-size:80%;line-height:145%}
.map_2{width:25em;font-size:80%;line-height:145%}
.favurl{background-repeat:no-repeat;background-position:0 1px;padding-left:20px}
.dan_tip{font-size:12px;margin-top:4px}
.dan_tip a{color:#b95b07}
#more,#u ul,#mMenu,.msg_holder{box-shadow:1px 1px 2px #ccc;-moz-box-shadow:1px 1px 2px #ccc;-webkit-box-shadow:1px 1px 2px #ccc;filter:progid:DXImageTransform.Microsoft.Shadow(Strength=2, Direction=135, Color=#cccccc)\9}
.hit_top{line-height:18px;margin:0 15px 10px 0;width:516px}
.hit_top .c-icon-bear{height:18px;margin-right:4px}
#rs_top_new,.hit_top_new{width:538px;font-size:13px;line-height:1.54;word-wrap:break-word;word-break:break-all;margin:0 0 14px}
.zhannei-si{margin:0 0 10px 121px}
.zhannei-si-none{margin:10px 0 -10px 121px}
.zhannei-search{margin:10px 0 0 121px;color:#999;font-size:14px}
.f a font[size="3"] font,.f font[size="-1"] a font{text-decoration:underline}
h3 a font{text-decoration:underline}
.c-title{font-weight:400;font-size:16px}
.c-title-size{font-size:16px}
.c-abstract{font-size:13px}
.c-abstract-size{font-size:13px}
.c-showurl{color:green;font-size:13px}
.c-showurl-color{color:green}
.c-cache-color{color:#666}
.c-lightblue{color:#77c}
.c-highlight-color{color:#c00}
.c-clearfix:after{content:".";display:block;height:0;clear:both;visibility:hidden}
.c-clearfix{zoom:1}
.c-wrap{word-break:break-all;word-wrap:break-word}
.c-icons-outer{overflow:hidden;display:inline-block;vertical-align:bottom;*vertical-align:-1px;_vertical-align:bottom}
.c-icons-inner{margin-left:-4px}
.c-container table.result,.c-container table.result-op{width:100%}
.c-container td.f{font-size:13px;line-height:1.54;width:auto}
.c-container .vd_newest_main{width:auto}
.c-customicon{display:inline-block;width:16px;height:16px;vertical-align:text-bottom;font-style:normal;overflow:hidden}
.c-tip-icon i{display:inline-block;cursor:pointer}
.c-tip-con{position:absolute;z-index:1;top:22px;left:-35px;background:#fff;border:1px solid #dcdcdc;border:1px solid rgba(0,0,0,.2);-webkit-transition:opacity .218s;transition:opacity .218s;-webkit-box-shadow:0 2px 4px rgba(0,0,0,.2);box-shadow:0 2px 4px rgba(0,0,0,.2);padding:5px 0;display:none;font-size:12px;line-height:20px}
.c-tip-arrow{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;top:-16px}
.c-tip-arrow-down{top:auto;bottom:0}
.c-tip-arrow em,.c-tip-arrow ins{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;border:8px solid transparent;border-style:dashed dashed solid}
.c-tip-arrow em{border-bottom-color:#d8d8d8}
.c-tip-arrow ins{border-bottom-color:#fff;top:2px}
.c-tip-arrow-down em,.c-tip-arrow-down ins{border-style:solid dashed dashed;border-color:transparent}
.c-tip-arrow-down em{border-top-color:#d8d8d8}
.c-tip-arrow-down ins{border-top-color:#fff;top:-2px}
.c-tip-arrow .c-tip-arrow-r{border-bottom-color:#82c9fa;top:2px}
.c-tip-arrow-down .c-tip-arrow-r{border-bottom-color:transparent;top:-2px}
.c-tip-arrow .c-tip-arrow-c{border-bottom-color:#fecc47;top:2px}
.c-tip-arrow-down .c-tip-arrow-c{border-bottom-color:transparent;top:-2px}
.c-tip-con h3{font-size:12px}
.c-tip-con .c-tip-title{margin:0 10px;display:inline-block;width:239px}
.c-tip-con .c-tip-info{color:#666;margin:0 10px 1px;width:239px}
.c-tip-con .c-tip-cer{width:370px;color:#666;margin:0 10px 1px}
.c-tip-con .c-tip-title{width:auto;_width:354px}
.c-tip-con .c-tip-item-i{padding:3px 0 3px 20px;line-height:14px}
.c-tip-con .c-tip-item-i .c-tip-item-icon{margin-left:-20px}
.c-tip-con .c-tip-menu ul{width:74px}
.c-tip-con .c-tip-menu ul{text-align:center}
.c-tip-con .c-tip-menu li a{display:block;text-decoration:none;cursor:pointer;background-color:#fff;padding:3px 0;color:#0000d0}
.c-tip-con .c-tip-menu li a:hover{display:block;background-color:#ebebeb}
.c-tip-con .c-tip-notice{width:239px;padding:0 10px}
.c-tip-con .c-tip-notice .c-tip-notice-succ{color:#4cbd37}
.c-tip-con .c-tip-notice .c-tip-notice-fail{color:#f13F40}
.c-tip-con .c-tip-notice .c-tip-item-succ{color:#444}
.c-tip-con .c-tip-notice .c-tip-item-fail{color:#aaa}
.c-tip-con .c-tip-notice .c-tip-item-fail a{color:#aaa}
.c-tip-close{right:10px;position:absolute;cursor:pointer}
.ecard{height:86px;overflow:hidden}
.c-tools{display:inline}
.c-tools-share{width:239px;padding:0 10px}
.c-fanyi{display:none;width:20px;height:20px;border:solid 1px #d1d1d1;cursor:pointer;position:absolute;margin-left:516px;text-align:center;color:#333;line-height:22px;opacity:.9;background-color:#fff}
.c-fanyi:hover{background-color:#39f;color:#fff;border-color:#39f;opacity:1}
.c-fanyi-title,.c-fanyi-abstract{display:none}
.icp_info{color:#666;margin-top:2px;font-size:13px}
.icon-gw,.icon-unsafe-icon{background:#2c99ff;vertical-align:text-bottom;*vertical-align:baseline;height:16px;padding-top:0;padding-bottom:0;padding-left:6px;padding-right:6px;line-height:16px;_padding-top:2px;_height:14px;_line-height:14px;font-size:12px;font-family:simsun;margin-left:10px;overflow:hidden;display:inline-block;-moz-border-radius:1px;-webkit-border-radius:1px;border-radius:1px;color:#fff}
a.icon-gw{color:#fff;background:#2196ff;text-decoration:none;cursor:pointer}
a.icon-gw:hover{background:#1e87ef}
a.icon-gw:active{height:15px;_height:13px;line-height:15px;_line-height:13px;padding-left:5px;background:#1c80d9;border-left:1px solid #145997;border-top:1px solid #145997}
.icon-unsafe-icon{background:#e54d4b}
#con-at{margin-bottom:9px;padding-left:121px;border-bottom:1px #ebebeb solid}
#con-at .result-op{font-size:13px;line-height:1.52em}
.wrapper_l #con-at .result-op{width:1058px}
.wrapper_s #con-at .result-op{width:869px}
#con-ar{margin-bottom:40px}
#con-ar .result-op{margin-bottom:28px;font-size:13px;line-height:1.52em}
.result_hidden{position:absolute;top:-10000px;left:-10000px}
#content_left .result-op,#content_left .result{margin-bottom:14px;border-collapse:collapse}
#content_left .c-border .result-op,#content_left .c-border .result{margin-bottom:25px}
#content_left .c-border .result-op:last-child,#content_left .c-border .result:last-child{margin-bottom:12px}
#content_left .result .f,#content_left .result-op .f{padding:0}
.subLink_factory{border-collapse:collapse}
.subLink_factory td{padding:0}
.subLink_factory td.middle,.subLink_factory td.last{color:#666}
.subLink_factory td a{text-decoration:underline}
.subLink_factory td.rightTd{text-align:right}
.subLink_factory_right{width:100%}
.subLink_factory_left td{padding-right:26px}
.subLink_factory_left td.last{padding:0}
.subLink_factory_left td.first{padding-right:75px}
.subLink_factory_right td{width:90px}
.subLink_factory_right td.first{width:auto}
.general_image_pic a{background:#fff no-repeat center center;text-decoration:none;display:block;overflow:hidden;text-align:left}
.res_top_banner{height:36px;text-align:left;border-bottom:1px solid #e3e3e3;background:#f7f7f7;font-size:13px;padding-left:8px;color:#333;position:relative;z-index:302}
.res_top_banner span{_zoom:1}
.res_top_banner .res_top_banner_icon{background-position:0 -216px;width:18px;height:18px;margin:9px 10px 0 0}
.res_top_banner .res_top_banner_icon_baiduapp{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/baiduappLogo_de45621.png) no-repeat 0 0;width:24px;height:24px;margin:3px 10px 0 0;position:relative;top:3px}
.res_top_banner .res_top_banner_icon_windows{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/winlogo_e925689.png) no-repeat 0 0;width:18px;height:18px;margin:9px 10px 0 0}
.res_top_banner .res_top_banner_download{display:inline-block;width:65px;line-height:21px;_padding-top:1px;margin:0 0 0 10px;color:#333;background:#fbfbfb;border:1px solid #b4b6b8;text-align:center;text-decoration:none}
.res_top_banner .res_top_banner_download:hover{border:1px solid #38f}
.res_top_banner .res_top_banner_download:active{background:#f0f0f0;border:1px solid #b4b6b8}
.res_top_banner .res_top_banner_close{background-position:-672px -144px;cursor:pointer;position:absolute;right:10px;top:10px}
.res_top_banner_for_win{height:34px;text-align:left;border-bottom:1px solid #f0f0f0;background:#fdfdfd;font-size:13px;padding-left:12px;color:#333;position:relative;z-index:302}
.res_top_banner_for_win span{_zoom:1;color:#666}
.res_top_banner_for_win .res_top_banner_download{display:inline-block;width:auto;line-height:21px;_padding-top:1px;margin:0 0 0 16px;color:#333;text-align:left;text-decoration:underline}
.res_top_banner_for_win .res_top_banner_icon_windows{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/winlogo_e925689.png) no-repeat 0 0;width:18px;height:18px;margin:8px 8px 0 0}
.res_top_banner_for_win .res_top_banner_close{background-position:-672px -144px;cursor:pointer;position:absolute;right:10px;top:10px}
.res-gap-right16{margin-right:16px}
.res-border-top{border-top:1px solid #f3f3f3}
.res-border-bottom{border-bottom:1px solid #f3f3f3}
.res-queryext-pos{position:relative;top:1px;_top:0}
.c-trust-ecard{height:86px;_height:97px;overflow:hidden}
@-moz-document url-prefix(){.result,.f{width:538px}}
body{min-width:1000px}
#ftCon{display:none}
#qrcode{display:none}
#pad-version{display:none}
#index_guide{display:none}
#index_logo{display:none}
#u1{display:none}
.s_ipt_wr{height:32px}
body{padding:0}
.s_form:after,.s_tab:after{content:".";display:block;height:0;clear:both;visibility:hidden}
.s_form{zoom:1;height:55px;padding:0 0 0 10px}
#result_logo{float:left;margin:7px 0 0}
#result_logo img{width:101px}
#head{padding:0;margin:0;width:100%;position:absolute;z-index:301;min-width:1000px;background:#fff;border-bottom:1px solid #ebebeb;position:fixed;_position:absolute;-webkit-transform:translateZ(0)}
#head .head_wrapper{_width:1000px}
#head.s_down{box-shadow:0 0 5px #888}
.fm{clear:none;float:left;margin:11px 0 0 10px}
#s_tab{background:#f8f8f8;line-height:36px;height:38px;padding:55px 0 0 121px;float:none;zoom:1}
#s_tab a,#s_tab b{width:54px;display:inline-block;text-decoration:none;text-align:center;color:#666;font-size:14px}
#s_tab b{border-bottom:2px solid #38f;font-weight:700;color:#323232}
#s_tab a:hover{color:#323232}
#content_left{width:540px;padding-left:121px;padding-top:5px}
#content_right{margin-top:45px}
#content_bottom{width:540px;padding-left:121px}
#page{padding:0 0 0 121px;margin:30px 0 40px}
.to_tieba,.to_zhidao_bottom{margin:10px 0 0 121px;padding-top:5px}
.nums{margin:0 0 0 121px;height:42px;line-height:42px}
#rs{padding:0;margin:6px 0 0 121px;width:600px}
#rs th{width:175px;line-height:22px}
#rs .tt{padding:0;line-height:30px}
#rs td{width:5px}
#rs table{width:540px}
#help{background:#f5f6f5;zoom:1;padding:0 0 0 50px;float:right}
#help a{color:#777;padding:0 15px;text-decoration:none}
#help a:hover{color:#333}
#foot{background:#f5f6f5;border-top:1px solid #ebebeb;text-align:left;height:42px;line-height:42px;margin-top:40px;*margin-top:0}
#foot .foot_c{float:left;padding:0 0 0 121px}
.content_none{padding:45px 0 25px 121px}
.nors p{font-size:18px;font-family:microsoft yahei;color:#000}
.nors p em{color:#c00}
.nors .tip_head{color:#666;font-size:13px;line-height:28px}
.nors li{color:#333;line-height:28px;font-size:13px;font-family:'宋体';padding-left:30px;list-style-position:inside;list-style-type:disc}
#mCon{top:5px}
.s_ipt_wr.bg,.s_btn_wr.bg,#su.bg{background-image:none}
.s_ipt_wr.bg{background:0 0}
.s_btn_wr{width:auto;height:auto;border-bottom:1px solid transparent;*border-bottom:0}
.s_btn{width:100px;height:34px;color:#fff;letter-spacing:1px;background:#3385ff;border-bottom:1px solid #2d78f4;outline:medium;*border-bottom:0;-webkit-appearance:none;-webkit-border-radius:0}
.s_btn.btnhover{background:#317ef3;border-bottom:1px solid #2868c8;*border-bottom:0;box-shadow:1px 1px 1px #ccc}
.s_btn_h{background:#3075dc;box-shadow:inset 1px 1px 3px #2964bb;-webkit-box-shadow:inset 1px 1px 3px #2964bb;-moz-box-shadow:inset 1px 1px 3px #2964bb;-o-box-shadow:inset 1px 1px 3px #2964bb}
#wrapper_wrapper .container_l .EC_ppim_top,#wrapper_wrapper .container_xl .EC_ppim_top{width:640px}
#wrapper_wrapper .container_s .EC_ppim_top{width:570px}
#head .c-icon-bear-round{display:none}
.container_l #content_right{width:384px}
.container_l{width:1212px}
.container_xl #content_right{width:384px}
.container_xl{width:1257px}
.index_tab_top{display:none}
.index_tab_bottom{display:none}
#lg{display:none}
#m{display:none}
#ftCon{display:none}
#ent_sug{position:absolute;margin:141px 0 0 130px;font-size:13px;color:#666}
.foot_fixed_bottom{position:fixed;bottom:0;width:100%;_position:absolute;_bottom:auto}
#head .headBlock{margin:-5px 0 6px 121px}
#content_left .leftBlock{margin-bottom:14px;padding-bottom:5px;border-bottom:1px solid #f3f3f3}
.hint_toprq_tips{position:relative;width:537px;height:19px;line-height:19px;overflow:hidden;display:none}
.hint_toprq_tips span{color:#666}
.hint_toprq_icon{margin:0 4px 0 0}
.hint_toprq_tips_items{width:444px;_width:440px;max-height:38px;position:absolute;left:95px;top:1px}
.hint_toprq_tips_items div{display:inline-block;float:left;height:19px;margin-right:18px;white-space:nowrap;word-break:keep-all}
.translateContent{max-width:350px}
.translateContent .translateTool{height:16px;margin:-3px 2px}
.translateContent .action-translate,.translateContent .action-search{display:inline-block;width:20px;height:16px;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/translate_tool_icon_57087b6.gif) no-repeat}
.translateContent .action-translate{background-position:0 0;border-right:1px solid #dcdcdc}
.translateContent .action-translate:hover{background-position:0 -20px}
.translateContent .action-search{background-position:-20px 0}
.translateContent .action-search:hover{background-position:-20px -20px}
.nums{width:538px}
.search_tool{_padding-top:15px}
.head_nums_cont_outer{height:40px;overflow:hidden;position:relative}
.head_nums_cont_inner{position:relative}
.search_tool_conter .c-gap-left{margin-left:23px}
.search_tool_conter .c-icon-triangle-down{opacity:.6}
.search_tool_conter .c-icon-triangle-down:hover{opacity:1}
.search_tool,.search_tool_close{float:right}
.search_tool,.search_tool_conter span{cursor:pointer;color:#666}
.search_tool:hover,.search_tool_conter span:hover{color:#333}
.search_tool_conter{font-size:12px;color:#666;margin:0 0 0 121px;height:42px;width:538px;line-height:42px;*height:auto;*line-height:normal;*padding:14px 0}
.search_tool_conter span strong{color:#666}
.c-tip-con .c-tip-langfilter ul{width:80px;text-align:left;color:#666}
.c-tip-con .c-tip-langfilter li a{text-indent:15px;color:#666}
.c-tip-con .c-tip-langfilter li span{text-indent:15px;padding:3px 0;color:#999;display:block}
.c-tip-con .c-tip-timerfilter ul{width:115px;text-align:left;color:#666}
.c-tip-con .c-tip-timerfilter-ft ul{width:180px}
.c-tip-con .c-tip-timerfilter-si ul{width:206px;padding:7px 10px 10px}
.c-tip-con .c-tip-timerfilter li a{text-indent:15px;color:#666}
.c-tip-con .c-tip-timerfilter li span{text-indent:15px;padding:3px 0;color:#999;display:block}
.c-tip-con .c-tip-timerfilter-ft li a,.c-tip-con .c-tip-timerfilter-ft li span{text-indent:20px}
.c-tip-custom{padding:0 15px 10px;position:relative;zoom:1}
.c-tip-custom hr{border:0;height:0;border-top:1px solid #ebebeb}
.c-tip-custom p{color:#b6b6b6;height:25px;line-height:25px;margin:2px 0}
.c-tip-custom .c-tip-custom-et{margin-bottom:7px}
.c-tip-custom-input,.c-tip-si-input{display:inline-block;font-size:11px;color:#333;margin-left:4px;padding:0 2px;width:74%;height:16px;line-height:16px\9;border:1px solid #ebebeb;outline:0;box-sizing:content-box;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;overflow:hidden;position:relative}
.c-tip-custom-input-init{color:#d4d4d4}
.c-tip-custom-input-focus,.c-tip-si-input-focus{border:1px solid #3385ff}
.c-tip-timerfilter-si .c-tip-si-input{width:138px;height:22px;line-height:22px;vertical-align:0;*vertical-align:-6px;_vertical-align:-5px;padding:0 5px;margin-left:0}
.c-tip-con .c-tip-timerfilter li .c-tip-custom-submit,.c-tip-con .c-tip-timerfilter li .c-tip-timerfilter-si-submit{display:inline;padding:4px 10px;margin:0;color:#333;border:1px solid #d8d8d8;font-family:inherit;font-weight:400;text-align:center;vertical-align:0;background-color:#f9f9f9;outline:0}
.c-tip-con .c-tip-timerfilter li .c-tip-custom-submit:hover,.c-tip-con .c-tip-timerfilter li .c-tip-timerfilter-si-submit:hover{display:inline;border-color:#388bff}
.c-tip-timerfilter-si-error,.c-tip-timerfilter-custom-error{display:none;color:#3385FF;padding-left:4px}
.c-tip-timerfilter-custom-error{padding:0;margin:-5px -13px 7px 0}
#c-tip-custom-calenderCont{position:absolute;background:#fff;white-space:nowrap;padding:5px 10px;color:#000;border:1px solid #e4e4e4;-webkit-box-shadow:0 2px 4px rgba(0,0,0,.2);box-shadow:0 2px 4px rgba(0,0,0,.2)}
#c-tip-custom-calenderCont p{text-align:center;padding:2px 0 4px;*padding:4px 0}
#c-tip-custom-calenderCont p i{color:#8e9977;cursor:pointer;text-decoration:underline;font-size:13px}
#c-tip-custom-calenderCont .op_cal{background:#fff}
.op_cal table{background:#eeefea;margin:0;border-collapse:separate}
.op_btn_pre_month,.op_btn_next_month{cursor:pointer;display:block;margin-top:6px}
.op_btn_pre_month{float:left;background-position:0 -46px}
.op_btn_next_month{float:right;background-position:-18px -46px}
.op_cal .op_mon_pre1{padding:0}
.op_mon th{text-align:center;font-size:12px;background:#FFF;font-weight:700;border:1px solid #FFF;padding:0}
.op_mon td{text-align:center;cursor:pointer}
.op_mon h5{margin:0;padding:0 4px;text-align:center;font-size:14px;background:#FFF;height:28px;line-height:28px;border-bottom:1px solid #f5f5f5;margin-bottom:5px}
.op_mon strong{font-weight:700}
.op_mon td{padding:0 5px;border:1px solid #fff;font-size:12px;background:#fff;height:100%}
.op_mon td.op_mon_pre_month{color:#a4a4a4}
.op_mon td.op_mon_cur_month{color:#00c}
.op_mon td.op_mon_next_month{color:#a4a4a4}
.op_mon td.op_mon_day_hover{color:#000;border:1px solid #278df2}
.op_mon td.op_mon_day_selected{color:#FFF;border:1px solid #278df2;background:#278df2}
.op_mon td.op_mon_day_disabled{cursor:not-allowed;color:#ddd}
.zhannei-si-none,.zhannei-si,.hit_quet,.zhannei-search{display:none}
#c-tip-custom-calenderCont .op_mon td.op_mon_cur_month{color:#000}
#c-tip-custom-calenderCont .op_mon td.op_mon_day_selected{color:#fff}
.c-icon-toen{width:24px;height:24px;line-height:24px;background-color:#1cb7fd;color:#fff;font-size:14px;font-weight:700;font-style:normal;display:block;display:inline-block;float:left;text-align:center}
.hint_common_restop{width:538px;color:#999;font-size:12px;text-align:left;margin:5px 0 10px 121px}
#con-at~#wrapper_wrapper .hint_common_restop{padding-top:7px}
.sitelink{overflow:auto;zoom:1}
.sitelink_summary{float:left;width:47%;padding-right:30px}
.sitelink_summary a{font-size:1.1em;position:relative}
.sitelink_summary_last{padding-right:0}
.sitelink_en{overflow:auto;zoom:1}
.sitelink_en_summary{float:left;width:47%;padding-right:30px}
.sitelink_en_summary a{font-size:1.1em;position:relative}
.sitelink_en_summary_last{padding-right:0}
.sitelink_en_summary_title,.sitelink_en_summary .m{height:22px;overflow:hidden}
.without-summary-sitelink-en-container{overflow:hidden;height:22px}
.without-summary-sitelink-en{float:left}
.without-summary-sitelink-en-delimiter{margin-right:5px;margin-left:5px}
.wise-qrcode-wrapper{height:42px;line-height:42px;position:absolute;margin-left:8px;top:0;z-index:300}
.wise-qrcode-icon-outer{overflow:hidden}
.wise-qrcode-icon{position:relative;display:inline-block;width:15px;height:15px;vertical-align:text-bottom;overflow:hidden;opacity:.5;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/qrcode_icon_ae03227.png) no-repeat;-webkit-transform:translateY(42px);-ms-transform:translateY(42px);transform:translateY(42px);-webkit-background-size:100% 100%;background-size:100%}
.wise-qrcode-container{padding:15px;background:#fff;display:none;top:61px;left:0;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%);-webkit-box-shadow:0 0 1px rgba(0,0,0,.5);box-shadow:0 0 1px rgba(0,0,0,.5)}
.wise-qrcode-wrapper.show:hover .wise-qrcode-container{display:block}
.wise-qrcode-image{width:90px;height:90px;display:inline-block;vertical-align:middle}
.wise-qrcode-image .wise-qrcode-canvas{width:100%;height:100%}
.wise-qrcode-right{display:inline-block;vertical-align:middle;margin-left:15px}
.wise-qrcode-title{font-size:16px;color:#000;line-height:26px}
.wise-qrcode-text{font-size:12px;line-height:22px;color:#555}
.c-frame{margin-bottom:18px}
.c-offset{padding-left:10px}
.c-gray{color:#666}
.c-gap-top-small{margin-top:5px}
.c-gap-top{margin-top:10px}
.c-gap-bottom-small{margin-bottom:5px}
.c-gap-bottom{margin-bottom:10px}
.c-gap-left{margin-left:12px}
.c-gap-left-small{margin-left:6px}
.c-gap-right{margin-right:12px}
.c-gap-right-small{margin-right:6px}
.c-gap-right-large{margin-right:16px}
.c-gap-left-large{margin-left:16px}
.c-gap-icon-right-small{margin-right:5px}
.c-gap-icon-right{margin-right:10px}
.c-gap-icon-left-small{margin-left:5px}
.c-gap-icon-left{margin-left:10px}
.c-container{width:538px;font-size:13px;line-height:1.54;word-wrap:break-word;word-break:break-word}
.c-container .c-container{width:auto}
.c-container table{border-collapse:collapse;border-spacing:0}
.c-container td{font-size:13px;line-height:1.54}
.c-default{font-size:13px;line-height:1.54;word-wrap:break-word;word-break:break-all}
.c-container .t,.c-default .t{line-height:1.54}
.c-default .t{margin-bottom:0}
.cr-content{width:259px;font-size:13px;line-height:1.54;color:#333;word-wrap:break-word;word-break:normal}
.cr-content table{border-collapse:collapse;border-spacing:0}
.cr-content td{font-size:13px;line-height:1.54;vertical-align:top}
.cr-offset{padding-left:17px}
.cr-title{font-size:14px;line-height:1.29;font-weight:700}
.cr-title-sub{float:right;font-size:13px;font-weight:400}
.c-row{*zoom:1}
.c-row:after{display:block;height:0;content:"";clear:both;visibility:hidden}
.c-span2{width:29px}
.c-span3{width:52px}
.c-span4{width:75px}
.c-span5{width:98px}
.c-span6{width:121px}
.c-span7{width:144px}
.c-span8{width:167px}
.c-span9{width:190px}
.c-span10{width:213px}
.c-span11{width:236px}
.c-span12{width:259px}
.c-span13{width:282px}
.c-span14{width:305px}
.c-span15{width:328px}
.c-span16{width:351px}
.c-span17{width:374px}
.c-span18{width:397px}
.c-span19{width:420px}
.c-span20{width:443px}
.c-span21{width:466px}
.c-span22{width:489px}
.c-span23{width:512px}
.c-span24{width:535px}
.c-span2,.c-span3,.c-span4,.c-span5,.c-span6,.c-span7,.c-span8,.c-span9,.c-span10,.c-span11,.c-span12,.c-span13,.c-span14,.c-span15,.c-span16,.c-span17,.c-span18,.c-span19,.c-span20,.c-span21,.c-span22,.c-span23,.c-span24{float:left;_display:inline;margin-right:17px;list-style:none}
.c-span-last{margin-right:0}
.c-span-last-s{margin-right:0}
.container_l .cr-content{width:351px}
.container_l .cr-content .c-span-last-s{margin-right:17px}
.container_l .cr-content-narrow{width:259px}
.container_l .cr-content-narrow .c-span-last-s{margin-right:0}
.c-border{width:518px;padding:9px;border:1px solid #e3e3e3;border-bottom-color:#e0e0e0;border-right-color:#ececec;box-shadow:1px 2px 1px rgba(0,0,0,.072);-webkit-box-shadow:1px 2px 1px rgba(0,0,0,.072);-moz-box-shadow:1px 2px 1px rgba(0,0,0,.072);-o-box-shadow:1px 2px 1px rgba(0,0,0,.072)}
.c-border .c-gap-left{margin-left:10px}
.c-border .c-gap-left-small{margin-left:5px}
.c-border .c-gap-right{margin-right:10px}
.c-border .c-gap-right-small{margin-right:5px}
.c-border .c-border{width:auto;padding:0;border:0;box-shadow:none;-webkit-box-shadow:none;-moz-box-shadow:none;-o-box-shadow:none}
.c-border .c-span2{width:34px}
.c-border .c-span3{width:56px}
.c-border .c-span4{width:78px}
.c-border .c-span5{width:100px}
.c-border .c-span6{width:122px}
.c-border .c-span7{width:144px}
.c-border .c-span8{width:166px}
.c-border .c-span9{width:188px}
.c-border .c-span10{width:210px}
.c-border .c-span11{width:232px}
.c-border .c-span12{width:254px}
.c-border .c-span13{width:276px}
.c-border .c-span14{width:298px}
.c-border .c-span15{width:320px}
.c-border .c-span16{width:342px}
.c-border .c-span17{width:364px}
.c-border .c-span18{width:386px}
.c-border .c-span19{width:408px}
.c-border .c-span20{width:430px}
.c-border .c-span21{width:452px}
.c-border .c-span22{width:474px}
.c-border .c-span23{width:496px}
.c-border .c-span24{width:518px}
.c-border .c-span2,.c-border .c-span3,.c-border .c-span4,.c-border .c-span5,.c-border .c-span6,.c-border .c-span7,.c-border .c-span8,.c-border .c-span9,.c-border .c-span10,.c-border .c-span11,.c-border .c-span12,.c-border .c-span13,.c-border .c-span14,.c-border .c-span15,.c-border .c-span16,.c-border .c-span17,.c-border .c-span18,.c-border .c-span19,.c-border .c-span20,.c-border .c-span21,.c-border .c-span22,.c-border .c-span23,.c-border .c-span24{margin-right:10px}
.c-border .c-span-last{margin-right:0}
.c-loading{display:block;width:50px;height:50px;background:url(//www.baidu.com/aladdin/img/tools/loading.gif) no-repeat 0 0}
.c-vline{display:inline-block;margin:0 3px;border-left:1px solid #ddd;width:0;height:12px;_vertical-align:middle;_overflow:hidden}
.c-icon{background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_5859e57.png) no-repeat 0 0;_background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_d5b04cc.gif)}
.c-icon{display:inline-block;width:14px;height:14px;vertical-align:text-bottom;font-style:normal;overflow:hidden}
.c-icon-unfold,.c-icon-fold,.c-icon-chevron-unfold,.c-icon-chevron-fold{width:12px;height:12px}
.c-icon-star,.c-icon-star-gray{width:60px}
.c-icon-qa-empty,.c-icon-safeguard,.c-icon-register-empty,.c-icon-zan,.c-icon-music,.c-icon-music-gray,.c-icon-location,.c-icon-warning,.c-icon-doc,.c-icon-xls,.c-icon-ppt,.c-icon-pdf,.c-icon-txt,.c-icon-play-black,.c-icon-gift,.c-icon-baidu-share,.c-icon-bear,.c-icon-bear-border,.c-icon-location-blue,.c-icon-hotAirBall,.c-icon-moon,.c-icon-streetMap,.c-icon-mv,.c-icon-zhidao-s,.c-icon-shopping{width:16px;height:16px}
.c-icon-bear-circle,.c-icon-warning-circle,.c-icon-warning-triangle,.c-icon-warning-circle-gray{width:18px;height:18px}
.c-icon-tieba,.c-icon-zhidao,.c-icon-bear-p,.c-icon-bear-pn{width:24px;height:24px}
.c-icon-ball-blue,.c-icon-ball-red{width:38px;height:38px}
.c-icon-unfold:hover,.c-icon-fold:hover,.c-icon-chevron-unfold:hover,.c-icon-chevron-fold:hover,.c-icon-download:hover,.c-icon-lyric:hover,.c-icon-v:hover,.c-icon-hui:hover,.c-icon-bao:hover,.c-icon-person:hover,.c-icon-high-v:hover,.c-icon-phone:hover,.c-icon-nuo:hover,.c-icon-fan:hover,.c-icon-med:hover,.c-icon-air:hover,.c-icon-share2:hover,.c-icon-v1:hover,.c-icon-v2:hover,.c-icon-write:hover,.c-icon-R:hover{border-color:#388bff}
.c-icon-unfold:active,.c-icon-fold:active,.c-icon-chevron-unfold:active,.c-icon-chevron-fold:active,.c-icon-download:active,.c-icon-lyric:active,.c-icon-v:active,.c-icon-hui:active,.c-icon-bao:active,.c-icon-person:active,.c-icon-high-v:active,.c-icon-phone:active,.c-icon-nuo:active,.c-icon-fan:active,.c-icon-med:active,.c-icon-air:active,.c-icon-share2:active,.c-icon-v1:active,.c-icon-v2:active,.c-icon-write:active,.c-icon-R:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}
.c-icon-v3:hover{border-color:#ffb300}
.c-icon-v3:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}
.c-icon-unfold,.c-icon-fold,.c-icon-chevron-unfold,.c-icon-chevron-fold,.c-icon-download,.c-icon-lyric{border:1px solid #d8d8d8;cursor:pointer}
.c-icon-v,.c-icon-hui,.c-icon-bao,.c-icon-person,.c-icon-high-v,.c-icon-phone,.c-icon-nuo,.c-icon-fan,.c-icon-med,.c-icon-air,.c-icon-share2,.c-icon-v1,.c-icon-v2,.c-icon-v3,.c-icon-write,.c-icon-R{border:1px solid #d8d8d8;cursor:pointer;border-color:transparent;_border-color:tomato;_filter:chroma(color=#ff6347)}
.c-icon-v1,.c-icon-v2,.c-icon-v3,.c-icon-v1-noborder,.c-icon-v2-noborder,.c-icon-v3-noborder,.c-icon-v1-noborder-disable,.c-icon-v2-noborder-disable,.c-icon-v3-noborder-disable{width:19px}
.c-icon-download,.c-icon-lyric{width:16px;height:16px}
.c-icon-play-circle,.c-icon-stop-circle{width:18px;height:18px}
.c-icon-play-circle-middle,.c-icon-stop-circle-middle{width:24px;height:24px}
.c-icon-play-black-large,.c-icon-stop-black-large{width:36px;height:36px}
.c-icon-play-black-larger,.c-icon-stop-black-larger{width:52px;height:52px}
.c-icon-flag{background-position:0 -144px}
.c-icon-bus{background-position:-24px -144px}
.c-icon-calendar{background-position:-48px -144px}
.c-icon-street{background-position:-72px -144px}
.c-icon-map{background-position:-96px -144px}
.c-icon-bag{background-position:-120px -144px}
.c-icon-money{background-position:-144px -144px}
.c-icon-game{background-position:-168px -144px}
.c-icon-user{background-position:-192px -144px}
.c-icon-globe{background-position:-216px -144px}
.c-icon-lock{background-position:-240px -144px}
.c-icon-plane{background-position:-264px -144px}
.c-icon-list{background-position:-288px -144px}
.c-icon-star-gray{background-position:-312px -144px}
.c-icon-circle-gray{background-position:-384px -144px}
.c-icon-triangle-down{background-position:-408px -144px}
.c-icon-triangle-up{background-position:-432px -144px}
.c-icon-triangle-up-empty{background-position:-456px -144px}
.c-icon-sort-gray{background-position:-480px -144px}
.c-icon-sort-up{background-position:-504px -144px}
.c-icon-sort-down{background-position:-528px -144px}
.c-icon-down-gray{background-position:-552px -144px}
.c-icon-up-gray{background-position:-576px -144px}
.c-icon-download-noborder{background-position:-600px -144px}
.c-icon-lyric-noborder{background-position:-624px -144px}
.c-icon-download-white{background-position:-648px -144px}
.c-icon-close{background-position:-672px -144px}
.c-icon-fail{background-position:-696px -144px}
.c-icon-success{background-position:-720px -144px}
.c-icon-triangle-down-g{background-position:-744px -144px}
.c-icon-refresh{background-position:-768px -144px}
.c-icon-chevron-left-gray{background-position:-816px -144px}
.c-icon-chevron-right-gray{background-position:-840px -144px}
.c-icon-setting{background-position:-864px -144px}
.c-icon-close2{background-position:-888px -144px}
.c-icon-chevron-top-gray-s{background-position:-912px -144px}
.c-icon-fullscreen{background-position:0 -168px}
.c-icon-safe{background-position:-24px -168px}
.c-icon-exchange{background-position:-48px -168px}
.c-icon-chevron-bottom{background-position:-72px -168px}
.c-icon-chevron-top{background-position:-96px -168px}
.c-icon-unfold{background-position:-120px -168px}
.c-icon-fold{background-position:-144px -168px}
.c-icon-chevron-unfold{background-position:-168px -168px}
.c-icon-qa{background-position:-192px -168px}
.c-icon-register{background-position:-216px -168px}
.c-icon-star{background-position:-240px -168px}
.c-icon-star-gray{position:relative}
.c-icon-star-gray .c-icon-star{position:absolute;top:0;left:0}
.c-icon-play-blue{background-position:-312px -168px}
.c-icon-pic{width:16px;background-position:-336px -168px}
.c-icon-chevron-fold{background-position:-360px -168px}
.c-icon-video{width:18px;background-position:-384px -168px}
.c-icon-circle-blue{background-position:-408px -168px}
.c-icon-circle-yellow{background-position:-432px -168px}
.c-icon-play-white{background-position:-456px -168px}
.c-icon-triangle-down-blue{background-position:-480px -168px}
.c-icon-chevron-unfold2{background-position:-504px -168px}
.c-icon-right{background-position:-528px -168px}
.c-icon-right-empty{background-position:-552px -168px}
.c-icon-new-corner{width:15px;background-position:-576px -168px}
.c-icon-horn{background-position:-600px -168px}
.c-icon-right-large{width:18px;background-position:-624px -168px}
.c-icon-wrong-large{background-position:-648px -168px}
.c-icon-circle-blue-s{background-position:-672px -168px}
.c-icon-play-gray{background-position:-696px -168px}
.c-icon-up{background-position:-720px -168px}
.c-icon-down{background-position:-744px -168px}
.c-icon-stable{background-position:-768px -168px}
.c-icon-calendar-blue{background-position:-792px -168px}
.c-icon-triangle-down-blue2{background-position:-816px -168px}
.c-icon-triangle-up-blue2{background-position:-840px -168px}
.c-icon-down-blue{background-position:-864px -168px}
.c-icon-up-blue{background-position:-888px -168px}
.c-icon-ting{background-position:-912px -168px}
.c-icon-piao{background-position:-936px -168px}
.c-icon-wrong-empty{background-position:-960px -168px}
.c-icon-warning-circle-s{background-position:-984px -168px}
.c-icon-chevron-left{background-position:-1008px -168px}
.c-icon-chevron-right{background-position:-1032px -168px}
.c-icon-circle-gray-s{background-position:-1056px -168px}
.c-icon-v,.c-icon-v-noborder{background-position:0 -192px}
.c-icon-hui{background-position:-24px -192px}
.c-icon-bao{background-position:-48px -192px}
.c-icon-phone{background-position:-72px -192px}
.c-icon-qa-empty{background-position:-96px -192px}
.c-icon-safeguard{background-position:-120px -192px}
.c-icon-register-empty{background-position:-144px -192px}
.c-icon-zan{background-position:-168px -192px}
.c-icon-music{background-position:-192px -192px}
.c-icon-music-gray{background-position:-216px -192px}
.c-icon-location{background-position:-240px -192px}
.c-icon-warning{background-position:-264px -192px}
.c-icon-doc{background-position:-288px -192px}
.c-icon-xls{background-position:-312px -192px}
.c-icon-ppt{background-position:-336px -192px}
.c-icon-pdf{background-position:-360px -192px}
.c-icon-txt{background-position:-384px -192px}
.c-icon-play-black{background-position:-408px -192px}
.c-icon-play-black:hover{background-position:-432px -192px}
.c-icon-gift{background-position:-456px -192px}
.c-icon-baidu-share{background-position:-480px -192px}
.c-icon-bear{background-position:-504px -192px}
.c-icon-R{background-position:-528px -192px}
.c-icon-bear-border{background-position:-576px -192px}
.c-icon-person,.c-icon-person-noborder{background-position:-600px -192px}
.c-icon-location-blue{background-position:-624px -192px}
.c-icon-hotAirBall{background-position:-648px -192px}
.c-icon-moon{background-position:-672px -192px}
.c-icon-streetMap{background-position:-696px -192px}
.c-icon-high-v,.c-icon-high-v-noborder{background-position:-720px -192px}
.c-icon-nuo{background-position:-744px -192px}
.c-icon-mv{background-position:-768px -192px}
.c-icon-fan{background-position:-792px -192px}
.c-icon-med{background-position:-816px -192px}
.c-icon-air{background-position:-840px -192px}
.c-icon-share2{background-position:-864px -192px}
.c-icon-v1,.c-icon-v1-noborder{background-position:-888px -192px}
.c-icon-v2,.c-icon-v2-noborder{background-position:-912px -192px}
.c-icon-v3,.c-icon-v3-noborder{background-position:-936px -192px}
.c-icon-v1-noborder-disable{background-position:-960px -192px}
.c-icon-v2-noborder-disable{background-position:-984px -192px}
.c-icon-v3-noborder-disable{background-position:-1008px -192px}
.c-icon-write{background-position:-1032px -192px}
.c-icon-zhidao-s{background-position:-1056px -192px}
.c-icon-shopping{background-position:-1080px -192px}
.c-icon-bear-circle{background-position:0 -216px}
.c-icon-warning-circle{background-position:-24px -216px}
.c-icon-warning-triangle{width:24px;background-position:-48px -216px}
.c-icon-warning-circle-gray{background-position:-72px -216px}
.c-icon-ball-red{background-position:0 -240px}
.c-icon-ball-blue{background-position:-48px -240px}
.c-icon-tieba{background-position:0 -288px}
.c-icon-zhidao{background-position:-48px -288px}
.c-icon-bear-p{background-position:-96px -288px}
.c-icon-bear-pn{background-position:-144px -288px}
.c-icon-download{background-position:0 -336px}
.c-icon-lyric{background-position:-24px -336px}
.c-icon-play-circle{background-position:-48px -336px}
.c-icon-play-circle:hover{background-position:-72px -336px}
.c-icon-stop-circle{background-position:-96px -336px}
.c-icon-stop-circle:hover{background-position:-120px -336px}
.c-icon-play-circle-middle{background-position:0 -360px}
.c-icon-play-circle-middle:hover{background-position:-48px -360px}
.c-icon-stop-circle-middle{background-position:-96px -360px}
.c-icon-stop-circle-middle:hover{background-position:-144px -360px}
.c-icon-play-black-large{background-position:0 -408px}
.c-icon-play-black-large:hover{background-position:-48px -408px}
.c-icon-stop-black-large{background-position:-96px -408px}
.c-icon-stop-black-large:hover{background-position:-144px -408px}
.c-icon-play-black-larger{background-position:0 -456px}
.c-icon-play-black-larger:hover{background-position:-72px -456px}
.c-icon-stop-black-larger{background-position:-144px -456px}
.c-icon-stop-black-larger:hover{background-position:-216px -456px}
.c-recommend{font-size:0;padding:5px 0;border:1px solid #f3f3f3;border-left:0;border-right:0}
.c-recommend .c-icon{margin-bottom:-4px}
.c-recommend .c-gray,.c-recommend a{font-size:13px}
.c-recommend-notopline{padding-top:0;border-top:0}
.c-recommend-vline{display:inline-block;margin:0 10px -2px;border-left:1px solid #d8d8d8;width:0;height:12px;_vertical-align:middle;_overflow:hidden}
.c-text{display:inline-block;padding:2px;text-align:center;vertical-align:text-bottom;font-size:12px;line-height:100%;font-style:normal;font-weight:400;color:#fff;overflow:hidden}
a.c-text{text-decoration:none}
.c-text-new{background-color:#f13f40}
.c-text-info{padding-left:0;padding-right:0;font-weight:700;color:#2b99ff;*vertical-align:baseline;_position:relative;_top:2px}
.c-text-info b{_position:relative;_top:-1px}
.c-text-info span{padding:0 2px;font-weight:400}
.c-text-important{background-color:#1cb7fd}
.c-text-public{background-color:#2b99ff}
.c-text-warning{background-color:#ff830f}
.c-text-prompt{background-color:#f5c537}
.c-text-danger{background-color:#f13f40}
.c-text-safe{background-color:#52c277}
.c-text-empty{padding-top:1px;padding-bottom:1px;border:1px solid #d8d8d8;cursor:pointer;color:#23b9fd;background-color:#fff}
.c-text-empty:hover{border-color:#388bff}
.c-text-empty:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}
.c-text-mult{padding-left:5px;padding-right:5px}
.c-text-gray{background-color:#666}
.c-btn,.c-btn:visited{color:#333!important}
.c-btn{display:inline-block;padding:0 14px;margin:0;height:24px;line-height:25px;font-size:13px;filter:chroma(color=#000000);*zoom:1;border:1px solid #d8d8d8;cursor:pointer;font-family:inherit;font-weight:400;text-align:center;vertical-align:middle;background-color:#f9f9f9;overflow:hidden;outline:0}
.c-btn:hover{border-color:#388bff}
.c-btn:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}
a.c-btn{text-decoration:none}
button.c-btn{height:26px;_line-height:18px;*overflow:visible}
button.c-btn::-moz-focus-inner{padding:0;border:0}
.c-btn .c-icon{margin-top:5px}
.c-btn-disable{color:#999!important}
.c-btn-disable:visited{color:#999!important}
.c-btn-disable:hover{border:1px solid #d8d8d8;cursor:default}
.c-btn-disable:active{border-color:#d8d8d8;background-color:#f9f9f9;box-shadow:none;-webkit-box-shadow:none;-moz-box-shadow:none;-o-box-shadow:none}
.c-btn-mini{padding-left:5px;padding-right:5px;height:18px;line-height:18px;font-size:12px}
button.c-btn-mini{height:20px;_height:18px;_line-height:14px}
.c-btn-mini .c-icon{margin-top:2px}
.c-btn-large{height:28px;line-height:28px;font-size:14px;font-family:"微软雅黑","黑体"}
button.c-btn-large{height:30px;_line-height:24px}
.c-btn-large .c-icon{margin-top:7px;_margin-top:6px}
.c-btn-primary,.c-btn-primary:visited{color:#fff!important}
.c-btn-primary{background-color:#388bff;border-color:#3c8dff #408ffe #3680e6}
.c-btn-primary:hover{border-color:#2678ec #2575e7 #1c6fe2 #2677e7;background-color:#388bff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i/9PO5r4AAAAD0lEQVR42gEEAPv/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);*background-image:none;background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}
.c-btn-primary:active{border-color:#178ee3 #1784d0 #177bbf #1780ca;background-color:#388bff;background-image:none;box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-webkit-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-moz-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-o-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15)}
.c-btn .c-icon{float:left}
.c-dropdown2{position:relative;display:inline-block;width:100%;height:26px;line-height:26px;font-size:13px;vertical-align:middle;outline:0;_font-family:SimSun;background-color:#fff;word-wrap:normal;word-break:normal}
.c-dropdown2 .c-dropdown2-btn-group{position:relative;height:24px;border:1px solid #999;border-bottom-color:#d8d8d8;border-right-color:#d8d8d8;-moz-user-select:none;-webkit-user-select:none;user-select:none}
.c-dropdown2:hover .c-dropdown2-btn-group,.c-dropdown2-hover .c-dropdown2-btn-group{box-shadow:inset 1px 1px 0 0 #d8d8d8;-webkit-box-shadow:inset 1px 1px 0 0 #d8d8d8;-moz-box-shadow:inset 1px 1px 0 0 #d8d8d8;-o-box-shadow:inset 1px 1px 0 0 #d8d8d8}
.c-dropdown2:hover .c-dropdown2-btn-icon,.c-dropdown2-hover .c-dropdown2-btn-icon{box-shadow:inset 0 1px 0 0 #d8d8d8;-webkit-box-shadow:inset 0 1px 0 0 #d8d8d8;-moz-box-shadow:inset 0 1px 0 0 #d8d8d8;-o-box-shadow:inset 0 1px 0 0 #d8d8d8}
.c-dropdown2:hover .c-dropdown2-btn-icon-border,.c-dropdown2-hover .c-dropdown2-btn-icon-border{background-color:#f2f2f2}
.c-dropdown2 .c-dropdown2-btn{height:24px;padding-left:10px;padding-right:10px;cursor:default;overflow:hidden;white-space:nowrap}
.c-dropdown2 .c-dropdown2-btn-icon{position:absolute;top:0;right:0;width:23px;height:24px;line-height:24px;background-color:#fff;padding:0 1px 0 10px}
.c-dropdown2 .c-dropdown2-btn-icon-border{height:24px;width:23px;border-left:1px solid #d9d9d9;text-align:center;zoom:1}
.c-dropdown2 .c-icon-triangle-down{*margin-top:5px;_margin-left:2px}
.c-dropdown2 .c-dropdown2-menu{position:absolute;left:0;top:100%;_margin-top:0;width:100%;overflow:hidden;border:1px solid #bbb;background:#fff;visibility:hidden}
.c-dropdown2 .c-dropdown2-menu-inner{overflow:hidden}
.c-dropdown2 .c-dropdown2-option{background-color:#fff;cursor:pointer}
.c-dropdown2 .c-dropdown2-selected{background-color:#f5f5f5}
.c-dropdown2-common ul,.c-dropdown2-common li{margin:0;padding:0;list-style:none}
.c-dropdown2-common .c-dropdown2-option{height:26px;line-height:26px;font-size:12px;color:#333;white-space:nowrap;cursor:pointer;padding-left:10px}
.c-dropdown2-common .c-dropdown2-selected{background-color:#f5f5f5}
.c-dropdown2-common .c-dropdown2-menu-group .c-dropdown2-group{padding-left:10px;font-weight:700;cursor:default}
.c-dropdown2-common .c-dropdown2-menu-group .c-dropdown2-option{padding-left:20px}
.c-img{display:block;min-height:1px;border:0 0}
.c-img3{width:52px}
.c-img4{width:75px}
.c-img6{width:121px}
.c-img7{width:144px}
.c-img12{width:259px}
.c-img15{width:328px}
.c-img18{width:397px}
.c-border .c-img3{width:56px}
.c-border .c-img4{width:78px}
.c-border .c-img7{width:144px}
.c-border .c-img12{width:254px}
.c-border .c-img15{width:320px}
.c-border .c-img18{width:386px}
.c-index{display:inline-block;padding:1px 0;color:#fff;width:14px;line-height:100%;font-size:12px;text-align:center;background-color:#8eb9f5}
.c-index-hot,.c-index-hot1{background-color:#f54545}
.c-index-hot2{background-color:#ff8547}
.c-index-hot3{background-color:#ffac38}
.c-input{display:inline-block;padding:0 4px;height:24px;line-height:24px\9;font-size:13px;border:1px solid #999;border-bottom-color:#d8d8d8;border-right-color:#d8d8d8;outline:0;box-sizing:content-box;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;vertical-align:top;overflow:hidden}
.c-input:hover{box-shadow:inset 1px 1px 1px 0 #d8d8d8;-webkit-box-shadow:inset 1px 1px 1px 0 #d8d8d8;-moz-box-shadow:inset 1px 1px 1px 0 #d8d8d8;-o-box-shadow:inset 1px 1px 1px 0 #d8d8d8}
.c-input .c-icon{float:right;margin-top:6px}
.c-input .c-icon-left{float:left;margin-right:4px}
.c-input input{float:left;height:22px;*padding-top:4px;margin-top:2px;font-size:13px;border:0;outline:0}
.c-input{width:180px}
.c-input input{width:162px}
.c-input-xmini{width:65px}
.c-input-xmini input{width:47px}
.c-input-mini{width:88px}
.c-input-mini input{width:70px}
.c-input-small{width:157px}
.c-input-small input{width:139px}
.c-input-large{width:203px}
.c-input-large input{width:185px}
.c-input-xlarge{width:341px}
.c-input-xlarge input{width:323px}
.c-input12{width:249px}
.c-input12 input{width:231px}
.c-input20{width:433px}
.c-input20 input{width:415px}
.c-border .c-input{width:178px}
.c-border .c-input input{width:160px}
.c-border .c-input-xmini{width:68px}
.c-border .c-input-xmini input{width:50px}
.c-border .c-input-mini{width:90px}
.c-border .c-input-mini input{width:72px}
.c-border .c-input-small{width:156px}
.c-border .c-input-small input{width:138px}
.c-border .c-input-large{width:200px}
.c-border .c-input-large input{width:182px}
.c-border .c-input-xlarge{width:332px}
.c-border .c-input-xlarge input{width:314px}
.c-border .c-input12{width:244px}
.c-border .c-input12 input{width:226px}
.c-border .c-input20{width:420px}
.c-border .c-input20 input{width:402px}
.c-numberset{*zoom:1}
.c-numberset:after{display:block;height:0;content:"";clear:both;visibility:hidden}
.c-numberset li{float:left;margin-right:17px;list-style:none}
.c-numberset .c-numberset-last{margin-right:0}
.c-numberset a{display:block;width:50px;text-decoration:none;text-align:center;border:1px solid #d8d8d8;cursor:pointer}
.c-numberset a:hover{border-color:#388bff}
.c-border .c-numberset li{margin-right:10px}
.c-border .c-numberset .c-numberset-last{margin-right:0}
.c-border .c-numberset a{width:54px}
.c-table{width:100%;border-collapse:collapse;border-spacing:0}
.c-table th,.c-table td{padding-left:10px;line-height:1.54;font-size:13px;border-bottom:1px solid #f3f3f3;text-align:left}
.cr-content .c-table th:first-child,.cr-content .c-table td:first-child{padding-left:0}
.c-table th{padding-top:4px;padding-bottom:4px;font-weight:400;color:#666;border-color:#f0f0f0;white-space:nowrap;background-color:#fafafa}
.c-table td{padding-top:6.5px;padding-bottom:6.5px}
.c-table-hasimg td{padding-top:10px;padding-bottom:10px}
.c-table a,.c-table em{text-decoration:none}
.c-table a:hover,.c-table a:hover em{text-decoration:underline}
.c-table a.c-icon:hover{text-decoration:none}
.c-table .c-btn:hover,.c-table .c-btn:hover em{text-decoration:none}
.c-table-nohihead th{background-color:transparent}
.c-table-noborder td{border-bottom:0}
.c-tabs-nav-movetop{margin:-10px -9px 0 -10px;position:relative}
.c-tabs-nav{border-bottom:1px solid #d9d9d9;background-color:#fafafa;line-height:1.54;font-size:0;*zoom:1;_overflow-x:hidden;_position:relative}
.c-tabs-nav:after{display:block;height:0;content:"";clear:both;visibility:hidden}
.c-tabs-nav .c-tabs-nav-btn{float:right;_position:absolute;_top:0;_right:0;_z-index:1;background:#fafafa}
.c-tabs-nav .c-tabs-nav-btn .c-tabs-nav-btn-prev,.c-tabs-nav .c-tabs-nav-btn .c-tabs-nav-btn-next{float:left;padding:6px 2px;cursor:pointer}
.c-tabs-nav .c-tabs-nav-btn .c-tabs-nav-btn-disable{cursor:default}
.c-tabs-nav .c-tabs-nav-view{_position:relative;overflow:hidden;*zoom:1;margin-bottom:-1px}
.c-tabs-nav .c-tabs-nav-view .c-tabs-nav-li{margin-bottom:0}
.c-tabs-nav .c-tabs-nav-more{float:left;white-space:nowrap}
.c-tabs-nav li,.c-tabs-nav a{color:#666;font-size:13px;*zoom:1}
.c-tabs-nav li{display:inline-block;margin-bottom:-1px;*display:inline;padding:3px 15px;vertical-align:bottom;border-style:solid;border-width:2px 1px 0;border-color:transparent;_border-color:tomato;_filter:chroma(color=#ff6347);list-style:none;cursor:pointer;white-space:nowrap;overflow:hidden}
.c-tabs-nav a{text-decoration:none}
.c-tabs-nav .c-tabs-nav-sep{height:16px;width:0;padding:0;margin-bottom:4px;border-style:solid;border-width:0 1px;border-color:transparent #fff transparent #dedede}
.c-tabs-nav .c-tabs-nav-selected{_position:relative;border-color:#2c99ff #e4e4e4 #fff #dedede;background-color:#fff;color:#000;cursor:default}
.c-tabs-nav-one .c-tabs-nav-selected{border-color:transparent;_border-color:tomato;_filter:chroma(color=#ff6347);background-color:transparent;color:#666}
.c-tabs .c-tabs .c-tabs-nav{padding:10px 0 5px;border:0 0;background-color:#fff}
.c-tabs .c-tabs .c-tabs-nav li,.c-tabs .c-tabs .c-tabs-nav a{color:#00c}
.c-tabs .c-tabs .c-tabs-nav li{padding:0 5px;position:static;margin:0 10px;border:0 0;cursor:pointer;white-space:nowrap}
.c-tabs .c-tabs .c-tabs-nav .c-tabs-nav-sep{height:11px;width:0;padding:0;margin:0 0 4px;border:0 0;border-left:1px solid #d8d8d8}
.c-tabs .c-tabs .c-tabs-nav .c-tabs-nav-selected{background-color:#2c99ff;color:#fff;cursor:default}
.c-tag{padding-top:3px;margin-bottom:3px;height:1.7em;font-size:13px;line-height:1.4em;transition:height .3s ease-in;-webkit-transition:height .3s ease-in;-moz-transition:height .3s ease-in;-ms-transition:height .3s ease-in;-o-transition:height .3s ease-in;*zoom:1;overflow:hidden}
.c-tag:after{display:block;height:0;content:"";clear:both;visibility:hidden}
.c-tag-cont{overflow:hidden;*zoom:1}
.c-tag-type,.c-tag-li,.c-tag-more,.c-tag-cont span{margin:2px 0}
.c-tag-type,.c-tag-li,.c-tag-cont span{float:left}
.c-tag-type,.c-tag-more{color:#666}
.c-tag-li,.c-tag-cont span{padding:0 4px;display:inline-block;margin-right:12px;white-space:nowrap;cursor:pointer;color:#00c}
.c-tag .c-tag-selected{background:#388bff;color:#fff}
.c-tag-more{float:right;background:#fff;cursor:pointer;*height:18px}
.c-tool{display:inline-block;width:56px;height:56px;background:url(//www.baidu.com/aladdin/img/tools/tools-5.png) no-repeat}
.c-tool-region{background-position:0 0}
.c-tool-calendar{background-position:-72px 0}
.c-tool-city{background-position:-144px 0}
.c-tool-phone-pos{background-position:-216px 0}
.c-tool-other{background-position:-288px 0}
.c-tool-midnight{background-position:-360px 0}
.c-tool-kefu{width:121px;background-position:-432px 0}
.c-tool-phone{background-position:-576px 0}
.c-tool-car{background-position:-648px 0}
.c-tool-station{background-position:0 -72px}
.c-tool-cheat{background-position:-72px -72px}
.c-tool-counter{background-position:-144px -72px}
.c-tool-time{background-position:-216px -72px}
.c-tool-zip{background-position:-288px -72px}
.c-tool-warning{background-position:-360px -72px}
.c-tool-ip{background-position:0 -144px}
.c-tool-unit{background-position:-72px -144px}
.c-tool-rate{background-position:-144px -144px}
.c-tool-conversion{background-position:-288px -144px}
.c-tool-ads{background-position:-360px -144px}
.soutu-input{padding-left:55px!important}
.soutu-input-image{position:absolute;left:1px;top:1px;height:28px;width:49px;z-index:1;padding:0;background:#e6e6e6;border:1px solid #e6e6e6}
.soutu-input-thumb{height:28px;width:28px;min-width:1px}
.soutu-input-close{position:absolute;right:0;top:0;cursor:pointer;display:block;width:22px;height:28px}
.soutu-input-close::after{content:" ";position:absolute;right:3px;top:50%;cursor:pointer;margin-top:-7px;display:block;width:14px;height:14px;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/soutu/img/soutu_icons_new_8abaf8a.png) no-repeat -163px 0}
.soutu-input-image:hover .soutu-input-close::after{background-position:-215px 2px}
.fb-hint{margin-top:5px;transition-duration:.9s;opacity:0;display:none;color:red}
.fb-img{display:none}
.fb-hint-tip{height:44px;line-height:24px;background-color:#38f;color:#fff;box-sizing:border-box;width:269px;font-size:16px;padding:10px;padding-left:14px;position:absolute;top:-65px;right:-15px;border-radius:3px;z-index:299}
.fb-hint-tip::before{content:"";width:0;height:0;display:block;position:absolute;border-left:8px solid transparent;border-right:8px solid transparent;border-top:8px solid #38f;bottom:-8px;right:25px}
.fb-mask,.fb-mask-light{position:fixed;top:0;left:0;bottom:0;right:0;z-index:296;background-color:#000;filter:alpha(opacity=60);background-color:rgba(0,0,0,.6)}
.fb-mask-light{background-color:#fff;filter:alpha(opacity=0);background-color:rgba(255,255,255,0)}
.fb-success .fb-success-text{text-align:center;color:#333;font-size:13px;margin-bottom:14px}
.fb-success-text.fb-success-text-title{color:#3b6;font-size:16px;margin-bottom:16px}
.fb-success-text-title i{width:16px;height:16px;margin-right:5px}
.fb-list-container{box-sizing:border-box;padding:4px 8px;position:absolute;top:0;left:0;bottom:0;right:0;z-index:298;display:block;width:100%;cursor:pointer;margin-top:-5px;margin-left:-5px}
.fb-list-container-hover{background-color:#fff;border:2px #38f solid}
.fb-list-container-first{box-sizing:border-box;padding-left:10px;padding-top:5px;position:absolute;top:0;left:0;bottom:0;right:0;z-index:297;display:block;width:100%;cursor:pointer;margin-top:-5px;margin-left:-5px;border:3px #f5f5f5 dashed;border-radius:3px}
.fb-des-content{font-size:13px!important;color:#000}
.fb-des-content::-webkit-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-des-content:-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-des-content::-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-des-content:-ms-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-btn,.fb-btn:visited{color:#333!important}
.fb-select{position:relative;background-color:#fff;border:1px solid #ccc}
.fb-select i{position:absolute;right:2px;top:7px}
.fb-type{width:350px;box-sizing:border-box;height:28px;font-size:13px;line-height:28px;border:0;word-break:normal;word-wrap:normal;position:relative;appearance:none;-moz-appearance:none;-webkit-appearance:none;display:inline-block;vertical-align:middle;line-height:normal;color:#333;background-color:transparent;border-radius:0;overflow:hidden;outline:0;padding-left:5px}
.fb-type::-ms-expand{display:none}
.fb-btn{display:inline-block;padding:0 14px;margin:0;height:24px;line-height:25px;font-size:13px;filter:chroma(color=#000000);*zoom:1;border:1px solid #d8d8d8;cursor:pointer;font-family:inherit;font-weight:400;text-align:center;vertical-align:middle;background-color:#f9f9f9;overflow:hidden;outline:0}
.fb-btn:hover{border-color:#388bff}
.fb-btn:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}
a.fb-btn{text-decoration:none}
button.fb-btn{height:26px;_line-height:18px;*overflow:visible}
button.fb-btn::-moz-focus-inner{padding:0;border:0}
.fb-btn .c-icon{margin-top:5px}
.fb-btn-primary,.fb-btn-primary:visited{color:#fff!important}
.fb-btn-primary{background-color:#388bff;_width:82px;border-color:#3c8dff #408ffe #3680e6}
.fb-btn-primary:hover{border-color:#2678ec #2575e7 #1c6fe2 #2677e7;background-color:#388bff;background-image:url(data:image/png;
		base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i/9PO5r4AAAAD0lEQVR42gEEAPv/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}
.fb-btn-primary:active{border-color:#178ee3 #1784d0 #177bbf #1780ca;background-color:#388bff;background-image:none;box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-webkit-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-moz-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-o-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15)}
.fb-feedback-right-dialog{position:fixed;z-index:299;bottom:0;right:0}
.fb-feedback-list-dialog,.fb-feedback-list-dialog-left{position:absolute;z-index:299}
.fb-feedback-list-dialog:before{content:"";width:0;height:0;display:block;position:absolute;top:15px;left:-6px;border-top:8px solid transparent;border-bottom:8px solid transparent;border-right:8px solid #fff}
.fb-feedback-list-dialog-left:before{content:"";width:0;height:0;display:block;position:absolute;top:15px;right:-6px;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:8px solid #fff}
.fb-header{padding-left:20px;padding-right:20px;margin-top:14px;text-align:left;-moz-user-select:none}
.fb-header .fb-close{color:#e0e0e0}
.fb-close{text-decoration:none;margin-top:2px;float:right;font-size:20px;font-weight:700;line-height:18px;color:#666;text-shadow:0 1px 0 #fff}
.fb-photo-block{display:none}
.fb-photo-block-title{font-size:13px;color:#333;padding-top:10px}
.fb-photo-block-title-span{color:#999}
.fb-photo-sub-block{margin-top:10px;margin-bottom:10px;width:60px;text-align:center}
.fb-photo-sub-block-hide{display:none}
.fb-photo-update-block{overflow:hidden}
.fb-photo-update-item-block{width:100px;height:100px;background:red;border:solid 1px #ccc;margin-top:10px;float:left;margin-right:20px;position:relative;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/feedback_add_photo_69ff822.png);background-repeat:no-repeat;background-size:contain;background-position:center center;background-size:24px 24px}
.fb-photo-block-title-ex{font-size:13px;float:right}
.fb-photo-block-title-ex img{vertical-align:text-top;margin-right:4px}
.fb-photo-block-title-span{margin-left:4px;color:#999}
.fb-photo-update-item-show-img{width:100%;height:100%;display:none}
.fb-photo-update-item-close{width:13px;height:13px;position:absolute;top:-6px;right:-6px;display:none}
.fb-photo-block input{display:none}
.fb-photo-update-hide{display:none}
.fb-photo-update-item-block{width:60px;height:60px;border:solid 1px #ccc;float:left}
.fb-photo-block-example{position:absolute;top:0;left:0;display:none;background-color:#fff;padding:14px;padding-top:0;width:392px}
.fb-photo-block-example-header{padding-top:14px;overflow:hidden}
.fb-photo-block-example-header p{float:left}
.fb-photo-block-example-header img{float:right;width:13px;height:13px}
.fb-photo-block-example-img img{margin:0 auto;margin-top:14px;display:block;width:200px}
.fb-photo-block-example-title{text-align:center}
.fb-photo-block-example-title-big{font-size:14px;color:#333}
.fb-photo-block-example-title-small{font-size:13px;color:#666}
.fb-header a.fb-close:hover{text-decoration:none}
.fb-photo-block-upinfo{width:100%}
.fb-header-tips{font-size:16px;margin:0;color:#333;text-rendering:optimizelegibility}
.fb-body{margin-bottom:0;padding:20px;padding-top:10px;overflow:hidden;text-align:left}
.fb-modal,.fb-success{background-color:#fff;cursor:default;top:100%;left:100%;width:390px;overflow:hidden;border:1px solid #999;*border:1px solid #ddd;font-size:13px;line-height:1.54}
.fb-textarea textarea{width:350px;height:64px;padding:4px;margin:10px 0;vertical-align:top;resize:none;overflow:auto;box-sizing:border-box;display:inline-block;border:1px solid #ccc;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border linear .2s,box-shadow linear .2s;-moz-transition:border linear .2s,box-shadow linear .2s;-ms-transition:border linear .2s,box-shadow linear .2s;-o-transition:border linear .2s,box-shadow linear .2s;transition:border linear .2s,box-shadow linear .2s}
.fb-selected{display:none;width:12px;height:12px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAFCAYAAACJmvbYAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAABYlAAAWJQFJUiTwAAAAJklEQVQI12NgwAEsuv/8xy9h3vX7P6oEKp/BHCqA0yhzdB0MDAwAFXkTK5la4mAAAAAASUVORK5CYII=) no-repeat 2px 3px}
.fb-guide{padding-top:10px;color:#9a9a9a;margin-left:-20px;padding-left:20px;border-right-width:0;margin-right:-20px;padding-right:25px;margin-bottom:-20px;padding-bottom:15px}
.fb-footer{padding-top:10px;text-align:left}
.fb-block{overflow:hidden;position:relative}
.fb-block .fb-email{height:28px;line-height:26px;width:350px;border:1px solid #ccc;padding:4px;padding-top:0;box-sizing:border-box;padding-bottom:0;display:inline-block;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;vertical-align:middle!important;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border linear .2s,box-shadow linear .2s;-moz-transition:border linear .2s,box-shadow linear .2s;-ms-transition:border linear .2s,box-shadow linear .2s;-o-transition:border linear .2s,box-shadow linear .2s;transition:border linear .2s,box-shadow linear .2s}
.fb-email{font-size:13px!important;color:#000}
.fb-email::-webkit-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-email:-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-email::-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-email:-ms-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-cut-block{height:15px;padding-bottom:10px}
.fb-canvas-block{height:172px;border:1px solid #ccc;margin-bottom:10px;position:relative;overflow:hidden;width:100%;background-position:center;box-sizing:border-box}
.fb-canvas-block img{width:350px;position:absolute}
.fb-canvas-block img[src=""]{opacity:0}
.fb-cut-input{width:14px;height:14px;margin:0;margin-right:10px;display:inline-block;border:1px solid #ccc}
.fb-cut-btn{width:60px!important}
#fb_tips_span{vertical-align:middle}
#fb_popwindow{display:block;left:457px;top:69.5px;position:absolute;width:450px;z-index:999999;background:none repeat scroll 0 0 #fff;border:1px solid #999;border-radius:3px;box-shadow:0 0 9px #999;padding:0}
#feedback_dialog_content{text-align:center}
#fb_right_post_save:hover{background-image:url(data:image/png;
		base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i/9PO5r4AAAAD0lEQVR42gEEAPv/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}
.fb-select-icon{position:absolute;bottom:6px;right:5px;width:16px;height:16px;box-sizing:content-box;background-position:center center;background-repeat:no-repeat;background-size:7px 4px;-webkit-background-size:7px 4px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAECAYAAABCxiV9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsSAAALEgHS3X78AAAAKElEQVQI12Ps7Or6z4ADMDIwMDBgU1BeVsbICOMgKygvK2PEMAbdBAAhxA08t5Q3VgAAAABJRU5ErkJggg==)}
.fb-select-shorter{position:relative;min-height:28px}
.fb-type-container{line-height:28px;position:absolute;top:28px;width:100%;background-color:#fff;border:1px solid #ccc;z-index:300;margin-left:-1px;display:none}
.fb-type-item,.fb-type-selected{height:28px;line-height:30px;padding-left:4px}
.fb-type-item:hover{background:#f5F5F5}
.fb-checkbox{position:relative;border-bottom:1px solid #eee;height:34px;line-height:35px}
.fb-checkbox:last-child{border-bottom:0}
.fb-list-wrapper{margin-top:-10px}
.fb-textarea-sug textarea{margin-top:0}
@media screen and (min-width:1921px){.slowmsg{left:50%!important;-webkit-transform:translateX(-50%);-ms-transform:translateX(-50%);transform:translateX(-50%)}
.wrapper_l #head{-webkit-transform-style:preserve-3d;transform-style:preserve-3d}
.head_wrapper{width:1196px;margin:0 auto;position:relative;-webkit-transform:translate3d(-52px,0,1px);transform:translate3d(-52px,0,1px)}
#head .headBlock{-webkit-box-sizing:border-box;box-sizing:border-box;margin-left:auto;margin-right:auto;width:1196px;padding-left:121px;-webkit-transform:translate3d(-52px,0,0);transform:translate3d(-52px,0,0)}
#s_tab.s_tab{padding-left:0}
#s_tab.s_tab .s_tab_inner{display:block;-webkit-box-sizing:border-box;box-sizing:border-box;padding-left:77px;width:1212px;margin:0 auto}
#con-at .result-op{margin-left:auto;margin-right:auto;-webkit-transform:translateX(-60px);-ms-transform:translateX(-60px);transform:translateX(-60px)}
#wrapper_wrapper{margin-left:-88px}
#container{-webkit-box-sizing:border-box;box-sizing:border-box;width:1212px;margin:0 auto}
.foot-inner{width:1212px;margin:0 auto}}
#seth{display:inline;behavior:url(#default#homepage)}
#setf{display:inline}
#sekj{margin-left:14px}
#st,#sekj{display:none}
.s_ipt_wr{border:1px solid #b6b6b6;border-color:#7b7b7b #b6b6b6 #b6b6b6 #7b7b7b;background:#fff;display:inline-block;vertical-align:top;width:539px;margin-right:0;border-right-width:0;border-color:#b8b8b8 transparent #ccc #b8b8b8;overflow:hidden}
.wrapper_s .s_ipt_wr{width:439px}
.wrapper_s .s_ipt{width:434px}
.wrapper_s .s_ipt_tip{width:434px}
.s_ipt_wr:hover,.s_ipt_wr.ipthover{border-color:#999 transparent #b3b3b3 #999}
.s_ipt_wr.iptfocus{border-color:#4791ff transparent #4791ff #4791ff}
.s_ipt_tip{color:#aaa;position:absolute;z-index:-10;font:16px/22px arial;height:32px;line-height:32px;padding-left:7px;overflow:hidden;width:526px}
.s_ipt{width:526px;height:22px;font:16px/18px arial;line-height:22px;margin:6px 0 0 7px;padding:0;background:transparent;border:0;outline:0;-webkit-appearance:none}
#kw{position:relative}
#u .username i{background-position:-408px -144px}
.bdpfmenu,.usermenu{border:1px solid #d1d1d1;position:absolute;width:105px;top:36px;z-index:302;box-shadow:1px 1px 5px #d1d1d1;-webkit-box-shadow:1px 1px 5px #d1d1d1;-moz-box-shadow:1px 1px 5px #d1d1d1;-o-box-shadow:1px 1px 5px #d1d1d1}
.bdpfmenu{font-size:12px;background-color:#fff}
.bdpfmenu a,.usermenu a{display:block;text-align:left;margin:0!important;padding:0 9px;line-height:26px;text-decoration:none}
.briiconsbg{background-repeat:no-repeat;background-size:300px 18px;background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_0c37e9b.png);background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_809ae65.gif)\9}
#u{z-index:301;position:absolute;right:0;top:0;margin:21px 9px 5px 0;padding:0}
.wrapper_s #u{margin-right:3px}
#u a{text-decoration:underline;color:#333;margin:0 7px}
.wrapper_s #u a{margin-right:0 6px}
#u div a{text-decoration:none}
#u a:hover{text-decoration:underline}
#u .back_org{color:#666;float:left;display:inline-block;height:24px;line-height:24px}
#u .bri{display:inline-block;width:24px;height:24px;float:left;line-height:24px;color:transparent;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_0c37e9b.png) no-repeat 4px 3px;background-size:300px 18px;background-image:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/icons_809ae65.gif)\9;overflow:hidden}
#u .bri:hover,#u .bri.brihover{background-position:-18px 3px}
#mCon #imeSIcon{background-position:-408px -144px;margin-left:0}
#mCon span{color:#333}
.bdpfmenu a:link,.bdpfmenu a:visited,#u .usermenu a:link,#u .usermenu a:visited{background:#fff;color:#333}
.bdpfmenu a:hover,.bdpfmenu a:active,#u .usermenu a:hover,#u .usermenu a:active{background:#38f;text-decoration:none;color:#fff}
.bdpfmenu{width:70px}
.usermenu{width:68px;right:8px}
#wrapper .bdnuarrow{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;top:-10px;left:50%;margin-left:-5px}
#wrapper .bdnuarrow em,#wrapper .bdnuarrow i{width:0;height:0;font-size:0;line-height:0;display:block;position:absolute;border:5px solid transparent;border-style:dashed dashed solid}
#wrapper .bdnuarrow em{border-bottom-color:#d8d8d8;top:-1px}
#wrapper .bdnuarrow i{border-bottom-color:#fff;top:0}
#prefpanel{background:#fafafa;display:none;opacity:0;position:fixed;_position:absolute;top:-359px;z-index:500;width:100%;min-width:960px;border-bottom:1px solid #ebebeb}
#prefpanel form{_width:850px}
#kw_tip{cursor:default;display:none;margin-top:1px}
#bds-message-wrapper{top:43px}
.quickdelete-wrap{position:relative}
.quickdelete-wrap input{width:500px}
.wrapper_l .quickdelete-wrap input{width:500px}
.wrapper_s .quickdelete-wrap input{width:402px}
input::-ms-clear{display:none}
.quickdelete{width:32px;height:32px;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/quickdelete_33e3eb8.png) no-repeat;background-position:10px 10px;position:absolute;display:block}
.quickdelete:hover{background-position:10px -24px}
#lh a{margin-left:25px}
.bdbriwrapper-tuiguang{display:none!important}
.soutu-input{padding-left:55px!important}
.soutu-input-image{position:absolute;left:1px;top:1px;height:28px;width:49px;z-index:1;padding:0;background:#e6e6e6;border:1px solid #e6e6e6}
.soutu-input-thumb{height:28px;width:28px;min-width:1px}
.soutu-input-close{position:absolute;right:0;top:0;cursor:pointer;display:block;width:22px;height:28px}
.soutu-input-close::after{content:" ";position:absolute;right:3px;top:50%;cursor:pointer;margin-top:-7px;display:block;width:14px;height:14px;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/soutu/img/soutu_icons_new_8abaf8a.png) no-repeat -163px 0}
.soutu-input-image:hover .soutu-input-close::after{background-position:-215px 2px}
.fb-hint{margin-top:5px;transition-duration:.9s;opacity:0;display:none;color:red}
.fb-img{display:none}
.fb-hint-tip{height:44px;line-height:24px;background-color:#38f;color:#fff;box-sizing:border-box;width:269px;font-size:16px;padding:10px;padding-left:14px;position:absolute;top:-65px;right:-15px;border-radius:3px;z-index:299}
.fb-hint-tip::before{content:"";width:0;height:0;display:block;position:absolute;border-left:8px solid transparent;border-right:8px solid transparent;border-top:8px solid #38f;bottom:-8px;right:25px}
.fb-mask,.fb-mask-light{position:fixed;top:0;left:0;bottom:0;right:0;z-index:296;background-color:#000;filter:alpha(opacity=60);background-color:rgba(0,0,0,.6)}
.fb-mask-light{background-color:#fff;filter:alpha(opacity=0);background-color:rgba(255,255,255,0)}
.fb-success .fb-success-text{text-align:center;color:#333;font-size:13px;margin-bottom:14px}
.fb-success-text.fb-success-text-title{color:#3b6;font-size:16px;margin-bottom:16px}
.fb-success-text-title i{width:16px;height:16px;margin-right:5px}
.fb-list-container{box-sizing:border-box;padding:4px 8px;position:absolute;top:0;left:0;bottom:0;right:0;z-index:298;display:block;width:100%;cursor:pointer;margin-top:-5px;margin-left:-5px}
.fb-list-container-hover{background-color:#fff;border:2px #38f solid}
.fb-list-container-first{box-sizing:border-box;padding-left:10px;padding-top:5px;position:absolute;top:0;left:0;bottom:0;right:0;z-index:297;display:block;width:100%;cursor:pointer;margin-top:-5px;margin-left:-5px;border:3px #f5f5f5 dashed;border-radius:3px}
.fb-des-content{font-size:13px!important;color:#000}
.fb-des-content::-webkit-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-des-content:-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-des-content::-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-des-content:-ms-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-btn,.fb-btn:visited{color:#333!important}
.fb-select{position:relative;background-color:#fff;border:1px solid #ccc}
.fb-select i{position:absolute;right:2px;top:7px}
.fb-type{width:350px;box-sizing:border-box;height:28px;font-size:13px;line-height:28px;border:0;word-break:normal;word-wrap:normal;position:relative;appearance:none;-moz-appearance:none;-webkit-appearance:none;display:inline-block;vertical-align:middle;line-height:normal;color:#333;background-color:transparent;border-radius:0;overflow:hidden;outline:0;padding-left:5px}
.fb-type::-ms-expand{display:none}
.fb-btn{display:inline-block;padding:0 14px;margin:0;height:24px;line-height:25px;font-size:13px;filter:chroma(color=#000000);*zoom:1;border:1px solid #d8d8d8;cursor:pointer;font-family:inherit;font-weight:400;text-align:center;vertical-align:middle;background-color:#f9f9f9;overflow:hidden;outline:0}
.fb-btn:hover{border-color:#388bff}
.fb-btn:active{border-color:#a2a6ab;background-color:#f0f0f0;box-shadow:inset 1px 1px 1px #c7c7c7;-webkit-box-shadow:inset 1px 1px 1px #c7c7c7;-moz-box-shadow:inset 1px 1px 1px #c7c7c7;-o-box-shadow:inset 1px 1px 1px #c7c7c7}
a.fb-btn{text-decoration:none}
button.fb-btn{height:26px;_line-height:18px;*overflow:visible}
button.fb-btn::-moz-focus-inner{padding:0;border:0}
.fb-btn .c-icon{margin-top:5px}
.fb-btn-primary,.fb-btn-primary:visited{color:#fff!important}
.fb-btn-primary{background-color:#388bff;_width:82px;border-color:#3c8dff #408ffe #3680e6}
.fb-btn-primary:hover{border-color:#2678ec #2575e7 #1c6fe2 #2677e7;background-color:#388bff;background-image:url(data:image/png;
		base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i/9PO5r4AAAAD0lEQVR42gEEAPv/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}
.fb-btn-primary:active{border-color:#178ee3 #1784d0 #177bbf #1780ca;background-color:#388bff;background-image:none;box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-webkit-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-moz-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15);-o-box-shadow:inset 1px 1px 1px rgba(0,0,0,.15)}
.fb-feedback-right-dialog{position:fixed;z-index:299;bottom:0;right:0}
.fb-feedback-list-dialog,.fb-feedback-list-dialog-left{position:absolute;z-index:299}
.fb-feedback-list-dialog:before{content:"";width:0;height:0;display:block;position:absolute;top:15px;left:-6px;border-top:8px solid transparent;border-bottom:8px solid transparent;border-right:8px solid #fff}
.fb-feedback-list-dialog-left:before{content:"";width:0;height:0;display:block;position:absolute;top:15px;right:-6px;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:8px solid #fff}
.fb-header{padding-left:20px;padding-right:20px;margin-top:14px;text-align:left;-moz-user-select:none}
.fb-header .fb-close{color:#e0e0e0}
.fb-close{text-decoration:none;margin-top:2px;float:right;font-size:20px;font-weight:700;line-height:18px;color:#666;text-shadow:0 1px 0 #fff}
.fb-photo-block{display:none}
.fb-photo-block-title{font-size:13px;color:#333;padding-top:10px}
.fb-photo-block-title-span{color:#999}
.fb-photo-sub-block{margin-top:10px;margin-bottom:10px;width:60px;text-align:center}
.fb-photo-sub-block-hide{display:none}
.fb-photo-update-block{overflow:hidden}
.fb-photo-update-item-block{width:100px;height:100px;background:red;border:solid 1px #ccc;margin-top:10px;float:left;margin-right:20px;position:relative;background:url(https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/feedback_add_photo_69ff822.png);background-repeat:no-repeat;background-size:contain;background-position:center center;background-size:24px 24px}
.fb-photo-block-title-ex{font-size:13px;float:right}
.fb-photo-block-title-ex img{vertical-align:text-top;margin-right:4px}
.fb-photo-block-title-span{margin-left:4px;color:#999}
.fb-photo-update-item-show-img{width:100%;height:100%;display:none}
.fb-photo-update-item-close{width:13px;height:13px;position:absolute;top:-6px;right:-6px;display:none}
.fb-photo-block input{display:none}
.fb-photo-update-hide{display:none}
.fb-photo-update-item-block{width:60px;height:60px;border:solid 1px #ccc;float:left}
.fb-photo-block-example{position:absolute;top:0;left:0;display:none;background-color:#fff;padding:14px;padding-top:0;width:392px}
.fb-photo-block-example-header{padding-top:14px;overflow:hidden}
.fb-photo-block-example-header p{float:left}
.fb-photo-block-example-header img{float:right;width:13px;height:13px}
.fb-photo-block-example-img img{margin:0 auto;margin-top:14px;display:block;width:200px}
.fb-photo-block-example-title{text-align:center}
.fb-photo-block-example-title-big{font-size:14px;color:#333}
.fb-photo-block-example-title-small{font-size:13px;color:#666}
.fb-header a.fb-close:hover{text-decoration:none}
.fb-photo-block-upinfo{width:100%}
.fb-header-tips{font-size:16px;margin:0;color:#333;text-rendering:optimizelegibility}
.fb-body{margin-bottom:0;padding:20px;padding-top:10px;overflow:hidden;text-align:left}
.fb-modal,.fb-success{background-color:#fff;cursor:default;top:100%;left:100%;width:390px;overflow:hidden;border:1px solid #999;*border:1px solid #ddd;font-size:13px;line-height:1.54}
.fb-textarea textarea{width:350px;height:64px;padding:4px;margin:10px 0;vertical-align:top;resize:none;overflow:auto;box-sizing:border-box;display:inline-block;border:1px solid #ccc;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border linear .2s,box-shadow linear .2s;-moz-transition:border linear .2s,box-shadow linear .2s;-ms-transition:border linear .2s,box-shadow linear .2s;-o-transition:border linear .2s,box-shadow linear .2s;transition:border linear .2s,box-shadow linear .2s}
.fb-selected{display:none;width:12px;height:12px;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAFCAYAAACJmvbYAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAABYlAAAWJQFJUiTwAAAAJklEQVQI12NgwAEsuv/8xy9h3vX7P6oEKp/BHCqA0yhzdB0MDAwAFXkTK5la4mAAAAAASUVORK5CYII=) no-repeat 2px 3px}
.fb-guide{padding-top:10px;color:#9a9a9a;margin-left:-20px;padding-left:20px;border-right-width:0;margin-right:-20px;padding-right:25px;margin-bottom:-20px;padding-bottom:15px}
.fb-footer{padding-top:10px;text-align:left}
.fb-block{overflow:hidden;position:relative}
.fb-block .fb-email{height:28px;line-height:26px;width:350px;border:1px solid #ccc;padding:4px;padding-top:0;box-sizing:border-box;padding-bottom:0;display:inline-block;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;vertical-align:middle!important;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border linear .2s,box-shadow linear .2s;-moz-transition:border linear .2s,box-shadow linear .2s;-ms-transition:border linear .2s,box-shadow linear .2s;-o-transition:border linear .2s,box-shadow linear .2s;transition:border linear .2s,box-shadow linear .2s}
.fb-email{font-size:13px!important;color:#000}
.fb-email::-webkit-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-email:-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-email::-moz-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-email:-ms-input-placeholder{font-size:13px!important;color:#9a9a9a}
.fb-cut-block{height:15px;padding-bottom:10px}
.fb-canvas-block{height:172px;border:1px solid #ccc;margin-bottom:10px;position:relative;overflow:hidden;width:100%;background-position:center;box-sizing:border-box}
.fb-canvas-block img{width:350px;position:absolute}
.fb-canvas-block img[src=""]{opacity:0}
.fb-cut-input{width:14px;height:14px;margin:0;margin-right:10px;display:inline-block;border:1px solid #ccc}
.fb-cut-btn{width:60px!important}
#fb_tips_span{vertical-align:middle}
#fb_popwindow{display:block;left:457px;top:69.5px;position:absolute;width:450px;z-index:999999;background:none repeat scroll 0 0 #fff;border:1px solid #999;border-radius:3px;box-shadow:0 0 9px #999;padding:0}
#feedback_dialog_content{text-align:center}
#fb_right_post_save:hover{background-image:url(data:image/png;
		base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAMAAACuX0YVAAAABlBMVEVnpv85i/9PO5r4AAAAD0lEQVR42gEEAPv/AAAAAQAFAAIros7PAAAAAElFTkSuQmCC);background-repeat:repeat-x;box-shadow:1px 1px 1px rgba(0,0,0,.4);-webkit-box-shadow:1px 1px 1px rgba(0,0,0,.4);-moz-box-shadow:1px 1px 1px rgba(0,0,0,.4);-o-box-shadow:1px 1px 1px rgba(0,0,0,.4)}
.fb-select-icon{position:absolute;bottom:6px;right:5px;width:16px;height:16px;box-sizing:content-box;background-position:center center;background-repeat:no-repeat;background-size:7px 4px;-webkit-background-size:7px 4px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAECAYAAABCxiV9AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsSAAALEgHS3X78AAAAKElEQVQI12Ps7Or6z4ADMDIwMDBgU1BeVsbICOMgKygvK2PEMAbdBAAhxA08t5Q3VgAAAABJRU5ErkJggg==)}
.fb-select-shorter{position:relative;min-height:28px}
.fb-type-container{line-height:28px;position:absolute;top:28px;width:100%;background-color:#fff;border:1px solid #ccc;z-index:300;margin-left:-1px;display:none}
.fb-type-item,.fb-type-selected{height:28px;line-height:30px;padding-left:4px}
.fb-type-item:hover{background:#f5F5F5}
.fb-checkbox{position:relative;border-bottom:1px solid #eee;height:34px;line-height:35px}
.fb-checkbox:last-child{border-bottom:0}
.fb-list-wrapper{margin-top:-10px}
.fb-textarea-sug textarea{margin-top:0}</style>

		

<noscript>
	<meta http-equiv="refresh" content="0; url=/s?wd=ip&oq=ip&tn=monline_4_dg&ie=utf-8&rsv_pq=a0f6cd0c0000d262&rsv_t=5488BRsscwPJcYs0QpTSq9MErvB9ZjpKp6c2tqB5Wz1clwUn4IeDe%2Flpm%2Bz5qSpsezwj&rqlang=cn&nojs=1&bqid=a0f6cd0c0000d262"/>
</noscript>


<script>

	var hashMatch = document.location.href.match(/#+(.*wd=[^&].+)/);

	if (hashMatch && hashMatch[0] && hashMatch[1]) {
		document.location.replace("http://"+location.host+"/s?"+hashMatch[1]);
	}

	//结果页js命名空间
	var bds = {
		comm:{
        	loginAction : []
		},
		se:{},
		su:{
				urdata:[],
			urSendClick:function(){}
		},
		util:{},
		use:{},
		_base64:{
			domain : "https://ss0.bdstatic.com/9uN1bjq8AAUYm2zgoY3K/",
			b64Exp : -1,
			pdc : -1
		}
	};

	//防止从结果页打开的页面中通过opener.xxx来影响百度页面
	var al_arr=[];
	var selfOpen = window.open;eval("var open = selfOpen;");
	var isIE=navigator.userAgent.indexOf("MSIE")!=-1&&!window.opera;
	var E = bds.ecom= {};
	document.cookie='ISWR=;domain=.baidu.com;path=/;expires=Fri, 02-Jan-1970 00:00:00 GMT';
	var detectIntervals = [{status: 18, time: 6000 }, {status: 17, time: 10000 }];
	detectIntervals.forEach(function (detect) {
        setTimeout(function() {
            var lefter = document.getElementById('content_left');
            var rsnum = document.getElementsByClassName('result').length;
            var contentno = document.getElementsByClassName('content_none').length;
            if (!lefter && !rsnum && !contentno) {
                var date = new Date();
                date.setTime(date.getTime() + 5 * 60 * 1000);
                document.cookie = 'ISWR=' + detect.status + ';domain=.baidu.com;path=/;expires=' + date.toGMTString() + ';';
            }
        }, detect.time);
    });
</script>
<script>
/* https域名转换工具 */
bds.util.domain = (function(){
	    																					            																							var list = {
        "graph.baidu.com": "https://sp0.baidu.com/-aYHfD0a2gU2pMbgoY3K",
		"p.qiao.baidu.com":"https://sp0.baidu.com/5PoXdTebKgQFm2e88IuM_a",
		"vse.baidu.com":"https://sp3.baidu.com/6qUDsjip0QIZ8tyhnq",
		"hdpreload.baidu.com":"https://sp3.baidu.com/7LAWfjuc_wUI8t7jm9iCKT-xh_",
		"lcr.open.baidu.com":"https://sp2.baidu.com/8LUYsjW91Qh3otqbppnN2DJv",
		"kankan.baidu.com":"https://sp3.baidu.com/7bM1dzeaKgQFm2e88IuM_a",
		"xapp.baidu.com":"https://sp2.baidu.com/yLMWfHSm2Q5IlBGlnYG",
		"dr.dh.baidu.com":"https://sp0.baidu.com/-KZ1aD0a2gU2pMbgoY3K",
		"xiaodu.baidu.com":"https://sp0.baidu.com/yLsHczq6KgQFm2e88IuM_a",
		"sensearch.baidu.com":"https://sp1.baidu.com/5b11fzupBgM18t7jm9iCKT-xh_",
		"s1.bdstatic.com":"https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K",
		"olime.baidu.com":"https://sp0.baidu.com/8bg4cTva2gU2pMbgoY3K",
		"app.baidu.com":"https://sp2.baidu.com/9_QWsjip0QIZ8tyhnq",
		"i.baidu.com":"https://sp0.baidu.com/74oIbT3kAMgDnd_",
		"c.baidu.com":"https://sp0.baidu.com/9foIbT3kAMgDnd_",
		"sclick.baidu.com":"https://sp0.baidu.com/5bU_dTmfKgQFm2e88IuM_a",
		"nsclick.baidu.com":"https://sp1.baidu.com/8qUJcD3n0sgCo2Kml5_Y_D3",
		"sestat.baidu.com":"https://sp1.baidu.com/5b1ZeDe5KgQFm2e88IuM_a",
		"eclick.baidu.com":"https://sp3.baidu.com/-0U_dTmfKgQFm2e88IuM_a",
		"api.map.baidu.com":"https://sp2.baidu.com/9_Q4sjOpB1gCo2Kml5_Y_D3",
		"ecma.bdimg.com":"https://ss1.bdstatic.com/-0U0bXSm1A5BphGlnYG",
		"ecmb.bdimg.com":"https://ss0.bdstatic.com/-0U0bnSm1A5BphGlnYG",
        "t1.baidu.com":"https://ss0.baidu.com/6ON1bjeh1BF3odCf",
        "t2.baidu.com":"https://ss1.baidu.com/6OZ1bjeh1BF3odCf",
        "t3.baidu.com":"https://ss2.baidu.com/6OV1bjeh1BF3odCf",
		"t10.baidu.com":"https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq",
		"t11.baidu.com":"https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq",
		"t12.baidu.com":"https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq",
		"i7.baidu.com":"https://ss0.baidu.com/73F1bjeh1BF3odCf",
		"i8.baidu.com":"https://ss0.baidu.com/73x1bjeh1BF3odCf",
		"i9.baidu.com":"https://ss0.baidu.com/73t1bjeh1BF3odCf",
		"b1.bdstatic.com":"https://ss0.bdstatic.com/9uN1bjq8AAUYm2zgoY3K",
		"ss.bdimg.com":"https://ss1.bdstatic.com/5aV1bjqh_Q23odCf",
		"opendata.baidu.com":"https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv",
		"api.open.baidu.com":"https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv",
		"tag.baidu.com":"https://sp1.baidu.com/6LMFsjip0QIZ8tyhnq",
		"f3.baidu.com":"https://sp2.baidu.com/-uV1bjeh1BF3odCf",
		"s.share.baidu.com":"https://sp0.baidu.com/5foZdDe71MgCo2Kml5_Y_D3",	
		"bdimg.share.baidu.com":"https://ss1.baidu.com/9rA4cT8aBw9FktbgoI7O1ygwehsv",
        "1.su.bdimg.com":"https://ss0.bdstatic.com/k4oZeXSm1A5BphGlnYG",
        "2.su.bdimg.com":"https://ss1.bdstatic.com/kvoZeXSm1A5BphGlnYG",
        "3.su.bdimg.com":"https://ss2.bdstatic.com/kfoZeXSm1A5BphGlnYG",
        "4.su.bdimg.com":"https://ss3.bdstatic.com/lPoZeXSm1A5BphGlnYG",
        "5.su.bdimg.com":"https://ss0.bdstatic.com/l4oZeXSm1A5BphGlnYG",
        "6.su.bdimg.com":"https://ss1.bdstatic.com/lvoZeXSm1A5BphGlnYG",
        "7.su.bdimg.com":"https://ss2.bdstatic.com/lfoZeXSm1A5BphGlnYG",
        "8.su.bdimg.com":"https://ss3.bdstatic.com/iPoZeXSm1A5BphGlnYG"
	};


	var get = function(url) {
		if(location.protocol === "http") {
			return url;
		}
		var reg = /^(http[s]?:\/\/)?([^\/]+)(.*)/,
		matches = url.match(reg);
		/* 判断传入参数是域名还是地址，分别做处理 */
		url = list.hasOwnProperty(matches[2])&&(list[matches[2]] + matches[3]) || url;
		return url;
	},
	set = function(kdomain,vdomain) {
		list[kdomain] = vdomain;
	};
	return {
		get : get,
		set : set
	}
})();
</script>




<script type="text/javascript" data-for="result">function G(n){return document.getElementById(n)}function ns_c_pj(n,e){var t=encodeURIComponent(window.document.location.href),i="",s="",o="",r=bds&&bds.comm&&bds.comm.did?bds.comm.did:"";wd=bds.comm.queryEnc,nsclickDomain=bds&&bds.util&&bds.util.domain?bds.util.domain.get("http://nsclick.baidu.com"):"http://nsclick.baidu.com",img=window["BD_PS_C"+(new Date).getTime()]=new Image,src="";for(v in n){switch(v){case"title":s=encodeURIComponent(n[v].replace(/<[^<>]+>/g,""));break;case"url":s=encodeURIComponent(n[v]);
break;default:s=n[v]}i+=v+"="+s+"&"}if(o="&mu="+t,src=nsclickDomain+"/v.gif?pid=201&"+(e||"")+i+"path="+t+"&wd="+wd+"&rsv_sid="+(bds.comm.ishome&&bds.comm.indexSid?bds.comm.indexSid:bds.comm.sid)+"&rsv_did="+r+"&t="+(new Date).getTime(),"undefined"!=typeof Cookie&&"undefined"!=typeof Cookie.get)Cookie.get("H_PS_SKIN")&&"0"!=Cookie.get("H_PS_SKIN")&&(src+="&rsv_skin=1");else{var c="";try{c=parseInt(document.cookie.match(new RegExp("(^| )H_PS_SKIN=([^;]*)(;|$)"))[2])}catch(a){}c&&"0"!=c&&(src+="&rsv_skin=1")
}return img.src=src,!0}function ns_c(n,e){return e===!0?ns_c_pj(n,"pj=www&rsv_sample=1&"):ns_c_pj(n,"pj=www&")}window.A||(window.bds=window.bds||{},bds.util=bds.util||{},bds.util.getWinWidth=function(){return window.document.documentElement.clientWidth},bds.util.setContainerWidth=function(){var n=G("container"),e=G("wrapper"),t=function(n,e){e.className=e.className.replace(n,"")},i=function(n,e){e.className=(e.className+" "+n).replace(/^\s+/g,"")},s=function(n,e){return n.test(e.className)};bds.util.getWinWidth()<1207?(n&&(t(/\bcontainer_l\b/g,n),s(/\bcontainer_s\b/,n)||i("container_s",n)),e&&(t(/\bwrapper_l\b/g,e),s(/\bwrapper_s\b/,e)||i("wrapper_s",e)),bds.comm.containerSize="s"):(n&&(t(/\bcontainer_s\b/g,n),s(/\bcontainer_l\b/,n)||i("container_l",n)),e&&(t(/\bwrapper_s\b/g,e),s(/\bwrapper_l\b/,e)||i("wrapper_l",e)),bds.comm.containerSize="l")
},function(){var n=[],e=!1,t=function(n,e){try{n.call(e)}catch(t){}},i=function(){this.ids=[],this.has=!0,this.list=[],this.logs=[],this.loadTimes=[],this.groupData=[],this.mergeFns=[],this._currentContainer=null};window.A=bds.aladdin={},t(i,window.A),bds.ready=function(i){"function"==typeof i&&(e?t(i):n.push(i))},bds.doReady=function(){for(e=!0;n.length;)t(n.shift())},bds.clearReady=function(){e=!1,n=[]},A.__reset=i;var s=function(){var n=document.getElementsByTagName("script");return function(){var e=n[n.length-1];
window.currentScriptElem&&(e=window.currentScriptElem);for(var t=e;t;){if(t.className&&/(?:^|\s)result(?:-op)?(?:$|\s)/.test(t.className)&&(tplname=t.getAttribute("tpl")))return t;t=t.parentNode}}}(),o=function(n,e,t){var i;if(n.initIndex?i=A.groupData[n.initIndex-1]:(i={container:n,data:{},handlers:[]},n.initIndex=A.groupData.length+1,A.groupData.push(i)),"function"==typeof e)i.handlers.push(e);else if("object"==typeof e)for(var s in e)e.hasOwnProperty(s)&&(i.data[s]=e[s]);else i.data[e]=t};A.init=A.setup=function(n,e){if(void 0!==n&&null!==n){var t=A._currentContainer||s();
t&&o(t,n,e)}},A.merge=function(n,e){A.mergeFns.push({tplName:n,fn:e})}}());</script>


	</head>
	

	<body link="#0000cc">
		


		
		<div id="wrapper" class="wrapper_l">
		
			

			

			

<script>if(window.bds&&bds.util&&bds.util.setContainerWidth){bds.util.setContainerWidth();}</script><div id="head"><div class="head_wrapper"><div class="s_form"><div class="s_form_wrapper"><style>.index-logo-srcnew {display: none;}@media (-webkit-min-device-pixel-ratio: 2),(min--moz-device-pixel-ratio: 2),(-o-min-device-pixel-ratio: 2),(min-device-pixel-ratio: 2){.index-logo-src {display: none;}.index-logo-srcnew {display: inline;}}</style><div id="lg"><img hidefocus="true" src="//www.baidu.com/img/bd_logo1.png" width="270" height="129"></div><a href="/" id="result_logo" onmousedown="return c({'fm':'tab','tab':'logo'})"><img class='index-logo-src' src="//www.baidu.com/img/baidu_jgylogo3.gif" alt="到百度首页" title="到百度首页"><img class='index-logo-srcnew' src="//www.baidu.com/img/baidu_jgylogo3.gif" alt="到百度首页" title="到百度首页"></a><form id="form" name="f" action="/s" class="fm"><input type="hidden" name="ie" value="utf-8"><input type="hidden" name="f" value="8"><input type="hidden" name="rsv_bp" value="1"><input type=hidden name=ch value=""><input type=hidden name=tn value="monline_4_dg"><input type=hidden name=bar value=""><span class="bg s_ipt_wr"><input id="kw" name="wd" class="s_ipt" value="ip" maxlength="255" autocomplete="off"></span><span class="bg s_btn_wr"><input type="submit" id="su" value="百度一下" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>输入法</span></div><ul id="mMenu"><li><a href="javascript:;" name="ime_hw">手写</a></li><li><a href="javascript:;" name="ime_py">拼音</a></li><li class="ln"></li><li><a href="javascript:;" name="ime_cl">关闭</a></li></ul></span></span><input type="hidden" name="oq" value="ip"><input type="hidden" name="rsv_pq" value="a0f6cd0c0000d262"><input type="hidden" name="rsv_t" value="5488BRsscwPJcYs0QpTSq9MErvB9ZjpKp6c2tqB5Wz1clwUn4IeDe/lpm+z5qSpsezwj"><input type="hidden" name="rqlang" value="cn"></form><div id="m"></div></div></div><div id="u"><a class="toindex" href="/">百度首页</a><a href="javascript:;" name="tj_settingicon" class="pf">设置<i class="c-icon c-icon-triangle-down"></i></a><a href="https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5" name="tj_login" class="lb" onclick="return false;">登录</a></div><div id="u1"><a href="http://news.baidu.com" name="tj_trnews" class="mnav">新闻</a><a href="https://www.hao123.com" name="tj_trhao123" class="mnav">hao123</a><a href="http://map.baidu.com" name="tj_trmap" class="mnav">地图</a><a href="http://v.baidu.com" name="tj_trvideo" class="mnav">视频</a><a href="http://tieba.baidu.com" name="tj_trtieba" class="mnav">贴吧</a><a href="http://xueshu.baidu.com" name="tj_trxueshu" class="mnav">学术</a><a href="https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5" name="tj_login" class="lb" onclick="return false;">登录</a><a href="http://www.baidu.com/gaoji/preferences.html" name="tj_settingicon" class="pf">设置</a><a href="http://www.baidu.com/more/" name="tj_briicon" class="bri" style="display: block;">更多产品</a></div></div></div>


<script>
/**
 * @description 图片base64加载
 * @author lizhouquan
 */


bds.base64 = (function () {
	//获取base64前置参数
	var _opt = bds._base64;

	//内部数据;
    var _containerAllId = "container",
        _containerLeftId = "content_left",
        _containerRightId = "content_right",
		_BOTTAGLSNAME = "BASE64_BOTTAG",
        _domain = bds._base64.domain,   //base64图片服务域名
        _imgWatch = [],             //图片加载观察list，如果没有onload，进行容错
        _domLoaded = [],            //标识对应dom是否已下载
        _data = [],                 //暂存请求回调数据
        _dataLoaded = [],        //数据是否返回
        _finish = [],            //是否已完成渲染
        _hasSpImg = false,          //是否有左侧模板sp_img走base64加载
        _expGroup = 0,              //左侧实验组
        _reqTime = 0,              //请求开始时间
        _reqEnd = 0,               //请求返回时间 - 右侧
        _reqEndL = 0,               //请求返回时间 - 左侧
        _rsst = 0,              	//请求开始时间 - 测速
        _rest = 0,               	//请求返回时间 - 测速
        _dt = 1,                   //domain类型
		_loadState = {},		   //记录imglist的状态
		_hasPreload = 0,		   //记录页面是否开启preload
        _ispdc = false;            //是否开启了性能统计

	//异步下发起下次搜索时重置变量
	var preXhrs = [],$ = window.$;
	if($) {
		$(window).on("swap_begin",function(){
			_imgWatch = [];             //图片加载观察list，如果没有onload，进行容错
			_domLoaded = [];            //标识对应dom是否已下载
			_data = [];                 //暂存请求回调数据
			_dataLoaded = [];        //数据是否返回
			_finish = [];            //是否已完成渲染
			_hasSpImg = false;          //是否有左侧模板sp_img走base64加载
			_expGroup = 0;              //左侧实验组
			_reqTime = 0;              //请求开始时间
			_reqEnd = 0;               //请求返回时间 - 右侧
			_reqEndL = 0;               //请求返回时间 - 左侧
			_rsst = 0;                  //请求开始时间 - 测速
			_rest = 0;                  //请求返回时间 - 测速
			_dt = 1;                   //domain类型
			_ispdc = false;            //是否开启了性能统计

			//停止正在执行的base64回调操作
			for(var i = 0 ; i < preXhrs.length; i++) {
				preXhrs[i].abort();
			}
		});
	}


    //初始化方法
    var init = function(imgRight,imgLeft,isPreload){
        var imgArr = imgRight || [], imgArr2 = imgLeft || [];
        if(window.__IS_IMG_PREFETCH){
            //异步base64去重
            function filter(img){
                return !window.__IS_IMG_PREFETCH.hasOwnProperty(img);
            }
            imgArr=$.grep(imgArr,filter);
            imgArr2=$.grep(imgArr2,filter);
        }
		if(window.__IMG_PRELOAD && isPreload) {
			//定义loadState，防止callback乱序
			_loadState["cbr"] = 0;
			_loadState["cbpr"] = 0;

			_hasPreload = 1; //标记页面中有预取

			var imgPreloadList = window.__IMG_PRELOAD = {};
			for(var i = 0; i < imgArr.length; i++) {
			   	if(!imgPreloadList.hasOwnProperty(imgArr[i])) {
					window.__IMG_PRELOAD[imgArr[i]] = true;
				}
			}
		} else if(window.__IMG_PRELOAD && !isPreload) {
			//同步base64右侧去重
			var tmpArr = [];
			for(var i = 0; i < imgArr.length; i++){
			   	if(!window.__IMG_PRELOAD.hasOwnProperty(imgArr[i])) {
					tmpArr.push(imgArr[i]);
				}
			}
			imgArr = tmpArr;
			//TODO
			//提取出函数
		}
		if(_opt.b64Exp) {
			_expGroup = _opt.b64Exp;
			if(_expGroup == 1){
				_domain = "http://b2.bdstatic.com/"; /*base64 new domain sample deploy*/
				_dt = 2;
			}
		}
        _ispdc= _opt.pdc>0 ? true : false;
		_reqTime = new Date()*1;
		if(_expGroup==2){
			//左右分别发请求
			if(imgArr2.length>0){
				_hasSpImg = true;
				loadJs(_domain + "image?imglist=" + imgArr2.join(",") + "&cb=bds.base64.cbl");
			}
			if(!isPreload) {
				cbl({});
			}
		}
		if(imgArr.length>0){
			//发送请求
			if(isPreload) {
				loadJs(_domain + "image?imglist=" + imgArr.join(",") + "&cb=bds.base64.cbpr");
			} else {
				loadJs(_domain + "image?imglist=" + imgArr.join(",") + "&cb=bds.base64.cbr");
			}
			if(_ispdc){
                if(bds.ready){
                    bds.ready(function(){
                        setTimeout(function(){
                            var _bottag = botTag.get();
                            var logstr = "dt=" + _dt + "&time=" + ((_reqEnd>0)?(_reqEnd-_reqTime):0) + "&bot=" + _bottag + "&rcount=" + imgArr.length;
                            window._B64_REQ_LOG = ((_reqEnd>0)?(_reqEnd-_reqTime):0) + "_" + imgArr.length;
                            if(_expGroup==2 && _reqEndL>0){
                                var _apics = document.getElementById("ala_img_pics");
                                var _lcount = (_apics&&_apics.children)?_apics.children.length:0;
                                logstr += "&time2=" + (_reqEndL-_reqTime) + "&lcount=" + _lcount;
                            }
                            if(Math.random()*100<10){
                                sendLog(logstr);
                            }
                        }, 2000);
                    });
                }
			}
		} else {
			if(!isPreload) {
				cbr({});
			}
		}
		if(imgArr.length>0 || imgArr2.length>0){
			if(!isPreload) {
				watchReq(imgArr.length);
			}
		}
    };

    //异步加载js
    function crc32 (str) {
        if(typeof str=="string"){
            var i,crc=0,j=0;
            for(i=0;i<str.length;i++){
                j=i%20+1;
                crc+=str.charCodeAt(i)<<j;
            }
            return Math.abs(crc);
        }
        return 0;
    }
    var loadJs = function (url) {
        var matchs = url.match(/.*(bds\.base64\.cb[rl])/);
        if(!matchs){
            return;
        }
        var imglist=url.match(/imglist=([^&]*)/);
        if(!imglist||!imglist[1]){
            return;
        }
        //see b64_base_popstate.js, this just sync result page
        callback_name=crc32(imglist[1].replace(/,/g,""));
        callback_name="cb_"+(callback_name+"").substr(Math.max(0,callback_name.length-8),8)+"_0";
        window[callback_name]=function(data){
            if(matchs[1] == "bds.base64.cbr") {
                cbr(data);
            }else if(matchs[1] == "bds.base64.cbl") {
                cbl(data);
            }
            window[callback_name]=null;
        };
        var url = matchs[0].replace(/bds\.base64\.cb[rl]/,callback_name);

        var a = document.createElement("script");
        a.setAttribute("type", "text/javascript");
        a.setAttribute("src", url);
        a.setAttribute("defer", "defer");
        a.setAttribute("async", "true");
        document.getElementsByTagName("head")[0].appendChild(a);
    };

    //图片回填
    var imgLoad = function(data,side){
        if(_finish[side]){
            return;
        }
        _finish[side] = true;
		if(side=="right"){
			botTag.ot(false); //设置超时标记减1.
		}
        //获取所有图片，通过data-base64-id属性获取需要回填的图片
        var imgs = document.getElementById(_expGroup!=1?((side=="left")?_containerLeftId:_containerRightId):_containerAllId).getElementsByTagName("IMG");
        for(var i=0;i<imgs.length;i++){
            var b64Id = imgs[i].getAttribute("data-b64-id");
            if(b64Id){
                var find = false;
				if(data.hasOwnProperty(b64Id)) {
                    setSrc(imgs[i],data[b64Id]);
					find = true;
				}
                if(!find){
                    //小容错
                    failover(imgs[i]);
                }
            }
        }
        fail_ie7();
    };
    function fail_ie7(){
        //外层容错 IE7
        setTimeout(function(){
            for( var i=0; i<_imgWatch.length; i++ ){
                var n = _imgWatch[i];
                if(!n.loaded){
                    failover(n.obj);
                }
            }
            _imgWatch=[];
        },200);
    }
    function setSrc(img,data){
        try{
            img.onerror = function(){
                failover(this);
            };

            //标记监视，供容错检查
            _imgWatch.push({
                obj:img,
                loaded:false
            });

            img.onload = function(){
                //标记已加载
                for( var i=0; i<_imgWatch.length; i++ ){
                    var m = _imgWatch[i];
                    if(m.obj == this){
                        m.loaded = true;
                    }
                }
            };
            img.src = "data:image\/jpeg;base64," + data;
        }catch(e){
            //触发exception
            failover(img);
        }
    }

    //容错，回填原始src
    var failover = function(img){
        if(img.getAttribute("data-b64-id")!=null && img.getAttribute("data-b64-id")!="" && img.getAttribute("data-src")!=null){
            img.src = img.getAttribute("data-src");
        }
    };

    var watchReq = function(len){
        var wt = 1250;
        if(len<6){
            wt = 1000;
        }else if(len>10){
            wt = 1500;
        }
        setTimeout(function(){
            if( !_dataLoaded["right"] ){
                var imgs = document.getElementById(_containerRightId).getElementsByTagName("IMG");
                for(var i=0;i<imgs.length;i++){
                    failover(imgs[i]);
                }
				_finish["right"] = true;
				//设置超时标记
				botTag.ot(true);
            }
			setTimeout(function(){
				if(_hasSpImg && !_dataLoaded["left"]){
                	var imgs = document.getElementById(_containerLeftId).getElementsByTagName("IMG");
                	for(var i=0;i<imgs.length;i++){
                    	failover(imgs[i]);
               		}
					_finish["left"] = true;
            	}
			},500);
        },wt);
    };

	/**
	 * base64网速检测标记
	 *   超时次数变量 BOT
	 *   初始：0
	 *   范围：0-6
	 *   变换规则：
	 *       每次超时，BOT +1;
	 * 		 每次正常：BOT -1;
	 *       到达边界值时，不再继续增加/减少
	 *	 如何使用：（未上线）
	 *   	 BOT大于3时，设置cookie: B64_BOT=1，VUI针对本次请求，读cookie，如果B64_BOT=1，关闭base64服务
	 *       当BOT小于3时，设置cookie: B64_BOT=0，VUI正常开启base64服务。
	 */
	var botTag = {
		ot : function(isInc){
			var _bottag = botTag.get();
			if(isInc){
				if(_bottag<6){
					_bottag++;
				}
			}else{
				if(_bottag>0){
					_bottag--;
				}
			}
			if( _bottag>=2 ){
				var date = new Date();
				date.setTime(date.getTime() + 24*3600*1000*5);
				//此处设置cookie
				document.cookie = "B64_BOT=1; expires=" + date.toGMTString();
				//_bottag = 0;
			}else if( _bottag<1 ){
			    if(document.cookie.match('B64_BOT=1')){
					document.cookie = "B64_BOT=0;";
				}
			}
			try{
				if(window.localStorage){
					window.localStorage[_BOTTAGLSNAME] = _bottag;
				}
			}catch(e){}
		},
		get : function(){
			try{
				if(window.localStorage){
					var _bottag = window.localStorage[_BOTTAGLSNAME];
						_bottag = _bottag?parseInt(_bottag):0;
				}else{
					return 0;
				}
				return _bottag;
			}catch(e){
				return 0;
			}
		}
	};

    //请求回调方法 - 右侧
    var cbr = function(data){
        _reqEnd = new Date()*1;
        if(_ispdc && bds.comm && _reqTime>0 && _reqEnd>0){
            bds.comm.cusval = "b64_" + _dt + "_" + ( _reqEnd - _reqTime );
        }
		_loadState["cbr"] = 1;
        callback(data, "right");
    };

    //请求回调方法 - 左侧
    var cbl = function(data){
		_reqEndL = new Date()*1;
        callback(data, "left");
    };

    //请求回调方法 - 预取
    var cbpr = function(data){
		_loadState["cbpr"] = 1;
        callback(data, "right");
    };

	var callback = function(data, side){
		_dataLoaded[side] = _hasPreload ? (_loadState.cbpr && _loadState.cbr) : true;

		if(data) {
			if(_data[side] === undefined) {_data[side] = {}};
			for(var key in data) {
				if(data.hasOwnProperty(key)) {
					_data[side][key] = data[key];
				}
			}
        }
        if(_domLoaded[side] && _dataLoaded[side]){
            imgLoad(_data[side], side);
        }
    };

    //设置Dom加载完成
    var setDomLoad = function(side){
        _domLoaded[side] = true;
        if(_dataLoaded[side]){
            imgLoad(_data[side],side);
        }
    };

	var predictImg = false; //右侧base64图片是否预取

	//发送日志
    var sendLog = function (src) {
        var loghost = "http://nsclick.baidu.com/v.gif?pid=315&rsv_yc_log=3&";

        var n = "b64log__" + (new Date()).getTime(),
            c = window[n] = new Image();
            c.onload = (c.onerror = function () {
                window[n] = null;
            });
        c.src = loghost + src + "&_t=" + new Date()*1; //LOG统计地址
        c = null; //释放变量c，避免产生内存泄漏的可能
    };


	//定义测速函数:
	//请求回调 - 测速
	cbs = function(data){
		_rest = new Date()*1;
		if( (_rest - _rsst) < 1500 ){
			botTag.ot(false);
		}else{
			botTag.ot(true);
		}
	};

	//测试速度
	ts = function(){
		_expGroup = 3;
		_rsst = new Date()*1;
		loadJs(_domain + "image?imglist=1241886729_3226161681_58,1072899117_2953388635_58,2469877062_2085031320_58,155831992_309216365_58,2539127170_1607411613_58,1160777122_283857721_58,1577144716_3149119526_58,2339041784_1038484334_58&cb=bds.base64.cbs");
	};

    return {
        init : init,
        cbl : cbl,
        cbr : cbr,
        cbpr : cbpr,
        setDomLoad : setDomLoad,
		cbs : cbs,
		ts : ts,
		predictImg : predictImg
    }
})();

</script>

<script>
/* 图片预取、base64预取代码 */

</script>

			

<!--cxy_all+monline_4_dg+9773813d24eb48cd90463dc6c2424316+000000000000000000000000000000000120459-->






















































	





















					        
		
										

				






		

	
        
			        
	
			        
	
			        
	
			        
			    

	
        
			        
	
			        
	
			        
	
			        
			    


























			

		
            
	            
                                                         <div class="s_tab" id="s_tab"><div class="s_tab_inner"><b>网页</b><a href="https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=ip" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a><a href="http://tieba.baidu.com/f?fr=wwwt&kw=ip" wdfield="kw"  onmousedown="return c({'fm':'tab','tab':'tieba'})" >贴吧</a><a href="http://zhidao.baidu.com/q?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word=ip" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'zhidao'})" >知道</a><a href="/sf/vsearch?pd=video&tn=vsearch&lid=a0f6cd0c0000d262&ie=utf-8&wd=ip&rsv_spt=7&rsv_bp=1&f=8&oq=ip&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"  onmousedown="return c({'fm':'tab','tab':'video'})" >视频</a><a href="http://music.taihe.com/search?fr=ps&ie=utf-8&key=ip" wdfield="key"  onmousedown="return c({'fm':'tab','tab':'music'})" >音乐</a><a href="http://image.baidu.com/i?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=ip" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'pic'})" >图片</a><a href="http://map.baidu.com/m?fr=ps01000&word=ip" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'map'})" >地图</a><a href="http://wenku.baidu.com/search?lm=0&od=0&ie=utf-8&word=ip" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'wenku'})" >文库</a><a href="http://www.baidu.com/more/"  onmousedown="return c({'fm':'tab','tab':'more'})" >更多»</a></div>
</div>


	            
    

	           	<div id="wrapper_wrapper">
				
	
			
	
		<!--[if IE 8]>
		<style>
		   .c-input input{padding-top:4px;}
		</style>
		<![endif]-->
		
			<style>
			    											 .op-ip-icon{line-height:0}.op-ip-detail table{width:100%;height:56px}.op-ip-detail td{vertical-align:middle;font-size:22px;line-height:22px;font-family:"微软雅黑" arial}.op-ip-tip{color:#aaa}.op-ip-no-tip{color:#000}.op-ip-query-e,.op-ip-query-res{display:none}.op-ip-query-e span{color:red}.op-ip-help-link a{color:#666}.op-bk-polysemy-bold{font-weight:700}.op-bk-polysemy-other span{display:block}.op-bk-polysemy-space{white-space:nowrap}.op-bk-polysemy-oneother .op-bk-polysemy-move,.op-bk-polysemy-oneother span{margin-left:0}.op-bk-polysemy-focus{height:22px;_height:24px;line-height:1.69em;margin-bottom:2px;overflow:hidden}.op-bk-polysemy-focustext{float:left;display:inline-block;height:22px;padding:0 8px 0 30px;background:url(//www.baidu.com/aladdin/img/bk_polysemy/bk_polyicon.png) 5px 0 no-repeat #3288ff;_background:url(//www.baidu.com/aladdin/img/bk_polysemy/bk_polyicon1.gif) 5px center no-repeat #3288ff;color:#fff}.op-bk-polysemy-focus a{display:inline-block;height:22px;line-height:1.69em;float:left;border-right:2px solid #fff;background:#f5f5f5;padding:0 8px;text-decoration:none;color:#333}.op-bk-polysemy-focus a.op-bk-polysemy_focusafirst{background:url(//www.baidu.com/aladdin/img/bk_polysemy/bk_polyicon.png) 0 -22px no-repeat #f5f5f5}.op-bk-polysemy-focusf{height:23px;_height:25px;line-height:1.69em;margin-bottom:2px;overflow:hidden}.op-bk-polysemy-focusleft{float:left;display:inline-block;height:21px;border:1px solid #38f}.op-bk-polysemy-focusrightf,.op-bk-polysemy-focustextf{border-top:1px solid #f0f0f0;border-bottom:1px solid #f0f0f0}.op-bk-polysemy-focustextf{float:left;display:inline-block;height:21px;padding-left:10px}.op-bk-polysemy-focustextf span{color:#38f}.op-bk-polysemy-focusrightf{float:left;display:inline-block;height:21px;border-right:1px solid #f0f0f0}.op-bk-polysemy-focusrightf span{display:inline-block;float:left;color:#ccc}.op-bk-polysemy-focusrightf a{display:inline-block;height:21px;line-height:1.54em;text-decoration:underline;border:none;background:#fff;float:left;padding:0 8px;color:#00c}.op-bk-polysemy-focusrightf a.op-bk-polysemy_focusrfirst{padding-left:4px;background:#fff;color:#00c}.op-bk-polysemy-album{position:relative;width:100%;display:block}.op-bk-polysemy-albumPr{position:relative}.op-bk-polysemy-albumMore{display:block;width:100%;height:18px;line-height:18px;background:#525252;background:rgba(82,82,82,.6);color:#fff;position:absolute;bottom:0;left:0;text-align:center;filter:alpha(opacity=60)}.op-bk-polysemy-albumBorder{width:99%;height:99%;position:absolute;border-right:1px solid #bfbfbf;border-bottom:1px solid #bfbfbf;right:-2px;bottom:-2px;overflow:hidden;z-index:59;_right:-3px}.op-bk-polysemy-albumBorderSec{right:-4px;bottom:-4px;_right:-5px}.op_jingyan_list{position:relative}.op_jingyan_list .op_jingyan_index{position:absolute;top:74px;left:0;width:20px;height:20px padding:1px 0;filter:progid:DXImageTransform.Microsoft.gradient(enabled='true', startColorstr='#99000000', endColorstr='#99000000');background-color:rgba(0,0,0,.6);font-size:12px;color:#ddd;text-align:center}:root .op_jingyan_list .op_jingyan_index{filter:none;background-color:rgba(0,0,0,.6)}.op_jingyan_list a{text-decoration:none;color:#333;font-size:12px}.op_jingyan_list img{height:92px}.op_jingyan_list_hide,.op_jingyan_list_showmore{border-top:1px solid #f3f3f3;text-align:center;padding-top:5px}.op_jingyan_list_hide span,.op_jingyan_list_showmore span{cursor:pointer}.op_jingyan_list2,.op_jingyan_list_hide,.op_jingyan_pager{display:none}.op_jingyan_pager{text-align:center;overflow:hidden;padding:4px 0}.op_jingyan_pager span{display:inline-block;_display:inline;border:1px solid #d5d5d5;overflow:hidden;padding:3px 7px;margin:0 1px;color:#00c;text-decoration:none;line-height:18px;font:400 12px Arial,Helvetica,sans-serif;text-align:center;vertical-align:middle}.op_jingyan_pager .op_jingyan_pager_current,.op_jingyan_pager .op_jingyan_pager_loading,.op_jingyan_pager .op_jingyan_pager_seperator{border:none;padding:4px 8px;color:#666}.op_jingyan_pager .op_jingyan_pager_current{color:#000}.op_jingyan_pager .op_jingyan_pager_item{cursor:pointer}.opr-recommends-merge-title{text-decoration:none}.opr-recommends-merge-title:hover{text-decoration:underline}.opr-recommends-merge-imgtext{display:block}.opr-recommends-merge-hide{display:none}.opr-recommends-merge-p{position:relative;_zoom:1}.opr-recommends-merge-d{min-height:20px;color:#999}.opr-recommends-merge-width-text{width:70px;text-align:center;margin:3px auto 0;font-size:12px;line-height:18px;word-break:break-all}.opr-recommends-merge-item{text-align:center}.opr-recommends-merge-mask{position:absolute;top:0;left:0;width:100%;_background:0 0;background:-webkit-radial-gradient(center,closest-side,rgba(255,255,255,0),rgba(0,0,0,.03));background:-moz-radial-gradient(center,closest-side,rgba(255,255,255,0),rgba(0,0,0,.03));background:-o-radial-gradient(center,closest-side,rgba(255,255,255,0),rgba(0,0,0,.03));background:-ms-radial-gradient(center,closest-side,rgba(255,255,255,0),rgba(0,0,0,.03))}.opr-recommends-merge-more-btn i{cursor:pointer}.opr-recommends-merge-layerbtn{position:absolute;right:0;bottom:0;width:1.23em;height:1.23em;background:url(//www.baidu.com/aladdin/img/right_recommends/layericon.png) no-repeat;_background-image:url(//www.baidu.com/aladdin/img/right_recommends/layericon.gif)}.opr-recommends-merge-layerbtn1,.opr-recommends-merge-layerbtn2{background-position:-48px 0}.opr-recommends-merge-layerbtn1,.opr-recommends-merge-layerbtn3{background-color:#999}.opr-recommends-merge-layerbtn1:hover,.opr-recommends-merge-layerbtn2,.opr-recommends-merge-layerbtn3:hover,.opr-recommends-merge-layerbtn4{background-color:#38f}.opr-recommends-merge-layerbtn3:hover,.opr-recommends-merge-layerbtn4:hover{background-position:-24px 0}.opr-recommends-merge-layer{padding:4px 9px;width:350px}.opr-recommends-merge-layer table{border-collapse:collapse;border-padding:0}.opr-recommends-merge-layer td{font-size:1em;line-height:1.67;vertical-align:top}.opr-recommends-merge-lastspan{display:none}.opr-recommends-merge-mbGap{margin-bottom:28px}.container_l .opr-recommends-merge-lastspan{display:block}.container_l .cr-content-narrow .opr-recommends-merge-lastspan{display:none}.opr-recommends-merge-dodge-wrap{margin-bottom:24px;font-size:1.1em}.opr-recommends-merge-user-layer{width:235px;position:absolute;border:1px solid #eee;border-radius:2px;margin-top:10px;margin-left:-60px;*margin-left:-140px;z-index:998;background:#fff;color:#333;font-size:13px;text-align:center;padding:14px 15px}.opr-recommends-merge-user-layer button{margin-top:12px;font-size:12px}.opr-recommends-merge-user-layer img{top:2px;position:relative}.opr-recommends-merge-user-secondBtn{margin-left:8px}.opr-recommends-merge-user-secondBtn i{-ms-transform:rotate(180deg);-moz-transform:rotate(180deg);-webkit-transform:rotate(180deg);-o-transform:rotate(180deg)}.opr-recommends-merge-user-layer-tips{position:absolute;margin-top:5px;margin-left:67px;*margin-left:-22px;border-left:6px solid transparent;border-right:6px solid transparent;border-bottom:6px solid #eee;width:0;height:0;z-index:999}.opr-recommends-merge-content{position:relative}.opr-recommends-merge-user-layer-tips-fff{margin-top:6px;border-bottom:6px solid #fff}.opr-recommends-merge-user-layer-hide{display:none}.opr-recommends-merge-user-layer-icon{position:relative;top:2px;width:14px;height:14px}.opr-recommends-merge-user-layer-con{position:absolute;width:312px;height:140px;top:0;padding-top:20px;z-index:999}.opr-toplist1-title{position:relative;margin-bottom:.5px}.opr-toplist1-table .opr-toplist1-right{text-align:right;white-space:nowrap}.opr-toplist1-from{text-align:right}.opr-toplist1-from a{text-decoration:none}.opr-toplist1-new{position:relative;top:1px}.opr-toplist1-st{margin-bottom:2px;margin-left:3px}.opr-toplist1-update{float:right}.opr-toplist1-refresh{font-size:13px;font-weight:400;text-decoration:none}.opr-toplist1-refresh .opr-toplist1-icon{background:url(//www.baidu.com/aladdin/tpl/right_toplist1/refresh.png) 0 0/100% 100% no-repeat;margin-left:3px;width:16px;height:16px}
								    			</style>
		

			

				
	 <script id="head_script">
        bds.comm.newagile = "1";
        bds.comm.jsversion = "006";
 		bds.comm.domain = "http://www.baidu.com";
        bds.comm.ubsurl = "https://sp0.baidu.com/5bU_dTmfKgQFm2e88IuM_a/union.gif";
        bds.comm.tn = "monline_4_dg";
        bds.comm.tng = "union";
        bds.comm.queryEnc = "ip";
        bds.comm.queryId = "a0f6cd0c0000d262";
        bds.comm.inter = "";
        bds.comm.resTemplateName = "baidulm";
        bds.comm.sugHost = "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su";
        bds.comm.ishome = 0;
        bds.comm.query = "ip";
        bds.comm.qid = "a0f6cd0c0000d262";
        bds.comm.eqid = "a0f6cd0c0000d262000000065bd608f5";	//eclipse项目使用
        bds.comm._se_click_track_flag = "";	//点击日志追查使用
        bds.comm.cid = "0";
        bds.comm.sid = "1459_21119";
        bds.comm.sampleval = [];// 通用抽样标记
        bds.comm.stoken = "";
        bds.comm.serverTime = "1540753653";
        bds.comm.user = "";
        bds.comm.username = "";
        bds.comm.userid = "0";
		bds.comm.__rdNum = "443";
        bds.comm.useFavo = "";
        bds.comm.pinyin = "ip";
        bds.comm.favoOn = "";
        bds.comm.speedInfo = "[{\"ModuleId\":9537,\"TimeCost\":118.75,\"TimeSelf\":11.9},{\"ModuleId\":9540,\"TimeCost\":-1,\"TimeSelf\":-1,\"Idc\":\"5\"},{\"ModuleId\":9527,\"TimeCost\":102.76,\"TimeSelf\":16.91,\"isHitCache\":true,\"SubProcess\":[{\"ProcessId\":9531,\"TimeCost\":0,\"isHitCache\":true},{\"ProcessId\":9536,\"TimeCost\":63.6,\"isHitCache\":false},{\"ProcessId\":9535,\"TimeCost\":21.95,\"isHitCache\":false},{\"ProcessId\":9532,\"TimeCost\":63.9}]}]";
        bds.comm.topHijack = null;
        bds.comm.isDebug = false;
		
        
        
        
        
                                                                                                                                                            
        bds.comm.iaurl=["http:\/\/www.ip138.com\/","http:\/\/www.ip.cn\/","https:\/\/www.ipip.net\/"];

		bds.comm.curResultNum = "10";
    	bds.comm.rightResultExist = false;
    	bds.comm.protectNum = 0;
    	bds.comm.zxlNum = 0;
        bds.comm.pageNum = parseInt('1')||1;

		
        bds.comm.pageSize = parseInt('10')||10;
	bds.comm.encTn = '72e1HP9OGsgapFPWCnwGplHi/uqoQuwj4/Bc8VTV2BruAzva0eHS9QbbM1299klti1uh';
		//base64实验变量
		
        //防止从结果页打开的页面中通过opener.xxx来影响百度页面

        bds.se.mon = {'loadedItems':[],'load':function(){},'srvt':-1};
        try {
            bds.se.mon.srvt = parseInt(document.cookie.match(new RegExp("(^| )BDSVRTM=([^;]*)(;|$)"))[2]);
            document.cookie="BDSVRTM=;expires=Sat, 01 Jan 2000 00:00:00 GMT";
        }catch(e){
            bds.se.mon.srvt=-1;
        }

        //兼容之前一些变量

        bdUser        = bds.comm.user?bds.comm.user:null;
        bdQuery       = bds.comm.query;
        bdUseFavo     = bds.comm.useFavo;
        bdFavoOn      = bds.comm.favoOn;
        bdCid         = bds.comm.cid;
        bdSid         = bds.comm.sid;
        bdServerTime  = bds.comm.serverTime;
        bdQid         = bds.comm.queryId;
        bdstoken      = bds.comm.stoken;
		_eclipse = "1";	//eclipse开关，暂时放这里
        login_success = [];

        bds.comm.seinfo = {'fm':'se','T':'1540753653','y':'7EFFBBA6','rsv_cache': (bds.se.mon.srvt>0)?0:1 };
        bds.comm.cgif = "https://sp0.baidu.com/9foIbT3kAMgDnd_/c.gif?t=0&q=ip&p=0&pn=1";

		bds.comm.upn = {"browser":"chrome","ie":"","os":"mac","win":"","browsertype":"chrome"};
        bds.comm.cookie = null;

        // url右侧推荐白名单标志 urlRecFlag=1:不请求推荐浮层数据，urlRecFlag=0:请求推荐浮层数据
                    bds.comm.urlRecFlag = "0";
                
                    bds.comm.bfe_sample=null;
        
        // 右侧广告定时变化开关
        // !!!!!!注意上线过程新首页静态文件与模版不一致问题!!!!!!看不懂请勿随意修改!!!!!!

        

		    </script>

		<script>
	(function(){
		var imgArr = [],imgArr2 = [];
		//构造数据 - 右侧
				imgArr = ["637761685_2996898776_58","945672136_2419824617_58","106350983_300155143_58","2165666746_3266153015_58","1662781649_2766431911_58","2152745441_2819612533_58","1706679956_732005834_58","3019280129_1050774952_58","2785716545_3176779281_58","898604244_4275218585_58","3216926485_2839654534_58","2369483862_1716647049_58"];
				//构造数据 - 左侧
				bds.base64.init(imgArr,imgArr2);
	})();
</script>

	
	            <div id="container" class="container_s">
	                <script>
	                    bds.util.setContainerWidth();
	                    bds.ready(function(){
	                        $(window).on("resize",function(){
	                            bds.util.setContainerWidth();
	                            bds.event.trigger("se.window_resize");
	                        });
	                        bds.util.setContainerWidth();
	                    });
	                </script>
			

			

	
	
	    <div id="content_right" class="cr-offset">
			
			


			
        <table cellpadding="0" cellspacing="0"><tr>
            <td align="left">
	        
	
	
            
	

            <div id="con-ar" >
                                            
	                                

        <div class="result-op xpath-log" tpl="right_recommends_merge" data-click='{"fm":"alxr","p1":1,"mu":"http:\/\/www.baidu.com\/s?wd=ip&srcid=21102","rsv_stl":0,"rsv_srcid":21102}'> 

    












































    
        		                	        
        
        
                                            
	
     
                        
    	    
    

    
    


<div class="cr-content ">
    

<style>
    .opr-recommends-merge-p,.opr-recommends-merge-img,.opr-recommends-merge-mask{height:75px;}
    .opr-recommends-merge-item-vertical .opr-recommends-merge-p,.opr-recommends-merge-item-vertical .opr-recommends-merge-img{height:100px;}
        </style>


<div class="opr-recommends-merge-content">
 
	<div class="cr-title c-clearfix">
            <a class="cr-title-sub opr-recommends-merge-more-btn" href="javascript:;" onclick="return false;" data-click="{'fm':'beha'}"><span>展开</span><i class="c-icon c-icon-chevron-bottom c-gap-left-small"></i></a>     
        <span title="相关术语">相关术语</span>
            </div>

<div class="opr-recommends-merge-panel">
        
<div class="c-row c-gap-top">
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'维珍宽带','rsv_re_uri':'4c665114cf7146da9802848dfdda3493'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E7%BB%B4%E7%8F%8D%E5%AE%BD%E5%B8%A6&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=4c665114cf7146da9802848dfdda3493"><img data-src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=637761685,2996898776&fm=58" data-b64-id="637761685_2996898776_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E7%BB%B4%E7%8F%8D%E5%AE%BD%E5%B8%A6&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=4c665114cf7146da9802848dfdda3493"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="维珍宽带" href="/s?wd=%E7%BB%B4%E7%8F%8D%E5%AE%BD%E5%B8%A6&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=4c665114cf7146da9802848dfdda3493">维珍宽带</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">世界上最快的宽带</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'测网速','rsv_re_uri':'d4348048548d4ff5ab5f38e821c51a54'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E6%B5%8B%E7%BD%91%E9%80%9F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=d4348048548d4ff5ab5f38e821c51a54"><img data-src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=945672136,2419824617&fm=58" data-b64-id="945672136_2419824617_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E6%B5%8B%E7%BD%91%E9%80%9F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=d4348048548d4ff5ab5f38e821c51a54"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="测网速" href="/s?wd=%E6%B5%8B%E7%BD%91%E9%80%9F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=d4348048548d4ff5ab5f38e821c51a54">测网速</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">测速网速测试服务</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  c-span-last-s opr-recommends-merge-item " data-click="{'rsv_re_ename':'外网ip','rsv_re_uri':'652c0179f6254383a72ddb72931ac041'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E5%A4%96%E7%BD%91ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=652c0179f6254383a72ddb72931ac041"><img data-src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=106350983,300155143&fm=58" data-b64-id="106350983_300155143_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E5%A4%96%E7%BD%91ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=652c0179f6254383a72ddb72931ac041"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="外网ip" href="/s?wd=%E5%A4%96%E7%BD%91ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=652c0179f6254383a72ddb72931ac041">外网ip</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">互联网分配的独占IP</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  c-span-last opr-recommends-merge-lastspan opr-recommends-merge-item " data-click="{'rsv_re_ename':'内网ip','rsv_re_uri':'664373dd910746189318d4bb53e9f71a'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E5%86%85%E7%BD%91ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=664373dd910746189318d4bb53e9f71a"><img data-src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=2165666746,3266153015&fm=58" data-b64-id="2165666746_3266153015_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E5%86%85%E7%BD%91ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=664373dd910746189318d4bb53e9f71a"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="内网ip" href="/s?wd=%E5%86%85%E7%BD%91ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=664373dd910746189318d4bb53e9f71a">内网ip</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">内网也就是局域网</p>
                    </div>
                            </div>   

    </div>
 

        
<div class="c-row c-gap-top">
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'手机号码定位','rsv_re_uri':'fa3ce951f3d34d1cb42122e80079fcbf'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%A0%81%E5%AE%9A%E4%BD%8D&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=fa3ce951f3d34d1cb42122e80079fcbf"><img data-src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1662781649,2766431911&fm=58" data-b64-id="1662781649_2766431911_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%A0%81%E5%AE%9A%E4%BD%8D&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=fa3ce951f3d34d1cb42122e80079fcbf"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="手机号码定位" href="/s?wd=%E6%89%8B%E6%9C%BA%E5%8F%B7%E7%A0%81%E5%AE%9A%E4%BD%8D&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=fa3ce951f3d34d1cb42122e80079fcbf">手机号码定位</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">基于GPS定位技术</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'子网掩码','rsv_re_uri':'e2fe81a768c5444295b08f0a4a7034d6'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E5%AD%90%E7%BD%91%E6%8E%A9%E7%A0%81&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=e2fe81a768c5444295b08f0a4a7034d6"><img data-src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=2152745441,2819612533&fm=58" data-b64-id="2152745441_2819612533_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E5%AD%90%E7%BD%91%E6%8E%A9%E7%A0%81&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=e2fe81a768c5444295b08f0a4a7034d6"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="子网掩码" href="/s?wd=%E5%AD%90%E7%BD%91%E6%8E%A9%E7%A0%81&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=e2fe81a768c5444295b08f0a4a7034d6">子网掩码</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">主机的位掩码</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  c-span-last-s opr-recommends-merge-item " data-click="{'rsv_re_ename':'ping','rsv_re_uri':'2990678b648140bb94b041f4812a5e3e'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=ping&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=2990678b648140bb94b041f4812a5e3e"><img data-src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1706679956,732005834&fm=58" data-b64-id="1706679956_732005834_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=ping&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=2990678b648140bb94b041f4812a5e3e"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="ping" href="/s?wd=ping&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=2990678b648140bb94b041f4812a5e3e">ping</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">网络诊断工具</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  c-span-last opr-recommends-merge-lastspan opr-recommends-merge-item " data-click="{'rsv_re_ename':'动态ip地址','rsv_re_uri':'c494b6c88a6e41a88d2e31a4abe3bcc4'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E5%8A%A8%E6%80%81ip%E5%9C%B0%E5%9D%80&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=c494b6c88a6e41a88d2e31a4abe3bcc4"><img data-src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3019280129,1050774952&fm=58" data-b64-id="3019280129_1050774952_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E5%8A%A8%E6%80%81ip%E5%9C%B0%E5%9D%80&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=c494b6c88a6e41a88d2e31a4abe3bcc4"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="动态ip地址" href="/s?wd=%E5%8A%A8%E6%80%81ip%E5%9C%B0%E5%9D%80&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=c494b6c88a6e41a88d2e31a4abe3bcc4">动态ip地址</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">每次上网分配到不同IP</p>
                    </div>
                            </div>   

    </div>
 

        
<div class="c-row c-gap-top">
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'虚拟专用网络','rsv_re_uri':'2345556c979043639efb0f98e79a3ea8'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E8%99%9A%E6%8B%9F%E4%B8%93%E7%94%A8%E7%BD%91%E7%BB%9C&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=2345556c979043639efb0f98e79a3ea8"><img data-src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=2785716545,3176779281&fm=58" data-b64-id="2785716545_3176779281_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E8%99%9A%E6%8B%9F%E4%B8%93%E7%94%A8%E7%BD%91%E7%BB%9C&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=2345556c979043639efb0f98e79a3ea8"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="虚拟专用网络" href="/s?wd=%E8%99%9A%E6%8B%9F%E4%B8%93%E7%94%A8%E7%BD%91%E7%BB%9C&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=2345556c979043639efb0f98e79a3ea8">虚拟专用网络</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">成本低、易于使用</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'router','rsv_re_uri':'c8ca587010eb4e36bf594b095ab246e9'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=router&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=c8ca587010eb4e36bf594b095ab246e9"><img data-src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=898604244,4275218585&fm=58" data-b64-id="898604244_4275218585_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=router&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=c8ca587010eb4e36bf594b095ab246e9"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="router" href="/s?wd=router&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=c8ca587010eb4e36bf594b095ab246e9">router</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">连接因特网的设备</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  c-span-last-s opr-recommends-merge-item " data-click="{'rsv_re_ename':'代理服务器','rsv_re_uri':'419e841d060b45678e3419d50612b888'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=419e841d060b45678e3419d50612b888"><img data-src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3216926485,2839654534&fm=58" data-b64-id="3216926485_2839654534_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=419e841d060b45678e3419d50612b888"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="代理服务器" href="/s?wd=%E4%BB%A3%E7%90%86%E6%9C%8D%E5%8A%A1%E5%99%A8&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=419e841d060b45678e3419d50612b888">代理服务器</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">重要的服务器安全功能</p>
                    </div>
                            </div>   

 

        
    
    <div class="c-span4  c-span-last opr-recommends-merge-lastspan opr-recommends-merge-item " data-click="{'rsv_re_ename':'nic','rsv_re_uri':'f508c26605084593a270fc6b41a46efc'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=nic&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=f508c26605084593a270fc6b41a46efc"><img data-src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2369483862,1716647049&fm=58" data-b64-id="2369483862_1716647049_58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=nic&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=f508c26605084593a270fc6b41a46efc"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="nic" href="/s?wd=nic&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=f508c26605084593a270fc6b41a46efc">nic</a></div>
                        <div class="opr-recommends-merge-d">
        	            	<p class="opr-recommends-merge-width-text">局域网中基本的部件</p>
                    </div>
                            </div>   

    </div>
 

<textarea class="opr-recommends-merge-hide opr-recommends-merge-more-textarea">
    <div class="opr-recommends-merge-morelists">
        
<div class="c-row c-gap-top">
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'wifi','rsv_re_uri':'cfce2e087e7e4ce7b64c8d55c93e4d0f'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=wifi&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=cfce2e087e7e4ce7b64c8d55c93e4d0f"><img  data-img="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3651691759,2239870902&fm=58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=wifi&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=cfce2e087e7e4ce7b64c8d55c93e4d0f"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="wifi" href="/s?wd=wifi&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=cfce2e087e7e4ce7b64c8d55c93e4d0f">wifi</a></div>
                                    </div>   

 

        
    
    <div class="c-span4  opr-recommends-merge-item " data-click="{'rsv_re_ename':'静态ip','rsv_re_uri':'52db1b07fb3845d2b052f11eb3f60e73'}">
                                                	<div class="opr-recommends-merge-p">
            <a target="_blank" href="/s?wd=%E9%9D%99%E6%80%81ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=52db1b07fb3845d2b052f11eb3f60e73"><img  data-img="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=335438567,1449351197&fm=58" class="c-img c-img4 opr-recommends-merge-img"/></a>
            <a class="opr-recommends-merge-mask" target="_blank" href="/s?wd=%E9%9D%99%E6%80%81ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=52db1b07fb3845d2b052f11eb3f60e73"></a>                    </div>
        <div class="c-gap-top-small"><a target="_blank" title="静态ip" href="/s?wd=%E9%9D%99%E6%80%81ip&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_recommends_merge_21102&amp;cq=ip&amp;srcid=28310&amp;rt=%E7%9B%B8%E5%85%B3%E6%9C%AF%E8%AF%AD&amp;recid=21102&amp;euri=52db1b07fb3845d2b052f11eb3f60e73">静态ip</a></div>
                                    </div>   

    </div>
 
</div>
</textarea>

</div>
</div>
<script>
    A.setup({platform:"pc",showType:""});
</script>


</div>
</div>
														
			                                            
	                                

        <div class="result-op xpath-log" tpl="right_toplist1" data-click='{"fm":"alxr","p1":2,"mu":"http:\/\/top.baidu.com\/buzz?b=1","rsv_stl":"0","rsv_srcid":20811}'> 

    












































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

    
    


<div class="cr-content ">
    

<div class="FYB_RD">
    <div class="cr-title opr-toplist1-title" title="搜索热点">
                            	<div class="opr-toplist1-update" data-click="{fm:'beha'}">
            <a class="OP_LOG_BTN opr-toplist1-refresh" href="javascript:void(0);">换一换<i class="c-gap-left-small c-icon opr-toplist1-icon"></i></a>
        </div>
                        搜索热点
    </div>
    <table class="c-table opr-toplist1-table">
                        <tbody >
                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-index-hot1 c-gap-icon-right-small">1</span><a target="_blank" title="警方进驻公交公司" href="/s?wd=%E8%AD%A6%E6%96%B9%E8%BF%9B%E9%A9%BB%E5%85%AC%E4%BA%A4%E5%85%AC%E5%8F%B8&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">警方进驻公交公司</a></span></td>
                <td class="opr-toplist1-right">45万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-index-hot2 c-gap-icon-right-small">2</span><a target="_blank" title="男子抢劫被反杀" href="/s?wd=%E7%94%B7%E5%AD%90%E6%8A%A2%E5%8A%AB%E8%A2%AB%E5%8F%8D%E6%9D%80&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">男子抢劫被反杀</a></span></td>
                <td class="opr-toplist1-right">44万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-index-hot3 c-gap-icon-right-small">3</span><a target="_blank" title="上港vs鲁能首发" href="/s?wd=%E4%B8%8A%E6%B8%AFvs%E9%B2%81%E8%83%BD%E9%A6%96%E5%8F%91&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">上港vs鲁能首发</a></span></td>
                <td class="opr-toplist1-right">43万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">4</span><a target="_blank" title="滞留塞班游客回国" href="/s?wd=%E6%BB%9E%E7%95%99%E5%A1%9E%E7%8F%AD%E6%B8%B8%E5%AE%A2%E5%9B%9E%E5%9B%BD&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">滞留塞班游客回国</a></span></td>
                <td class="opr-toplist1-right">43万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">5</span><a target="_blank" title="海星下潜6000米" href="/s?wd=%E6%B5%B7%E6%98%9F%E4%B8%8B%E6%BD%9C6000%E7%B1%B3&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">海星下潜6000米</a></span></td>
                <td class="opr-toplist1-right">43万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">6</span><a target="_blank" title="准备吊起坠江公交" href="/s?wd=%E5%87%86%E5%A4%87%E5%90%8A%E8%B5%B7%E5%9D%A0%E6%B1%9F%E5%85%AC%E4%BA%A4&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">准备吊起坠江公交</a></span></td>
                <td class="opr-toplist1-right">42万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">7</span><a target="_blank" title="公交坠江打捞遗体" href="/s?wd=%E5%85%AC%E4%BA%A4%E5%9D%A0%E6%B1%9F%E6%89%93%E6%8D%9E%E9%81%97%E4%BD%93&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">公交坠江打捞遗体</a></span></td>
                <td class="opr-toplist1-right">36万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">8</span><a target="_blank" title="杨幂祝福唐嫣" href="/s?wd=%E6%9D%A8%E5%B9%82%E7%A5%9D%E7%A6%8F%E5%94%90%E5%AB%A3&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">杨幂祝福唐嫣</a></span></td>
                <td class="opr-toplist1-right">36万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">9</span><a target="_blank" title="重庆大巴车坠江" href="/s?wd=%E9%87%8D%E5%BA%86%E5%A4%A7%E5%B7%B4%E8%BD%A6%E5%9D%A0%E6%B1%9F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">重庆大巴车坠江</a></span></td>
                <td class="opr-toplist1-right">36万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">10</span><a target="_blank" title="老太乞讨广播打假" href="/s?wd=%E8%80%81%E5%A4%AA%E4%B9%9E%E8%AE%A8%E5%B9%BF%E6%92%AD%E6%89%93%E5%81%87&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">老太乞讨广播打假</a></span></td>
                <td class="opr-toplist1-right">30万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                </tbody>
                                <tbody style="display:none">
                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">11</span><a target="_blank" title="巴萨VS皇马首发" href="/s?wd=%E5%B7%B4%E8%90%A8VS%E7%9A%87%E9%A9%AC%E9%A6%96%E5%8F%91&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">巴萨VS皇马首发</a></span></td>
                <td class="opr-toplist1-right">26万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">12</span><a target="_blank" title="保车黑老大落网" href="/s?wd=%E4%BF%9D%E8%BD%A6%E9%BB%91%E8%80%81%E5%A4%A7%E8%90%BD%E7%BD%91&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">保车黑老大落网</a></span></td>
                <td class="opr-toplist1-right">26万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">13</span><a target="_blank" title="厦航化险为夷" href="/s?wd=%E5%8E%A6%E8%88%AA%E5%8C%96%E9%99%A9%E4%B8%BA%E5%A4%B7&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">厦航化险为夷</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">14</span><a target="_blank" title="吴彦祖脱发" href="/s?wd=%E5%90%B4%E5%BD%A6%E7%A5%96%E8%84%B1%E5%8F%91&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">吴彦祖脱发</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">15</span><a target="_blank" title="南非学生持刀攻击" href="/s?wd=%E5%8D%97%E9%9D%9E%E5%AD%A6%E7%94%9F%E6%8C%81%E5%88%80%E6%94%BB%E5%87%BB&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">南非学生持刀攻击</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">16</span><a target="_blank" title="希金斯再次当总统" href="/s?wd=%E5%B8%8C%E9%87%91%E6%96%AF%E5%86%8D%E6%AC%A1%E5%BD%93%E6%80%BB%E7%BB%9F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">希金斯再次当总统</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">17</span><a target="_blank" title="泰达vs申花" href="/s?wd=%E6%B3%B0%E8%BE%BEvs%E7%94%B3%E8%8A%B1&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">泰达vs申花</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">18</span><a target="_blank" title="收保车费被判刑" href="/s?wd=%E6%94%B6%E4%BF%9D%E8%BD%A6%E8%B4%B9%E8%A2%AB%E5%88%A4%E5%88%91&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">收保车费被判刑</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">19</span><a target="_blank" title="驾考 无限电作弊" href="/s?wd=%E9%A9%BE%E8%80%83+%E6%97%A0%E9%99%90%E7%94%B5%E4%BD%9C%E5%BC%8A&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">驾考 无限电作弊</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">20</span><a target="_blank" title="埃及身亡器官不见" href="/s?wd=%E5%9F%83%E5%8F%8A%E8%BA%AB%E4%BA%A1%E5%99%A8%E5%AE%98%E4%B8%8D%E8%A7%81&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">埃及身亡器官不见</a></span></td>
                <td class="opr-toplist1-right">25万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                </tbody>
                                <tbody style="display:none">
                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">21</span><a target="_blank" title="爵士vs鹈鹕" href="/s?wd=%E7%88%B5%E5%A3%ABvs%E9%B9%88%E9%B9%95&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">爵士vs鹈鹕</a></span></td>
                <td class="opr-toplist1-right">24万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">22</span><a target="_blank" title="唐嫣罗晋官宣大婚" href="/s?wd=%E5%94%90%E5%AB%A3%E7%BD%97%E6%99%8B%E5%AE%98%E5%AE%A3%E5%A4%A7%E5%A9%9A&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">唐嫣罗晋官宣大婚</a></span></td>
                <td class="opr-toplist1-right">24万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">23</span><a target="_blank" title="马天宇否认整容" href="/s?wd=%E9%A9%AC%E5%A4%A9%E5%AE%87%E5%90%A6%E8%AE%A4%E6%95%B4%E5%AE%B9&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">马天宇否认整容</a></span></td>
                <td class="opr-toplist1-right">24万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">24</span><a target="_blank" title="DNA之父沃森车祸" href="/s?wd=DNA%E4%B9%8B%E7%88%B6%E6%B2%83%E6%A3%AE%E8%BD%A6%E7%A5%B8&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">DNA之父沃森车祸</a></span></td>
                <td class="opr-toplist1-right">24万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">25</span><a target="_blank" title="太阳4连败" href="/s?wd=%E5%A4%AA%E9%98%B34%E8%BF%9E%E8%B4%A5&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">太阳4连败</a></span></td>
                <td class="opr-toplist1-right">24万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">26</span><a target="_blank" title="46岁民警因公牺牲" href="/s?wd=46%E5%B2%81%E6%B0%91%E8%AD%A6%E5%9B%A0%E5%85%AC%E7%89%BA%E7%89%B2&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">46岁民警因公牺牲</a></span></td>
                <td class="opr-toplist1-right">24万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">27</span><a target="_blank" title="机构改革方案获批" href="/s?wd=%E6%9C%BA%E6%9E%84%E6%94%B9%E9%9D%A9%E6%96%B9%E6%A1%88%E8%8E%B7%E6%89%B9&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">机构改革方案获批</a></span></td>
                <td class="opr-toplist1-right">24万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">28</span><a target="_blank" title="德比无C罗梅西" href="/s?wd=%E5%BE%B7%E6%AF%94%E6%97%A0C%E7%BD%97%E6%A2%85%E8%A5%BF&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">德比无C罗梅西</a></span></td>
                <td class="opr-toplist1-right">23万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">29</span><a target="_blank" title="巴特尔当篮协主席" href="/s?wd=%E5%B7%B4%E7%89%B9%E5%B0%94%E5%BD%93%E7%AF%AE%E5%8D%8F%E4%B8%BB%E5%B8%AD&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">巴特尔当篮协主席</a></span></td>
                <td class="opr-toplist1-right">23万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">30</span><a target="_blank" title="刑警追捕嫌犯骨折" href="/s?wd=%E5%88%91%E8%AD%A6%E8%BF%BD%E6%8D%95%E5%AB%8C%E7%8A%AF%E9%AA%A8%E6%8A%98&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">刑警追捕嫌犯骨折</a></span></td>
                <td class="opr-toplist1-right">23万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                </tbody>
                                <tbody style="display:none">
                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">31</span><a target="_blank" title="詹姆斯遭肘击倒地" href="/s?wd=%E8%A9%B9%E5%A7%86%E6%96%AF%E9%81%AD%E8%82%98%E5%87%BB%E5%80%92%E5%9C%B0&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">詹姆斯遭肘击倒地</a></span></td>
                <td class="opr-toplist1-right">22万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">32</span><a target="_blank" title="英超老板飞机坠毁" href="/s?wd=%E8%8B%B1%E8%B6%85%E8%80%81%E6%9D%BF%E9%A3%9E%E6%9C%BA%E5%9D%A0%E6%AF%81&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">英超老板飞机坠毁</a></span></td>
                <td class="opr-toplist1-right">22万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">33</span><a target="_blank" title="叙利亚 四方峰会" href="/s?wd=%E5%8F%99%E5%88%A9%E4%BA%9A+%E5%9B%9B%E6%96%B9%E5%B3%B0%E4%BC%9A&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">叙利亚 四方峰会</a></span></td>
                <td class="opr-toplist1-right">22万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">34</span><a target="_blank" title="卢琳中华小姐夺冠" href="/s?wd=%E5%8D%A2%E7%90%B3%E4%B8%AD%E5%8D%8E%E5%B0%8F%E5%A7%90%E5%A4%BA%E5%86%A0&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">卢琳中华小姐夺冠</a></span></td>
                <td class="opr-toplist1-right">22万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">35</span><a target="_blank" title="撞老太太逃逸躲藏" href="/s?wd=%E6%92%9E%E8%80%81%E5%A4%AA%E5%A4%AA%E9%80%83%E9%80%B8%E8%BA%B2%E8%97%8F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">撞老太太逃逸躲藏</a></span></td>
                <td class="opr-toplist1-right">22万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">36</span><a target="_blank" title="扮鬼吓人罚睡墓地" href="/s?wd=%E6%89%AE%E9%AC%BC%E5%90%93%E4%BA%BA%E7%BD%9A%E7%9D%A1%E5%A2%93%E5%9C%B0&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">扮鬼吓人罚睡墓地</a></span></td>
                <td class="opr-toplist1-right">22万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">37</span><a target="_blank" title="曼联VS埃弗顿首发" href="/s?wd=%E6%9B%BC%E8%81%94VS%E5%9F%83%E5%BC%97%E9%A1%BF%E9%A6%96%E5%8F%91&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">曼联VS埃弗顿首发</a></span></td>
                <td class="opr-toplist1-right">21万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">38</span><a target="_blank" title="网贷集资嫌犯落网" href="/s?wd=%E7%BD%91%E8%B4%B7%E9%9B%86%E8%B5%84%E5%AB%8C%E7%8A%AF%E8%90%BD%E7%BD%91&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">网贷集资嫌犯落网</a></span></td>
                <td class="opr-toplist1-right">21万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">39</span><a target="_blank" title="水杯爆裂宜家判赔" href="/s?wd=%E6%B0%B4%E6%9D%AF%E7%88%86%E8%A3%82%E5%AE%9C%E5%AE%B6%E5%88%A4%E8%B5%94&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">水杯爆裂宜家判赔</a></span></td>
                <td class="opr-toplist1-right">21万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">40</span><a target="_blank" title="俄德法土四国峰会" href="/s?wd=%E4%BF%84%E5%BE%B7%E6%B3%95%E5%9C%9F%E5%9B%9B%E5%9B%BD%E5%B3%B0%E4%BC%9A&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">俄德法土四国峰会</a></span></td>
                <td class="opr-toplist1-right">21万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                </tbody>
                                <tbody style="display:none">
                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">41</span><a target="_blank" title="首位女院士陈化兰" href="/s?wd=%E9%A6%96%E4%BD%8D%E5%A5%B3%E9%99%A2%E5%A3%AB%E9%99%88%E5%8C%96%E5%85%B0&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">首位女院士陈化兰</a></span></td>
                <td class="opr-toplist1-right">21万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">42</span><a target="_blank" title="莫文蔚 祈福" href="/s?wd=%E8%8E%AB%E6%96%87%E8%94%9A+%E7%A5%88%E7%A6%8F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">莫文蔚 祈福</a></span></td>
                <td class="opr-toplist1-right">20万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">43</span><a target="_blank" title="幼儿园嫌犯被捕" href="/s?wd=%E5%B9%BC%E5%84%BF%E5%9B%AD%E5%AB%8C%E7%8A%AF%E8%A2%AB%E6%8D%95&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">幼儿园嫌犯被捕</a></span></td>
                <td class="opr-toplist1-right">19万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">44</span><a target="_blank" title="香山索道停止运营" href="/s?wd=%E9%A6%99%E5%B1%B1%E7%B4%A2%E9%81%93%E5%81%9C%E6%AD%A2%E8%BF%90%E8%90%A5&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">香山索道停止运营</a></span></td>
                <td class="opr-toplist1-right">18万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">45</span><a target="_blank" title="山西辟谣猪肉吃死" href="/s?wd=%E5%B1%B1%E8%A5%BF%E8%BE%9F%E8%B0%A3%E7%8C%AA%E8%82%89%E5%90%83%E6%AD%BB&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">山西辟谣猪肉吃死</a></span></td>
                <td class="opr-toplist1-right">18万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">46</span><a target="_blank" title="山东绝杀浙江" href="/s?wd=%E5%B1%B1%E4%B8%9C%E7%BB%9D%E6%9D%80%E6%B5%99%E6%B1%9F&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">山东绝杀浙江</a></span></td>
                <td class="opr-toplist1-right">18万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">47</span><a target="_blank" title="美国匹兹堡枪击" href="/s?wd=%E7%BE%8E%E5%9B%BD%E5%8C%B9%E5%85%B9%E5%A0%A1%E6%9E%AA%E5%87%BB&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">美国匹兹堡枪击</a></span></td>
                <td class="opr-toplist1-right">17万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">48</span><a target="_blank" title="非法集资夫妻回国" href="/s?wd=%E9%9D%9E%E6%B3%95%E9%9B%86%E8%B5%84%E5%A4%AB%E5%A6%BB%E5%9B%9E%E5%9B%BD&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">非法集资夫妻回国</a></span></td>
                <td class="opr-toplist1-right">13万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">49</span><a target="_blank" title="特斯拉数据遭调查" href="/s?wd=%E7%89%B9%E6%96%AF%E6%8B%89%E6%95%B0%E6%8D%AE%E9%81%AD%E8%B0%83%E6%9F%A5&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">特斯拉数据遭调查</a></span></td>
                <td class="opr-toplist1-right">13万<i class="opr-toplist1-st c-icon c-icon-up"></i></td>
            </tr>
                                    <tr>
                                                                                                                                                                        
                                                    <td><span><span class="c-index  c-gap-icon-right-small">50</span><a target="_blank" title="卡舒吉未婚妻拒美" href="/s?wd=%E5%8D%A1%E8%88%92%E5%90%89%E6%9C%AA%E5%A9%9A%E5%A6%BB%E6%8B%92%E7%BE%8E&tn=monline_4_dg&usm=1&ie=utf-8&rsv_cq=ip&rsv_dl=0_right_fyb_pchot_20811_01">卡舒吉未婚妻拒美</a></span></td>
                <td class="opr-toplist1-right">11万<i class="opr-toplist1-st c-icon "></i></td>
            </tr>
                </tbody>
                            </table>
        <div class="OP_LOG_BTN c-gap-top-small opr-toplist1-from">
        </span><a target="_blank" href="http://www.baidu.com/link?url=S3JUv9GsRaTi11cdFGDmldy7W5FnNEeTObhvbTXZS6qkFPUFWPHk07q0VTtFd-vr">查看更多>></a>    </div>
    </div>
<script data-compress="off">
    //为阿拉丁单条结果实例创建数据
    //此标签用来准备注释，不需要添加 data-merge
 A.setup({
        num:'5'
    });
</script>


</div>
</div>
														
			    	
    
</div>

            
            


            
            
	
	

            
            
<div>
</div>


            
        </td></tr></table>
    </div>
		

			<script>
	if(bds.base64){
		bds.base64.setDomLoad("right");
	}
</script>
	
	

				
				






<div class="head_nums_cont_outer OP_LOG" ><div class="head_nums_cont_inner" style="top:-42px"><div class="search_tool_conter"><span class="c-gap-left-samll search_tool_close"><i class="c-icon searchTool-up c-icon-chevron-top-gray-s"></i>收起工具</span><span class="search_tool_la">所有网页<i class="c-icon c-icon-triangle-down"></i></span><span class="search_tool_tf c-gap-left">时间不限<i class="c-icon c-icon-triangle-down"></i></span><span class="search_tool_ft c-gap-left">所有网页和文件<i class="c-icon c-icon-triangle-down"></i></span><span class="search_tool_si c-gap-left">站点内检索<i class="c-icon c-icon-triangle-down"></i></span></div><div class="nums"><div class="search_tool" ><i class="c-icon searchTool-spanner c-icon-setting"></i>搜索工具</div><span class="nums_text">百度为您找到相关结果约24,700,000个</span></div></div></div>
<script type="text/javascript">
	bds.comm.search_tool = {};
	bds.comm.search_tool.sl_lang = "cn";
	bds.comm.search_tool.st = "";
	bds.comm.search_tool.et = "";
	bds.comm.search_tool.stftype = "";
	bds.comm.search_tool.ft = "";
	bds.comm.search_tool.si = "";
	bds.comm.search_tool.exact = "";
	bds.comm.search_tool.oneDay = "1540667253";
	bds.comm.search_tool.oneWeek = "1540148853";
	bds.comm.search_tool.oneMonth = "1538161653";
	bds.comm.search_tool.oneYear = "1509217653";
	bds.comm.search_tool.thisDay = "1540656000";
	bds.comm.search_tool.thisWeek = "1540137600";
	bds.comm.search_tool.thisMonth = "1538150400";
	bds.comm.search_tool.thisYear = "1509206400";
	bds.comm.search_tool.actualResultLang = "cn";
</script>










<div id="content_left">
	

	
		
			
	
	

	
	
				
				
			
	

	
	
											
						
	            			
						

			
		
		

								

		
					        
		                             

    















































    
    
    

<div class="result-op c-container"  srcid="6006"  fk="119.130.202.144" id="1" tpl="ip" mu="http://www.ip138.com/" data-op="{'y':'DCA3EF7B'}" data-click="{'p1':'1','rsv_bdr':'0','fm':'alop',rsv_stl:'0'}">
            
        <h3 class="t c-gap-bottom-small">
        <a href="http://www.baidu.com/link?url=Tb03QziE06fJDRedRVl8N7-7nsp82kgvjzrD0sLojFW" target="_blank"><em>IP</em>地址查询</a>
        </h3>
        
        <div class="c-border">
<script type="text/javascript" data-compress="off">
    window.opuiLikeShareContent6006 = '#百度搜索#刚才在百度搜“ip”  我的ip地址119.130.202.144  属于广东省广州市 电信。查ip归属地，很方便，你也来试试？';
</script>
<div class="c-row">
	    <div class="c-span3 op-ip-icon"><img class="c-img c-img3" src="//www.baidu.com/aladdin/img/tools/ip.png">
    </div>
        <div class="c-span21 c-span-last op-ip-detail">
    <table><tr><td>
    		<span class="c-gap-right">本机IP:&nbsp;119.130.202.144</span>广东省广州市 电信	    
    </td></tr></table>
    </div>
</div>
<div class="c-row c-gap-top">
    <div class="c-span10">
        <input class="c-input c-input-large op-ip-input" type="text" value="" maxlength="15" placeholder="请输入ip地址" tip="请输入ip地址" autocomplete="off">
    </div>
    <div class="c-span14 c-span-last">
        <a class="c-btn c-btn-primary op-ip-do-submit OP_LOG_BTN"  href="#" onclick="return false;"  hideFocus="true">查询</a>
    </div>
</div>
<div class="c-gap-top-small op-ip-query-e">
    <span>请输入有效的ip地址</span>
</div>
<div class="c-gap-top-small op-ip-query-res">
    <span class="op-ip-query-res-txt"></span>
</div>
<div class="c-gap-top op-ip-help-link">
    <a class="c-gap-right" href="http://www.baidu.com/link?url=g_coratEwvpA3VB_15MOyisTIcpY7CciQwr9qdQAArYqtT5MOAwJEqCKh1thaugfvWeRAL5QoA0VW0dbCI_c0YV4yj0ko-6eP-zEx8Unmvm" target="_blank">本机IP查看方法</a>
    <a href="http://www.baidu.com/link?url=g_coratEwvpA3VB_15MOyisTIcpY7CciQwr9qdQAArYqtT5MOAwJEqCKh1thaugfs91CzvQjT7Hz6vGiKWG8EfUQQusVWnDw8kd9FhCABcy" target="_blank">IP地址设置方法</a>
</div>

</div>                
        
        <div class="c-gap-top-small"><span class="c-showurl">www.ip138.com/ </span><span class="c-tools" id="tools_9991465190363775754_1" data-tools="{title:'IP地址查询',url:'http://www.ip138.com/'}"><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></span> - <a target="_blank" href="http://open.baidu.com/" class="op_LAMP"></a></div> 
        
    
</div>

    
	    	

								
		
						
			
		

								

		
						
							
							
																																																																																																																				<div class="result c-container " id="2" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' }"  ><h3 class="t"><a 
	        data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DD6B',
			'F3':'54E5243F',
			'T':'1540753653',
						'y':'49F2DBFF'
			 
									}"
        href = "http://www.baidu.com/link?url=mQiWVlwTEvHOlnvjZInnEF_PxoCyxbcwENv0PJHf18S"

		            target="_blank"
        		
		><em>IP</em>.cn - <em>IP</em> 地址查询 | 地理位置 | 手机归属地</a></h3><div class="c-abstract">专业本机 <em>IP</em> 地址查询、手机 <em>IP</em> 地址、地理位置查询、<em>IP</em> 数据库、手机号归属地查询、电话号码黄页查询,可查广告、骚扰、快递、银行、保险、房地产、中介电话。</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=mQiWVlwTEvHOlnvjZInnEF_PxoCyxbcwENv0PJHf18S" class="c-showurl" style="text-decoration:none;">www.<b>ip</b>.cn/&nbsp;</a><div class="c-tools" id="tools_16142889619366112436_2" data-tools='{"title":"IP.cn - IP 地址查询 | 地理位置 | 手机归属地","url":"http://www.baidu.com/link?url=mQiWVlwTEvHOlnvjZInnEF_PxoCyxbcwENv0PJHf18S"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed4fece763105392230e54f7387ec0d0622e888e5cd6391b17483da1&p=8b2a975fc8d509ff57ee957e4c439f&newp=8249cf1c86cc42ae58bbc7710f54c9231610db2151d7d7106b82c825d7331b001c3bbfb423261303d9c37b6307a84d57e1f53376310923a3dda5c91d9fb4c57479de&user=baidu&fm=sc&query=ip&qid=a0f6cd0c0000d262&p1=2" 
                        target="_blank" 
                    class="m">百度快照</a><span class="c-pingjia">&nbsp;-&nbsp;<a href="https://www.baidu.com/tools?url=http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DmQiWVlwTEvHOlnvjZInnEF_PxoCyxbcwENv0PJHf18S&jump=https%3A%2F%2Fkoubei.baidu.com%2Fp%2Fsentry%3Ftitle%3D%02IP%03.%01cn%01%20%01-%01%20%02IP%03%20%01%E5%9C%B0%E5%9D%80%01%E6%9F%A5%E8%AF%A2%01%20%01%7C%01%20%01%E5%9C%B0%E7%90%86%01%E4%BD%8D%E7%BD%AE%01%20%01%7C%01%20%01%E6%89%8B%E6%9C%BA%01%E5%BD%92%E5%B1%9E%01%E5%9C%B0%01%26q%3Dip%26from%3Dps_pc4&key=surl" target="_blank" class="m" data-click="{'rsv_comments':'1'}" data-from="ps_pc4">47条评价</a></span></div></div>
											
		
						
			
		

								

		
						
							
							
																																																																																																																				 

    











































 
 
 


         
                                                        						        	                                                                                    

    	          
	

    
    


<div class="result-op c-container xpath-log"  srcid="1547"  id="3" tpl="bk_polysemy" mu="https://baike.baidu.com/item/IP/224599" data-op="{'y':'3FBBFAFF'}" data-click="{'p1':'3','rsv_bdr':'0','fm':'albk',rsv_stl:''}">
            
        <h3 class="t c-gap-bottom-small">
        <a href="http://www.baidu.com/link?url=E-1wuMey5SECWBZLQ71O9exkO0vLoWEjQ1M_0aXXUt28e328jk3TLlxyHnFgUIZfro1e8L8RvglaYoWFumt3C_" target="_blank"><em>IP</em>_百度百科</a>
        </h3>
        
        
    <div class="c-row">
                        <div class="c-span6">
            <a href="http://www.baidu.com/link?url=E-1wuMey5SECWBZLQ71O9exkO0vLoWEjQ1M_0aXXUt28e328jk3TLlxyHnFgUIZfro1e8L8RvglaYoWFumt3C_" target="_blank" class="op-bk-polysemy-album op-se-listen-recommend" style="_height:121px">
                <img class="c-img c-img6" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=301415937,375913658&fm=58&bpow=1024&bpoh=860"  />
                            </a>
        </div>
        <div class="c-span18 c-span-last">
                                                                                                        <p>
                    网络之间互连的协议（<em>IP</em>）是Internet Protocol的外语缩写，中文缩写为“网协”.网络之间互连的协议也就是为计算机网络相互连接进行通信而设计的协议。在因特网中，它是能使连接到网上的所有计算机网络实现相互通信的一套规则，规定了计算机...   
                </p>
                                           
                <p>
                                                                                                                            <a class="c-gap-right-small op-se-listen-recommend" href="http://www.baidu.com/link?url=Trmf4LrI94-PkzSqhcT1FpFPpyArnEbidyW5apetFKgPwoCrJtnWtxLR5cluEVwaf7xLQw0EcpRv6njRqZ5K7K" target="_blank" title="基本原理">基本原理</a>
                                                                                                        <a class="c-gap-right-small op-se-listen-recommend" href="http://www.baidu.com/link?url=Trmf4LrI94-PkzSqhcT1FpFPpyArnEbidyW5apetFKgPwoCrJtnWtxLR5cluEVwaIBOKkr5s1nmySVW-JU3Yja" target="_blank" title="分片和重组">分片和重组</a>
                                                                                                        <a class="c-gap-right-small op-se-listen-recommend" href="http://www.baidu.com/link?url=Trmf4LrI94-PkzSqhcT1FpFPpyArnEbidyW5apetFKgPwoCrJtnWtxLR5cluEVwakuh727mo_5nuxBVHwxo8qq" target="_blank" title="地址">地址</a>
                                                                                                        <a class="c-gap-right-small op-se-listen-recommend" href="http://www.baidu.com/link?url=Trmf4LrI94-PkzSqhcT1FpFPpyArnEbidyW5apetFKgPwoCrJtnWtxLR5cluEVwaJNCz3mn2J051AuTxkvl1va" target="_blank" title="IP协议"><em>IP</em>协议</a>
                                                                                                        <a class="c-gap-right-small op-se-listen-recommend" href="http://www.baidu.com/link?url=Trmf4LrI94-PkzSqhcT1FpFPpyArnEbidyW5apetFKgPwoCrJtnWtxLR5cluEVwaUW_QTu68J_ybDHMaw-6J5a" target="_blank" title="分类">分类</a>
                                                                                                        <a class="c-gap-right-small op-se-listen-recommend" href="http://www.baidu.com/link?url=Trmf4LrI94-PkzSqhcT1FpFPpyArnEbidyW5apetFKgPwoCrJtnWtxLR5cluEVwaMdqzyLaMij2T37omJfUY6_" target="_blank" title="V6简介">V6简介</a>
                                                                                                        <a href="http://www.baidu.com/link?url=E-1wuMey5SECWBZLQ71O9exkO0vLoWEjQ1M_0aXXUt28e328jk3TLlxyHnFgUIZfro1e8L8RvglaYoWFumt3C_" target="_blank" class="op-se-listen-recommend">更多&gt;&gt;</a>
                                        </p>
                                                            <p class=" op-bk-polysemy-move"><span class="c-showurl">baike.baidu.com/ </span><span class="c-tools" id="tools_12309499150314453016_3" data-tools="{title:'IP_百度百科',url:'http://baike.baidu.com/item/IP/224599?fr=aladdin'}"><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></span></p> 
        </div>
            
    </div>
       
                
        

    
</div>

											
		
						
			
		

								

		
						
							
							
																																																																																																																				 

    












































    	    	    	    	    	

    
    


<div class="result-op c-container xpath-log"  srcid="1537"  id="4" tpl="jingyan_summary" mu="https://jingyan.baidu.com/article/63f2362816d56c0208ab3dd5.html" data-op="{'y':'EE69FE88'}" data-click="{'p1':'4','rsv_bdr':'0','fm':'alop',rsv_stl:'0'}">
            
        <h3 class="t c-gap-bottom-small">
        <a href="http://www.baidu.com/link?url=g_coratEwvpA3VB_15MOyisTIcpY7CciQwr9qdQAArYqtT5MOAwJEqCKh1thaugflqvB5W3yjiXMfLzLNbyOwyuPcHHPzVegMRdgLuB2gQW" target="_blank">怎么查看自己电脑的<em>IP</em>地址？_百度经验</a>
        </h3>
        
        <div class="c-border">

<div class="c-row c-gap-bottom op_jingyan_list1">
                <div class="c-span6 op_jingyan_list">
                <a href="http://www.baidu.com/link?url=QwyPrJ9e4LPgAZPAhMauJdUAC9OUEpvL-3WBWUvbPVyx1La7x4yTqEbS_YYzZvu6QI1TrrDq2w4GueTIghLao1s6COfYejPRVphwFkYzfq_v9pRqLibVOiHOWBU3dJ_m" target="_blank"><img class="c-img c-img6" src="https://ss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=3933917974,2118814643&fm=58" />
                    <p class="c-gap-top-small">使用Windows+R键打开“运行”窗口，然...</p>                </a>
                <span class="op_jingyan_index">1</span>
            </div>
                <div class="c-span6 op_jingyan_list">
                <a href="http://www.baidu.com/link?url=QwyPrJ9e4LPgAZPAhMauJdUAC9OUEpvL-3WBWUvbPVyx1La7x4yTqEbS_YYzZvu6QI1TrrDq2w4GueTIghLao1s6COfYejPRVphwFkYzfq16MQhRYiav9SE-w6aDzuPy" target="_blank"><img class="c-img c-img6" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=4278919389,2696330599&fm=58" />
                    <p class="c-gap-top-small">进入命令窗口之后，输入：ipconfig/all...</p>                </a>
                <span class="op_jingyan_index">2</span>
            </div>
                <div class="c-span6 op_jingyan_list">
                <a href="http://www.baidu.com/link?url=QwyPrJ9e4LPgAZPAhMauJdUAC9OUEpvL-3WBWUvbPVyx1La7x4yTqEbS_YYzZvu6QI1TrrDq2w4GueTIghLao1s6COfYejPRVphwFkYzfq_WhWr6SsQcBBKXPXOQMrJP" target="_blank"><img class="c-img c-img6" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1209172316,2863924349&fm=58" />
                    <p class="c-gap-top-small">进入“网络和共享中心”（在控制面板可...</p>                </a>
                <span class="op_jingyan_index">3</span>
            </div>
                <div class="c-span6 c-span-last op_jingyan_list">
                <a href="http://www.baidu.com/link?url=QwyPrJ9e4LPgAZPAhMauJdUAC9OUEpvL-3WBWUvbPVyx1La7x4yTqEbS_YYzZvu6QI1TrrDq2w4GueTIghLao1s6COfYejPRVphwFkYzfq1_Kl_YCmHFcWBm-RwWBilo" target="_blank"><img class="c-img c-img6" src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=316696914,3301026224&fm=58" />
                    <p class="c-gap-top-small">完成第一步后，就进入了“网络连接状态...</p>                </a>
                <span class="op_jingyan_index">4</span>
            </div>
    </div>
<div class="c-row  op_jingyan_list2">
                <div class="c-span6 c-span-last op_jingyan_list">
                <a href="http://www.baidu.com/link?url=QwyPrJ9e4LPgAZPAhMauJdUAC9OUEpvL-3WBWUvbPVyx1La7x4yTqEbS_YYzZvu6QI1TrrDq2w4GueTIghLao1s6COfYejPRVphwFkYzfq0p9RiFswJ0LqPBfy_crFGN" target="_blank"><img class="c-img c-img6" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=210874460,3180177426&fm=58" />
                    <p class="c-gap-top-small">在详细列表里我们就可以看到网络的详细...</p>                </a>
                <span class="op_jingyan_index">5</span>
            </div>
    </div>
<p class="c-gap-top-small op_jingyan_list_showmore"><span class="OP_LOG_BTN">显示全部 <i class="c-icon c-icon-chevron-bottom"></i></span></p>
<p class="c-gap-top-small op_jingyan_list_hide"><span class="OP_LOG_BTN">收起 <i class="c-icon c-icon-chevron-top "></i></span></p>

<script data-compress="off">
    A.setup({
        'detailFlag':'true',
        'images': [{"@text":"","imglinkurl":"http:\/\/jingyan.baidu.com\/album\/63f2362816d56c0208ab3dd5.html?picindex=2","imgtext":"\u4f7f\u7528Windows+R\u952e\u6253\u5f00\u201c\u8fd0\u884c\u201d\u7a97\u53e3\uff0c\u7136...","imgurl":"https:\/\/ss1.baidu.com\/6ONXsjip0QIZ8tyhnq\/it\/u=3933917974,2118814643&fm=58"},{"@text":"","imglinkurl":"http:\/\/jingyan.baidu.com\/album\/63f2362816d56c0208ab3dd5.html?picindex=3","imgtext":"\u8fdb\u5165\u547d\u4ee4\u7a97\u53e3\u4e4b\u540e\uff0c\u8f93\u5165\uff1aipconfig\/all...","imgurl":"https:\/\/ss0.baidu.com\/6ONWsjip0QIZ8tyhnq\/it\/u=4278919389,2696330599&fm=58"},{"@text":"","imglinkurl":"http:\/\/jingyan.baidu.com\/album\/63f2362816d56c0208ab3dd5.html?picindex=4","imgtext":"\u8fdb\u5165\u201c\u7f51\u7edc\u548c\u5171\u4eab\u4e2d\u5fc3\u201d\uff08\u5728\u63a7\u5236\u9762\u677f\u53ef...","imgurl":"https:\/\/ss2.baidu.com\/6ONYsjip0QIZ8tyhnq\/it\/u=1209172316,2863924349&fm=58"},{"@text":"","imglinkurl":"http:\/\/jingyan.baidu.com\/album\/63f2362816d56c0208ab3dd5.html?picindex=5","imgtext":"\u5b8c\u6210\u7b2c\u4e00\u6b65\u540e\uff0c\u5c31\u8fdb\u5165\u4e86\u201c\u7f51\u7edc\u8fde\u63a5\u72b6\u6001...","imgurl":"https:\/\/ss0.baidu.com\/6ONWsjip0QIZ8tyhnq\/it\/u=316696914,3301026224&fm=58"},{"@text":"","imglinkurl":"http:\/\/jingyan.baidu.com\/album\/63f2362816d56c0208ab3dd5.html?picindex=6","imgtext":"\u5728\u8be6\u7ec6\u5217\u8868\u91cc\u6211\u4eec\u5c31\u53ef\u4ee5\u770b\u5230\u7f51\u7edc\u7684\u8be6\u7ec6...","imgurl":"https:\/\/ss2.baidu.com\/6ONYsjip0QIZ8tyhnq\/it\/u=210874460,3180177426&fm=58"}]
    });
</script>
<script>A.setup(function(){var _this=this,pageSize=8,$pager=_this.find(".op_jingyan_pager"),$showmore=_this.find(".op_jingyan_list_showmore"),$hiedmore=_this.find(".op_jingyan_list_hide"),$list1=_this.find(".op_jingyan_list1"),$list2=_this.find(".op_jingyan_list2"),currentPage=1,count=_this.data.images.length,pageCount=Math.ceil(count/pageSize);$showmore.find("span").click(function(){$list2.show(),$hiedmore.show(),$pager.show(),$showmore.hide()}),$hiedmore.find("span").click(function(){$list2.hide(),$hiedmore.hide(),$pager.hide(),$showmore.show(),currentPage=1,renderRow(1),renderPager()});var renderPager=function(){var count=pageCount;if(!(count<1)){var html=[],shown={},draw=function(index){if(shown[index])return"";if(shown[index]=true,index==currentPage)return'<span class="op_jingyan_pager_current">'+currentPage+"</span>";else return'<span class="op_jingyan_pager_item" data-page="'+index+'">'+index+"</span>"};if(currentPage>1)html.push('<span class="op_jingyan-prev op_jingyan_pager_item" data-page="'+(currentPage-1)+'">上一页</span>');var point=currentPage;if(count-2<point)point=count-2;if(point<5)if(count<5)point=count;else point=5;if(point>5)html.push(draw(1)),html.push('<span class="op_jingyan_pager_seperator">...</span>'),html.push(draw(point-2)),html.push(draw(point-1));else for(var i=1;i<point;i++)html.push(draw(i));if(html.push(draw(point)),point=currentPage,point<3)point=3;if(count-point<4)if(point=count-2,point<1)point=1;if(count-point>4)html.push(draw(point+1)),html.push(draw(point+2)),html.push('<span class="op_jingyan_pager_seperator">...</span>'),html.push(draw(count));else for(var i=point;i<=count;i++)html.push(draw(i));if(currentPage<count)html.push('<span class="op_jingyan-next op_jingyan_pager_item" data-page="'+(currentPage+1)+'">下一页</span>');$pager.html(html.join(""));var items=$pager.find(".op_jingyan_pager_item");items.each(function(){var index=parseInt($(this).attr("data-page"),10);$(this).click(function(){renderRow(index);var oldPage=currentPage;currentPage=index,$pager.html('<span class="op_jingyan_pager_loading">加载中...</span>'),renderPager()
})})}},renderRow=function(index){index-=1;for(var imgData=_this.data.images.slice(index*pageSize,index*pageSize+pageSize),list1Html=[],list2Html=[],i=0;i<pageSize/2;i++)if(imgData[i])list1Html.push(renderCell(imgData[i],index*pageSize+i));for(var i=pageSize/2;i<=pageSize;i++)if(imgData[i])list2Html.push(renderCell(imgData[i],index*pageSize+i));$list1.html(list1Html.join("")),$list2.html(list2Html.join(""))},renderCell=function(data,index){var cellHtml=[];if(3===index%(pageSize/2))cellHtml.push('<div class="c-span6 c-span-last op_jingyan_list">');else cellHtml.push('<div class="c-span6 op_jingyan_list">');if(data.imglinkurl)cellHtml.push('<a href="'+data.imglinkurl+'" target="_blank">');if(data.imgurl)cellHtml.push('<img class="c-img c-img6" src="'+data.imgurl+'" />');if(data.imgtext&&"true"==_this.data.detailFlag)cellHtml.push('<p class="c-gap-top-small">'+data.imgtext+"</p>");if(data.imglinkurl)cellHtml.push("</a>");return cellHtml.push('<span class="op_jingyan_index">'+(parseInt(index,10)+1)+"</span>"),cellHtml.push("</div>"),cellHtml.join("")};renderPager()});</script>
</div>                
        
        <div class="c-gap-top-small"><span class="c-showurl">jingyan.baidu.com </span><span class="c-tools" id="tools_10201300503380117840_4" data-tools="{title:'怎么查看自己电脑的IP地址？_百度经验',url:'http://jingyan.baidu.com/article/63f2362816d56c0208ab3dd5.html'}"><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></span></div> 
        
    
</div>

											
		
						
			
		

								

		
						
							
							
																																																																																																																				<div class="result c-container " id="5" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' }"  ><h3 class="t"><a 
	        data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DE6B',
			'F3':'54E5243F',
			'T':'1540753653',
						'y':'7BF397BD'
			 
									}"
        href = "http://www.baidu.com/link?url=_tTXh6-tm5N_q4P2gn6-TkjFTRx96dWULJzezREwTXy"

		            target="_blank"
        		
		>IPIP.NET_最专业的 <em>IP</em> 地址库_IPIP.NET</a></h3><div class="c-abstract"><em>IP</em>数据定位 使用<em>IP</em> 地址来确定用户的地理位置信息,国内区县 <em>IP</em> 库与国内 <em>IP</em> 高精度定位可以更好的满足客户自身用户画像的需求。 综合定位服务 为有精细地理位置需求...</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=_tTXh6-tm5N_q4P2gn6-TkjFTRx96dWULJzezREwTXy" class="c-showurl" style="text-decoration:none;">https://www.ipip.net/&nbsp;</a><div class="c-tools" id="tools_5007911797486747897_5" data-tools='{"title":"IPIP.NET_最专业的 IP 地址库_IPIP.NET","url":"http://www.baidu.com/link?url=_tTXh6-tm5N_q4P2gn6-TkjFTRx96dWULJzezREwTXy"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed19fa950d100b92235c43801467958b5768d4e414c4224655023ba3ed287952&p=8567c64ad48815b106bd9b7d0c1089&newp=c97ada5380934eac59ebcc2d02149e231610db2151d6d11e6b82c825d7331b001c3bbfb423261303d9c37b6307a84d57e1f53376310923a3dda5c91d9fb4c57479d0&user=baidu&fm=sc&query=ip&qid=a0f6cd0c0000d262&p1=5" 
                        target="_blank" 
                    class="m">百度快照</a></div></div>
											
		
						
			
		

								

		
						
							
							
																																																																																																																				<div class="result c-container " id="6" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' }"  ><h3 class="t"><a 
	        data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DEEA',
			'F3':'54E5243F',
			'T':'1540753653',
						'y':'4FFA5C74'
			 
									}"
        href = "http://www.baidu.com/link?url=CEb7G6xIzvGrDNcWDp7nBIWHfiYNRS398w50BWqcjRO"

		            target="_blank"
        		
		><em>ip</em>地址查询</a></h3><div class="c-row c-gap-top-small"><div class="general_image_pic c-span6"><a class="c-img6" style="height:75px"
          href="http://www.baidu.com/link?url=CEb7G6xIzvGrDNcWDp7nBIWHfiYNRS398w50BWqcjRO"
                target="_blank"
      ><img class="c-img c-img6" src="https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3127111184,1789145426&fm=58&s=4DA63D72D6DACA310373A0CF020010A3&bpow=121&bpoh=75"  style="height:75px;" /></a></div><div class="c-span18 c-span-last"><div class="c-abstract">英文 您的计算机或网络可能正在发送自动访问请求,要继续访问,请输入以下字母:...</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=CEb7G6xIzvGrDNcWDp7nBIWHfiYNRS398w50BWqcjRO" class="c-showurl" style="text-decoration:none;"><b>ip</b>.chinaz.com/&nbsp;</a><div class="c-tools" id="tools_7227007445166602704_6" data-tools='{"title":"ip地址查询","url":"http://www.baidu.com/link?url=CEb7G6xIzvGrDNcWDp7nBIWHfiYNRS398w50BWqcjRO"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9d78d513d99803bb1fadca71575091240e55f37e218c92027fa3c212c8380809506694ea7a7d0d&p=8e3f890a85cc43ff57ee957f565198&newp=882a9644d78703e905be9b7c5f568c231610db2151d6d0106b82c825d7331b001c3bbfb423261303d9c37b6307a84d57e1f53376310923a3dda5c91d9fb4c57479cc65722d&user=baidu&fm=sc&query=ip&qid=a0f6cd0c0000d262&p1=6" 
                        target="_blank" 
                    class="m">百度快照</a><span class="c-pingjia">&nbsp;-&nbsp;<a href="https://www.baidu.com/tools?url=http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCEb7G6xIzvGrDNcWDp7nBIWHfiYNRS398w50BWqcjRO&jump=https%3A%2F%2Fkoubei.baidu.com%2Fp%2Fsentry%3Ftitle%3D%02ip%03%E5%9C%B0%E5%9D%80%01%E6%9F%A5%E8%AF%A2%01%26q%3Dip%26from%3Dps_pc4&key=surl" target="_blank" class="m" data-click="{'rsv_comments':'1'}" data-from="ps_pc4">1713条评价</a></span></div></div></div></div>
											
		
						
			
		

								

		
						
							
							
																																																																																																																				<div class="result c-container " id="7" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' ,'rsv_cd':'pt:'}"  ><h3 class="t"><a 
	        data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DD6B',
			'F3':'54E5243F',
			'T':'1540753653',
						'y':'6DE7FF81'
			 
									}"
        href = "http://www.baidu.com/link?url=5lUYbisFse-YbRpcFzGSPzROTaLxtvy5ZHrXRTi8q0aYPZBDZQg4dh1J30U1nGtr"

		            target="_blank"
        		
		><em>IP</em>-COM 官方网站</a></h3><div class="c-abstract">全球领先的行业网络通信设备供应商和无线解决方案提供商,主要从事无线、网关和交换机等商用级网络设备的研发、生产与销售;致力于为行业用户提供领先的无线工程解决方案</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=5lUYbisFse-YbRpcFzGSPzROTaLxtvy5ZHrXRTi8q0aYPZBDZQg4dh1J30U1nGtr" class="c-showurl" style="text-decoration:none;">https://www.<b>ip</b>-com.com.cn/&nbsp;</a><div class="c-tools" id="tools_4997057614182943844_7" data-tools='{"title":"IP-COM 官方网站","url":"http://www.baidu.com/link?url=5lUYbisFse-YbRpcFzGSPzROTaLxtvy5ZHrXRTi8q0aYPZBDZQg4dh1J30U1nGtr"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9d78d513d99803bb1fadca71575091245843811021ca95503ac3933fc8264c413137bee4302267558e9a6b6776fe1541&p=8e3f890a85cc43ff57ee947a565198&newp=882a9645d28703e905be9b7c5f568c231610db2151d4d0116b82c825d7331b001c3bbfb423261303d9c37b6307a84d57e1f53376310923a3dda5c91d9fb4c57479cc65722d&user=baidu&fm=sc&query=ip&qid=a0f6cd0c0000d262&p1=7" 
                        target="_blank" 
                    class="m">百度快照</a><span class="c-pingjia">&nbsp;-&nbsp;<a href="https://www.baidu.com/tools?url=http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D5lUYbisFse-YbRpcFzGSPzROTaLxtvy5ZHrXRTi8q0aYPZBDZQg4dh1J30U1nGtr&jump=https%3A%2F%2Fkoubei.baidu.com%2Fp%2Fsentry%3Ftitle%3D%02IP%03-%01COM%01%20%01%E5%AE%98%E6%96%B9%01%E7%BD%91%E7%AB%99%01%26q%3Dip%26from%3Dps_pc1&key=surl" target="_blank" class="m" data-click="{'rsv_comments':'1'}" data-from="ps_pc1">评价</a></span></div></div>
											
		
						
			
		

								

		
						
							
							
																																																																																																																				<div class="result c-container " id="8" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' }"  ><h3 class="t"><a 
	        data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DD6B',
			'F3':'54E5343F',
			'T':'1540753653',
						'y':'FAEFCF7B'
			 
									}"
        href = "http://www.baidu.com/link?url=EQMv6Ual6lxab_NE875bUOZre5v6KR5xPY8xtUnzQ1ZNgL_7L9tIEiSVE3RBJYLGD5Sk4Dmjrg7nOt9CBbPPcqnaCnKNovrnSWX9rPNjWGi"

		            target="_blank"
        		
		><em>IP</em>地址_百度百科</a></h3><div class="c-abstract"><span class=" newTimeFactor_before_abs m">2018年10月16日&nbsp;-&nbsp;</span><em>IP</em>地址是指互联网协议地址(英语:Internet Protocol Address,又译为网际协议地址),是<em>IP</em> Address的缩写。<em>IP</em>地址...</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=EQMv6Ual6lxab_NE875bUOZre5v6KR5xPY8xtUnzQ1ZNgL_7L9tIEiSVE3RBJYLGD5Sk4Dmjrg7nOt9CBbPPcqnaCnKNovrnSWX9rPNjWGi" class="c-showurl" style="text-decoration:none;">https://baike.baidu.com/item/<b>I</b>...&nbsp;</a><div class="c-tools" id="tools_10591858088171242399_8" data-tools='{"title":"IP地址_百度百科","url":"http://www.baidu.com/link?url=EQMv6Ual6lxab_NE875bUOZre5v6KR5xPY8xtUnzQ1ZNgL_7L9tIEiSVE3RBJYLGD5Sk4Dmjrg7nOt9CBbPPcqnaCnKNovrnSWX9rPNjWGi"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed19fa950d100b8735420dd7743ca080462482d45f93130a1c187bb8fd707d0d7fb1d20b6016a4384b9af2210530142bc18cc28a57debc9022288333712d5cd04e4991&p=9a6cd3108cd512a05abd9b790c4f&newp=c366c00e86cc46ae09be9b7c554c92695c16ed643dc3864e1290c408d23f061d4866e0be23281605d6c0797347c2080ba8ff612e6152&user=baidu&fm=sc&query=ip&qid=a0f6cd0c0000d262&p1=8" 
                        target="_blank" 
                    class="m">百度快照</a></div></div>
											
		
						
			
		

								

		
						
							
							
																																																																																																																				<div class="result c-container " id="9" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' }"  ><h3 class="t c-title-en"><a 
	        data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DD6B',
			'F3':'54E5243F',
			'T':'1540753653',
						'y':'CFC7F8FF'
			 
									}"
        href = "http://www.baidu.com/link?url=_B0lHRIamFo-7yOTZ34PfbsvWGOiwn2mGhsBxFLsRoudwNauSBYpVH-j-jkqPVwS"

		            target="_blank"
        		
		>What Is My <em>IP</em>? Shows your real <em>IP</em> - IPv4 - IPv6 - WhatIsMyIP...</a></h3><div class="c-abstract c-abstract-en">IPv4 Address, IPv6 Address, <em>IP</em> Address Lookup, Change <em>IP</em>, Hide <em>IP</em>, <em>IP</em> WHOIS, Internet Speed Test, Trace An Email, Host Name Lookup, User Agent, ...</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=_B0lHRIamFo-7yOTZ34PfbsvWGOiwn2mGhsBxFLsRoudwNauSBYpVH-j-jkqPVwS" class="c-showurl" style="text-decoration:none;">https://www.whatismyip.com/&nbsp;</a><div class="c-tools" id="tools_1816378838550645041_9" data-tools='{"title":"What Is My IP? Shows your real IP - IPv4 - IPv6 - WhatIsMyIP....","url":"http://www.baidu.com/link?url=_B0lHRIamFo-7yOTZ34PfbsvWGOiwn2mGhsBxFLsRoudwNauSBYpVH-j-jkqPVwS"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed19fa950d100b92235c438014798d83532495cc03c8264c413037bee43a3655599393733c43&p=9a6cd3108cd512a05abd9b7d0d158e&newp=c366c00e86cc42af5bbcc7710f4e8d231610db2151d6d301298ffe0cc4241a1a1a3aecbf2321170ed5c2786106ab4257eff532743d0034f1f689df08d2ecce7e7e&user=baidu&fm=sc&query=ip&qid=a0f6cd0c0000d262&p1=9" 
                        target="_blank" 
                    class="m">百度快照</a>&nbsp;-&nbsp;<a href="http://www.baidu.com/link?url=E-1wuMey5SECWBZLQ71O9gkQn6calhbXyjaWvmjbdTBwP_yVcfLGyg7vqXNZ71Y96N58akDlXZzEPjbuH7SmnPDrCekhEZqbmbCVRdyTgcZPYKK12C077lwNOzGHriD5svSoUSjJS1TEUP0ybYNe_EsPrSrZtkPLjySUmEeH5dvcJ_PoL82gtBr_9_pANX11" target="_blank" class="m">翻译此页</a></div></div>
											
		
						
			
		

								

		
						
							
							
																																																																																																																				<div class="result c-container " id="10" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' }"  ><h3 class="t c-title-en"><a 
	        data-click="{
			'F':'778317EA',
			'F1':'9D73F1E4',
			'F2':'4CA6DD6B',
			'F3':'54E5243F',
			'T':'1540753653',
						'y':'DFCB9EE7'
			 
									}"
        href = "http://www.baidu.com/link?url=7fRP9Q60kw5A9M3ST_IoVSgcD6pND39cN8wr4XepE07fBTzgQ-LCCc6mr9qHFFG0"

		            target="_blank"
        		
		>What Is My <em>IP</em> Address - Online Privacy and Safety Experts</a></h3><div class="c-abstract c-abstract-en">Find out what your <em>IP</em> address is revealing about you! My <em>IP</em> address information shows your city, region, country, ISP and location on a map. Many ...</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=7fRP9Q60kw5A9M3ST_IoVSgcD6pND39cN8wr4XepE07fBTzgQ-LCCc6mr9qHFFG0" class="c-showurl" style="text-decoration:none;">www.whatismyipaddress....&nbsp;</a><div class="c-tools" id="tools_11759697984420420541_10" data-tools='{"title":"What Is My IP Address - Online Privacy and Safety Experts","url":"http://www.baidu.com/link?url=7fRP9Q60kw5A9M3ST_IoVSgcD6pND39cN8wr4XepE07fBTzgQ-LCCc6mr9qHFFG0"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9d78d513d99803bb1fadca71575091240e55f37e2192955068d4e40dc9371d1a0639a8e06571465293923d2616af3e0db7af2b&p=90759a46d6c810ec0be2963f1e0586&newp=8b2a971d8adf5bb708e2977e065ecb231610db2151d6d31e6b82c825d7331b001c3bbfb423261303d9c37b6307a84d57e1f53376310923a3dda5c91d9fb4c57479d07b286a04&user=baidu&fm=sc&query=ip&qid=a0f6cd0c0000d262&p1=10" 
                        target="_blank" 
                    class="m">百度快照</a>&nbsp;-&nbsp;<a href="http://www.baidu.com/link?url=S3JUv9GsRaTi11cdFGDmlivadAaSRb6esLnlj3xNh_fUlWQZem4ajN1EP_aC2DlIhkE1TPwzYyh1ifRFv4QpWs95Pq3u_EmVAJJxaQ6YNZcqo740kaRuAf5hMBLFeM14H_4dG2Qhy-ESBVIJMagGmj6lvIbFibdZ8GLwaLmhl8bCtnY2_cniyA_0w9U4en6K" target="_blank" class="m">翻译此页</a></div></div>
											
		
						
			
	
	
				
	
	
	
	

	
	

</div>

	
        <div style="clear:both;height:0;"></div>
	    
        
    <div id="rs"><div class="tt">相关搜索</div><table cellpadding="0"><tr><th><a href="/s?wd=%E6%89%8B%E6%9C%BAip%E5%9C%B0%E5%9D%80%E6%80%8E%E4%B9%88%E4%BF%AE%E6%94%B9&rsf=1&rsp=0&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">手机ip地址怎么修改</a></th><td></td><th><a href="/s?wd=ip%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D&rsf=1&rsp=1&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">ip什么意思</a></th><td></td><th><a href="/s?wd=%E6%89%8B%E6%9C%BAip%E5%9C%B0%E5%9D%80%E6%98%AF%E5%9B%BA%E5%AE%9A%E7%9A%84%E5%90%97&rsf=1&rsp=2&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">手机ip地址是固定的吗</a></th></tr><tr><th><a href="/s?wd=ip%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D&rsf=1&rsp=3&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">ip是什么意思</a></th><td></td><th><a href="/s?wd=%E5%A4%A7ip%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D&rsf=1&rsp=4&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">大ip是什么意思</a></th><td></td><th><a href="/s?wd=%E5%85%AC%E7%BD%91ip%E5%92%8C%E7%A7%81%E7%BD%91ip%E7%9A%84%E5%8C%BA%E5%88%AB&rsf=1&rsp=5&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">公网ip和私网ip的区别</a></th></tr><tr><th><a href="/s?wd=%E6%89%8B%E6%9C%BAip%E5%9C%B0%E5%9D%80&rsf=1&rsp=6&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">手机ip地址</a></th><td></td><th><a href="/s?wd=ip%E5%9C%B0%E5%9D%80&rsf=1&rsp=7&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">ip地址</a></th><td></td><th><a href="/s?wd=%E6%88%91%E7%9A%84ip%E5%9C%B0%E5%9D%80&rsf=1&rsp=8&f=1&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rqlang=cn&rs_src=0&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh">我的ip地址</a></th></tr></table></div>

<div id="page" >


	    <strong><span class="fk fk_cur"><i class="c-icon c-icon-bear-p"></i></span><span class="pc">1</span></strong><a href="/s?wd=ip&pn=10&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">2</span></a><a href="/s?wd=ip&pn=20&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">3</span></a><a href="/s?wd=ip&pn=30&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">4</span></a><a href="/s?wd=ip&pn=40&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">5</span></a><a href="/s?wd=ip&pn=50&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">6</span></a><a href="/s?wd=ip&pn=60&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">7</span></a><a href="/s?wd=ip&pn=70&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">8</span></a><a href="/s?wd=ip&pn=80&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">9</span></a><a href="/s?wd=ip&pn=90&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh"><span class="fk fkd"><i class="c-icon c-icon-bear-pn"></i></span><span class="pc">10</span></a><a href="/s?wd=ip&pn=10&oq=ip&tn=monline_4_dg&ie=utf-8&usm=1&rsv_pq=a0f6cd0c0000d262&rsv_t=72e1HP9OGsgapFPWCnwGplHi%2FuqoQuwj4%2FBc8VTV2BruAzva0eHS9QbbM1299klti1uh&rsv_page=1" class="n">下一页&gt;</a>


</div>
<div id="content_bottom">



</div>
    


			
			
			</div>
			
			
			
			
	
<script>
try{document.cookie="WWW_ST=;expires=Sat, 01 Jan 2000 00:00:00 GMT";}catch(e){}
</script>


	<div id="foot"><div class="foot-inner"><span id="help" style="float:left;padding-left:121px"><a href="http://help.baidu.com/question" target="_blank" onmousedown="return c({'fm':'behb','tab':'help','url':this.href,'title':this.innerHTML})">帮助</a><a href="http://www.baidu.com/search/jubao.html" target="_blank" onmousedown="return c({'fm':'behb','tab':'jubao','url':this.href,'title':this.innerHTML})">举报</a><a class="feedback" onclick="return false;" href="javascript:;" target="_blank" onmousedown="return ns_c({'fm':'behb','tab':'feedback'})">用户反馈</a></span></div></div>
			
      
  
		
		    
	<div class="c-tips-container" id="c-tips-container"></div>
	
			</div>
		
		</div>
					
		

		

	</body>
	
	

	<script type="text/javascript" src="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/jquery/jquery-1.10.2.min_65682a2.js"></script>
	
		
		<script type="text/javascript">var Cookie={set:function(e,t,o,i,s,n){document.cookie=e+"="+(n?t:escape(t))+(s?"; expires="+s.toGMTString():"")+(i?"; path="+i:"; path=/")+(o?"; domain="+o:"")},get:function(e,t){var o=document.cookie.match(new RegExp("(^| )"+e+"=([^;]*)(;|$)"));return null!=o?unescape(o[2]):t},clear:function(e,t,o){this.get(e)&&(document.cookie=e+"="+(t?"; path="+t:"; path=/")+(o?"; domain="+o:"")+";expires=Fri, 02-Jan-1970 00:00:00 GMT")}};!function(){function save(e){var t=[];for(tmpName in options)options.hasOwnProperty(tmpName)&&"duRobotState"!==tmpName&&t.push('"'+tmpName+'":"'+options[tmpName]+'"');
var o="{"+t.join(",")+"}";bds.comm.personalData?$.ajax({url:"//www.baidu.com/ups/submit/addtips/?product=ps&tips="+encodeURIComponent(o)+"&_r="+(new Date).getTime(),success:function(){writeCookie(),"function"==typeof e&&e()}}):(writeCookie(),"function"==typeof e&&setTimeout(e,0))}function set(e,t){options[e]=t}function get(e){return options[e]}function writeCookie(){if(options.hasOwnProperty("sugSet")){var e="0"==options.sugSet?"0":"3";clearCookie("sug"),Cookie.set("sug",e,document.domain,"/",expire30y)
}if(options.hasOwnProperty("sugStoreSet")){var e=0==options.sugStoreSet?"0":"1";clearCookie("sugstore"),Cookie.set("sugstore",e,document.domain,"/",expire30y)}if(options.hasOwnProperty("isSwitch")){var t={0:"2",1:"0",2:"1"},e=t[options.isSwitch];clearCookie("ORIGIN"),Cookie.set("ORIGIN",e,document.domain,"/",expire30y)}if(options.hasOwnProperty("imeSwitch")){var e=options.imeSwitch;clearCookie("bdime"),Cookie.set("bdime",e,document.domain,"/",expire30y)}}function writeBAIDUID(){var e,t,o,i=Cookie.get("BAIDUID");
/FG=(\d+)/.test(i)&&(t=RegExp.$1),/SL=(\d+)/.test(i)&&(o=RegExp.$1),/NR=(\d+)/.test(i)&&(e=RegExp.$1),options.hasOwnProperty("resultNum")&&(e=options.resultNum),options.hasOwnProperty("resultLang")&&(o=options.resultLang),Cookie.set("BAIDUID",i.replace(/:.*$/,"")+("undefined"!=typeof o?":SL="+o:"")+("undefined"!=typeof e?":NR="+e:"")+("undefined"!=typeof t?":FG="+t:""),".baidu.com","/",expire30y,!0)}function clearCookie(e){Cookie.clear(e,"/"),Cookie.clear(e,"/",document.domain),Cookie.clear(e,"/","."+document.domain),Cookie.clear(e,"/",".baidu.com")
}function reset(e){options=defaultOptions,save(e)}var defaultOptions={sugSet:1,sugStoreSet:1,isSwitch:1,isJumpHttps:1,imeSwitch:0,resultNum:10,skinOpen:1,resultLang:0,duRobotState:"000"},options={},tmpName,expire30y=new Date;expire30y.setTime(expire30y.getTime()+94608e7);try{if(bds&&bds.comm&&bds.comm.personalData){if("string"==typeof bds.comm.personalData&&(bds.comm.personalData=eval("("+bds.comm.personalData+")")),!bds.comm.personalData)return;for(tmpName in bds.comm.personalData)defaultOptions.hasOwnProperty(tmpName)&&bds.comm.personalData.hasOwnProperty(tmpName)&&"SUCCESS"==bds.comm.personalData[tmpName].ErrMsg&&(options[tmpName]=bds.comm.personalData[tmpName].value)
}try{parseInt(options.resultNum)||delete options.resultNum,parseInt(options.resultLang)||"0"==options.resultLang||delete options.resultLang}catch(e){}writeCookie(),"sugSet"in options||(options.sugSet=3!=Cookie.get("sug",3)?0:1),"sugStoreSet"in options||(options.sugStoreSet=Cookie.get("sugstore",0));var BAIDUID=Cookie.get("BAIDUID");"resultNum"in options||(options.resultNum=/NR=(\d+)/.test(BAIDUID)&&RegExp.$1?parseInt(RegExp.$1):10),"resultLang"in options||(options.resultLang=/SL=(\d+)/.test(BAIDUID)&&RegExp.$1?parseInt(RegExp.$1):0),"isSwitch"in options||(options.isSwitch=2==Cookie.get("ORIGIN",0)?0:1==Cookie.get("ORIGIN",0)?2:1),"imeSwitch"in options||(options.imeSwitch=Cookie.get("bdime",0))
}catch(e){}window.UPS={writeBAIDUID:writeBAIDUID,reset:reset,get:get,set:set,save:save}}(),function(){var e="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/plugins/every_cookie_4644b13.js";("Mac68K"==navigator.platform||"MacPPC"==navigator.platform||"Macintosh"==navigator.platform||"MacIntel"==navigator.platform)&&(e="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/plugins/every_cookie_mac_82990d4.js"),setTimeout(function(){$.ajax({url:e,cache:!0,dataType:"script"})},0);var t=navigator&&navigator.userAgent?navigator.userAgent:"",o=document&&document.cookie?document.cookie:"",i=!!(t.match(/(msie [2-8])/i)||t.match(/windows.*safari/i)&&!t.match(/chrome/i)||t.match(/(linux.*firefox)/i)||t.match(/Chrome\/29/i)||t.match(/mac os x.*firefox/i)||o.match(/\bISSW=1/)||0==UPS.get("isSwitch"));
bds&&bds.comm&&(bds.comm.supportis=!i,bds.comm.isui=!0),window.__restart_confirm_timeout=!0,window.__confirm_timeout=8e3,window.__disable_is_guide=!0,window.__disable_swap_to_empty=!0,window.__switch_add_mask=!0;var s="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/js/all_async_search_862ff2e.js",n="/script";document.write("<script src='"+s+"'><"+n+">"),bds.comm.newindex&&$(window).on("index_off",function(){$('<div class="c-tips-container" id="c-tips-container"></div>').insertAfter("#wrapper"),window.__sample_dynamic_tab&&$("#s_tab").remove()
}),bds.comm&&bds.comm.ishome&&Cookie.get("H_PS_PSSID")&&(bds.comm.indexSid=Cookie.get("H_PS_PSSID"));var a=$(document).find("#s_tab").find("a");a&&a.length>0&&a.each(function(e,t){t.innerHTML&&t.innerHTML.match(/新闻/)&&(t.innerHTML="资讯",t.href="//www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=",t.setAttribute("sync",!0))})}();</script>

			

	
		


	

	
		
				
	

	
	<script>
    A.merge("ip",function(){A.setup(function(){function showErrorMessage(){tr_res.style.display="none",tr_e.style.display="block"}function trim(str){var trimer=new RegExp("[\\s\\t\\xa0\\u3000]","g");return str.replace(trimer,"")}function dbc2sbc(ip_input){return ip_input.replace(/./g,function(a,b,c){var code=a.charCodeAt(0);if("undefined"!=typeof dbcHashTable[code])return dbcHashTable[code];else return a})}function validateIP(ip_input){if(!ip_input)return false;if(!/\d\./g.test(ip_input))return false;var ipArr=ip_input.split(".");if(4!=ipArr.length)return false;for(var temp,i=0,l=ipArr.length;i<l;i++){if(temp=ipArr[i],""===temp)return false;if(temp=1*temp,0==i&&temp<=0)return false;if(isNaN(temp)||temp>255||temp<0)return false}return true}function formatIP(ip_input){for(var ipArr=ip_input.split("."),i=0;i<ipArr.length;i++)ipArr[i]=1*ipArr[i];return ipArr.join(".")}function startSearching(){searching=true,txt.disabled=true}function endSearching(){searching=false,txt.disabled=false;try{if(false==txt.disabled)ipTimer=setTimeout(function(){txt.focus()},50)}catch(e){}}function resetSearch(count){return function(){if(queryCount==count&&searching)txt_res.innerHTML='<span style="color:#F00">'+query_error_txt+"</span>",endSearching()}}function submitVal(val){if(queryCount++,validateIP(val)){txt.value=val=formatIP(val),tr_e.style.display="none",tr_res.style.display="block",txt_res.innerHTML='<span style="color:#666">查询中...</span>';var resourceId=t.srcid;if(t.ajax(val,resourceId,{success:function(data){if(data){var d=data[0];if(d)txt_res.innerHTML="<b>"+d.origip+'来自<span style="color:#f00">'+d.location+"</span></b>";else txt_res.innerHTML='<span style="color:#F00">'+query_error_txt+"</span>",endSearching()}endSearching()},error:function(data){txt_res.innerHTML='<span style="color:#F00">'+query_error_txt+"</span>",endSearching()},timeout:function(data){txt_res.innerHTML='<span style="color:#F00">'+query_error_txt+"</span>",endSearching()}}),startSearching(),window.baidu_aladdin_mid_temp_ip_timer)clearTimeout(window.baidu_aladdin_mid_temp_ip_timer);
window.baidu_aladdin_mid_temp_ip_timer=setTimeout(function(count){return resetSearch(count)}(queryCount),6e3)}else showErrorMessage()}function searchButtonEventListner(e){if(e=e||window.event,searching)return false;var val=trim(txt.value);if(val=dbc2sbc(val),submitVal(val),e)e.preventDefault(),e.stopPropagation()}function bindSearchEvent(){$(txt).keydown(function(e){var e=e||window.event;if(e&&13==e.keyCode)searchButtonEventListner(e)}),$(txt).mouseover(function(e){if("请输入ip地址"!=this.value)this.select()}),$(btn).click(function(e){searchButtonEventListner(e)}),$(btn).keydown(function(e){if(e=e||window.event,e&&13==e.keyCode)searchButtonEventListner(e)})}var t=this,isIE=!-[1],isIE6=isIE&&!window.XMLHttpRequest,dbcHashTable={65297:"1",65298:"2",65299:"3",65300:"4",65301:"5",65302:"6",65303:"7",65304:"8",65305:"9",65296:"0",65294:"."},txt=t.find(".op-ip-input")[0],btn=t.find(".op-ip-do-submit")[0],tr_res=t.find(".op-ip-query-res")[0],txt_res=t.find(".op-ip-query-res-txt")[0],tr_e=t.find(".op-ip-query-e")[0],query_error_txt="抱歉没有找到此ip地址的信息",searching=false,queryCount=0,ipTimer=null;if(isIE6){try{document.execCommand("BackgroundImageCache",false,true),txt.setAttribute("placeholder","")}catch(err){}$(txt).addClass("op-ip-tip"),txt.value=txt.getAttribute("tip")||"",$(txt).on("focus",function(e){var curValue=trim(txt.value);if(curValue==txt.getAttribute("tip"))txt.value="",$(txt).removeClass("op-ip-tip"),$(txt).addClass("op-ip-no-tip")}),$(txt).on("blur",function(e){var curValue=trim(txt.value);if(""==curValue)txt.value=txt.getAttribute("tip"),$(txt).removeClass("op-ip-no-tip"),$(txt).addClass("op-ip-tip")})}bindSearchEvent(),this.dispose=function(){window.opuiLikeShareContent6006=null,clearTimeout(ipTimer),clearTimeout(window.baidu_aladdin_mid_temp_ip_timer)}});});A.merge("bk_polysemy",function(){A.setup(function(){var _this=this,$focusrightf=_this.find(".op-bk-polysemy-focusrightf:first span");if($focusrightf.length)$focusrightf.last().remove()});});A.merge("right_recommends_merge",function(){A.setup(function(){function bindLayers($btns,a){if(bds.se&&bds.se.tip)$.each($btns,function(i,v){var $v=$(v),$parent=$v.parents(".opr-recommends-merge-item"),$layer=$parent.find(".opr-recommends-merge-layer-p"),$contentHtml=$layer.find(".opr-recommends-merge-layer"),x=getX($v);$.each($contentHtml.find("img"),function(i,v){var $v=$(v);if($v.attr("data-img"))$v.attr("src",$v.attr("data-img"))});var tip=new bds.se.tip({target:v,align:"right",content:$contentHtml,arrow:{offset:x},offset:{x:x,y:25}});obj.push({dom:v,tip:tip})})}var _this=this,$layerbtns=_this.find(".opr-recommends-merge-layerbtn"),$moreBtn=_this.find(".opr-recommends-merge-more-btn"),$dodgeBtn=_this.find(".opr-recommends-merge-dodge"),$dodgeTip=_this.find(".opr-recommends-merge-dodge-tip"),$content=_this.find(".opr-recommends-merge-content"),obj=[],pageFormat=bds.comm.containerSize,showType=_this.data.showType,getX=function($o){$o=$($o);var $container=$(_this.container),x=$container.width()-($o.offset().left-$container.offset().left)-$o.width(),maxX=185;if(x<0)x=0;else if(x>maxX)x=maxX;return x};if($dodgeBtn[0]&&function(){$dodgeBtn.click(function(){var $this=$(this);if($content.toggle(),"隐藏信息"==$this.html()){if("1"==showType)$.setCookie("BD_CON_LEVEL","1",{expires:15552e6});else $.removeCookie("BD_CON_LEVEL");$this.html("继续浏览"),$dodgeTip.html("以下图片可能让您感觉不适，您可以")}else{if($this.html("隐藏信息"),"1"==showType)$.removeCookie("BD_CON_LEVEL");else $.setCookie("BD_CON_LEVEL","1",{expires:15552e6});$dodgeTip.html("如果以下图片让您感觉不适，您可以")}})}(),"pc"==_this.data.platform)bds.event.on("se.window_resize",function(){if(bds.comm.containerSize!==pageFormat)pageFormat=bds.comm.containerSize,$.each(obj,function(i,v){var tip=v.tip,_x=getX(v.dom);tip.setOffset({x:_x}),tip.setArrow({offset:_x})})}),bds.event.on("se.api_tip_ready",function(){bindLayers($layerbtns)}),bindLayers($layerbtns);$moreBtn.on("click",function(){var $this=$(this),dom_this=$this[0];if($moreTxt=$this.find("span"),$moreIcon=$this.find(".c-icon"),$panel=$this.parent().next(".opr-recommends-merge-panel"),!dom_this.moreLists&&(dom_this.moreLists=[]),$this.hasClass("opr-recommends-merge-close"))$moreTxt.text("展开"),$moreIcon.removeClass("c-icon-chevron-top").addClass("c-icon-chevron-bottom"),$(dom_this.moreLists).hide();
else if($moreTxt.text("收起"),$moreIcon.addClass("c-icon-chevron-top").removeClass("c-icon-chevron-bottom"),!dom_this.moreLists.length){var $textarea=$panel.find(".opr-recommends-merge-more-textarea"),$moreLayerBtns=[];$panel.append($textarea.val()),$textarea.remove(),dom_this.moreLists=$panel.find(".opr-recommends-merge-morelists"),$moreLayerBtns=dom_this.moreLists.find(".opr-recommends-merge-layerbtn");var $_imgs=dom_this.moreLists.find(".opr-recommends-merge-img");$.each($_imgs,function(i,v){var $v=$(v);$v.attr("src",$v.attr("data-img"))});var $_imgsB=dom_this.moreLists.find(".opr-recommends-merge-imgtext");if($_imgsB.parent().remove(),"pc"==_this.data.platform)bds.event.on("se.api_tip_ready",function(){bindLayers($moreLayerBtns)}),bindLayers($moreLayerBtns,1)}else $(dom_this.moreLists).show();$this.toggleClass("opr-recommends-merge-close")});var $userIcon=_this.find(".opr-recommends-merge-user-layer-icon"),$layerCon=_this.find(".opr-recommends-merge-user-layer-con"),$layerp1=_this.find(".opr-recommends-merge-user-layer-p1"),$layerp2=_this.find(".opr-recommends-merge-user-layer-p2");$layerCon.on("click",function(e){e.preventDefault()}),$userIcon.hover(function(){$layerCon.removeClass("opr-recommends-merge-user-layer-hide"),ns_c&&ns_c({item:"right_recommends_merge",act:"user_hover",qid:bds.comm.qid})},function(){$layerCon.addClass("opr-recommends-merge-user-layer-hide")}),$userIcon.on("click",function(e){e.preventDefault()}),$layerCon.hover(function(){$layerCon.removeClass("opr-recommends-merge-user-layer-hide")},function(){$layerCon.addClass("opr-recommends-merge-user-layer-hide")});var userLayerTimer;$layerCon.find("button").on("click",function(){$layerp1.remove(),$layerCon.find("button").remove(),$layerp2.text("感谢您的反馈"),userLayerTimer=setTimeout(function(){$userIcon.hide(),$layerCon.css("z-index","999"),$layerCon.fadeOut()},600)}),_this.dispose=function(){userLayerTimer&&clearTimeout(userLayerTimer),$layerCon.stop()}});});A.merge("right_toplist1",function(){A.setup(function(){var _this=this,$tb=_this.find("tbody"),$refresh=_this.find(".opr-toplist1-refresh"),currentPage=0;if(_this.data.num>0)$refresh.on("click",function(e){if(currentPage<_this.data.num-1)++currentPage;else currentPage=0;$tb.hide(),$tb.eq(currentPage).show(),e.preventDefault()})});});
bds.comm.resultPage = 1;
bds._base64 = {
     domain : "https://ss0.bdstatic.com/9uN1bjq8AAUYm2zgoY3K/",
     b64Exp : -1,
     pdc : 0
};
if(bds.comm.supportis){
    window.__restart_confirm_timeout=true;
    window.__confirm_timeout=8000;
    window.__disable_is_guide=true;
    window.__disable_swap_to_empty=true;
}
initPreload({
    'isui':true,
    'index_form':"#form",
    'index_kw':"#kw",
    'result_form':"#form",
    'result_kw':"#kw"
});
</script>

	


	
		<script type="text/javascript">_WWW_SRV_T =147.4;</script>
	
	

</html>
<!--cxy_ex+1540753653+2429190775+d41d8cd98f00b204e9800998ecf8427e--><!--cxy_all+monline_4_dg+fef18d5f65810a0d305d6bc2068148ae+000000000000000000000000000000000259858-->
百度城市ip ['\n    \t\t', '本机IP:\xa0119.130.202.144', '广东省广州市 电信\t    \n    ']

进程已结束,退出代码0

"""

文本列表 = 文本.split("\n")

for 行 in 文本列表:
    if '本机IP' in 行 and 'c-gap-right' in 行 and '/span' in 行:
        ip行=行
        #print("ip行",ip行)
        break  # 结束循环
规则='.{0,}&nbsp;'
ip行 =re.sub(规则, '', ip行)#替换   ,count=0,re.S|re.I

规则='<.{0,}'
ip地址 =re.sub(规则, '', ip行)#替换   ,count=0,re.S|re.I


规则='.{0,}>'
ip城市 =re.sub(规则, '', ip行)#替换   ,count=0,re.S|re.I

print("ip地址:",ip地址)
print("ip城市:",ip城市)

