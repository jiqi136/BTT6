# -*- coding:utf-8
import os  # 本地操作
import re
import time


def fewfg():
    if '"最后回复时间">' in 每栏 and "title=" in 每栏 and "threadlist_reply_date" in 每栏:
        print(每栏)

        规则 = '.{1,}最后回复时间">'
        最后回复时间 = re.sub(规则, '', 每栏)  # 替换   ,count=0,re.S|re.I
        规则 = '<.{0,}'
        最后回复时间 = re.sub(规则, '', 最后回复时间)  # 替换   ,count=0,re.S|re.I
        最后回复时间 = 最后回复时间.strip()  # 默认则是去除空格
        最后回复时间列表.append(最后回复时间)  # 列表追加

        print("最后回复时间", 最后回复时间)

    if '"回复"' in 每栏 and "title=" in 每栏 and "threadlist_rep_num" in 每栏:
        print(每栏)

        规则 = '.{1,}回复">'
        回复数 = re.sub(规则, '', 每栏)  # 替换   ,count=0,re.S|re.I
        规则 = '<.{0,}'
        回复数 = re.sub(规则, '', 回复数)  # 替换   ,count=0,re.S|re.I
        回复数 = 回复数.strip()  # 默认则是去除空格
        回复数列表.append(回复数)  # 列表追加

        print("回复数", 回复数)

    if 'href=' in 每栏 and "title=" in 每栏 and "noreferrer" in 每栏:
        print(每栏)

        规则 = '.{1,}href="'
        帖子链接 = re.sub(规则, '', 每栏)  # 替换   ,count=0,re.S|re.I
        规则 = '".{0,}'
        帖子链接 = re.sub(规则, '', 帖子链接)  # 替换   ,count=0,re.S|re.I
        帖子链接 = 帖子链接.strip()  # 默认则是去除空格

        帖子链接 = 'http://tieba.baidu.com{}'.format(帖子链接)  # '代入 '{}'
        帖子链接列表.append(帖子链接)  # 列表追加
        print("帖子链接", 帖子链接)


        print("最后回复时间列表数", len(最后回复时间列表))
        print("回复数列表数", len(回复数列表))
        print("帖子链接列表数", len(帖子链接列表))
        time.sleep(10000)  # 等待

网页="""E:\python3an\an\python.exe E:/PY学习文件/BTT影视剧/发贴推广/百度回帖留网址ID.py
{'User-Agent': 'Mozilla/5.0(WindowsNT6.0)AppleWebKit/772.5(KHTML,likeGecko)Chrome/81.0.1084.36Safari/536.5'}
网页采集,全部完成
返回网页内容 ：  <Response [200]>
返回网页内容文本 ：  <!DOCTYPE html>
<!--STATUS OK-->
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <link rel="search" type="application/opensearchdescription+xml" href="/tb/cms/content-search.xml" title="百度贴吧" />
            <meta name="keywords" content="始祖家族,美剧,电视剧,资源">
    <meta name="description" content="本吧热帖: 1-求五季资源 2-【始祖家族】衍生剧【吸血鬼后裔】10月25号开播！ 3-百度贴吧始祖家族吧拒绝任何广告发现必封！ 4-始祖家族  1---5  完结  精心整理好啦  no，剪 5-初代吸血鬼「始祖家族」「1--5季」已整！理????? 6-?（初代吸血鬼）（始祖家族）1～5已整理? 7-百度贴吧始祖家族吧日常签到水贴大楼！">
    <title>始祖家族吧-百度贴吧--美剧吸血鬼日记衍生剧The Originals贴吧 </title>
    

    
<script>
    void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>    <link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/static-common/style/tb.js/dialog_bda1025.css,/tb/static-common/lib/tbui/style/all_f29e774.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/index_4fc89ea.css,/tb/_/search_8bbfc49.css,/tb/_/fixed_bar_af8c791.css" />
<link rel="shortcut icon" href="https://gsp0.baidu.com/5aAHeD3nKhI2p27j8IqW0jdnxx1xbK/tb/favicon.ico"/>

<script>
    // 页面的基本信息
    var PageData = {
        'tbs': "3b22fb4e08ce68ee1541357000"    };

    PageData.page = "frs";

    // 用户的基本信息
    PageData.user = {
        'id': 0,
        'name': "",
        'no_un': 0,
        'is_login': 0,
        'is_new_user': 1,
        'portrait': "00000000",
        'name_url': "&ie=utf-8"    };

    // 吧的基本信息
    PageData.forum = {
        'id': 7739963,
        'name': "\u59cb\u7956\u5bb6\u65cf",
        'first_class': "\u7535\u89c6\u5267",
        'second_class': "\u7f8e\u5267"    };

    if (Object.freeze) {
        (function deepFreeze(o) {
            var prop, propKey;
            Object.freeze(o);
            for (propKey in o) {
                prop = o[propKey];
                if (!o.hasOwnProperty(propKey) ||
                    typeof prop !== 'object' ||
                    !prop ||
                    Object.isFrozen(prop)) {
                    continue;
                }
                deepFreeze(prop);
            }
        })(PageData);
    }
</script>

    <script> alog('speed.set', 'ht', +new Date); </script>

        <!-- 引入百度统计 -->
    <script>
        var _hmt = _hmt || [];
        (function() {
          var hm = document.createElement("script");
          hm.src = "https://hm.baidu.com/hm.js?98b9d8c2fd6608d564bf2ac2ae642948";
          var s = document.getElementsByTagName("script")[0]; 
          s.parentNode.insertBefore(hm, s);
        })();
    </script>

</head>

<body>
<div class="wrap1">
    <div class="wrap2">
        
<div class="header">
    <div id="pagelet_common/pagelet/userbar"></div>


<div id="head" class="search_bright clearfix">
<div class="head_inner">
    <div class="search_top clearfix">
        <div class="search_nav j_search_nav">
            <!-- 资讯、贴吧、知道、视频、音乐、图片、地图、文库 -->
            <a rel="noreferrer"  param="wd"
               href=https://www.baidu.com/s?cl=3&amp; >网页</a>
            <a rel="noreferrer"  param="word" href="http://www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;fr=tieba&amp;">资讯</a>
            <b>贴吧</b>
            <a rel="noreferrer"  param="word"
               href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;">知道</a>
            <!-- <a rel="noreferrer"  param="word" href="http://v.baidu.com/v?ct=301989888&amp;rn=20&amp;pn=0&amp;db=0&amp;s=21&amp;">视频</a> -->
            <a rel="noreferrer"  param="word" href="http://www.baidu.com/sf/vsearch?pd=video&amp;tn=vsearch&amp;ct=301989888&amp;rn=20&amp;pn=0&amp;db=0&amp;s=21&amp;rsv_spt=11&amp;">视频</a>
            <a rel="noreferrer"  param="key" href="http://music.baidu.com/search?fr=tieba&">音乐</a>
            <a rel="noreferrer"  param="word"
               href="http://image.baidu.com/i?tn=baiduimage&amp;ct=201326592&amp;lm=-1&amp;cl=2&amp;">图片</a>
            <a rel="noreferrer"  param="word" href="http://map.baidu.com/m?fr=map006&amp;">地图</a>
            <a rel="noreferrer"  href="http://wenku.baidu.com/search?fr=tieba&lm=0&od=0&" param="word" target="_blank">文库</a>
        </div>
    </div>
    <div class="search_main_wrap">
        <div class="search_main clearfix">
            <div class="search_form">
                <a rel="noreferrer"  title="到贴吧首页" href="/" class="search_logo" id="search_logo_large"></a>
                <a rel="noreferrer"  id="search_logo_small" class="" title="到贴吧首页" href="/"></a>
                <form name="f1" class="clearfix j_search_form" action="/f"
                      id="tb_header_search_form">
                                        <input class="search_ipt search_inp_border j_search_input tb_header_search_input"
                           name="kw1" value="始祖家族" type="text" autocomplete="off" size="42"
                           tabindex="1" id="wd1" maxlength="100" x-webkit-grammar="builtin:search"
                           x-webkit-speech="true"/>
                    <input autocomplete="off" type="hidden" name="kw" value="始祖家族" id="wd2"/>
                    <span class="search_btn_wrap search_btn_enter_ba_wrap">
                        <a rel="noreferrer"  class="search_btn search_btn_enter_ba j_enter_ba" href="#"
                           onclick="return false;"
                           onmousedown="this.className+=' search_btn_down'"
                           onmouseout="this.className=this.className.replace('search_btn_down','')">进入贴吧</a>
                    </span>
                    <span class="search_btn_wrap">
                        <a rel="noreferrer"  class="search_btn j_search_post" href="#" onclick="return false;"
                           onmousedown="this.className+=' search_btn_down'"
                           onmouseout="this.className=this.className.replace('search_btn_down','')">全吧搜索</a>
                    </span>
                    <a rel="noreferrer"  class="senior-search-link" href="//tieba.baidu.com/f/search/adv">高级搜索</a>
                    <div id="pagelet_search/pagelet/search_ad"></div>                </form>
                                <p style="display:none;" class="switch_radios">
                    <input type="radio" class="nowtb" name="tb" id="nowtb"><label
                        for="nowtb">吧内搜索</label>
                    <input type="radio" class="searchtb" name="tb" id="searchtb"><label for="searchtb">搜贴</label>
                    <input type="radio" class="authortb" name="tb" id="authortb"><label for="authortb">搜人</label>
                    <input type="radio" class="jointb" checked="checked" name="tb" id="jointb"><label
                        for="jointb">进吧</label>
                    <input type="radio" class="searchtag" name="tb" id="searchtag"
                           style="display:none;"><label for="searchtag"
                                                        style="display:none;">搜标签</label>
                </p>
            </div>
        </div>
    </div>
</div>
</div>
<script>
if (window.alog && window.alog.fire) {
    alog('speed.set', 'c_widget_search_show', +new Date);
    alog.fire("mark");
}
</script>

<div id="pagelet_search/pagelet/search_logic"></div><div id="pagelet_frs-header/pagelet/head"></div></div>
<div class="content" id="content">
    <div id="pagelet_frs-base/pagelet/content"></div></div>
<div class="foot">
    <div id="pagelet_frs-footer/pagelet/content_footer"></div></div>
<div id="fixed_bar" class="">
    <img src="//tb1.bdstatic.com/tb/cms/PC%E7%AB%AF%E5%BA%95%E9%83%A8%E9%80%9A%E6%A0%8F%E5%BC%B9%E5%B1%821000x120.png" alt="">
    <img src="//tb2.bdstatic.com/tb/img/icon_close_b98955a.png" alt="" class="close">
</div>
    </div>
</div>

<script src="//tb1.bdstatic.com/??/tb/static-common/js/promise_3464b70.js,/tb/static-common/js/promise_config_91c2822.js,/tb/static-common/lib/uri.js/src/URI.min_e84a17a.js,/tb/static-common/js/jquery/jquery_ba2d628.js,/tb/static-common/js/jquery/jquery-ui-1.10.3.custom_65f256d.js,/tb/static-common/js/jquery/jquery.ui.droppable_3b547e9.js,/tb/static-common/js/jquery/jquery.lazyload_49a7282.js,/tb/static-common/lib/fis-module/fis_c1e11e0.js,/tb/static-common/js/__aop_af3a579.js,/tb/static-common/js/baiduTemplate_841433b.js,/tb/static-common/js/jcarousellite_1.0.1_a033082.js,/tb/static-common/js/page_link_2ec40cf.js,/tb/static-common/js/pageconf_8abbe38.js,/tb/static-common/js/tb_0329f65.js,/tb/static-common/js/tb_extend_000de9f.js,/tb/static-common/js/tb_fis_config_6ca7118.js,/tb/static-common/js/tb_stats_ba8deb9.js,/tb/static-common/js/underscore_b23cfa6.js,/tb/static-common/js/qrcode_f84ab06.js,/tb/static-common/lib/fis-module/module_5ae89d6.js,/tb/static-common/lib/bigpipe.js/lib/bigpipe_eabdb6b.js,/tb/static-common/js/bigpipe_config_9c152a9.js,/tb/static-common/js/lcs/lib/Long_8276e76.js,/tb/static-common/js/lcs/lcsas_4e45cc0.js"></script>
<script src="//tb1.bdstatic.com/??/tb/static-common/js/common/MessageSystem_2f3859e.js,/tb/static-common/js/common/CommonManager_main_d3b4283.js,/tb/static-common/js/common/passport/pass_shell_7351279.js,/tb/static-common/js/common/passport/passport_reset_ec12f65.js,/tb/static-common/js/common/passport/PassportFillName_925655f.js,/tb/static-common/js/common/uiDecorator_125371a.js,/tb/static-common/js/common/passport/PassportLogin_fe8162a.js,/tb/static-common/js/common/user/User_11fe4ca.js,/tb/static-common/js/common/crosspage_msg_system/utils/LCFManager_f2555be.js,/tb/static-common/js/common/crosspage_msg_system/utils/MessageProxy_25dc8d9.js,/tb/static-common/js/common/crosspage_msg_system/utils/SWFListen_87d118b.js,/tb/static-common/js/common/crosspage_msg_system/utils/SWFRequest_f586836.js,/tb/static-common/js/common/crosspage_msg_system/MsgSystem_9ef7035.js,/tb/static-common/js/common/user_message/UserMessage_e770e9e.js,/tb/static-common/js/tb_https_2f6042d.js"></script>
<div id="pagelet_frs-footer/pagelet/extension"></div><script type="text/javascript">window.alogObjectConfig={product:"14",page:"14_21",monkey_page:"",speed_page:"",speed:{sample:"0.001"},monkey:{sample:"0.001"},exception:{sample:"0.001"},feature:{sample:"0.001"},cus:{sample:"0.001"},csp:{sample:"0.001","default-src":[{match:"*bae.baidu.com",target:"Accept,Warn"},{match:"*.baidu.com,*.bdstatic.com,*.bdimg.com,localhost,*.hao123.com,*.hao123img.com",target:"Accept"},{match:/^(127|172|192|10)(\.\d+){3}$/,target:"Accept"},{match:"*",target:"Accept,Warn"}]}},void function(e,t,a,c,n,o){function r(t){e.attachEvent?e.attachEvent("onload",t,!1):e.addEventListener&&e.addEventListener("load",t)}function s(e,a,c){c=c||15;var n=new Date;n.setTime((new Date).getTime()+1e3*c),t.cookie=e+"="+escape(a)+";path=/;expires="+n.toGMTString()}function i(e){var a=t.cookie.match(new RegExp("(^| )"+e+"=([^;]*)(;|$)"));return null!=a?unescape(a[2]):null}function p(){var e=i("PMS_JT");if(e){s("PMS_JT","",-1);try{e=e.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),e=e&&e[1]&&e[2]?{s:parseInt(e[1]),r:e[2]}:{}}catch(a){e={}}e.r&&t.referrer.replace(/#.*/,"")!=e.r||alog("speed.set","wt",e.s)}}if(e.alogObjectConfig){var m=e.alogObjectConfig.sample,l=e.alogObjectConfig.rand;c="https:"===e.location.protocol?"https://fex.bdstatic.com"+c:"http://fex.bdstatic.com"+c,m&&l&&l>m||(r(function(){alog("speed.set","lt",+new Date),n=t.createElement(a),n.async=!0,n.src=c+"?v="+~(new Date/864e5)+~(new Date/864e5),o=t.getElementsByTagName(a)[0],o.parentNode.insertBefore(n,o)}),p())}}(window,document,"script","/hunter/alog/dp.min.js");</script>
<script type="text/javascript">!function(){"use strict";Bigpipe.addEventListener("beforepageletload",function(e){e.on("styleloaded",function(){this.dpStyleLoadedTime=+new Date}),e.on("scriptloaded",function(){this.dpScriptLoadedTime=+new Date})}),Bigpipe.addEventListener("pageletstyleloaded",function(e){e.emit("styleloaded"),this.dpSelfStyleLoadedTime=+new Date}),Bigpipe.addEventListener("pageletscriptloaded",function(e){e.emit("scriptloaded"),this.dpSelfScriptLoadedTime=+new Date}),Bigpipe.addEventListener("pageloaded",function(e){var d,a,t,o=[{name:"frs-header/pagelet/head",showKey:"c_head_pagelet_show",loadedKey:"c_head_pagelet_loaded"},{name:"search/pagelet/search_logic",showKey:"c_search_pagelet_show",loadedKey:"c_search_pagelet_loaded"},{name:"frs-list/pagelet/content",showKey:"c_list_pagelet_show",loadedKey:"c_list_pagelet_loaded"},{name:"frs-aside/pagelet/aside",showKey:"c_aside_pagelet_show",loadedKey:"c_aside_pagelet_loaded"},{name:"frs-footer/pagelet/content_footer",showKey:"c_foot_pagelet_show",loadedKey:"c_foot_pagelet_loaded"}];$.each(o,function(){var o=e[this.name];o&&alog&&alog.fire&&(alog("speed.set",this.showKey,this.isSelf?o.dpSelfStyleLoadedTime:o.dpStyleLoadedTime),alog.fire("mark"),alog("speed.set",this.loadedKey,this.isSelf?o.dpSelfScriptLoadedTime:o.dpScriptLoadedTime),alog.fire("mark"),d=!d||d>o.dpStyleLoadedTime?o.dpStyleLoadedTime:d,a=!a||a>o.dpScriptLoadedTime?o.dpScriptLoadedTime:a,t=!t||t<o.dpStyleLoadedTime?o.dpStyleLoadedTime:t)}),d&&a&&(alog("speed.set","c_first_pagelet_show",d),alog.fire("mark"),alog("speed.set","c_first_pagelet_loaded",a),alog.fire("mark")),alog("speed.set","drt",t)})}();</script><script src="//tb1.bdstatic.com/??/tb/_/title_3ff1a8b.js,/tb/_/fixed_bar_e002a0a.js"></script>

</body>
</html>
<code class="pagelet_html" id="pagelet_html_search/pagelet/search_logic" style="display:none;"><!----></code><script>Bigpipe.register("search/pagelet/search_logic", {"parent":"","scripts":["\/tb\/_\/http_transform_d9b1cbd.js","\/tb\/_\/suggestion_bb9fd35.js","\/tb\/_\/search_handler_7e7697d.js","\/tb\/_\/search_dialog_b4dc63b.js","\/tb\/_\/search_logic_13e7c51.js"],"styles":["\/tb\/_\/http_transform_d41d8cd.css","\/tb\/_\/suggestion_c2d979b.css"]}).then(function(pagelet){    _.Module.use('search/widget/suggestion', [], function () {
    });
    _.Module.use('search/widget/search_logic', [
        $('#head'),
        {
            product: 'frs',
            forumName: '始祖家族',
            searchFixed: '1',
            sugOn: '1'
        }
    ]);
});</script><code class="pagelet_html" id="pagelet_html_frs-base/pagelet/content" style="display:none;"><!--    <div class="forum_content clearfix">
        <div class="main" id="content_wrap">
            <div id="pagelet_frs-list/pagelet/content"></div>        </div>
        <div class="aside" id="aside">
            <div id="pagelet_frs-aside/pagelet/aside"></div>        </div>
    </div>
--></code><script>Bigpipe.register("frs-base/pagelet/content", {"parent":"","scripts":["\/tb\/_\/content_1216e5e.js","\/tb\/_\/page_router_294733d.js"],"styles":["\/tb\/_\/page_router_6d81cff.css"]}).then(function(pagelet){    _.Module.use('tbui/widget/page_router', [pagelet]);
    _.Module.use('frs-base/pagelet/content', [pagelet], function (instance) {

    });
});</script><code class="pagelet_html" id="pagelet_html_frs-footer/pagelet/content_footer" style="display:none;"><!--
<div class="frs_content_footer_pagelet">
	
	
		
		<div class="editor_wrap_bright ">
	<div id="pagelet_poster/pagelet/rich_poster"></div>	</div>

	
	
<div id="footer" class="footer">   
                                                                                                      
	<span>&copy;2018 Baidu</span>
	<a pv_code="0" href="/tb/eula.html" target="_blank">贴吧协议</a>	<span>|</span>
	<a pv_code="0" href="https://tieba.baidu.com/tb/cms/tieba-fe/tieba_promise.html" target="_blank">隐私政策</a>	<span>|</span>
	<a pv_code="0" href="http://tieba.baidu.com/tb/system.html" target="_blank">吧主制度</a>	<span>|</span>
	<a class="ueg_feedback-link" data-site="feedbackLink"  pv_code="0" href="http://tieba.baidu.com/hermes/feedback" target="_blank">意见反馈</a>	<span>|</span>
	<a pv_code="0" href="/tb/zt/declare/" target="_blank">网络谣言警示</a>	</div>

</div>

--></code><script>Bigpipe.register("frs-footer/pagelet/content_footer", {"parent":"","scripts":["\/tb\/_\/frs-footer\/content_footer_1afa6e4.js","\/tb\/_\/tbcopy_0deb361.js","\/tb\/_\/duoku_servers_dialog_0291705.js","\/tb\/_\/duoku_servers_list_046cdf2.js","\/tb\/_\/footer_8d5b425.js"],"styles":["\/tb\/_\/frs-footer\/content_footer_e1ac3c2.css","\/tb\/_\/duoku_servers_dialog_f50364d.css","\/tb\/_\/duoku_servers_list_42e14c2.css","\/tb\/_\/footer_fd940ae.css"]}).then(function(pagelet){_.Module.use('common/widget/footer', [], function(){});
_.Module.use('frs-footer/pagelet/content_footer', [pagelet]);
});</script><code class="pagelet_html" id="pagelet_html_common/pagelet/userbar" style="display:none;"><!--<div class="common-pagelet-userbar">
    
<div id="local_flash_cnt"></div>

</div>
--></code><script>Bigpipe.register("common/pagelet/userbar", {"parent":"","scripts":["\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/http_transform_d9b1cbd.js","\/tb\/_\/tdou_open_type_a72e1ed.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/base_dialog_user_bar_ea71e42.js","\/tb\/_\/qianbao_cashier_dialog_5247354.js","\/tb\/_\/qianbao_purchase_member_efbbe6b.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/cashier_dialog_d52cf7c.js","\/tb\/_\/pay_member_c57f92d.js","\/tb\/_\/event_center_ca531c9.js","\/tb\/_\/new_message_system_eb357ea.js","\/tb\/_\/join_vip_dialog_9242ef7.js","\/tb\/_\/user_head_00b2e11.js","\/tb\/_\/js_pager_6b8af39.js","\/tb\/_\/wallet_dialog_56e1f90.js","\/tb\/_\/card_a7ea147.js","\/tb\/_\/userbar_32c5b26.js"],"styles":["\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/http_transform_d41d8cd.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/base_dialog_user_bar_da68a26.css","\/tb\/_\/qianbao_cashier_dialog_c1e313a.css","\/tb\/_\/qianbao_purchase_member_d190d50.css","\/tb\/_\/cashier_dialog_0390325.css","\/tb\/_\/pay_member_d41d8cd.css","\/tb\/_\/new_message_system_bea7f16.css","\/tb\/_\/user_head_35f26e0.css","\/tb\/_\/js_pager_5be1e39.css","\/tb\/_\/wallet_dialog_8be3b12.css","\/tb\/_\/card_e028cbd.css","\/tb\/_\/userbar_b56525c.css"]}).then(function(pagelet){    // PageData.product = frs TODO
    _.Module.use("common/widget/Userbar", {
        page: 'frs',
        userLevel:null,
        userScore:null,
        vipInfo:null,
        isVideoPGCUser: 0,
        lcsKey: '', // flash_lcs.js 中使用
        bluePush: {
            unit: {"url":["http:\/\/push.dui1dui.com\/tieba\/awaken"],"button":["\u9a6c\u4e0a\u62a2"],"text":["\u4eb2\u7231\u7684\uff0c\u4f60\u4e0d\u77e5\u9053\u5417\uff1f\u4f60\u8d26\u6237\u4e2d\u7684\u84dd\u94bb\u53ef\u4ee5\u7528\u6765\u5151\u6362\u8d34\u5427\u4f1a\u5458\uff01\u540d\u989d\u6709\u9650\uff0c\u901f\u6765\u62a2\uff01"]},
            handle: null,
            diamond: null        },
        userBarConfigData: {"switch":"0","word":"hao123","url":"https:\/\/www.hao123.com\/?tn=50000076_hao_pg"}    });
});</script><code class="pagelet_html" id="pagelet_html_search/pagelet/search_ad" style="display:none;"><!----></code><script>Bigpipe.register("search/pagelet/search_ad", {"parent":"","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_frs-header/pagelet/head" style="display:none;"><!--

<div class="head_main">
        <div class="head_top">
        

<div id="pagelet_platform-activity/pagelet/full_width_head"></div>    </div>
    <div class="head_middle">
        


    </div>
    <div class="head_content">
        



<div class="card_banner card_banner_link" >
      <img src='https://imgsa.baidu.com/forum/pic/item/d143ad4bd11373f0317075b2a90f4bfbfbed044b.jpg' id="forum-card-banner" />
  
  <div class='gift-goin'>
    <div class="gift-goin-left">
        <div class="gift-goin-con">
            <div class="gift-goin-con-start">
                <p class="gift-goin-con-title">本吧礼赞</p>
                <div class="gift-goin-con-title thanks"><em>感谢你与</em><span class="forum-name-sub">本吧</span><em>的一同成长</em></div>
            </div>
            <div class="gift-goin-con-list">
                <div class="gift-goin-con-title"><em>感谢你与</em><span class="forum-name-sub">本吧</span><em>的一同成长</em></div>
                <div class="gift-goin-con-check">
                    <ul class="gift-goin-con-check-list"></ul>
                    <a href="javascript:;" class="j-check-gift" j-check-gift>查看榜单 ></a>
                </div>
            </div>
        </div>
        <img src="//tb2.bdstatic.com/tb/img/ihome_batou_icon_636b52f.png" height="50" width="50" alt="" class="gift-goin-img j-goin-gift"/>
    </div>
</div>



</div>

<div class="card_top_wrap clearfix card_top_theme ">
   <div class="card_top_right">
       <div id="pagelet_forum/pagelet/sign_mod"></div>   </div>
   <div class="card_top clearfix">
              <div class="card_head">
           <a rel="noreferrer" href="/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8">
               <img class="card_head_img" id="forum-card-head" src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b150_150&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=0fb65ad0543424e519d057f16811e867&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2Ff703738da97739127a678ef1f9198618377ae2d9.jpg"/>
           </a>
       </div>

       <div class="card_title">
           <a rel="noreferrer" class=" card_title_fname" title=""
              href="/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8">
               始祖家族吧
           </a>
                                 <div class="focus_btn_wrap">
               <div id="pagelet_forum/pagelet/focus_btn"></div>           </div>
           <div class="card_num">
               <div id="pagelet_forum/pagelet/forum_card_number"></div>           </div>
       </div>

       <p class="card_slogan">美剧吸血鬼日记衍生剧The Originals贴吧</p>

       <div class="card_info">
           <ul class="forum_dir_info bottom_list clearfix">
                                  <li>
                                          </li>
                   <li>
                       <span class="dir_text">目录：</span>
                   </li>
                   <li>
                                                  <a rel="noreferrer" target="_blank"
                              href="/f/fdir?fd=电视剧&ie=utf-8&sd=美剧">美剧</a>
                                          </li>
                          </ul>
       </div>
   </div>
</div>
<div id="pagelet_frs-header/pagelet/head_content_middle"></div><div id="pagelet_navigation/pagelet/navigation"></div><div id="pagelet_frs-header/pagelet/head_content_bottom"></div>    </div>
</div>
--></code><script>Bigpipe.register("frs-header/pagelet/head", {"parent":"","scripts":["\/tb\/_\/head_main_c294af5.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/loader_12d7714.js","\/tb\/_\/game_head_info_2bba44c.js","\/tb\/_\/http_transform_d9b1cbd.js","\/tb\/_\/preview_e43ce97.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/base_dialog_user_bar_ea71e42.js","\/tb\/_\/qianbao_cashier_dialog_5247354.js","\/tb\/_\/qianbao_purchase_tdou_81a2c40.js","\/tb\/_\/show_dialog_d46d0a5.js","\/tb\/_\/payment_dialog_title_3e773b9.js","\/tb\/_\/tdou_get_99d9a78.js","\/tb\/_\/rsa_safe_299a966.js","\/tb\/_\/paykey_safe_payment_37d2c7b.js","\/tb\/_\/captcha_57d747c.js","\/tb\/_\/captcha_dialog_ceaacd2.js","\/tb\/_\/captcha_safe_payment_7f700b4.js","\/tb\/_\/mobile_safe_payment_5c23e71.js","\/tb\/_\/tbean_safe_3668241.js","\/tb\/_\/tbean_safe_ajax_5dbae2e.js","\/tb\/_\/tdou_data_747c462.js","\/tb\/_\/umoney_1379f71.js","\/tb\/_\/tdou_template_8d6b3f6.js","\/tb\/_\/tdou_builder_05101dd.js","\/tb\/_\/tdou_view_operation_bootstrap_7f5fd6b.js","\/tb\/_\/tdou_view_cashier_6afe462.js","\/tb\/_\/tdou_open_type_a72e1ed.js","\/tb\/_\/tdou_view_util_d282db0.js","\/tb\/_\/tdou_view_auto_redirect_c5d928c.js","\/tb\/_\/umoney_query_e6ef23a.js","\/tb\/_\/tdou_view_check_f11908d.js","\/tb\/_\/tdou_counter_cbe5c8a.js","\/tb\/_\/tdou_view_fec0b7b.js","\/tb\/_\/tdou_3289666.js","\/tb\/_\/tcharge_dialog_1cd4f09.js","\/tb\/_\/qianbao_purchase_member_efbbe6b.js","\/tb\/_\/cashier_dialog_d52cf7c.js","\/tb\/_\/pay_member_c57f92d.js","\/tb\/_\/tdou_view_pay_ff7307f.js","\/tb\/_\/send_gift_success_44f81c6.js","\/tb\/_\/gift_page_ctrl_1c87a1c.js","\/tb\/_\/gift_loading_css_1eb1d70.js","\/tb\/_\/send_gift_dialog_44902d3.js","\/tb\/_\/raking_gift_dialog_c9e92e9.js","\/tb\/_\/gift_batou_goin_71900f5.js"],"styles":["\/tb\/_\/head_main_6892579.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/game_head_info_765f80b.css","\/tb\/_\/forum_card_62fcc00.css","\/tb\/_\/http_transform_d41d8cd.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/base_dialog_user_bar_da68a26.css","\/tb\/_\/qianbao_cashier_dialog_c1e313a.css","\/tb\/_\/qianbao_purchase_tdou_4b31f54.css","\/tb\/_\/payment_dialog_title_5433211.css","\/tb\/_\/tdou_get_a4d3fd4.css","\/tb\/_\/paykey_safe_payment_8f2a8db.css","\/tb\/_\/captcha_8dce960.css","\/tb\/_\/captcha_safe_payment_d41d8cd.css","\/tb\/_\/mobile_safe_payment_8c5a3b9.css","\/tb\/_\/tbean_safe_3c779a3.css","\/tb\/_\/tbean_safe_ajax_d41d8cd.css","\/tb\/_\/umoney_f12b09a.css","\/tb\/_\/tdou_template_f7dd2ac.css","\/tb\/_\/umoney_query_b5c3dca.css","\/tb\/_\/tdou_d41d8cd.css","\/tb\/_\/qianbao_purchase_member_d190d50.css","\/tb\/_\/cashier_dialog_0390325.css","\/tb\/_\/pay_member_d41d8cd.css","\/tb\/_\/send_gift_success_24ee666.css","\/tb\/_\/gift_page_ctrl_eac352f.css","\/tb\/_\/gift_loading_css_e2c23e9.css","\/tb\/_\/send_gift_dialog_0b498fd.css","\/tb\/_\/raking_gift_dialog_da61760.css","\/tb\/_\/gift_batou_goin_d46b5b1.css"]}).then(function(pagelet){    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.use('tbui/widget/httpTransform', [], function () {
    });
_.Module.use('tbui/widget/preview', [], function(){});
    _.Module.use('encourage-blue/widget/gift_batou_goin', {
        $container: '.gift-goin',
    });
    _.Module.use('frs-header/widget/head_main', [{
        kw: "始祖家族",
        source: ""
    }], function () {
    });
});</script><code class="pagelet_html" id="pagelet_html_frs-footer/pagelet/extension" style="display:none;"><!--













<div class="firework-wrap">
    <a class="j-firework-sender firework-sender"  locate="放烟花入口#放烟花统计"></a>
</div>
<div class="firework-wrap2">
    <div class="firework-main-wrap">
        <div class="firework-countdown"></div>
        <div class="firework-notice"></div>
        <div class="firework-list"></div>
    </div> 
</div>





<div id="global_notice_wrap" class="global_notice_wrap"></div>









<div id="pagelet_platform-official/pagelet/official_extension"></div>
--></code><script>Bigpipe.register("frs-footer/pagelet/extension", {"parent":"","scripts":["\/tb\/_\/preview_e43ce97.js","\/tb\/_\/tb_skin_1cfab79.js","\/tb\/_\/frs-footer\/frs_from_guide_55b4caa.js","\/tb\/_\/bubble_tip_8091dc2.js","\/tb\/_\/tbcopy_0deb361.js","\/tb\/_\/tbshare_share_f216378.js","\/tb\/_\/tbshare_popup_a9745dd.js","\/tb\/_\/aside_float_bar_121fac3.js","\/tb\/_\/frs-footer\/aside_float_btns_f53982c.js","\/tb\/_\/verify_manager_phone_cba5a4d.js","\/tb\/_\/inform_manager_verify_phone_f5289a5.js","\/tb\/_\/detect_manager_block_3e52a76.js","\/tb\/_\/card_a7ea147.js","\/tb\/_\/icon_tip_925c28b.js","\/tb\/_\/umoney_query_e6ef23a.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/base_dialog_user_bar_ea71e42.js","\/tb\/_\/qianbao_cashier_dialog_5247354.js","\/tb\/_\/qianbao_purchase_tdou_81a2c40.js","\/tb\/_\/tdou_open_type_a72e1ed.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/tdou_template_8d6b3f6.js","\/tb\/_\/tdou_builder_05101dd.js","\/tb\/_\/tdou_view_util_d282db0.js","\/tb\/_\/rsa_safe_299a966.js","\/tb\/_\/paykey_safe_payment_37d2c7b.js","\/tb\/_\/captcha_57d747c.js","\/tb\/_\/captcha_dialog_ceaacd2.js","\/tb\/_\/captcha_safe_payment_7f700b4.js","\/tb\/_\/mobile_safe_payment_5c23e71.js","\/tb\/_\/tbean_safe_3668241.js","\/tb\/_\/tbean_safe_ajax_5dbae2e.js","\/tb\/_\/tdou_data_747c462.js","\/tb\/_\/tdou_view_check_f11908d.js","\/tb\/_\/tdou_counter_cbe5c8a.js","\/tb\/_\/tdou_view_fec0b7b.js","\/tb\/_\/qianbao_purchase_member_efbbe6b.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/cashier_dialog_d52cf7c.js","\/tb\/_\/pay_member_c57f92d.js","\/tb\/_\/umoney_1379f71.js","\/tb\/_\/tdou_view_operation_bootstrap_7f5fd6b.js","\/tb\/_\/tdou_view_cashier_6afe462.js","\/tb\/_\/tdou_view_auto_redirect_c5d928c.js","\/tb\/_\/tdou_view_pay_ff7307f.js","\/tb\/_\/firework_v2_43f8946.js","\/tb\/_\/show_dialog_d46d0a5.js","\/tb\/_\/payment_dialog_title_3e773b9.js","\/tb\/_\/tdou_get_99d9a78.js","\/tb\/_\/tdou_3289666.js","\/tb\/_\/tcharge_dialog_1cd4f09.js","\/tb\/_\/novel_icons_5f06004.js","\/tb\/_\/global_notice_8f03246.js","\/tb\/_\/pay_util_e0a3684.js","\/tb\/_\/umoney_promotion_dialog_0174dae.js","\/tb\/_\/snowflow_6f0903a.js","\/tb\/_\/join_vip_dialog_9242ef7.js","\/tb\/_\/dialog_d31c70c.js","\/tb\/_\/util_fdb7481.js","\/tb\/_\/cont_sign_card_641fc4e.js","\/tb\/_\/net_proxy_f5ecab7.js","\/tb\/_\/use_controller_e92bca8.js","\/tb\/_\/buy_controller_516c900.js","\/tb\/_\/tieba_sign_card_f938fb7.js","\/tb\/_\/loader_12d7714.js"],"styles":["\/tb\/_\/frs-footer\/extension_d41d8cd.css","\/tb\/_\/bubble_tip_8f22754.css","\/tb\/_\/tbshare_share_99dc1ff.css","\/tb\/_\/tbshare_popup_d41d8cd.css","\/tb\/_\/aside_float_bar_6249cd0.css","\/tb\/_\/verify_manager_phone_7d1435e.css","\/tb\/_\/card_e028cbd.css","\/tb\/_\/icon_tip_db299f2.css","\/tb\/_\/umoney_query_b5c3dca.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/base_dialog_user_bar_da68a26.css","\/tb\/_\/qianbao_cashier_dialog_c1e313a.css","\/tb\/_\/qianbao_purchase_tdou_4b31f54.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/tdou_template_f7dd2ac.css","\/tb\/_\/paykey_safe_payment_8f2a8db.css","\/tb\/_\/captcha_8dce960.css","\/tb\/_\/captcha_safe_payment_d41d8cd.css","\/tb\/_\/mobile_safe_payment_8c5a3b9.css","\/tb\/_\/tbean_safe_3c779a3.css","\/tb\/_\/tbean_safe_ajax_d41d8cd.css","\/tb\/_\/qianbao_purchase_member_d190d50.css","\/tb\/_\/cashier_dialog_0390325.css","\/tb\/_\/pay_member_d41d8cd.css","\/tb\/_\/umoney_f12b09a.css","\/tb\/_\/firework_v2_2e35f90.css","\/tb\/_\/payment_dialog_title_5433211.css","\/tb\/_\/tdou_get_a4d3fd4.css","\/tb\/_\/tdou_d41d8cd.css","\/tb\/_\/novel_icons_02ab048.css","\/tb\/_\/global_notice_8c177cf.css","\/tb\/_\/umoney_promotion_dialog_a2d7347.css","\/tb\/_\/snowflow_45a89bb.css","\/tb\/_\/dialog_6ed86bb.css","\/tb\/_\/cont_sign_card_73a332e.css","\/tb\/_\/buy_controller_a328148.css","\/tb\/_\/tieba_sign_card_2928c29.css"]}).then(function(pagelet){_.Module.use('tbui/widget/preview', [], function(){});
_.Module.use('tbui/widget/tb_skin', [
	"normal",
	'20130803'
]);
	_.Module.use("frs-footer/widget/frs_from_guide");
	_.Module.use('frs-footer/widget/aside_float_btns', [{
        isBottle: 0,
        isNewBottle: 0,
        bottleTid: ""    }]);
    _.Module.use('ueglib/widget/inform_manager_verifyPhone', [
        false,
        false,
        false    ]);
    _.Module.use('ueglib/widget/detect_manager_block', [], function (moduleInstance) {
        moduleInstance.setBlockState(false);
    });
    _.Module.use('user/widget/icon_tip',{
        myIcons:[] ,
        pagelet: pagelet
        });
_.Module.use('encourage-base/widget/firework_v2', [{
    fireworks: null}], function(){});
_.Module.use('encourage-base/widget/global_notice', [{
    scores: [],
    level : [],
    fireworkOptionsConf: "",
    isFireworkV2: "1"
}], function(){});
    _.Module.use('yunying/widget/snowflow', [{
            content: '始祖家族',
            page: 'frs',
            snowflowImg: '',
            snowflowUrl: ''
        }]
    );
    _.Module.use('encourage-props/widget/tieba_sign_card',[{
        superboy: []    }]);
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
});</script><code class="pagelet_html" id="pagelet_html_frs-list/pagelet/content" style="display:none;"><!--<div id="pagelet_frs-list/pagelet/thread"></div>--></code><script>Bigpipe.register("frs-list/pagelet/content", {"parent":"frs-base\/pagelet\/content","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/aside" style="display:none;"><!--<div id="pagelet_frs-aside/pagelet/normal_aside"></div>--></code><script>Bigpipe.register("frs-aside/pagelet/aside", {"parent":"frs-base\/pagelet\/content","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_poster/pagelet/rich_poster" style="display:none;"><!--




<a name="sub"></a>
<div id="tb_rich_poster_container" class="tb_rich_poster_container">
    <div id="rich_ueditor_tpl">
        <div id="tb_rich_poster" class="tb_rich_poster">
            <div class="j_bubble_container"></div>

            
                        <div class="poster_head clearfix">
                <div class="poster_head_text">
                                            <a class="add_thread_btn post_head_btn cur" title="发表新贴" href="javascript:;"><span  class="post_head_btn_icon post_head_btn_icon_post"></span>发表新贴</a>

                        

                        
                                                <a class="add_vote_btn post_head_btn" title="发起投票" target="_blank" href="/newvote/createvote?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8"><span  class="post_head_btn_icon post_head_btn_icon_vote"></span>发起投票</a>

                        
                    
                </div>

                                <div class="poster_head_surveillance j_surveillance">
                    发贴请遵守 <a href="/tb/eula.html" target="_blank" onclick="$.stats.track('post_agreement', 'poster')">贴吧协议及“七条底线”</a>
					<a href="javascript:;" id="frs_footer_tieba_report" class="btn_tousu fr post_head_tousu" data-checkun="un">贴吧投诉</a>                    <button type="button" class="poster_disable_float j_disable_float" title="停止浮动">停止浮动</button>
                </div>
            </div>
            
                        







			<div class="poster_body editor_wrapper">
                                <div class="poster_component title_container">
                    <div class="poster_title">标&nbsp;&nbsp;题:</div>
                    <div class="j_title_wrap">
                        <input type="text" class="editor_textfield editor_title ui_textfield j_title j_topic_sug_input" name="title" autocomplete="off" />
                        <span class="topic_add_btn j_topic_add_btn"></span>
                        <p class="fullscreen-word-limit"><span class="fullscreen-limit j-fullscreen-wl">0</span>/30</p>
                    </div>
                    <div class="poster_error j_error"></div>
                </div>
                
                
                                <div class="poster_component editor_content_wrapper ueditor_container">
                    <div class="poster_reply">内&nbsp;&nbsp;容:</div>
                    <div class="old_style_wrapper">
                        <div id="ueditor_replace" style="width: 700px; height: 220px;"></div>
                    </div>
                    <div class="poster_error j_error"></div>
                </div>

                                <div class="j_poster_share poster_share">
                    <label><input type="checkbox" class="j_use_share"/> 发表后自动分享本贴</label>
                </div>

                                <div class="j_poster_signature poster_signature">
                    <label><input type="checkbox" class="j_use_signature"/> 使用签名档</label>&nbsp;
                    <span class="j_signature_wrapper signature_wrapper">
                        <select name="sign_id" class='j_sign_id'>

                        </select>
                        &nbsp;<a style="color:#0449BE" target="_blank" href="/i/sys/jump?type=signsetting">查看全部</a>
                    </span>
                </div>

                
                
                                <div class="poster_component editor_bottom_panel clearfix">
                    <div class="j_floating">
                        <button class="btn_default btn_middle j_submit poster_submit" title="Ctrl+Enter快捷发表">
                            发 表
                        </button>
                        <span class="poster_posting_status j_posting_status"></span>

                        <div class="poster_draft_status j_draft" style="display: none;">
                            <span class="j_content"></span>
                            <span title="清空草稿" class="poster_draft_delete j_clear"></span>
                        </div>
                        <button class="btn_sub btn_middle j_clear_fullscreen poster_clear_fullscreen" title="">
                            退 出
                        </button>
                    </div>
                </div>

            </div>


            
                                </div>
    </div>
</div>
--></code><script>Bigpipe.register("poster/pagelet/rich_poster", {"parent":"frs-footer\/pagelet\/content_footer","scripts":["\/tb\/_\/poster\/rich_poster_af27300.js","\/tb\/_\/placeholder_fd56d8e.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/show_dialog_d46d0a5.js","\/tb\/_\/sms_verify_dialog_cb7b503.js","\/tb\/_\/forbidden_ea6d3fd.js","\/tb\/_\/poster\/poster_context_af70d7c.js","\/tb\/_\/snowflow_6f0903a.js","\/tb\/_\/tdou_open_type_a72e1ed.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/base_dialog_user_bar_ea71e42.js","\/tb\/_\/qianbao_cashier_dialog_5247354.js","\/tb\/_\/qianbao_purchase_member_efbbe6b.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/cashier_dialog_d52cf7c.js","\/tb\/_\/pay_member_c57f92d.js","\/tb\/_\/poster\/post_signature_29deca7.js","\/tb\/_\/poster\/mouse_pwd_355b0e7.js","\/tb\/_\/tbcopy_0deb361.js","\/tb\/_\/tbshare_share_f216378.js","\/tb\/_\/poster\/share_thread_c8aa28c.js","\/tb\/_\/poster\/jiyan_service_2327c7f.js","\/tb\/_\/poster\/bsk_service_c6680a4.js","\/tb\/_\/poster\/params_xss_handler_2083372.js","\/tb\/_\/rsa_safe_299a966.js","\/tb\/_\/paykey_safe_payment_37d2c7b.js","\/tb\/_\/captcha_57d747c.js","\/tb\/_\/captcha_dialog_ceaacd2.js","\/tb\/_\/captcha_safe_payment_7f700b4.js","\/tb\/_\/mobile_safe_payment_5c23e71.js","\/tb\/_\/tbean_safe_3668241.js","\/tb\/_\/qianbao_purchase_tdou_81a2c40.js","\/tb\/_\/payment_dialog_title_3e773b9.js","\/tb\/_\/tdou_get_99d9a78.js","\/tb\/_\/tbean_safe_ajax_5dbae2e.js","\/tb\/_\/tdou_data_747c462.js","\/tb\/_\/umoney_1379f71.js","\/tb\/_\/tdou_template_8d6b3f6.js","\/tb\/_\/tdou_builder_05101dd.js","\/tb\/_\/tdou_view_operation_bootstrap_7f5fd6b.js","\/tb\/_\/tdou_view_cashier_6afe462.js","\/tb\/_\/tdou_view_util_d282db0.js","\/tb\/_\/tdou_view_auto_redirect_c5d928c.js","\/tb\/_\/umoney_query_e6ef23a.js","\/tb\/_\/tdou_view_check_f11908d.js","\/tb\/_\/tdou_counter_cbe5c8a.js","\/tb\/_\/tdou_view_fec0b7b.js","\/tb\/_\/tdou_3289666.js","\/tb\/_\/tcharge_dialog_1cd4f09.js","\/tb\/_\/tool_696c6e8.js","\/tb\/_\/loader_12d7714.js","\/tb\/_\/tpl_async_15_395293f.js","\/tb\/_\/loader_630632a.js","\/tb\/_\/like_tip_4f71dda.js","\/tb\/_\/poster\/post_service_171be80.js","\/tb\/_\/poster\/topic_suggestion_4827396.js","\/tb\/_\/poster\/post_prefix_50ae20e.js","\/tb\/_\/word_limit_47b28de.js","\/tb\/_\/poster\/post_manager_968b3bd.js","\/tb\/_\/complaint_bar_owner_5356b96.js","\/tb\/_\/bubble_tip_8091dc2.js","\/tb\/_\/poster\/rich_poster_a480e11.js","\/tb\/_\/ueditor_base_634b3f5.js","\/tb\/_\/ueditor_extend_base_29960fa.js","\/tb\/_\/background_5c34c50.js","\/tb\/_\/auto_link_e48bd2b.js","\/tb\/_\/tb_gram_a17c017.js","\/tb\/_\/slide_select_cdc6bf0.js","\/tb\/_\/image_flash_editor_96f9f79.js","\/tb\/_\/scroll_panel_0150f9a.js","\/tb\/_\/image_exif_285bafe.js","\/tb\/_\/image_uploader_3de9609.js","\/tb\/_\/image_uploader_manager_5464722.js","\/tb\/_\/picture_uploader_3ea0841.js","\/tb\/_\/picture_selector_5b9d2c7.js","\/tb\/_\/picture_web_selector_0035b16.js","\/tb\/_\/picture_214d3ba.js","\/tb\/_\/custom_emotion_24326d5.js","\/tb\/_\/ueditor_emotion_ad18456.js","\/tb\/_\/emotion_4add196.js","\/tb\/_\/ueditor_video_28e14c1.js","\/tb\/_\/video_1d31e34.js","\/tb\/_\/sketchpad_0ea952f.js","\/tb\/_\/scrawl_0005979.js","\/tb\/_\/jquery_caret_a83afb9.js","\/tb\/_\/ueditor_topic_e81e6a5.js","\/tb\/_\/topic_09c6508.js","\/tb\/_\/topic_suggestion_9bb3805.js","\/tb\/_\/fullscreen_9b3dd34.js","\/tb\/_\/height_limit_e4b1ffa.js","\/tb\/_\/draft_91a3223.js","\/tb\/_\/at_68fdde7.js","\/tb\/_\/counter_d482e1c.js","\/tb\/_\/word_limit_0f6ca1b.js","\/tb\/_\/join_vip_dialog_9242ef7.js","\/tb\/_\/props_data_2514f70.js","\/tb\/_\/bubble_factory_279ffe5.js","\/tb\/_\/post_setting_0ce6f36.js","\/tb\/_\/setting_f184c24.js","\/tb\/_\/pay_util_e0a3684.js","\/tb\/_\/medal_549f6f1.js","\/tb\/_\/paypost_data_70c1ba1.js","\/tb\/_\/paypost_agree_dialog_a4c48b3.js","\/tb\/_\/paypost_editor_7d000d4.js","\/tb\/_\/paypost_867d76a.js"],"styles":["\/tb\/_\/poster\/rich_poster_20b1f62.css","\/tb\/_\/placeholder_7eb7ce6.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/sms_verify_dialog_cd843b0.css","\/tb\/_\/forbidden_752e552.css","\/tb\/_\/snowflow_45a89bb.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/base_dialog_user_bar_da68a26.css","\/tb\/_\/qianbao_cashier_dialog_c1e313a.css","\/tb\/_\/qianbao_purchase_member_d190d50.css","\/tb\/_\/cashier_dialog_0390325.css","\/tb\/_\/pay_member_d41d8cd.css","\/tb\/_\/tbshare_share_99dc1ff.css","\/tb\/_\/poster\/share_thread_cbacfa9.css","\/tb\/_\/paykey_safe_payment_8f2a8db.css","\/tb\/_\/captcha_8dce960.css","\/tb\/_\/captcha_safe_payment_d41d8cd.css","\/tb\/_\/mobile_safe_payment_8c5a3b9.css","\/tb\/_\/tbean_safe_3c779a3.css","\/tb\/_\/qianbao_purchase_tdou_4b31f54.css","\/tb\/_\/payment_dialog_title_5433211.css","\/tb\/_\/tdou_get_a4d3fd4.css","\/tb\/_\/tbean_safe_ajax_d41d8cd.css","\/tb\/_\/umoney_f12b09a.css","\/tb\/_\/tdou_template_f7dd2ac.css","\/tb\/_\/umoney_query_b5c3dca.css","\/tb\/_\/tdou_d41d8cd.css","\/tb\/_\/like_tip_65eb23b.css","\/tb\/_\/poster\/topic_suggestion_f8eb4d2.css","\/tb\/_\/word_limit_3c5481d.css","\/tb\/_\/complaint_bar_owner_a993083.css","\/tb\/_\/bubble_tip_8f22754.css","\/tb\/_\/poster\/rich_poster_681aa2c.css","\/tb\/_\/ueditor_base_1d8237b.css","\/tb\/_\/ueditor_extend_base_d41d8cd.css","\/tb\/_\/background_c5ba91f.css","\/tb\/_\/tb_gram_d41d8cd.css","\/tb\/_\/slide_select_9a5a934.css","\/tb\/_\/image_flash_editor_8f43e09.css","\/tb\/_\/scroll_panel_eb74727.css","\/tb\/_\/picture_uploader_410491b.css","\/tb\/_\/picture_web_selector_e779653.css","\/tb\/_\/picture_ccc8af7.css","\/tb\/_\/custom_emotion_2d0490a.css","\/tb\/_\/ueditor_emotion_a5eeac8.css","\/tb\/_\/ueditor_video_1453a78.css","\/tb\/_\/sketchpad_fad481d.css","\/tb\/_\/scrawl_5840a35.css","\/tb\/_\/ueditor_topic_bb19767.css","\/tb\/_\/topic_suggestion_3234253.css","\/tb\/_\/fullscreen_a139ec1.css","\/tb\/_\/at_d03b8c9.css","\/tb\/_\/post_setting_46ea748.css","\/tb\/_\/setting_ca19f87.css","\/tb\/_\/medal_5022a4b.css","\/tb\/_\/paypost_agree_dialog_fd57709.css","\/tb\/_\/paypost_editor_6d704da.css"]}).then(function(pagelet){if (!window.PosterContext) {
_.Module.use('poster/widget/poster_context', [{
    blockInfo: {
        is_block : 0,
        block_reason:'',
        opgroup : '',
        days_tofree:0,
        block_errno: '0'
    }
}], function() {
    PosterContext.loadContextFromPageData($.extend({},PageData,{
        user:{
                        id: PageData.user.id,
            name: PageData.user.name,
            level: 1,
            isFavorForum: 0,
            isLogin: !!PageData.user.is_login,
            isBlocked: 0,
            isBlack: 0,
            noUsername: !!PageData.user.no_un,
            canPost: 0,
            canVote: 0,
            forbidFlag: 0,
            signNumber: 0,
            superboy: "",
            memberLevel: 0        }
    }));
    PosterContext.loadAuthorities({"img_num":100,"video_num":1,"smiley_num":100,"white_list":["http:\/\/www.tudou.com\/","http:\/\/v.blog.sohu.com\/","http:\/\/tv.sohu.com\/","http:\/\/share.vrs.sohu.com\/","http:\/\/my.tv.sohu.com\/","http:\/\/player.56.com\/","http:\/\/www.56.com\/","http:\/\/kankanews.com\/","http:\/\/video6.smgbb.cn\/","http:\/\/www.youku.com\/","http:\/\/player.youku.com\/","http:\/\/static.youku.com\/","http:\/\/www.ku6.com\/","http:\/\/player.ku6.com\/","http:\/\/video.sina.com.cn\/","http:\/\/vhead.blog.sina.com.cn\/","http:\/\/you.video.sina.com.cn\/","http:\/\/video.qq.com\/","http:\/\/www.baidu.com\/","http:\/\/box.baidu.com\/","http:\/\/hi.baidu.com\/","http:\/\/mv.baidu.com\/","http:\/\/mvimg.baidu.com\/","http:\/\/mvideo.baidu.com\/","http:\/\/player.cntv.cn\/","http:\/\/player.xiyou.cntv.cn\/","http:\/\/www.yinyuetai.com\/","http:\/\/player.yinyuetai.com\/","http:\/\/www.aipai.com\/","http:\/\/www.cutv.com\/","http:\/\/player.cutv.com\/","http:\/\/www.pptv.com\/","http:\/\/v.pptv.com\/","http:\/\/www.letv.com\/","http:\/\/www.iqiyi.com\/","http:\/\/yule.iqiyi.com\/","http:\/\/player.video.qiyi.com\/","http:\/\/www.ifeng.com\/","http:\/\/s.v.ifeng.com\/","http:\/\/v.ifeng.com\/","http:\/\/www.m1905.com\/","http:\/\/www.joy.cn\/","http:\/\/client.joy.cn\/","http:\/\/www.molihe.com\/","http:\/\/mv.molihe.com\/","http:\/\/swf.molihe.com\/","http:\/\/www.baomihua.com\/","http:\/\/video.baomihua.com\/","http:\/\/www.ouou.com\/","http:\/\/flash.ouou.com\/","http:\/\/dv.ouou.com\/","http:\/\/misc.home.news.cn\/","http:\/\/www.news.cn\/","http:\/\/www.wasu.cn\/","http:\/\/play1.wasu.cn\/","http:\/\/play.wasu.cn\/","http:\/\/v.iask.com\/","http:\/\/i7.imgs.letv.com\/","http:\/\/static.video.qq.com\/","http:\/\/player.pptv.com\/","http:\/\/v.pps.tv\/","http:\/\/ipd.pps.tv\/","http:\/\/www.funshion.com\/","http:\/\/player.pps.tv\/","http:\/\/api.funshion.com\/","http:\/\/www.hunantv.com\/","http:\/\/video.brtn.cn","http:\/\/news.brtn.cn\/","http:\/\/life.brtn.cn\/","http:\/\/mil.brtn.cn\/","http:\/\/finance.brtn.cn\/","http:\/\/btv.brtn.cn\/","http:\/\/host.brtn.cn\/","http:\/\/zmbj.brtn.cn\/","http:\/\/www.brtn.cn\/","http:\/\/ent.brtn.cn\/","http:\/\/sports.brtn.cn\/","http:\/\/legal.brtn.cn\/","http:\/\/tv.brtn.cn\/","http:\/\/iptv.brtn.cn\/","http:\/\/yst.brtn.cn\/","http:\/\/pxgw.brtn.cn\/","http:\/\/zcmx.brtn.cn\/","http:\/\/zhanbo.brtn.cn\/","http:\/\/app.brtn.cn\/","http:\/\/search.brtn.cn\/","http:\/\/itv.brtn.cn\/","http:\/\/www.meipai.com\/","http:\/\/www.acfun.tv\/","https:\/\/ssl.acfun.tv\/","http:\/\/m.acfun.tv\/","http:\/\/www.bilibili.com\/","http:\/\/share.acg.tv\/","http:\/\/static.hdslb.com\/","http:\/\/bangumi.bilibili.com"],"is_readonly":0,"can_local_upload":null,"paypost":"","music_num":10,"attachment_num":5,"attachment_size":209715200,"long_editor":false,"float_editor":"","custom_emotion":false,"emotion_transform":false,"tb_gram":false,"formula_editor":""});
});
}
	_.Module.use('ueditor/widget/ueditor_base');
_.Module.use('ueditor/widget/ueditor_extend_base');
_.Module.use('ueditor/widget/background', [UE, EditorUI]);
_.Module.use('ueditor/widget/auto_link', [UE, EditorUI]);
_.Module.use('ueditor/widget/picture', [UE, EditorUI, {
	props: {
		'103':[]	}
}]);
_.Module.use('ueditor/widget/emotion', [UE, EditorUI]);
_.Module.use('ueditor/widget/video', [UE, EditorUI, {
	is_video_pgc_user: 0}]);
_.Module.use('ueditor/widget/scrawl', [UE, EditorUI]);
        _.Module.use('ueditor/widget/jquery_caret');
    _.Module.use('ueditor/widget/topic', [UE, EditorUI]);
_.Module.use('ueditor/widget/topic_suggestion', [UE, EditorUI]);
    _.Module.use('ueditor/widget/fullscreen', [UE, EditorUI]);
_.Module.use('ueditor/widget/height_limit', [UE, EditorUI]);
_.Module.use('ueditor/widget/draft', [UE, EditorUI]);
_.Module.use('ueditor/widget/at', [UE, EditorUI]);
_.Module.use('ueditor/widget/counter', [UE, EditorUI]);
_.Module.use('ueditor/widget/word_limit', [UE, EditorUI]);
_.Module.use('encourage-thread/widget/setting', [UE, EditorUI, {
	scores: [],
	level : []}]);
_.Module.use('encourage-thread/widget/medal', [UE, EditorUI, {
	defaultBubble: [],
	level: 0}]);
_.Module.use('encourage-thread/widget/paypost', [UE, EditorUI, {
    isPaypost		: 0, 
    needPaypostAgree: !0}]);
_.Module.use("poster/widget/rich_poster", {
    prefix: undefined,
    hotTopic: '',//传递后台抓取话题
    // placeholder: '',
    feedback:'<p>温馨提示：反馈bug、帐号异常或删贴问题时，请提供文字形式的问题帐号（非截图）、问题发生的时间，并尽可能上传截图，以上信息有助于贴吧更好的解决您的问题。<\/p>',
    QinglangData: {"qingLangExtType":"","title":"","content":""},
    user: {
        memberLevel : 0,
        user_nickname: ''
    },
    blockInfo: {
        is_block : 0,
        block_reason:'',
        opgroup : '',
        days_tofree:0,
    },
    snowflow: {
        img : '',
        url : ''
    },
    pagelet: pagelet,
    initPage: 'frs'
});
});</script><code class="pagelet_html" id="pagelet_html_forum/pagelet/focus_btn" style="display:none;"><!--
<a rel="noreferrer" href="#" onclick="return false"
   class="focus_btn islike_focus" id="j_head_focus_btn"
   style="margin-top:2px;"></a>
--></code><script>Bigpipe.register("forum/pagelet/focus_btn", {"parent":"frs-header\/pagelet\/head","scripts":["\/tb\/_\/focus_btn_9db672d.js","\/tb\/_\/tool_696c6e8.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/loader_12d7714.js","\/tb\/_\/tpl_async_15_395293f.js","\/tb\/_\/loader_630632a.js","\/tb\/_\/like_tip_4f71dda.js","\/tb\/_\/attention_category_game_5978a17.js","\/tb\/_\/focus_btn_bb15d87.js"],"styles":["\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/like_tip_65eb23b.css","\/tb\/_\/attention_category_game_d2d4220.css","\/tb\/_\/focus_btn_21ad291.css"]}).then(function(pagelet){    _.Module.use('forum/widget/focus_btn', [{
        'islike': '0',
        'levelId': '1',
        'levelName': '',
        'userLevel': null,
        'isCategoryOfGame': true,
        'firstClass': '电视剧',
        'forumVdir': null,
        'isBawu': null    }]);
    _.Module.use('forum/pagelet/focus_btn', [pagelet], function () {});
});</script><code class="pagelet_html" id="pagelet_html_frs-header/pagelet/head_content_middle" style="display:none;"><!--


<div class="game_frs_in_head">
    </div>
<div id="pagelet_platform-official/pagelet/official_head_block"></div><div id="pagelet_entertainment-liveshow/pagelet/lecai_head"></div><div id="pagelet_entertainment-liveshow/pagelet/video_head"></div>--></code><script>Bigpipe.register("frs-header/pagelet/head_content_middle", {"parent":"frs-header\/pagelet\/head","scripts":["\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/loader_12d7714.js","\/tb\/_\/scroll_panel_0150f9a.js","\/tb\/_\/game_rank_in_head_a46e35a.js","\/tb\/_\/game_frs_head_b792766.js"],"styles":["\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/game_frs_in_head_8026069.css","\/tb\/_\/scroll_panel_eb74727.css","\/tb\/_\/game_rank_in_head_94ba4ce.css","\/tb\/_\/game_frs_head_218209e.css"]}).then(function(pagelet){    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
});</script><code class="pagelet_html" id="pagelet_html_navigation/pagelet/navigation" style="display:none;"><!--<div class="nav_wrap " id="tb_nav">
        <ul class="nav_list j_nav_list">
                                <li class=" focus j_tbnav_tab " data-tab-main>
    <a href="/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8" class="j_nav_local_tab_link j_tbnav_tab_a" id="tab_forumname" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabmain">看贴</a>
</li>                                <li class=" j_tbnav_tab " data-tab-album>
    <a href="/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&tab=album" class="j_nav_local_tab_link j_tbnav_tab_a" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabfrsphotogood" frs-page="main" id="tab_picture">图片</a>
</li>                                <li class=" j_tbnav_tab " data-tab-good>
    <a href="/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&tab=good" class="j_nav_local_tab_link j_tbnav_tab_a" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabgood">精品</a>
</li>                                <li class=" j_tbnav_tab " data-tab-video>
    <a href="/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&tab=video" class="j_nav_local_tab_link j_tbnav_tab_a" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabvideo">视频</a>
</li>                                <li class=" j_tbnav_tab " data-tab-group>
    <a href="/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&tab=group" class="j_nav_local_tab_link j_tbnav_tab_a" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabgroup">群组</a>
</li>            </ul>
                            <form class="search_internal_wrap pull_right j_search_internal_forum">
                <input class="search_internal_input j_search_internal_input" value="" placeholder="吧内搜索" type="text"/>
                <button class="search_internal_btn" type="submit"/>
                <i></i></button>
            </form>
            </div>

--></code><script>Bigpipe.register("navigation/pagelet/navigation", {"parent":"frs-header\/pagelet\/head","scripts":["\/tb\/_\/navigator_b701689.js","\/tb\/_\/search_handler_26666a8.js","\/tb\/_\/tbnav_bright_2ccca48.js"],"styles":["\/tb\/_\/tbnav_bright_0afa1a2.css"]}).then(function(pagelet){    _.Module.use('navigation/widget/tbnav_bright', [
        $('#tb_nav'),
        {
            jq_search: $('#tb_nav').find('.j_search_internal_forum'),
            forumName: '始祖家族'
        },
        {
            promotion_setting: [[]]        }
    ]);
    _.Module.use('navigation/widget/navigator', [pagelet, true], function (instance) {

    });
});</script><code class="pagelet_html" id="pagelet_html_frs-header/pagelet/head_content_bottom" style="display:none;"><!----></code><script>Bigpipe.register("frs-header/pagelet/head_content_bottom", {"parent":"frs-header\/pagelet\/head","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_frs-list/pagelet/thread" style="display:none;"><!--<div id="content_leftList" class="content_leftList j-content-leftList clearfix">
    <div id="pagelet_platform-base/pagelet/professional_manager"></div><div id="pagelet_platform-thread/pagelet/platform_thread_header"></div><div id="pagelet_live/pagelet/live"></div><div id="pagelet_frs-list/pagelet/thread_list"></div><div id="pagelet_frs-list/pagelet/thread_footer"></div></div>
--></code><script>Bigpipe.register("frs-list/pagelet/thread", {"parent":"frs-list\/pagelet\/content","scripts":["\/tb\/_\/thread_631d0b6.js","\/tb\/_\/popup_zhang_8e0fca3.js"],"styles":["\/tb\/_\/top_activity_20d5624.css","\/tb\/_\/popup_zhang_434a867.css"]}).then(function(pagelet){    _.Module.use('frs-list/widget/popup_zhang', [], function () {
    });
    _.Module.use('frs-list/pagelet/thread', [pagelet], function (instance) {

    });
});</script>
<code class="pagelet_html" id="pagelet_html_platform-activity/pagelet/full_width_head" style="display:none;"><!--<div class="top_iframe" style="position:relative;z-index:9999;">
    </div>


--></code><script>Bigpipe.register("platform-activity/pagelet/full_width_head", {"parent":"frs-header\/pagelet\/head","scripts":["\/tb\/_\/full_width_head_6874452.js","\/tb\/_\/preview_e43ce97.js","\/tb\/_\/iframe_head_f52cc7a.js","\/tb\/_\/activity_btv_3cd04b8.js"],"styles":["\/tb\/_\/full_width_head_ca1a4d5.css","\/tb\/_\/iframe_head_b5db402.css","\/tb\/_\/activity_btv_2cc5469.css"]}).then(function(pagelet){_.Module.use('tbui/widget/preview', [], function(){});
    _.Module.use('platform-activity/widget/fullWidthHead', [], function(){});
});</script><code class="pagelet_html" id="pagelet_html_forum/pagelet/sign_mod" style="display:none;"><!--
    <div class="sign_mod_bright" id="sign_mod">
        
<div class="sign_tip_container">
    <div class="j_succ_info sign_succ1" style="display:none">
        <div class="sign_tip_bdwrap clearfix">
            <div class="sign_tip_bd_arr"></div>
            <div class="sign_tip_main">
                <div class="sign_succ_calendar">
                    <div class="sign_succ_calendar_title">
                        <div class="calendar_title_month clearfix">
                            <div class="calendar_month_next j_calendar_month_next">&nbsp;</div>
                            <div class="calendar_month_prev j_calendar_month_prev">&nbsp;</div>
                            <div class="calendar_month_span j_calendar_month">&nbsp;</div>
                        </div>
                    </div>
                    <table class="sign_succ_table "
                            >
                        <thead align="center">
                        <tr class="sign_succ_canlerdar_head">
                            <td>日</td>
                            <td>一</td>
                            <td>二</td>
                            <td>三</td>
                            <td>四</td>
                            <td>五</td>
                            <td>六</td>
                        </tr>
                        </thead>
                        <tbody align="center" class="sign_succ_canlerdar_days j_canlerdar_days">
                        <tr>
                            <td class="j_1_0">&nbsp;</td>
                            <td class="j_1_1">&nbsp;</td>
                            <td class="j_1_2">&nbsp;</td>
                            <td class="j_1_3">&nbsp;</td>
                            <td class="j_1_4">&nbsp;</td>
                            <td class="j_1_5">&nbsp;</td>
                            <td class="j_1_6">&nbsp;</td>
                        </tr>
                        <tr>
                            <td class="j_2_0">&nbsp;</td>
                            <td class="j_2_1">&nbsp;</td>
                            <td class="j_2_2">&nbsp;</td>
                            <td class="j_2_3">&nbsp;</td>
                            <td class="j_2_4">&nbsp;</td>
                            <td class="j_2_5">&nbsp;</td>
                            <td class="j_2_6">&nbsp;</td>
                        </tr>
                        <tr>
                            <td class="j_3_0">&nbsp;</td>
                            <td class="j_3_1">&nbsp;</td>
                            <td class="j_3_2">&nbsp;</td>
                            <td class="j_3_3">&nbsp;</td>
                            <td class="j_3_4">&nbsp;</td>
                            <td class="j_3_5">&nbsp;</td>
                            <td class="j_3_6">&nbsp;</td>
                        </tr>
                        <tr>
                            <td class="j_4_0">&nbsp;</td>
                            <td class="j_4_1">&nbsp;</td>
                            <td class="j_4_2">&nbsp;</td>
                            <td class="j_4_3">&nbsp;</td>
                            <td class="j_4_4">&nbsp;</td>
                            <td class="j_4_5">&nbsp;</td>
                            <td class="j_4_6">&nbsp;</td>
                        </tr>
                        <tr class="j_5" style="display:none">
                            <td class="j_5_0">&nbsp;</td>
                            <td class="j_5_1">&nbsp;</td>
                            <td class="j_5_2">&nbsp;</td>
                            <td class="j_5_3">&nbsp;</td>
                            <td class="j_5_4">&nbsp;</td>
                            <td class="j_5_5">&nbsp;</td>
                            <td class="j_5_6">&nbsp;</td>
                        </tr>
                        <tr class="j_6" style="display:none">
                            <td class="j_6_0">&nbsp;</td>
                            <td class="j_6_1">&nbsp;</td>
                            <td class="j_6_2">&nbsp;</td>
                            <td class="j_6_3">&nbsp;</td>
                            <td class="j_6_4">&nbsp;</td>
                            <td class="j_6_5">&nbsp;</td>
                            <td class="j_6_6">&nbsp;</td>
                        </tr>
                        </tbody>
                    </table>
                </div>

                <div class="sign_tip_boards">
                    <div class="sign_tip_board sign_tip_board_urank j_sign_ad_mobi">
                        <div class="sign_tip_board_ico"></div>
                        <p>签到排名：今日本吧第<span class="sign_index_num j_signin_index"></span>个签到，</p>

                        <p><span class="j_succ_text">本吧因你更精彩，明天继续来努力！</span></p>
                    </div>
                    <div class="sign_tip_board sign_tip_board_barrank">
                        <div class="sign_tip_board_ico"></div>
                                                    <p>本吧排名：<a rel="noreferrer" target="_blank"
                                       href="/sign/index?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8">15</a>
                            </p>
                                                <p>本吧签到人数：671</p>
                    </div>
                </div>

            </div>

            <div class="sign_tip_aside">

                                                        <div class="sign_tip_sbox sign_tip_sbox_first sign_tip_sbox_1key">
                        <div class="sign_tip_sbox_hd">一键签到</div>
                        <div class="sign_tip_sbox_bd">
                            <div class="sign_tip_sbox_cnt">
                                <a rel="noreferrer" class="sign_tip_sbox_card j_sign_tip_1key_icon sign_tip_sbox_card_pencil"
                                   href="/tbmall/tshow?tab=detail" target="_blank"></a>

                                <div class="sign_tip_sbox_txt">可签<span class="orange_text">7</span>级以上的吧<span
                                        class="orange_text">50</span>个
                                </div>
                                <div class="sign_tip_sbox_btn">
                                    <a rel="noreferrer" href="/home/main?id=00000000#stipsign" target="_blank"
                                       class="btn-sub btn-small">
                                        <b class="sign_crown sign_crown_pencil" title="无瑕的T秀勋章"></b> 一键签到
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                
                <div class="sign_tip_sbox sign_tip_sbox_fixsign">
                    <div class="sign_tip_sbox_hd sign_tip_sbox_hd_inf j_need_rpln_wrap">本月漏签<span
                            class="j_lack_sign_monthly_count sign_num">0</span>次！
                    </div>
                    <div class="sign_tip_sbox_bd">
                        <div class="sign_tip_sbox_cnt">
                            <a rel="noreferrer" href="/tbmall/propslist?category=108" class="sign_tip_sbox_card" target="_blank"><span
                                    class="sign_num"><span class="j_rpln_card_count">0</span></span></a>

                            <div class="sign_tip_sbox_txt">成为超级会员，赠送8张补签卡</div>
                            <div class="sign_tip_sbox_btn">
                                <a rel="noreferrer" href="#" class="btn-sub btn-small j_lack_sign_monthly_help"
                                   target="_blank">如何使用？</a>

                                <div class="lack_sign_monthly_tip_wrap">
                                    <div class="ui_card_wrap lack_sign_monthly_tip_card j_lack_sign_monthly_tip_card"
                                         style="display:none;">
                                        <div class="ui_card_content ">
                                            <div class="time_gift_tip">点击日历上漏签日期，即可进行<span
                                                    class="strongerText">补签</span>。
                                            </div>
                                        </div>
                                        <span class="arrow ui_white_down" style="left:48%;"></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="sign_tip_sbox sign_tip_sbox_chainsign">
                    <div class="sign_tip_sbox_hd sign_tip_sbox_hd_inf">
                        连续签到：<span class="sign_num j_sign_succ_keep"></span>天&nbsp;&nbsp;累计签到：<span
                            class="sign_num j_sign_succ_count"></span>天
                    </div>
                    <div class="sign_tip_sbox_bd">
                        <div class="sign_tip_sbox_cnt">
                            <a rel="noreferrer" href="/tbmall/propslist?category=108" class="sign_tip_sbox_card" target="_blank"><span
                                    class="sign_num"><span
                                        class="j_sign_chainsign_num">0</span></span></a>

                            <div class="sign_tip_sbox_txt">超级会员单次开通12个月以上，赠送连续签到卡3张</div>
                            <div class="sign_tip_sbox_btn"><a rel="noreferrer" href="#" class="btn-sub btn-small j_cont_sign_card"
                                                              target="_blank">使用连续签到卡</a></div>
                        </div>
                    </div>
                </div>

                <div class="sign_tip_sbox sign_tip_sbox_last sign_tip_sbox_rights">
                    <div class="sign_tip_sbox_bd j_sign_rights">
                        <div class="sign_rights_display clearfix">
                            <div class="sign_rights_icon j_sign_rights_icon rights_1"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_2"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_3"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_4"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_5"></div>
                            <span class="split_line"></span>
                            <a rel="noreferrer" href="/f/like/level?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&lv_t=lv_nav_who" class="balv_help"
                               title="签到规则" target="_blank"></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

        <div id="signstar_wrapper" class="j_sign_box sign_box_bright">
            <a rel="noreferrer" href="#" onclick="return false" data-dw="1" tabindex="3"
               title="签到"
               class="j_signbtn sign_btn_bright">
                                <span class="sign_today_date">11月05日</span>
                <span class="sign_month_lack_days">漏签<span class="j_sign_month_lack_days">0</span>天</span>
            </a>
        </div>

        
            </div>
--></code><script>Bigpipe.register("forum/pagelet/sign_mod", {"parent":"frs-header\/pagelet\/head","scripts":["\/tb\/_\/sign100_c123624.js","\/tb\/_\/sign_shai_1b5c0f0.js","\/tb\/_\/captcha_57d747c.js","\/tb\/_\/captcha_dialog_ceaacd2.js","\/tb\/_\/card_a7ea147.js","\/tb\/_\/bubble_tip_8091dc2.js","\/tb\/_\/tdou_open_type_a72e1ed.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/base_dialog_user_bar_ea71e42.js","\/tb\/_\/qianbao_cashier_dialog_5247354.js","\/tb\/_\/qianbao_purchase_member_efbbe6b.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/cashier_dialog_d52cf7c.js","\/tb\/_\/pay_member_c57f92d.js","\/tb\/_\/join_vip_dialog_9242ef7.js","\/tb\/_\/dialog_d31c70c.js","\/tb\/_\/util_fdb7481.js","\/tb\/_\/cont_sign_card_641fc4e.js","\/tb\/_\/sign_mod_701b8a7.js"],"styles":["\/tb\/_\/captcha_8dce960.css","\/tb\/_\/card_e028cbd.css","\/tb\/_\/bubble_tip_8f22754.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/base_dialog_user_bar_da68a26.css","\/tb\/_\/qianbao_cashier_dialog_c1e313a.css","\/tb\/_\/qianbao_purchase_member_d190d50.css","\/tb\/_\/cashier_dialog_0390325.css","\/tb\/_\/pay_member_d41d8cd.css","\/tb\/_\/dialog_6ed86bb.css","\/tb\/_\/cont_sign_card_73a332e.css","\/tb\/_\/sign_mod_539e18c.css","\/tb\/_\/sign_tip_98d0754.css"]}).then(function(pagelet){    _.Module.use('forum/widget/sign_mod', [$('#sign_mod'), {
        'hasClass': 1,
        'page': '',
        'isLike':0, // 是否已like本吧
        'isBlock':0, // 是否已封禁
        'isSignIn':0, // 今日是否已经签到
        'signForumInfo':{"is_on":true,"is_filter":false,"forum_info":{"forum_id":7739963,"level_1_dir_name":"\u7535\u89c6\u5267"},"current_rank_info":{"sign_count":671,"member_count":73758,"sign_rank":15,"dir_rate":"0.1"},"yesterday_rank_info":{"sign_count":1332,"member_count":73755,"sign_rank":31,"dir_rate":"0.1"},"weekly_rank_info":{"sign_count":1332,"member_count":73756,"sign_rank":30},"monthly_rank_info":{"sign_count":1321,"member_count":73761,"sign_rank":31},"level_1_dir_name":"\u7535\u89c6\u5267","level_2_dir_name":"\u7f8e\u5267"},
        'memberTitle': '',
        'memberNumber': '73758',
        'isActivitySign': '',
        'userProp': null    },
    {
        'sign_mod_tiptitle1': '签到经验奖励',
        'sign_mod_tiptitle2': '连续签到双倍经验',
        'sign_mod_tiptitle3': '加粗字体使用特权',
        'sign_mod_tiptitle4': '红色字体使用特权',
        'sign_mod_tiptitle5': '一举橙名',
        'sign_mod_tiptext1': '签到即奖励2个经验值。<br \/>手机签到额外奖励2个经验值。',
        'sign_mod_tiptext2': '连续签到奖励经验值双倍。',
        'sign_mod_tiptext3': '在本吧发贴时可以使用加粗字体。',
        'sign_mod_tiptext4': '在本吧发贴时可以使用红色字体。',
        'sign_mod_tiptext5': '在本吧用户ID橙名高亮显示。',
        'sign_mod_tipcondition1': '条件：每天点击签到后即可获得。',
        'sign_mod_tipcondition2': '条件：保持连续签到2天及以上。',
        'sign_mod_tipcondition3': '条件：连续签到10天及以上，不能中断哦',
        'sign_mod_tipcondition4': '条件：连续签到20天及以上，不能中断哦',
        'sign_mod_tipcondition5': '条件：连续签到30天及以上，不能中断哦',
        'sign_mod_card_title': '一键签到，最高<span>6倍经验！<\/span>',
        'sign_mod_card_detail': '',
        'sign_mod_card_positive_btn': '<i class=\"icon\"><\/i>客户端免费体验',
        'sign_mod_card_no_txt': '<i class=\"icon\"><\/i>会员一键签到',
    }]);
});</script><code class="pagelet_html" id="pagelet_html_forum/pagelet/forum_card_number" style="display:none;"><!--<span class="">
  <span class="card_numLabel">关注：</span>
  <span class="card_menNum">73,758</span>
  <span class="card_numLabel">贴子：</span>
  <span class="card_infoNum">442,283</span>
</span>
--></code><script>Bigpipe.register("forum/pagelet/forum_card_number", {"parent":"frs-header\/pagelet\/head","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_platform-official/pagelet/official_extension" style="display:none;"><!--

--></code><script>Bigpipe.register("platform-official/pagelet/official_extension", {"parent":"frs-footer\/pagelet\/extension","scripts":["\/tb\/_\/js_redirect_ed0cfa9.js","\/tb\/_\/platform_spread_layer_6e2b6ed.js","\/tb\/_\/platform_spread_video_d1aecb9.js"],"styles":["\/tb\/_\/platform_spread_layer_9230140.css","\/tb\/_\/platform_spread_video_846939d.css"]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/normal_aside" style="display:none;"><!--<div id="pagelet_entertainment-liveshow/pagelet/promoter_privilege_preview"></div><div id="pagelet_encourage-celebrity/pagelet/celebrity"></div><div class="aside_region app_download_box" id="">
    <h4 class="region_header clearfix">
        扫二维码下载贴吧客户端        <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
        
<div class="clearfix app_download_wrap">
	<div class="app_download_icon">
		
	</div>
	<div class="app_download_info">
		下载贴吧APP<br />看高清直播、视频！
	</div>
</div>
    </div>
    <div class="region_footer"></div>
</div>
<div class="aside_region nani_app_download_box" id="">
    <h4 class="region_header clearfix">
        扫二维码下载伙拍小视频        <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
        
<div class="clearfix app_download_wrap">
	<div class="app_download_icon">
		<img src="//tb2.bdstatic.com/tb/img/frs-aside/icon_80f56c0.png" width="75"/>
	</div>
	<div class="app_download_info">
		来伙拍小视频<br />找到伙伴，一拍即合
	</div>
</div>
    </div>
    <div class="region_footer"></div>
</div>
<div id="pagelet_encourage-tbguess/pagelet/sidebar"></div><div id="pagelet_frs-aside/pagelet/star"></div><div id="pagelet_frs-aside/pagelet/forum_info"></div><div id="pagelet_frs-aside/pagelet/zyq"></div><div id="pagelet_frs-aside/pagelet/search_back"></div><div id="pagelet_frs-aside/pagelet/hottopic"></div><div id="pagelet_frs-aside/pagelet/ad"></div>        <div id="branding_ads">
        </div>
--></code><script>Bigpipe.register("frs-aside/pagelet/normal_aside", {"parent":"frs-aside\/pagelet\/aside","scripts":["\/tb\/_\/frs-aside\/base_aside_0b0c387.js"],"styles":["\/tb\/_\/aside_region_6df4cfc.css","\/tb\/_\/frs-aside\/app_download_fa586fe.css","\/tb\/_\/frs-aside\/nani_app_download_312c759.css"]}).then(function(pagelet){    _.Module.use('frs-aside/pagelet/base_aside', {
        forumName: "\u59cb\u7956\u5bb6\u65cf",
        forumSecLvName: "\u7f8e\u5267",
        brandAdsenseSwitch: 2    });
});</script><code class="pagelet_html" id="pagelet_html_platform-official/pagelet/official_head_block" style="display:none;"><!--
--></code><script>Bigpipe.register("platform-official/pagelet/official_head_block", {"parent":"frs-header\/pagelet\/head_content_middle","scripts":["\/tb\/_\/preview_e43ce97.js"],"styles":[]}).then(function(pagelet){_.Module.use('tbui/widget/preview', [], function(){});
});</script><code class="pagelet_html" id="pagelet_html_entertainment-liveshow/pagelet/lecai_head" style="display:none;"><!----></code><script>Bigpipe.register("entertainment-liveshow/pagelet/lecai_head", {"parent":"frs-header\/pagelet\/head_content_middle","scripts":[],"styles":["\/tb\/_\/lecai_iframe_a48aee4.css"]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_entertainment-liveshow/pagelet/video_head" style="display:none;"><!----></code><script>Bigpipe.register("entertainment-liveshow/pagelet/video_head", {"parent":"frs-header\/pagelet\/head_content_middle","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_platform-base/pagelet/professional_manager" style="display:none;"><!--



--></code><script>Bigpipe.register("platform-base/pagelet/professional_manager", {"parent":"frs-list\/pagelet\/thread","scripts":["\/tb\/_\/professional_manager_tips_41b690e.js"],"styles":["\/tb\/_\/professional_manager_tips_af0267b.css","\/tb\/_\/by_forum_db9c68b.css"]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_platform-thread/pagelet/platform_thread_header" style="display:none;"><!--
--></code><script>Bigpipe.register("platform-thread/pagelet/platform_thread_header", {"parent":"frs-list\/pagelet\/thread","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_live/pagelet/live" style="display:none;"><!--<div id="pagelet_live/pagelet/live_thread"></div>--></code><script>Bigpipe.register("live/pagelet/live", {"parent":"frs-list\/pagelet\/thread","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_entertainment-liveshow/pagelet/promoter_privilege_preview" style="display:none;"><!----></code><script>Bigpipe.register("entertainment-liveshow/pagelet/promoter_privilege_preview", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_encourage-celebrity/pagelet/celebrity" style="display:none;"><!--<div class="aside_region celebrity" id="">
    <h4 class="region_header clearfix">
                <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
        <div class="intro">
    <div class="col2-left">
        <a class="gift-wrapper j-gift-buy" href="javascript:;">
            <span class="gift">
                <img src="//tb2.bdstatic.com/tb/img/single_member_100_0b51e9e.png">
            </span>
            皇冠身份
        </a>
    </div>
    <div class="col2-right">
        <ul class="privilege-list">
            <li>
                <i class="icon icon-red-thread-title"></i>
                发贴红色标题
            </li>
            <li>
                <i class="icon icon-red-name"></i>
                显示红名
            </li>
            <li>
                <i class="icon icon-sign-exp"></i>
                签到六倍经验
            </li>
        </ul>
    </div>
</div>
    <div class="more-privilege-container">
        <div class="first-show-container">
            <button class="purchase-member-btn j-gift-buy">兑换本吧会员</button>
        </div>
    </div>
    <p class="gray-text">赠送补签卡1张，获得<a href="#" class="celebrity-purchase-exp" onclick="return false" target="_blank">[经验书购买权]</a>
    </p>

    </div>
    <div class="region_footer"></div>
</div>
--></code><script>Bigpipe.register("encourage-celebrity/pagelet/celebrity", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":["\/tb\/_\/celebrity_widget_a676416.js","\/tb\/_\/celebrity_forum_dialog_dc04b7c.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/umoney_query_e6ef23a.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/base_dialog_user_bar_ea71e42.js","\/tb\/_\/qianbao_cashier_dialog_5247354.js","\/tb\/_\/qianbao_purchase_tdou_81a2c40.js","\/tb\/_\/tdou_open_type_a72e1ed.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/tdou_template_8d6b3f6.js","\/tb\/_\/tdou_builder_05101dd.js","\/tb\/_\/tdou_view_util_d282db0.js","\/tb\/_\/rsa_safe_299a966.js","\/tb\/_\/paykey_safe_payment_37d2c7b.js","\/tb\/_\/captcha_57d747c.js","\/tb\/_\/captcha_dialog_ceaacd2.js","\/tb\/_\/captcha_safe_payment_7f700b4.js","\/tb\/_\/mobile_safe_payment_5c23e71.js","\/tb\/_\/tbean_safe_3668241.js","\/tb\/_\/tbean_safe_ajax_5dbae2e.js","\/tb\/_\/tdou_data_747c462.js","\/tb\/_\/tdou_view_check_f11908d.js","\/tb\/_\/tdou_counter_cbe5c8a.js","\/tb\/_\/tdou_view_fec0b7b.js","\/tb\/_\/qianbao_purchase_member_efbbe6b.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/cashier_dialog_d52cf7c.js","\/tb\/_\/pay_member_c57f92d.js","\/tb\/_\/umoney_1379f71.js","\/tb\/_\/tdou_view_operation_bootstrap_7f5fd6b.js","\/tb\/_\/tdou_view_cashier_6afe462.js","\/tb\/_\/tdou_view_auto_redirect_c5d928c.js","\/tb\/_\/tdou_view_pay_ff7307f.js","\/tb\/_\/show_dialog_d46d0a5.js","\/tb\/_\/payment_dialog_title_3e773b9.js","\/tb\/_\/tdou_get_99d9a78.js","\/tb\/_\/tdou_3289666.js","\/tb\/_\/tcharge_dialog_1cd4f09.js","\/tb\/_\/join_vip_dialog_9242ef7.js","\/tb\/_\/forum_member_dialog_1139bd7.js","\/tb\/_\/exp_package_dialog_67a3307.js","\/tb\/_\/npc_vote_action_0c26f5f.js","\/tb\/_\/celebrity_b5cf0a5.js","\/tb\/_\/dialog_d31c70c.js","\/tb\/_\/util_fdb7481.js","\/tb\/_\/cont_sign_card_641fc4e.js","\/tb\/_\/net_proxy_f5ecab7.js","\/tb\/_\/use_controller_e92bca8.js","\/tb\/_\/buy_controller_516c900.js","\/tb\/_\/celebrity_expball_13260da.js"],"styles":["\/tb\/_\/aside_region_6df4cfc.css","\/tb\/_\/celebrity_widget_974def6.css","\/tb\/_\/celebrity_forum_dialog_b44a28b.css","\/tb\/_\/umoney_query_b5c3dca.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/base_dialog_user_bar_da68a26.css","\/tb\/_\/qianbao_cashier_dialog_c1e313a.css","\/tb\/_\/qianbao_purchase_tdou_4b31f54.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/tdou_template_f7dd2ac.css","\/tb\/_\/paykey_safe_payment_8f2a8db.css","\/tb\/_\/captcha_8dce960.css","\/tb\/_\/captcha_safe_payment_d41d8cd.css","\/tb\/_\/mobile_safe_payment_8c5a3b9.css","\/tb\/_\/tbean_safe_3c779a3.css","\/tb\/_\/tbean_safe_ajax_d41d8cd.css","\/tb\/_\/qianbao_purchase_member_d190d50.css","\/tb\/_\/cashier_dialog_0390325.css","\/tb\/_\/pay_member_d41d8cd.css","\/tb\/_\/umoney_f12b09a.css","\/tb\/_\/payment_dialog_title_5433211.css","\/tb\/_\/tdou_get_a4d3fd4.css","\/tb\/_\/tdou_d41d8cd.css","\/tb\/_\/forum_member_dialog_1d49009.css","\/tb\/_\/exp_package_dialog_5cb5fdb.css","\/tb\/_\/npc_vote_action_5b250b1.css","\/tb\/_\/celebrity_81c8269.css","\/tb\/_\/dialog_6ed86bb.css","\/tb\/_\/cont_sign_card_73a332e.css","\/tb\/_\/buy_controller_a328148.css","\/tb\/_\/celebrity_expball_e0bb045.css"]}).then(function(pagelet){    _.Module.use('encourage-celebrity/widget/celebrity', {
        celebrity: null,
        isCelebrityForum: false,
        user: {"is_login":false,"Parr_scores":null,"mParr_props":null},
        forum: {"forum_id":7739963,"forum_name":null},
        isCurForumMember: false,
        memberLastDays: 0    });
    _.Module.use('encourage-celebrity/widget/celebrity_expball', {"pageData":{"Parr_scores":null,"Parr_props":null,"forum":{"forum_id":7739963,"forum_name":"\u59cb\u7956\u5bb6\u65cf","dir_info":{"level_1_name":"\u7535\u89c6\u5267","level_2_name":"\u7f8e\u5267"},"kw":"\u59cb\u7956\u5bb6\u65cf","title":"\u59cb\u7956\u5bb6\u65cf\u5427-\u767e\u5ea6\u8d34\u5427--\u7f8e\u5267\u5438\u8840\u9b3c\u65e5\u8bb0\u884d\u751f\u5267The Originals\u8d34\u5427","description":"\u672c\u5427\u70ed\u5e16: 1-\u6c42\u4e94\u5b63\u8d44\u6e90 2-\u3010\u59cb\u7956\u5bb6\u65cf\u3011\u884d\u751f\u5267\u3010\u5438\u8840\u9b3c\u540e\u88d4\u301110\u670825\u53f7\u5f00\u64ad\uff01 3-\u767e\u5ea6\u8d34\u5427\u59cb\u7956\u5bb6\u65cf\u5427\u62d2\u7edd\u4efb\u4f55\u5e7f\u544a\u53d1\u73b0\u5fc5\u5c01\uff01 4-\u59cb\u7956\u5bb6\u65cf  1---5  \u5b8c\u7ed3  \u7cbe\u5fc3\u6574\u7406\u597d\u5566  no\uff0c\u526a 5-\u521d\u4ee3\u5438\u8840\u9b3c\u300c\u59cb\u7956\u5bb6\u65cf\u300d\u300c1--5\u5b63\u300d\u5df2\u6574\uff01\u7406????? 6-?\uff08\u521d\u4ee3\u5438\u8840\u9b3c\uff09\uff08\u59cb\u7956\u5bb6\u65cf\uff091\uff5e5\u5df2\u6574\u7406? 7-\u767e\u5ea6\u8d34\u5427\u59cb\u7956\u5bb6\u65cf\u5427\u65e5\u5e38\u7b7e\u5230\u6c34\u8d34\u5927\u697c\uff01","keywords":"\u59cb\u7956\u5bb6\u65cf,\u7f8e\u5267,\u7535\u89c6\u5267,\u8d44\u6e90"},"user":{"is_login":false,"user_id":0,"user_name":"","no_un":false,"mobile":"","email":"","is_new_user":1,"portrait":"00000000","start_time":1541356999}}}, function (expball) {
        var $voteNum = $('.j_vote_num');
        expball.setCallback(function (data) {
            $voteNum.html(+$voteNum.html() + (data['add_vote_num'] || 0));
        });
    });
});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/star" style="display:none;"><!----></code><script>Bigpipe.register("frs-aside/pagelet/star", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/hottopic" style="display:none;"><!--
<div class="topic_list_box">
    <div class="item_hd">
        <span class="title">贴吧热议榜</span>
    </div>
    <ul class="topic_list_hot topic_list j_topic_toplist">
        
            <li class="topic_item">
                <span class="topic_flag_hot">1</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257651&amp;topic_name=LOL%E6%80%BB%E5%86%B3%E8%B5%9BiG%E5%A4%BA%E5%86%A0" class="topic_name">LOL总决赛iG夺冠</a>
                <span class="topic_num">1350473</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag_hot">2</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257680&amp;topic_name=%E5%85%B0%E6%B5%B7%E9%AB%98%E9%80%9F%E4%B8%A5%E9%87%8D%E4%BA%8B%E6%95%85" class="topic_name">兰海高速严重事故</a>
                <span class="topic_num">1339210</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag_hot">3</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257681&amp;topic_name=S8%E5%86%A0%E5%86%9B%E7%9A%AE%E8%82%A4" class="topic_name">S8冠军皮肤</a>
                <span class="topic_num">1331543</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag">4</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257691&amp;topic_name=%E9%A3%9E%E5%BE%80%E4%B8%89%E4%BA%9A%E5%AE%A2%E6%9C%BA%E8%BF%AB%E9%99%8D" class="topic_name">飞往三亚客机迫降</a>
                <span class="topic_num">1185805</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag">5</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257696&amp;topic_name=%E9%92%88%E7%81%B8%E6%9C%89%E6%9C%9B%E5%85%A5%E7%BE%8E%E5%8C%BB%E4%BF%9D" class="topic_name">针灸有望入美医保</a>
                <span class="topic_num">1164113</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag">6</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257690&amp;topic_name=%E6%AD%A6%E5%A4%A7%E9%9D%96%E5%A4%BA%E5%86%A0" class="topic_name">武大靖夺冠</a>
                <span class="topic_num">1115909</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag">7</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257692&amp;topic_name=%E5%88%98%E9%9B%AF%E7%89%B9%E9%82%80%E8%B5%B0%E7%A7%80%E7%BB%B4%E5%AF%86" class="topic_name">刘雯特邀走秀维密</a>
                <span class="topic_num">1022333</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag">8</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257541&amp;topic_name=%E5%A4%AA%E5%B9%B3%E9%97%B4%E5%8F%8C%E7%9C%BC%E8%A2%AB%E6%8C%96" class="topic_name">太平间双眼被挖</a>
                <span class="topic_num">961951</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag">9</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257642&amp;topic_name=%E6%B8%A3%E6%B8%A3%E8%BE%89%E9%9B%86%E4%BC%9A" class="topic_name">渣渣辉集会</a>
                <span class="topic_num">779945</span>
            </li>

        
            <li class="topic_item">
                <span class="topic_flag">10</span>
                <a rel="noreferrer"  target="_blank" href="http://tieba.baidu.com/hottopic/browse/hottopic?topic_id=257710&amp;topic_name=%E5%8D%A1%E7%BA%B3%E7%93%A6%E7%BD%97%E6%98%AF%E4%B8%8D%E6%98%AF%E5%90%83%E5%A4%B4%E9%B8%A1" class="topic_name">卡纳瓦罗是不是吃头鸡</a>
                <span class="topic_num">430306</span>
            </li>

            </ul>
</div>

--></code><script>Bigpipe.register("frs-aside/pagelet/hottopic", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":["\/tb\/_\/frs-aside\/hottopic_262fd11.js"],"styles":["\/tb\/_\/frs-aside\/hottopic_0a620f9.css"]}).then(function(pagelet){    _.Module.use('frs-aside/widget/hottopic', {
        isAdvertisement: 2    });
});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/ad" style="display:none;"><!--


--></code><script>Bigpipe.register("frs-aside/pagelet/ad", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":["\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/loader_12d7714.js"],"styles":["\/tb\/_\/login_dialog_cc7c082.css"]}).then(function(pagelet){    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
});</script><code class="pagelet_html" id="pagelet_html_frs-list/pagelet/thread_list" style="display:none;"><!--

<ul id="thread_list" class="threadlist_bright j_threadlist_bright">
                <li class="thread_top_list_folder">
                <ul id="thread_top_list" class="thread_top_list">
                    <li class=" j_thread_list thread_top j_thread_list clearfix" data-field='{&quot;id&quot;:5899416824,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:122243342481,&quot;reply_num&quot;:25,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:true,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                    <a rel="noreferrer"  href="javascript:;" title="点击隐藏本贴" data-field='{&quot;tid&quot;:5899416824}'               class="j_thread_hidden icon_thread_hidden"></a>
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">25</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit 
">
    <i class="icon-top" alt="置顶" title="置顶" ></i>
    
    <a rel="noreferrer" href="/p/5899416824" title="【始祖家族】衍生剧【吸血鬼后裔】10月25号开播！" target="_blank" class="j_th_tit ">【始祖家族】衍生剧【吸血鬼后裔】10月25号开播！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10-1</span>
</div>
            </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list thread_top j_thread_list clearfix" data-field='{&quot;id&quot;:5899415739,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:122243329179,&quot;reply_num&quot;:4,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:true,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                    <a rel="noreferrer"  href="javascript:;" title="点击隐藏本贴" data-field='{&quot;tid&quot;:5899415739}'               class="j_thread_hidden icon_thread_hidden"></a>
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">4</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    <i class="icon-top" alt="置顶" title="置顶" ></i>
    
    <a rel="noreferrer" href="/p/5899415739" title="百度贴吧始祖家族吧日常签到水贴大楼！" target="_blank" class="j_th_tit ">百度贴吧始祖家族吧日常签到水贴大楼！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10-1</span>
</div>
            </div>
                                </div>
    </div>
</li>
                </ul>
                                <a rel="noreferrer"  id="thread_top_folder" class="icon_top_folder" href="javascript:;"
                     ></a>
            </li>
        <li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5937148668,&quot;author_name&quot;:&quot;\u8f6f\u59b9\u8bb0\u518c&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;4362e8bdafe5a6b9e8aeb0e5868c2fac&quot;,&quot;first_post_id&quot;:122714204331,&quot;reply_num&quot;:3,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">3</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5937148668" title="对于始祖家族的完结真的很可惜，刚刚看完的，整理了一下，发出来！" target="_blank" class="j_th_tit ">对于始祖家族的完结真的很可惜，刚刚看完的，整理了一下，发出来！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 软妹记册"
          data-field='{&quot;user_id&quot;:2888786499}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8f6f\u59b9\u8bb0\u518c&quot;,&quot;id&quot;:&quot;4362e8bdafe5a6b9e8aeb0e5868c2fac&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%BD%AF%E5%A6%B9%E8%AE%B0%E5%86%8C&ie=utf-8&id=4362e8bdafe5a6b9e8aeb0e5868c2fac&fr=frs" target="_blank">软妹记册</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">11-4</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            自取吧 
        </div>


            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5937148668"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="10818" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=771100788b18367aaddc77df1e43a7ed/47c3fb1001e93901e67f406f76ec54e736d19679.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=1a14ae2f9f58d109c4e3a9bae163cdbf/c9fcc3cec3fdfc0355052ee9d93f8794a4c22666.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    

<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 软妹记册">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8f6f\u59b9\u8bb0\u518c&quot;,&quot;id&quot;:&quot;4362e8bdafe5a6b9e8aeb0e5868c2fac&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%BD%AF%E5%A6%B9%E8%AE%B0%E5%86%8C&ie=utf-8&id=4362e8bdafe5a6b9e8aeb0e5868c2fac&fr=frs" target="_blank">软妹记册</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            11-4        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5805201504,&quot;author_name&quot;:&quot;babydog_lg&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;77fd62616279646f675f6c67fc01&quot;,&quot;first_post_id&quot;:120978321498,&quot;reply_num&quot;:28,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">28</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5805201504" title="为什么每集都有同性恋的内容啊，看来编剧真是对此乐此不疲" target="_blank" class="j_th_tit ">为什么每集都有同性恋的内容啊，看来编剧真是对此乐此不疲</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: babydog_lg"
          data-field='{&quot;user_id&quot;:33357175}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;babydog_lg&quot;,&quot;id&quot;:&quot;77fd62616279646f675f6c67fc01&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=babydog_lg&ie=utf-8&id=77fd62616279646f675f6c67fc01&fr=frs" target="_blank">babydog_lg</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1540803125) no-repeat -750px  0;top:0px;left:0px" data-slot="1"  data-name="tiancheng" data-field='{&quot;name&quot;:&quot;tiancheng&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u5929\u79e4\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,15&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="天秤座印记"  locate="tiancheng_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">7-22</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            为什么每集都有同性恋的内容啊，看来编剧真是对此乐此不疲
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 葬FUN">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u846cFUN&quot;,&quot;id&quot;:&quot;a2fce891ac46554e0704&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%91%ACFUN&ie=utf-8&id=a2fce891ac46554e0704&fr=frs" target="_blank">葬FUN</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            11-1        </span>
</div>
                </div>
                                </div>
    </div>
</li>



<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5933281507,&quot;author_name&quot;:&quot;\u6d77\u6d77\u6d77\u7ef5\u5b9d\u5b9d\u554a&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;45c8e6b5b7e6b5b7e6b5b7e7bbb5e5ae9de5ae9de5958a034f&quot;,&quot;first_post_id&quot;:122664465144,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5933281507" title="求五季资源" target="_blank" class="j_th_tit ">求五季资源</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 海海海绵宝宝啊"
          data-field='{&quot;user_id&quot;:1325647941}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6d77\u6d77\u6d77\u7ef5\u5b9d\u5b9d\u554a&quot;,&quot;id&quot;:&quot;45c8e6b5b7e6b5b7e6b5b7e7bbb5e5ae9de5ae9de5958a034f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%B5%B7%E6%B5%B7%E6%B5%B7%E7%BB%B5%E5%AE%9D%E5%AE%9D%E5%95%8A&ie=utf-8&id=45c8e6b5b7e6b5b7e6b5b7e7bbb5e5ae9de5ae9de5958a034f&fr=frs" target="_blank">海海海绵...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">11-1</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            可以给我分享下第五季资源吗，谢谢你们了亲，tangmy518（vx）海海海绵宝宝啊（百度云）
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 海海海绵宝宝啊">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6d77\u6d77\u6d77\u7ef5\u5b9d\u5b9d\u554a&quot;,&quot;id&quot;:&quot;45c8e6b5b7e6b5b7e6b5b7e7bbb5e5ae9de5ae9de5958a034f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%B5%B7%E6%B5%B7%E6%B5%B7%E7%BB%B5%E5%AE%9D%E5%AE%9D%E5%95%8A&ie=utf-8&id=45c8e6b5b7e6b5b7e6b5b7e7bbb5e5ae9de5ae9de5958a034f&fr=frs" target="_blank">海海海绵...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            11-1        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:4396336641,&quot;author_name&quot;:&quot;\u98ce\u5439\u98de\u4e86\u4e91&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;96a0e9a38ee590b9e9a39ee4ba86e4ba918249&quot;,&quot;first_post_id&quot;:85230367877,&quot;reply_num&quot;:4,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">4</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/4396336641" title="【始祖家族】《始祖家族》里你能我喜欢的一句话是对话台词是？？" target="_blank" class="j_th_tit ">【始祖家族】《始祖家族》里你能我喜欢的一句话是对话台词是？？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 风吹飞了云"
          data-field='{&quot;user_id&quot;:1233297558}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u98ce\u5439\u98de\u4e86\u4e91&quot;,&quot;id&quot;:&quot;96a0e9a38ee590b9e9a39ee4ba86e4ba918249&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%A3%8E%E5%90%B9%E9%A3%9E%E4%BA%86%E4%BA%91&ie=utf-8&id=96a0e9a38ee590b9e9a39ee4ba86e4ba918249&fr=frs" target="_blank">风吹飞了云</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">2016-03</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            先上我的：死亡在黑暗处跳舞～
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 套路空">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5957\u8def\u7a7a&quot;,&quot;id&quot;:&quot;8132e5a597e8b7afe7a9ba50d8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%A5%97%E8%B7%AF%E7%A9%BA&ie=utf-8&id=8132e5a597e8b7afe7a9ba50d8&fr=frs" target="_blank">套路空</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-24        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5918368862,&quot;author_name&quot;:&quot;CC992532517&quot;,&quot;author_nickname&quot;:&quot;CC992532517&quot;,&quot;author_portrait&quot;:&quot;8b4943433939323533323531375041&quot;,&quot;first_post_id&quot;:122485441450,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5918368862" title="求百度云" target="_blank" class="j_th_tit ">求百度云</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: CC992532517"
          data-field='{&quot;user_id&quot;:1095780747}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;CC992532517&quot;,&quot;id&quot;:&quot;8b4943433939323533323531375041&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=CC992532517&ie=utf-8&id=8b4943433939323533323531375041&fr=frs" target="_blank">CC992532517</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1540803125) no-repeat -1450px  0;top:0px;left:0px" data-slot="1"  data-name="wxhong" data-field='{&quot;name&quot;:&quot;wxhong&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u7ea2\u82b1\u4f1a&quot;,&quot;intro&quot;:&quot;\u5730\u9707\u9ad8\u5188\uff0c\u4e00\u6d3e\u6eaa\u5c71\u5343\u53e4\u79c0;\u95e8\u671d\u5927\u6d77\uff0c\u4e09\u5408\u6cb3\u6c34\u4e07\u5e74\u6d41\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/p\/3178653968&quot;,&quot;price&quot;:10000,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,29&quot;}}' target="_blank"   href="http://tieba.baidu.com/p/3178653968"  class="j_icon_slot"  title="红花会"  locate="wxhong_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1540803125) no-repeat -1150px  0;top:0px;left:28px" data-slot="2"  data-name="baiyang" data-field='{&quot;name&quot;:&quot;baiyang&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;2&quot;,&quot;title&quot;:&quot;\u767d\u7f8a\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,23&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="白羊座印记"  locate="baiyang_1#icon"  style="top: 0px; left:28px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: CC992532517">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;CC992532517&quot;,&quot;id&quot;:&quot;8b4943433939323533323531375041&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=CC992532517&ie=utf-8&id=8b4943433939323533323531375041&fr=frs" target="_blank">CC992532517</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-18        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5889151449,&quot;author_name&quot;:&quot;JEAlous45&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;b8c34a45416c6f757334356a43&quot;,&quot;first_post_id&quot;:122101624305,&quot;reply_num&quot;:5,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">5</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5889151449" title="初代看完真是太难受了" target="_blank" class="j_th_tit ">初代看完真是太难受了</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: JEAlous45"
          data-field='{&quot;user_id&quot;:1131070392}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;JEAlous45&quot;,&quot;id&quot;:&quot;b8c34a45416c6f757334356a43&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=JEAlous45&ie=utf-8&id=b8c34a45416c6f757334356a43&fr=frs" target="_blank">JEAlous45</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-21</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            尼克劳斯真是承包了太多泪点 父爱如山 可以说吸血鬼日记和初代吸血鬼是是我青春的回忆了 刚刚看完真
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: MeAndKaka_">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;MeAndKaka_&quot;,&quot;id&quot;:&quot;1b9a4d65416e644b616b615fcbcc&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=MeAndKaka_&ie=utf-8&id=1b9a4d65416e644b616b615fcbcc&fr=frs" target="_blank">MeAndKaka_</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-12        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5761801318,&quot;author_name&quot;:&quot;\u571f\u80a5\u5706\u52c7\u58eb&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c2e3e59c9fe882a5e59c86e58b87e5a3ab7b8e&quot;,&quot;first_post_id&quot;:120436465858,&quot;reply_num&quot;:6,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">6</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5761801318" title="第五季怎么回事？一群小混混就把世界搅个天翻地覆，在有能力重创" target="_blank" class="j_th_tit ">第五季怎么回事？一群小混混就把世界搅个天翻地覆，在有能力重创</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 土肥圆勇士"
          data-field='{&quot;user_id&quot;:2390483906}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u571f\u80a5\u5706\u52c7\u58eb&quot;,&quot;id&quot;:&quot;c2e3e59c9fe882a5e59c86e58b87e5a3ab7b8e&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%9C%9F%E8%82%A5%E5%9C%86%E5%8B%87%E5%A3%AB&ie=utf-8&id=c2e3e59c9fe882a5e59c86e58b87e5a3ab7b8e&fr=frs" target="_blank">土肥圆勇士</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">6-22</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            第五季怎么回事？一群小混混就把世界搅个天翻地覆，在有能力重创或团灭他们的时候居然不出手，编辑
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: Tide_1">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Tide_1&quot;,&quot;id&quot;:&quot;05e5546964655f311486&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=Tide_1&ie=utf-8&id=05e5546964655f311486&fr=frs" target="_blank">Tide_1</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-8        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5795271747,&quot;author_name&quot;:&quot;\u7ebf\u4e0a\u6307\u5357\u9488&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;5893e7babfe4b88ae68c87e58d97e992882a37&quot;,&quot;first_post_id&quot;:120836047215,&quot;reply_num&quot;:5,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">5</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5795271747" title="这就是本剧的颜值担当，明眼人应该能看出来问题" target="_blank" class="j_th_tit ">这就是本剧的颜值担当，明眼人应该能看出来问题</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 线上指南针"
          data-field='{&quot;user_id&quot;:925537112}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7ebf\u4e0a\u6307\u5357\u9488&quot;,&quot;id&quot;:&quot;5893e7babfe4b88ae68c87e58d97e992882a37&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%BA%BF%E4%B8%8A%E6%8C%87%E5%8D%97%E9%92%88&ie=utf-8&id=5893e7babfe4b88ae68c87e58d97e992882a37&fr=frs" target="_blank">线上指南针</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">7-14</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5795271747"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="27576" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=8f7e50949e58d109c4b6a1b0e168e086/b0cec51c8701a18bd5fc21a5922f07082938fedb.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=728e40f905f79052ef1f47363cc8d6ca/11385343fbf2b211c139b6a4c68065380dd78ec0.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: Tide_1">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Tide_1&quot;,&quot;id&quot;:&quot;05e5546964655f311486&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=Tide_1&ie=utf-8&id=05e5546964655f311486&fr=frs" target="_blank">Tide_1</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-8        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5849183187,&quot;author_name&quot;:&quot;i990049&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;0957693939303034397500&quot;,&quot;first_post_id&quot;:121575923754,&quot;reply_num&quot;:4,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">4</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5849183187" title="没看懂霍普怎么触发狼人诅咒的" target="_blank" class="j_th_tit ">没看懂霍普怎么触发狼人诅咒的</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: i990049"
          data-field='{&quot;user_id&quot;:7689993}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;i990049&quot;,&quot;id&quot;:&quot;0957693939303034397500&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=i990049&ie=utf-8&id=0957693939303034397500&fr=frs" target="_blank">i990049</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-21</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            狼妈男友不是去教堂拿日记了吗？怎么就跟神父被杀了？
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 芯茜泰坪">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u82af\u831c\u6cf0\u576a&quot;,&quot;id&quot;:&quot;ed25e88aafe88c9ce6b3b0e59daad713&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%8A%AF%E8%8C%9C%E6%B3%B0%E5%9D%AA&ie=utf-8&id=ed25e88aafe88c9ce6b3b0e59daad713&fr=frs" target="_blank">芯茜泰坪</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-6        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5841200402,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121469415605,&quot;reply_num&quot;:7,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">7</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5841200402" title="最终季了，好舍不得" target="_blank" class="j_th_tit ">最终季了，好舍不得</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-15</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            作为最典型的吸血鬼系列美剧之一《初代吸血鬼》第五季强势回归，当然毫无意外地登上了热搜榜，毕竟
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5841200402"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="49862" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=aea39b0b25381f309e4c85ab99316031/ee78f335e5dde711a063eac5aaefce1b9d16616e.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=03761e88ab1ea8d38a22740ca731314e/ac6eddc451da81cb09572afe5f66d0160924314b.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 芯茜泰坪">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u82af\u831c\u6cf0\u576a&quot;,&quot;id&quot;:&quot;ed25e88aafe88c9ce6b3b0e59daad713&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%8A%AF%E8%8C%9C%E6%B3%B0%E5%9D%AA&ie=utf-8&id=ed25e88aafe88c9ce6b3b0e59daad713&fr=frs" target="_blank">芯茜泰坪</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-6        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5704597925,&quot;author_name&quot;:&quot;422751708&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;eae33432323735313730384207&quot;,&quot;first_post_id&quot;:119777772190,&quot;reply_num&quot;:16,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">16</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5704597925" title="新剧来了~~" target="_blank" class="j_th_tit ">新剧来了~~</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 422751708"
          data-field='{&quot;user_id&quot;:121824234}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;422751708&quot;,&quot;id&quot;:&quot;eae33432323735313730384207&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=422751708&ie=utf-8&id=eae33432323735313730384207&fr=frs" target="_blank">422751708</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1540803125) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,76&quot;,&quot;2&quot;:&quot;1540803125,77&quot;,&quot;3&quot;:&quot;1540803125,78&quot;,&quot;4&quot;:&quot;1540803125,79&quot;,&quot;5&quot;:&quot;1540803125,80&quot;,&quot;6&quot;:&quot;1540803125,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">5-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            除此之外，CW还公布了《吸血鬼日记》系列全新分支剧集《吸血鬼传承》，聚焦狼人﹑吸血鬼﹑女巫混血的
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5704597925"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="98062" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=36fd091cd83f8794d3aa402ce22b22cd/32ede6529822720ea84b085e77cb0a46f31fabac.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=37ab6feac68065387beaa41ba7e6a044/a6efce1b9d16fdfa0be92c4ab88f8c5495ee7b89.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 芯茜泰坪">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u82af\u831c\u6cf0\u576a&quot;,&quot;id&quot;:&quot;ed25e88aafe88c9ce6b3b0e59daad713&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%8A%AF%E8%8C%9C%E6%B3%B0%E5%9D%AA&ie=utf-8&id=ed25e88aafe88c9ce6b3b0e59daad713&fr=frs" target="_blank">芯茜泰坪</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-6        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5904185058,&quot;author_name&quot;:&quot;FDandMT&quot;,&quot;author_nickname&quot;:&quot;MT-Hope&quot;,&quot;author_portrait&quot;:&quot;b6074644616e644d54e9d2&quot;,&quot;first_post_id&quot;:122305659103,&quot;reply_num&quot;:1,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">1</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5904185058" title="探讨大K这个特别角色" target="_blank" class="j_th_tit ">探讨大K这个特别角色</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: MT-Hope"
          data-field='{&quot;user_id&quot;:3538487222}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;FDandMT&quot;,&quot;id&quot;:&quot;b6074644616e644d54e9d2&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=FDandMT&ie=utf-8&id=b6074644616e644d54e9d2&fr=frs" target="_blank">MT<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/>Hope</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10-5</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            大K这个角色 从第一季开始追 补上日记部分 他藏很深的人性善念 被卡琳娜 卡密 以叔 海莉 丽贝卡 Hope 大
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5904185058"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="5219" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=a45448db0e3b5bb5be8228fc06e3f900/c3c6a700baa1cd11feeb3b50b412c8fcc3ce2d7f.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=5d23d10bdc1373f0f53f6f9794344afb/b21c8701a18b87d6ab1fe26f0a0828381f30fd65.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: MT-Hope">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;FDandMT&quot;,&quot;id&quot;:&quot;b6074644616e644d54e9d2&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=FDandMT&ie=utf-8&id=b6074644616e644d54e9d2&fr=frs" target="_blank">MT<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/>Hope</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-5        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5899776177,&quot;author_name&quot;:&quot;\u758f\u758f\u758f\u57ce&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;b7b9e7968fe7968fe7968fe59f8ed36b&quot;,&quot;first_post_id&quot;:122247668477,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5899776177" title="为啥人人视频始祖家族又下架了" target="_blank" class="j_th_tit ">为啥人人视频始祖家族又下架了</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 疏疏疏城"
          data-field='{&quot;user_id&quot;:1809037751}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u758f\u758f\u758f\u57ce&quot;,&quot;id&quot;:&quot;b7b9e7968fe7968fe7968fe59f8ed36b&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%96%8F%E7%96%8F%E7%96%8F%E5%9F%8E&ie=utf-8&id=b7b9e7968fe7968fe7968fe59f8ed36b&fr=frs" target="_blank">疏疏疏城</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10-1</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            为啥人人视频始祖家族又下架了
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 疏疏疏城">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u758f\u758f\u758f\u57ce&quot;,&quot;id&quot;:&quot;b7b9e7968fe7968fe7968fe59f8ed36b&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%96%8F%E7%96%8F%E7%96%8F%E5%9F%8E&ie=utf-8&id=b7b9e7968fe7968fe7968fe59f8ed36b&fr=frs" target="_blank">疏疏疏城</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            10-1        </span>
</div>
                </div>
                                </div>
    </div>
</li>



<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5898877873,&quot;author_name&quot;:&quot;\u7b2c\u4e8c\u4e2a\u4f602012&quot;,&quot;author_nickname&quot;:&quot;\u6211\u53eb\u767d\u5c0f\u98de\u2642&quot;,&quot;author_portrait&quot;:&quot;e171e7acace4ba8ce4b8aae4bda032303132722b&quot;,&quot;first_post_id&quot;:122236413720,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5898877873" title="这个女的是谁演的，怎么也想不起来是在哪一集里面的" target="_blank" class="j_th_tit ">这个女的是谁演的，怎么也想不起来是在哪一集里面的</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 我叫白小飞♂"
          data-field='{&quot;user_id&quot;:728920545}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7b2c\u4e8c\u4e2a\u4f602012&quot;,&quot;id&quot;:&quot;e171e7acace4ba8ce4b8aae4bda032303132722b&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%AC%AC%E4%BA%8C%E4%B8%AA%E4%BD%A02012&ie=utf-8&id=e171e7acace4ba8ce4b8aae4bda032303132722b&fr=frs" target="_blank">我叫白小...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1540803125) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,76&quot;,&quot;2&quot;:&quot;1540803125,77&quot;,&quot;3&quot;:&quot;1540803125,78&quot;,&quot;4&quot;:&quot;1540803125,79&quot;,&quot;5&quot;:&quot;1540803125,80&quot;,&quot;6&quot;:&quot;1540803125,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-30</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            这个女的是谁演的，怎么也想不起来是在哪一集里面的 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5898877873"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="44427" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=b3b9d51e66600c33f02cd6ca2a7c7d36/ac10464e251f95ca091284bcc4177f3e660952eb.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=d1fe88229a2bd40742c7d3f54bb29f51/f703738da97739126bc1936bf5198618377ae2d1.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 我叫白小飞♂">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7b2c\u4e8c\u4e2a\u4f602012&quot;,&quot;id&quot;:&quot;e171e7acace4ba8ce4b8aae4bda032303132722b&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%AC%AC%E4%BA%8C%E4%B8%AA%E4%BD%A02012&ie=utf-8&id=e171e7acace4ba8ce4b8aae4bda032303132722b&fr=frs" target="_blank">我叫白小...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-30        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5862957093,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121763517218,&quot;reply_num&quot;:21,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">21</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5862957093" title="百度贴吧始祖家族吧拒绝任何广告发现必封！" target="_blank" class="j_th_tit ">百度贴吧始祖家族吧拒绝任何广告发现必封！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-31</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 会飞的荷兰驴">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-30        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5896211952,&quot;author_name&quot;:&quot;\u7b49\u5f85\u4eab\u53d7&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;631fe7ad89e5be85e4baabe58f975904&quot;,&quot;first_post_id&quot;:122201942828,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5896211952" title="小HOPE演X战警黑凤凰小时候" target="_blank" class="j_th_tit ">小HOPE演X战警黑凤凰小时候</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 等待享受"
          data-field='{&quot;user_id&quot;:72949603}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7b49\u5f85\u4eab\u53d7&quot;,&quot;id&quot;:&quot;631fe7ad89e5be85e4baabe58f975904&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%AD%89%E5%BE%85%E4%BA%AB%E5%8F%97&ie=utf-8&id=631fe7ad89e5be85e4baabe58f975904&fr=frs" target="_blank">等待享受</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-28</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
             
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5896211952"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="38333" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=970d853ebede9c82a630f18d5cb1ac33/bc1bd78b87d6277f9b7a533f25381f30e924fc63.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C217%3Bap%3D%CA%BC%D7%E6%BC%D2%D7%E5%B0%C9%2C90%2C225/sign=0a711690d433c895a67e9873e1281080/faf2b2119313b07ecfd5310f01d7912397dd8c48.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="25533" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=d75ce7e99182d158bbd751b3b03a35e1/9a91f1d6277f9e2f015d7c0f1230e924b899f363.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C224%3Bap%3D%CA%BC%D7%E6%BC%D2%D7%E5%B0%C9%2C90%2C232/sign=09e65b134fa7d933bfa8e47b9d70b263/b3119313b07eca80636d58e09c2397dda1448348.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><div class="threadlist_video"><img src="http://imgsrc.baidu.com/forum/pic/item/dcc451da81cb39dbcfba0651dd160924ab1830ba.jpg"/><a rel="noreferrer"  href="#" data-threadid="5896211952" data-forumid="7739963" data-isfive="0" data-video="http://player.youku.com/player.php/sid/XMzgzOTYyODI5Mg==/partnerid/8d5ffe2a068f4077/v.swf" data-type="" data-duration="" class="threadlist_btn_play j_m_flash"></a></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 等待享受">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7b49\u5f85\u4eab\u53d7&quot;,&quot;id&quot;:&quot;631fe7ad89e5be85e4baabe58f975904&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%AD%89%E5%BE%85%E4%BA%AB%E5%8F%97&ie=utf-8&id=631fe7ad89e5be85e4baabe58f975904&fr=frs" target="_blank">等待享受</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-28        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5866215752,&quot;author_name&quot;:&quot;\u66f2\u6bd4\u683c\u91cc\u5179\u66fc&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;fe8ee69bb2e6af94e6a0bce9878ce585b9e69bbccb60&quot;,&quot;first_post_id&quot;:121806693763,&quot;reply_num&quot;:4,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">4</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5866215752" title="请问始祖家族5在哪可以看，等太久了了" target="_blank" class="j_th_tit ">请问始祖家族5在哪可以看，等太久了了</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 曲比格里兹曼"
          data-field='{&quot;user_id&quot;:1623953150}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u66f2\u6bd4\u683c\u91cc\u5179\u66fc&quot;,&quot;id&quot;:&quot;fe8ee69bb2e6af94e6a0bce9878ce585b9e69bbccb60&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%9B%B2%E6%AF%94%E6%A0%BC%E9%87%8C%E5%85%B9%E6%9B%BC&ie=utf-8&id=fe8ee69bb2e6af94e6a0bce9878ce585b9e69bbccb60&fr=frs" target="_blank">曲比格里...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1540803125) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,76&quot;,&quot;2&quot;:&quot;1540803125,77&quot;,&quot;3&quot;:&quot;1540803125,78&quot;,&quot;4&quot;:&quot;1540803125,79&quot;,&quot;5&quot;:&quot;1540803125,80&quot;,&quot;6&quot;:&quot;1540803125,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-3</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            请问始祖家族5在哪可以看，等太久了了
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 曲比格里兹曼">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u66f2\u6bd4\u683c\u91cc\u5179\u66fc&quot;,&quot;id&quot;:&quot;fe8ee69bb2e6af94e6a0bce9878ce585b9e69bbccb60&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%9B%B2%E6%AF%94%E6%A0%BC%E9%87%8C%E5%85%B9%E6%9B%BC&ie=utf-8&id=fe8ee69bb2e6af94e6a0bce9878ce585b9e69bbccb60&fr=frs" target="_blank">曲比格里...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-23        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5890335967,&quot;author_name&quot;:&quot;\u9976\u4e86\u6211\u54273838&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;0edee9a5b6e4ba86e68891e590a733383338576e&quot;,&quot;first_post_id&quot;:122118351900,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5890335967" title="求BGM" target="_blank" class="j_th_tit ">求BGM</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 饶了我吧3838"
          data-field='{&quot;user_id&quot;:1851252238}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9976\u4e86\u6211\u54273838&quot;,&quot;id&quot;:&quot;0edee9a5b6e4ba86e68891e590a733383338576e&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%A5%B6%E4%BA%86%E6%88%91%E5%90%A73838&ie=utf-8&id=0edee9a5b6e4ba86e68891e590a733383338576e&fr=frs" target="_blank">饶了我吧3...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-22</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            请问各位大佬，始祖家族第五季第五集的最后BGM是啥啊？跪求！！！
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 饶了我吧3838">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9976\u4e86\u6211\u54273838&quot;,&quot;id&quot;:&quot;0edee9a5b6e4ba86e68891e590a733383338576e&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%A5%B6%E4%BA%86%E6%88%91%E5%90%A73838&ie=utf-8&id=0edee9a5b6e4ba86e68891e590a733383338576e&fr=frs" target="_blank">饶了我吧3...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-22        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5824974907,&quot;author_name&quot;:&quot;\u6cef\u79bb\u4f24&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c253e6b3afe7a6bbe4bca48854&quot;,&quot;first_post_id&quot;:121254971215,&quot;reply_num&quot;:5,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">5</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5824974907" title="猪妈真的，写死就算了，还要死不瞑目" target="_blank" class="j_th_tit ">猪妈真的，写死就算了，还要死不瞑目</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 泯离伤"
          data-field='{&quot;user_id&quot;:1418220482}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6cef\u79bb\u4f24&quot;,&quot;id&quot;:&quot;c253e6b3afe7a6bbe4bca48854&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%B3%AF%E7%A6%BB%E4%BC%A4&ie=utf-8&id=c253e6b3afe7a6bbe4bca48854&fr=frs" target="_blank">泯离伤</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-4</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            猪妈真的，写死就算了，还要死不瞑目
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5824974907"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="62590" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=8c630ef6ad8b87d65017a31d37380401/0dcb592eb9389b5070bd5c958935e5dde6116e55.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=53fe09fd15d8bc3ec60806c2b2b0a41e/a5c27d1ed21b0ef424aa2499d1c451da80cb3eb2.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="91662" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=608819a59422720e7b9beaf84bfb267f/bb106fd8bc3eb1355a850b7caa1ea8d3fc1f4455.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=678b9222a16eddc426e7b4f309e0b4fd/b219ebc4b74543a9eb59460b12178a82b80114b2.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 紫藤情缘">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7d2b\u85e4\u60c5\u7f18&quot;,&quot;id&quot;:&quot;665ce7b4abe897a4e68385e7bc98ec04&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%B4%AB%E8%97%A4%E6%83%85%E7%BC%98&ie=utf-8&id=665ce7b4abe897a4e68385e7bc98ec04&fr=frs" target="_blank">紫藤情缘</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-9        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5874194094,&quot;author_name&quot;:&quot;\u5929\u50b2\u67ab\u5c9a&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c108e5a4a9e582b2e69eabe5b29a0c00&quot;,&quot;first_post_id&quot;:121907446545,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5874194094" title="第三季第九集贵族女弹的是《寓言》？这首歌是改编歌？" target="_blank" class="j_th_tit ">第三季第九集贵族女弹的是《寓言》？这首歌是改编歌？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 天傲枫岚"
          data-field='{&quot;user_id&quot;:788673}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5929\u50b2\u67ab\u5c9a&quot;,&quot;id&quot;:&quot;c108e5a4a9e582b2e69eabe5b29a0c00&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%A4%A9%E5%82%B2%E6%9E%AB%E5%B2%9A&ie=utf-8&id=c108e5a4a9e582b2e69eabe5b29a0c00&fr=frs" target="_blank">天傲枫岚</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1540803125) no-repeat -50px  0;top:0px;left:0px" data-slot="1"  data-name="mojie" data-field='{&quot;name&quot;:&quot;mojie&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u9b54\u7faf\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,1&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="魔羯座印记"  locate="mojie_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-9</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            第三季第九集贵族女弹的是《寓言》？这首歌是改编歌？
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 天傲枫岚">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5929\u50b2\u67ab\u5c9a&quot;,&quot;id&quot;:&quot;c108e5a4a9e582b2e69eabe5b29a0c00&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%A4%A9%E5%82%B2%E6%9E%AB%E5%B2%9A&ie=utf-8&id=c108e5a4a9e582b2e69eabe5b29a0c00&fr=frs" target="_blank">天傲枫岚</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-9        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5845765126,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121530670072,&quot;reply_num&quot;:6,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">6</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5845765126" title="放不下我的kc啊！" target="_blank" class="j_th_tit ">放不下我的kc啊！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            我本来已经不生气了，直到看到了这个图。 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5845765126"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="30631" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=def39b5f282dd42a5f5c09a9330b778c/f22706cf3bc79f3df1052a06b7a1cd11728b293e.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=06fdb9a1d433c895a67e9873e12872f0/dbb44aed2e738bd4bac57c07ac8b87d6277ff924.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 辣椒小棉签🔥">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u53ee\u96f6\u549a\u9686&quot;,&quot;id&quot;:&quot;5b2fe58faee99bb6e5929ae99a86bf1d&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%8F%AE%E9%9B%B6%E5%92%9A%E9%9A%86&ie=utf-8&id=5b2fe58faee99bb6e5929ae99a86bf1d&fr=frs" target="_blank">辣椒小棉...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-8        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5728905245,&quot;author_name&quot;:&quot;\u68a8\u82b1\u9999\u00b0&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;b725e6a2a8e88ab1e9a699c2b0031c&quot;,&quot;first_post_id&quot;:120068215578,&quot;reply_num&quot;:20,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">20</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5728905245" title="始祖家族剧终季第六集，关于海莉的死，不愿相信" target="_blank" class="j_th_tit ">始祖家族剧终季第六集，关于海莉的死，不愿相信</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 梨花香°"
          data-field='{&quot;user_id&quot;:469968311}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u68a8\u82b1\u9999\u00b0&quot;,&quot;id&quot;:&quot;b725e6a2a8e88ab1e9a699c2b0031c&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%A2%A8%E8%8A%B1%E9%A6%99%C2%B0&ie=utf-8&id=b725e6a2a8e88ab1e9a699c2b0031c&fr=frs" target="_blank">梨花香°</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">6-3</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5728905245"><li><div class="threadlist_video"><img src="http://imgsrc.baidu.com/forum/pic/item/4134970a304e251f7de81561ab86c9177f3e5308.jpg"/><a rel="noreferrer"  href="#" data-threadid="5728905245" data-forumid="7739963" data-isfive="0" data-video="http://tb-video.bdstatic.com/tieba-smallvideo-transcode/818933_020ced0c92f04b87c0ee8aed353b0274_0.mp4"data-vsrc="http://tieba.baidu.com/mo/q/movideo/page?thumbnail=4134970a304e251f7de81561ab86c9177f3e5308&amp;video=10_a2fc00cc2a7311ce963325371016c0dd&amp;product=tieba-movideo" data-type="movideo" data-duration="" class="threadlist_btn_play j_m_flash"></a></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 673685880">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;673685880&quot;,&quot;id&quot;:&quot;3f133637333638353838308102&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=673685880&ie=utf-8&id=3f133637333638353838308102&fr=frs" target="_blank">673685880</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-6        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5870275963,&quot;author_name&quot;:&quot;\u4e54\u6728\u81ea\u71c3u&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;d438e4b994e69ca8e887aae7878375925e&quot;,&quot;first_post_id&quot;:121857505052,&quot;reply_num&quot;:0,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">0</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5870275963" title="那个假笑男孩好像克老斯" target="_blank" class="j_th_tit ">那个假笑男孩好像克老斯</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 乔木自燃u"
          data-field='{&quot;user_id&quot;:1586641108}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4e54\u6728\u81ea\u71c3u&quot;,&quot;id&quot;:&quot;d438e4b994e69ca8e887aae7878375925e&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%B9%94%E6%9C%A8%E8%87%AA%E7%87%83u&ie=utf-8&id=d438e4b994e69ca8e887aae7878375925e&fr=frs" target="_blank">乔木自燃u</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-6</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 乔木自燃u">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4e54\u6728\u81ea\u71c3u&quot;,&quot;id&quot;:&quot;d438e4b994e69ca8e887aae7878375925e&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%B9%94%E6%9C%A8%E8%87%AA%E7%87%83u&ie=utf-8&id=d438e4b994e69ca8e887aae7878375925e&fr=frs" target="_blank">乔木自燃u</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-6        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5824148820,&quot;author_name&quot;:&quot;craneofcloud&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;30f36372616e656f66636c6f75647704&quot;,&quot;first_post_id&quot;:121245089515,&quot;reply_num&quot;:17,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">17</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5824148820" title="克劳斯的血脉断了，但elijha的没断" target="_blank" class="j_th_tit ">克劳斯的血脉断了，但elijha的没断</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: craneofcloud"
          data-field='{&quot;user_id&quot;:74969904}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;craneofcloud&quot;,&quot;id&quot;:&quot;30f36372616e656f66636c6f75647704&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=craneofcloud&ie=utf-8&id=30f36372616e656f66636c6f75647704&fr=frs" target="_blank">craneofcloud</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-4</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            都死了，那elijha血脉中的吸血鬼都得死。 那么问题来了，elijha血脉中有哪些主角？还没死的
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: lcy621860">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;lcy621860&quot;,&quot;id&quot;:&quot;609c6c63793632313836304201&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=lcy621860&ie=utf-8&id=609c6c63793632313836304201&fr=frs" target="_blank">lcy621860</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            9-6        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5793550315,&quot;author_name&quot;:&quot;\u62c2\u6653\u4e36\u6e05\u660e&quot;,&quot;author_nickname&quot;:&quot;\u5624\u5624\u5624\ud83d\udcaf\u2103&quot;,&quot;author_portrait&quot;:&quot;c4c9e68b82e69993e4b8b6e6b885e6988e343f&quot;,&quot;first_post_id&quot;:120812486688,&quot;reply_num&quot;:3,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">3</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5793550315" title="谁有剧里hope的照片啊。撩头发的我忘记是第几集了。先要图片" target="_blank" class="j_th_tit ">谁有剧里hope的照片啊。撩头发的我忘记是第几集了。先要图片</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 嘤嘤嘤💯℃"
          data-field='{&quot;user_id&quot;:1060424132}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u62c2\u6653\u4e36\u6e05\u660e&quot;,&quot;id&quot;:&quot;c4c9e68b82e69993e4b8b6e6b885e6988e343f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%8B%82%E6%99%93%E4%B8%B6%E6%B8%85%E6%98%8E&ie=utf-8&id=c4c9e68b82e69993e4b8b6e6b885e6988e343f&fr=frs" target="_blank">嘤嘤嘤<img src="//tb1.bdstatic.com/tb/cms/nickemoji/4-21.png" class="nicknameEmoji" style="width:13px;height:13px"/><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-17.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">7-13</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            谁有剧里hope的照片啊。撩头发的我忘记是第几集了。先要图片做头像。
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5793550315"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="82936" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=c34ae5cb7ff082022dc7993d7bcbd7d4/8d1a4cf33a87e9505b2bf2841c385343fbf2b430.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=f5517b1ad962853592e0d229a0d477c6/810a19d8bc3eb1355dfbb653aa1ea8d3fd1f441d.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 嘤嘤嘤💯℃">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u62c2\u6653\u4e36\u6e05\u660e&quot;,&quot;id&quot;:&quot;c4c9e68b82e69993e4b8b6e6b885e6988e343f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%8B%82%E6%99%93%E4%B8%B6%E6%B8%85%E6%98%8E&ie=utf-8&id=c4c9e68b82e69993e4b8b6e6b885e6988e343f&fr=frs" target="_blank">嘤嘤嘤<img src="//tb1.bdstatic.com/tb/cms/nickemoji/4-21.png" class="nicknameEmoji" style="width:13px;height:13px"/><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-17.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5858525834,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121705128292,&quot;reply_num&quot;:16,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">16</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5858525834" title="始祖家族S4E5剧评：转变" target="_blank" class="j_th_tit ">始祖家族S4E5剧评：转变</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-28</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5858525834"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="59996" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=129000db76cb0a468577833b5b53da1d/08e0f48ba61ea8d3e37c96259a0a304e251f584b.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=4fb956da34dbb6fd255be52e391faa18/8326cffc1e178a82a7629d81fb03738da977e8b1.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 会飞的荷兰驴">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5851011314,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121600097887,&quot;reply_num&quot;:18,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">18</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5851011314" title="《始祖家族》克劳斯——冷血杀人魔也可以是温柔父亲" target="_blank" class="j_th_tit ">《始祖家族》克劳斯——冷血杀人魔也可以是温柔父亲</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-22</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5851011314"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="50387" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=11ec5a9bfb03738dde1f0420832b9c68/0ab7bdef76094b3604423ed6aecc7cd98c109dd7.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=f48d24a353df8db1bc2e7c6c3918dc54/f9dcd100baa1cd11da66571bb412c8fcc3ce2d3c.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 会飞的荷兰驴">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:2867143117,&quot;author_name&quot;:&quot;\u97f3\u4e50\u6c34\u679cJoyce&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c1e1e99fb3e4b990e6b0b4e69e9c4a6f796365230e&quot;,&quot;first_post_id&quot;:45990184702,&quot;reply_num&quot;:206,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:true,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">206</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    <i class="icon-good" alt="精品" title="精品" ></i>
    
    <a rel="noreferrer" href="/p/2867143117" title="【始祖家族】好喜欢大K的台词呀，大家一起来念～" target="_blank" class="j_th_tit ">【始祖家族】好喜欢大K的台词呀，大家一起来念～</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 音乐水果Joyce"
          data-field='{&quot;user_id&quot;:237232577}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u97f3\u4e50\u6c34\u679cJoyce&quot;,&quot;id&quot;:&quot;c1e1e99fb3e4b990e6b0b4e69e9c4a6f796365230e&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%9F%B3%E4%B9%90%E6%B0%B4%E6%9E%9CJoyce&ie=utf-8&id=c1e1e99fb3e4b990e6b0b4e69e9c4a6f796365230e&fr=frs" target="_blank">音乐水果J...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">2014-03</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            念着玩念着玩～别Pia楼主～
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm2867143117"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="63606" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=c7dbf36203e939015657853c4bdc78de/79bdaf33c895d1431649af6171f082025aaf074b.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=30d6cd6e8501a18bf0eb1247ae140608/6c224f4a20a44623b2f5ee209a22720e0cf3d7b1.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:2752454262,&quot;author_name&quot;:&quot;\u4fde\u77e2&quot;,&quot;author_nickname&quot;:&quot;\u6d45\u91ce\u4e45\u5ddd\u00ba&quot;,&quot;author_portrait&quot;:&quot;a2b3e4bf9ee79fa2be1f&quot;,&quot;first_post_id&quot;:42835999653,&quot;reply_num&quot;:488,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:true,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">488</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    <i class="icon-good" alt="精品" title="精品" ></i>
    
    <a rel="noreferrer" href="/p/2752454262" title="【始祖家族】外媒票选最有爱的50对美剧情侣 五十次迷人碰撞" target="_blank" class="j_th_tit ">【始祖家族】外媒票选最有爱的50对美剧情侣 五十次迷人碰撞</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 浅野久川º"
          data-field='{&quot;user_id&quot;:532591522}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4fde\u77e2&quot;,&quot;id&quot;:&quot;a2b3e4bf9ee79fa2be1f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BF%9E%E7%9F%A2&ie=utf-8&id=a2b3e4bf9ee79fa2be1f&fr=frs" target="_blank">浅野久川<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-1.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1540803125) no-repeat -1850px  0;top:0px;left:0px" data-slot="1"  data-name="wangzhe" data-field='{&quot;name&quot;:&quot;wangzhe&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u738b\u8005\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u53c2\u52a02014\u5df4\u897f\u4e16\u754c\u676f\u8bb8\u613f\u80dc\u5229\u6d3b\u52a8\u6709\u673a\u4f1a\u53ef\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/tbguess\/worldcup\/guessrank#badge&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,37&quot;}}' target="_blank"   href="http://tieba.baidu.com/tbguess/worldcup/guessrank#badge"  class="j_icon_slot"  title="王者印记"  locate="wangzhe_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">2014-01</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
             【转载要么跟我说句要么注明出处】 只有这个世界上还存在“肥皂剧”，就会有无数观众操心剧中的痴男怨女们最后能否找到爱情归宿，所以难免会对他们的
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm2752454262"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="75294" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=2823596d050828386858d41688a98538/74d8a3628535e5dde84d57ad74c6a7efce1b627d.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=be69f4b8808ba61edfeec827710f960a/1ad5ad6eddc451da8e97fe99b4fd5266d016325a.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5782655683,&quot;author_name&quot;:&quot;\u672a\u591f\u6591&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;1806e69caae5a49fe696916430&quot;,&quot;first_post_id&quot;:120669298949,&quot;reply_num&quot;:2,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">2</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5782655683" title="敌军还有30秒，到达战场" target="_blank" class="j_th_tit ">敌军还有30秒，到达战场</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 未够斑"
          data-field='{&quot;user_id&quot;:811861528}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u672a\u591f\u6591&quot;,&quot;id&quot;:&quot;1806e69caae5a49fe696916430&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%9C%AA%E5%A4%9F%E6%96%91&ie=utf-8&id=1806e69caae5a49fe696916430&fr=frs" target="_blank">未够斑</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">7-5</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5782655683"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="11700" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=89753517fed3572c66b794deba234f1e/b74ee2eef01f3a29ae51b7309525bc315d607c49.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=fc9a30c7c53d70cf4cfaaa05c8e7d300/e7cd7b899e510fb38c801569d533c895d0430cb6.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5818020440,&quot;author_name&quot;:&quot;Niklusr&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;25034e696b6c7573722570&quot;,&quot;first_post_id&quot;:121167992436,&quot;reply_num&quot;:3,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">3</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5818020440" title="刚刚看了第五季第八集，看得心难受，求一下片尾曲名字" target="_blank" class="j_th_tit ">刚刚看了第五季第八集，看得心难受，求一下片尾曲名字</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: Niklusr"
          data-field='{&quot;user_id&quot;:1881473829}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Niklusr&quot;,&quot;id&quot;:&quot;25034e696b6c7573722570&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=Niklusr&ie=utf-8&id=25034e696b6c7573722570&fr=frs" target="_blank">Niklusr</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">7-31</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            刚刚看了第五季第八集，看得心难受，求一下片尾曲名字 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5818020440"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="92066" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=a39455e88a18367aaddc77df1e43a7ed/47c3fb1001e9390132fa15ff77ec54e737d19615.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=ce91fbbf9e58d109c4e3a9bae163cebf/c9fcc3cec3fdfc0381807b79d83f8794a5c22672.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5828305468,&quot;author_name&quot;:&quot;\u8c4c\u8c46\u7a00\u996dFreya&quot;,&quot;author_nickname&quot;:&quot;\u6635\u79f0\u771f\u4e0d\u597d\u6539\ud83d\udcaf&quot;,&quot;author_portrait&quot;:&quot;a9d1e8b18ce8b186e7a880e9a5ad467265796185bb&quot;,&quot;first_post_id&quot;:121296883105,&quot;reply_num&quot;:3,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">3</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5828305468" title="为了把Klaus的泪截下来。(截了好多下。)始祖家族完结了，" target="_blank" class="j_th_tit ">为了把Klaus的泪截下来。(截了好多下。)始祖家族完结了，</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 昵称真不好改💯"
          data-field='{&quot;user_id&quot;:3146109353}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8c4c\u8c46\u7a00\u996dFreya&quot;,&quot;id&quot;:&quot;a9d1e8b18ce8b186e7a880e9a5ad467265796185bb&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%B1%8C%E8%B1%86%E7%A8%80%E9%A5%ADFreya&ie=utf-8&id=a9d1e8b18ce8b186e7a880e9a5ad467265796185bb&fr=frs" target="_blank">昵称真不...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-6</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            为了把Klaus的泪截下来。(截了好多下。)始祖家族完结了，心里空空的，我不知道结局是好是坏，最后克劳
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5828305468"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="32946" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=14b4a5f6d5f9d72a1731181fe41a040d/f20d093e6709c93d7e37cf3e933df8dcd30054c8.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=75716aa803b30f24359aec0bf8aed343/f9198618367adab44415da8a87d4b31c8601e436.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="77779" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=c21604e636292df59796a4178c017059/821b3c90f603738dff8fcdebbf1bb051fa19ecc9.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=342803fa9d8fa0ec7fc7640516ac5bee/2934349b033b5bb59f12e1373ad3d539b700bc36.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="70023" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=e28e90c100d79123e0b59c769d0475bb/9674abc451da81cb11d543045e66d016082431e6.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=aa283a0512178a82ce3c7fa8c638728d/f3d3572c11dfa9eca21d96de6ed0f703908fc1cc.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        <div class="small_pic_num center_text">共&nbsp;6&nbsp;张</div>
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:4153566752,&quot;author_name&quot;:&quot;\u5c0f\u697c\u5b64\u9b42&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;8d8de5b08fe6a5bce5ada4e9ad82041f&quot;,&quot;first_post_id&quot;:78873603111,&quot;reply_num&quot;:61,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">61</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/4153566752" title="【始祖家族】科普一下为什么始祖杀不死" target="_blank" class="j_th_tit ">【始祖家族】科普一下为什么始祖杀不死</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 小楼孤魂"
          data-field='{&quot;user_id&quot;:520392077}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5c0f\u697c\u5b64\u9b42&quot;,&quot;id&quot;:&quot;8d8de5b08fe6a5bce5ada4e9ad82041f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%B0%8F%E6%A5%BC%E5%AD%A4%E9%AD%82&ie=utf-8&id=8d8de5b08fe6a5bce5ada4e9ad82041f&fr=frs" target="_blank">小楼孤魂</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">2015-11</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            看见好多人说什么砍头什么的。始祖的身体不可毁坏，除非白桦树桩才能毁坏始祖身体。就是说始祖的四
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5826374779,&quot;author_name&quot;:&quot;xu18768979251&quot;,&quot;author_nickname&quot;:&quot;\u4ec0\u4e48\u9b3c\u261e\ud83d\udca8&quot;,&quot;author_portrait&quot;:&quot;401978753138373638393739323531fba6&quot;,&quot;first_post_id&quot;:121272705521,&quot;reply_num&quot;:3,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">3</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5826374779" title="真的感人(┯_┯)" target="_blank" class="j_th_tit ">真的感人(┯_┯)</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 什么鬼☞💨"
          data-field='{&quot;user_id&quot;:2801473856}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;xu18768979251&quot;,&quot;id&quot;:&quot;401978753138373638393739323531fba6&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=xu18768979251&ie=utf-8&id=401978753138373638393739323531fba6&fr=frs" target="_blank">什么鬼<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-11.png" class="nicknameEmoji" style="width:13px;height:13px"/><img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-35.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-5</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            真的感人(┯_┯) 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5826374779"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="30825" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=383d03ebbc7eca80125031e5a113bbe4/e90178f41bd5ad6e57e8c1228dcb39dbb7fd3cfb.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=61e827bd4fa98226b8c12b2fbab9b801/7af40ad162d9f2d3dd008127a5ec8a136227cce1.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="39192" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=20e8c1228dcb39dbc1956f54e026251d/507980246b600c337a687b00164c510fd8f9a184.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=4f9b405a00f431adbcd243317b0dadaf/3b292df5e0fe9925411dcc9838a85edf8cb171e1.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="80840" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=22d3086ca8c27d1ea57333c62be58157/a338040e0cf3d7ca8d2785befe1fbe096963a9c4.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=3c6ceac000d79123e0e0947c9d0f5b82/9c16fdfaaf51f3de426303ac98eef01f3b297921.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        <div class="small_pic_num center_text">共&nbsp;6&nbsp;张</div>
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5855782915,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121666320206,&quot;reply_num&quot;:18,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">18</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5855782915" title="始祖家族最终季，古老的家族，该何去何从" target="_blank" class="j_th_tit ">始祖家族最终季，古老的家族，该何去何从</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-26</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5855782915"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="48487" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=41ef2e6f013387449c90277e613ff5c0/0b54531f95cad1c8104d8c18723e6709c93d5131.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=1cd3d224d90735fa91f04eb1ae6a0eb3/728da9773912b31b079abd168b18367adab4e11f.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5839736046,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121449773105,&quot;reply_num&quot;:8,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">8</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5839736046" title="心疼死K啦" target="_blank" class="j_th_tit ">心疼死K啦</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-14</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5839736046"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="50272" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=29808cd36fd9f2d320442ced99dca62a/8f95fa5494eef01f685dabf7edfe9925bc317d55.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=9b63f93c6a09c93d07f20effaf06f9dc/34fae6cd7b899e515dc789264fa7d933c8950db2.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5811669840,&quot;author_name&quot;:&quot;\u671d\u5929\u69121994&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;3debe69c9de5a4a9e6a49231393934d646&quot;,&quot;first_post_id&quot;:121077415682,&quot;reply_num&quot;:8,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">8</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5811669840" title="我不接受大K为了她女儿要死！或者以叔代替大K，或者始祖家族任" target="_blank" class="j_th_tit ">我不接受大K为了她女儿要死！或者以叔代替大K，或者始祖家族任</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 朝天椒1994"
          data-field='{&quot;user_id&quot;:1188490045}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u671d\u5929\u69121994&quot;,&quot;id&quot;:&quot;3debe69c9de5a4a9e6a49231393934d646&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%9C%9D%E5%A4%A9%E6%A4%921994&ie=utf-8&id=3debe69c9de5a4a9e6a49231393934d646&fr=frs" target="_blank">朝天椒1994</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">7-26</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            我不接受大K为了她女儿要死！或者以叔代替大K，或者始祖家族任何人都不行！为了新剧，🐷妈就非要写
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:3042355986,&quot;author_name&quot;:&quot;\u8431\u8349\u4ed9\u5b50&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;3314e890b1e88d89e4bb99e5ad90c000&quot;,&quot;first_post_id&quot;:50497776384,&quot;reply_num&quot;:353,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">353</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/3042355986" title="【始祖家族】HOPE？千年道行，就给掌上明珠取了这土名字？" target="_blank" class="j_th_tit ">【始祖家族】HOPE？千年道行，就给掌上明珠取了这土名字？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 萱草仙子"
          data-field='{&quot;user_id&quot;:12588083}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8431\u8349\u4ed9\u5b50&quot;,&quot;id&quot;:&quot;3314e890b1e88d89e4bb99e5ad90c000&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%90%B1%E8%8D%89%E4%BB%99%E5%AD%90&ie=utf-8&id=3314e890b1e88d89e4bb99e5ad90c000&fr=frs" target="_blank">萱草仙子</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">2014-05</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
             Andreya（她母亲的birth name，意思是勇敢的） Adolphya（德，高贵的狼） Amanda （拉丁，被爱的） Anastasia（希腊，复活） Marisa（法，显赫的公主
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm3042355986"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="84048" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=d73e9d727ed98d1076810433110f9437/34a9792442a7d9333176effdaf4bd11372f00178.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C293%3Bap%3D%CA%BC%D7%E6%BC%D2%D7%E5%B0%C9%2C90%2C301/sign=b8d7a9b4324e251fe2f7e4f097bdaa67/b3fb43166d224f4ad947789d0bf790529922d166.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5693345789,&quot;author_name&quot;:&quot;\u5f20ZM\u55b5\u55b5&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;319be5bca05a4de596b5e596b55331&quot;,&quot;first_post_id&quot;:119646547147,&quot;reply_num&quot;:5,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">5</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5693345789" title="第五季第三集伊利亚弹的所有钢琴曲有人知道吗" target="_blank" class="j_th_tit ">第五季第三集伊利亚弹的所有钢琴曲有人知道吗</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 张ZM喵喵"
          data-field='{&quot;user_id&quot;:827562801}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5f20ZM\u55b5\u55b5&quot;,&quot;id&quot;:&quot;319be5bca05a4de596b5e596b55331&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%BC%A0ZM%E5%96%B5%E5%96%B5&ie=utf-8&id=319be5bca05a4de596b5e596b55331&fr=frs" target="_blank">张ZM喵喵</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">5-10</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            第五季第三集伊利亚弹的所有钢琴曲 曲名
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5848009286,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121560088828,&quot;reply_num&quot;:13,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">13</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5848009286" title="E和A是爱情吗？" target="_blank" class="j_th_tit ">E和A是爱情吗？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5848009286"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="76062" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=9fa5d5c30746f21fc9615651c6144759/b991d01ea8d3fd1f095b39023d4e251f95ca5f56.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=c9a497d3bbfd5266a72b3c1c9b23962b/cefc1e178a82b90102ff580b7e8da9773912efbc.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5842295616,&quot;author_name&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;,&quot;first_post_id&quot;:121484166686,&quot;reply_num&quot;:11,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">11</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5842295616" title="终于完结了，什么，还有衍生剧？" target="_blank" class="j_th_tit ">终于完结了，什么，还有衍生剧？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 会飞的荷兰驴"
          data-field='{&quot;user_id&quot;:3369066950}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-16</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5842295616"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="21600" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=de607da04b2309f7e73aa510423e20ca/ea42babf6c81800a88f2e13abc3533fa828b478d.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=35e8201adf1b0ef46ce89856edff51da/aec379310a55b3197aeeea414ea98226cffc17ea.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5852773037,&quot;author_name&quot;:&quot;\u8fd9\u6897\u8bf4\u5230\u660e\u5e74&quot;,&quot;author_nickname&quot;:&quot;\u6765\u798f\u5728\u6253\u80a0\u80c3\ud83d\ude02&quot;,&quot;author_portrait&quot;:&quot;a01be8bf99e6a297e8afb4e588b0e6988ee5b9b43997&quot;,&quot;first_post_id&quot;:121624042054,&quot;reply_num&quot;:4,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">4</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5852773037" title="最后相爱相杀了大k" target="_blank" class="j_th_tit ">最后相爱相杀了大k</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 来福在打肠胃😂"
          data-field='{&quot;user_id&quot;:2537102240}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8fd9\u6897\u8bf4\u5230\u660e\u5e74&quot;,&quot;id&quot;:&quot;a01be8bf99e6a297e8afb4e588b0e6988ee5b9b43997&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%BF%99%E6%A2%97%E8%AF%B4%E5%88%B0%E6%98%8E%E5%B9%B4&ie=utf-8&id=a01be8bf99e6a297e8afb4e588b0e6988ee5b9b43997&fr=frs" target="_blank">来福在打...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1540803125) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,76&quot;,&quot;2&quot;:&quot;1540803125,77&quot;,&quot;3&quot;:&quot;1540803125,78&quot;,&quot;4&quot;:&quot;1540803125,79&quot;,&quot;5&quot;:&quot;1540803125,80&quot;,&quot;6&quot;:&quot;1540803125,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-24</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            最后相爱相杀了大k
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: ☜扫码关注公号">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u884c\u8d70\u7684\u5fe7\u4f24l&quot;,&quot;id&quot;:&quot;2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%A1%8C%E8%B5%B0%E7%9A%84%E5%BF%A7%E4%BC%A4l&ie=utf-8&id=2fdee8a18ce8b5b0e79a84e5bfa7e4bca46c85cf&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-12.png" class="nicknameEmoji" style="width:13px;height:13px"/>扫码关...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5824572298,&quot;author_name&quot;:&quot;kithis&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;5d8d6b6974686973c10f&quot;,&quot;first_post_id&quot;:121250375648,&quot;reply_num&quot;:7,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">7</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5824572298" title="看完结局想看下你们讨论，各种贴吧已经被资源整垮了" target="_blank" class="j_th_tit ">看完结局想看下你们讨论，各种贴吧已经被资源整垮了</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: kithis"
          data-field='{&quot;user_id&quot;:264342877}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;kithis&quot;,&quot;id&quot;:&quot;5d8d6b6974686973c10f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=kithis&ie=utf-8&id=5d8d6b6974686973c10f&fr=frs" target="_blank">kithis</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-4</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            没有任何心情表态
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: kithis">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;kithis&quot;,&quot;id&quot;:&quot;5d8d6b6974686973c10f&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=kithis&ie=utf-8&id=5d8d6b6974686973c10f&fr=frs" target="_blank">kithis</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-31        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5849868639,&quot;author_name&quot;:&quot;\u8bf4\u4e0d\u5b9a\u5f88\u660e\u767d&quot;,&quot;author_nickname&quot;:&quot;\u7231\u770b\u7f8e\u5267\ud83d\ude01&quot;,&quot;author_portrait&quot;:&quot;b7cbe8afb4e4b88de5ae9ae5be88e6988ee799bd5138&quot;,&quot;first_post_id&quot;:121584938252,&quot;reply_num&quot;:1,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">1</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5849868639" title="O(∩_∩)O【始祖家族1—5季】整理好" target="_blank" class="j_th_tit ">O(∩_∩)O【始祖家族1—5季】整理好</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 爱看美剧😁"
          data-field='{&quot;user_id&quot;:944884663}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8bf4\u4e0d\u5b9a\u5f88\u660e\u767d&quot;,&quot;id&quot;:&quot;b7cbe8afb4e4b88de5ae9ae5be88e6988ee799bd5138&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%AF%B4%E4%B8%8D%E5%AE%9A%E5%BE%88%E6%98%8E%E7%99%BD&ie=utf-8&id=b7cbe8afb4e4b88de5ae9ae5be88e6988ee799bd5138&fr=frs" target="_blank">爱看美剧<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-25.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-21</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            O(∩_∩)O【始祖家族1—5季】整理好 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5849868639"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="77584" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=0eef66c10746f21fc9615651c6144759/b991d01ea8d3fd1f98118a003d4e251f95ca5f8e.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=58ee24d1bbfd5266a72b3c1c9b23972b/cefc1e178a82b90193b5eb097e8da9773912eff4.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 爱看美剧😁">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8bf4\u4e0d\u5b9a\u5f88\u660e\u767d&quot;,&quot;id&quot;:&quot;b7cbe8afb4e4b88de5ae9ae5be88e6988ee799bd5138&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%AF%B4%E4%B8%8D%E5%AE%9A%E5%BE%88%E6%98%8E%E7%99%BD&ie=utf-8&id=b7cbe8afb4e4b88de5ae9ae5be88e6988ee799bd5138&fr=frs" target="_blank">爱看美剧<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-25.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-25        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5825662280,&quot;author_name&quot;:&quot;\u827eai88&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;ea05e889be616938382b94&quot;,&quot;first_post_id&quot;:121263831960,&quot;reply_num&quot;:36,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">36</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5825662280" title="🌸（初代吸血鬼）（始祖家族）1～5已整理👇" target="_blank" class="j_th_tit ">🌸（初代吸血鬼）（始祖家族）1～5已整理👇</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 艾ai88"
          data-field='{&quot;user_id&quot;:2485847530}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u827eai88&quot;,&quot;id&quot;:&quot;ea05e889be616938382b94&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%89%BEai88&ie=utf-8&id=ea05e889be616938382b94&fr=frs" target="_blank">艾ai88</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1540803125) no-repeat -1150px  0;top:0px;left:0px" data-slot="1"  data-name="baiyang" data-field='{&quot;name&quot;:&quot;baiyang&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u767d\u7f8a\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1540803125,23&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="白羊座印记"  locate="baiyang_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-5</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            来取
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5825662280"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="52086" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=86e71cdc4ea7d933bffdec719d7bfd2a/38212db5c9ea15cebf87c6c1ba003af33b87b2a3.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=315a681458e736d158138c00ab6b4ec2/d009b3de9c82d15845eb7f798c0a19d8bd3e4288.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 戕荼曌瞾夙◎">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5e1d\u846c\u5919&quot;,&quot;id&quot;:&quot;07e1e5b89de891ace5a499f777&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%B8%9D%E8%91%AC%E5%A4%99&ie=utf-8&id=07e1e5b89de891ace5a499f777&fr=frs" target="_blank">戕荼曌瞾...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-25        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5826068028,&quot;author_name&quot;:&quot;tzrtzx&quot;,&quot;author_nickname&quot;:&quot;\u53ef\u7231\u5154\u5154\ud83c\udf6d&quot;,&quot;author_portrait&quot;:&quot;6a7f747a72747a78d305&quot;,&quot;first_post_id&quot;:121269238166,&quot;reply_num&quot;:3332,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">3332</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5826068028" title="初代吸血鬼「始祖家族」「1--5季」已整！理❗️❕⬇️" target="_blank" class="j_th_tit ">初代吸血鬼「始祖家族」「1--5季」已整！理❗️❕⬇️</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 可爱兔兔🍭"
          data-field='{&quot;user_id&quot;:97746794}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;tzrtzx&quot;,&quot;id&quot;:&quot;6a7f747a72747a78d305&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=tzrtzx&ie=utf-8&id=6a7f747a72747a78d305&fr=frs" target="_blank">可爱兔兔<img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-12.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-5</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            初代吸血鬼「始祖家族」「1--5季」已整！理❗️❕⬇️
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 张宝宝6678">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5f20\u5b9d\u5b9d6678&quot;,&quot;id&quot;:&quot;d62be5bca0e5ae9de5ae9d363637383023&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%BC%A0%E5%AE%9D%E5%AE%9D6678&ie=utf-8&id=d62be5bca0e5ae9de5ae9d363637383023&fr=frs" target="_blank">张宝宝6678</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-23        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5846741644,&quot;author_name&quot;:&quot;\u6700\u540e\u9340\u5bc2\u9759&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;a24ce69c80e5908ee98d80e5af82e99d990526&quot;,&quot;first_post_id&quot;:121543257830,&quot;reply_num&quot;:3,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">3</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5846741644" title="各位大神，第五季都是在哪里看的啊，求资源" target="_blank" class="j_th_tit ">各位大神，第五季都是在哪里看的啊，求资源</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 最后鍀寂静"
          data-field='{&quot;user_id&quot;:637881506}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6700\u540e\u9340\u5bc2\u9759&quot;,&quot;id&quot;:&quot;a24ce69c80e5908ee98d80e5af82e99d990526&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%9C%80%E5%90%8E%E9%8D%80%E5%AF%82%E9%9D%99&ie=utf-8&id=a24ce69c80e5908ee98d80e5af82e99d990526&fr=frs" target="_blank">最后鍀寂静</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-19</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            各位大神，第五季都是在哪里看的啊，求资源
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 会飞的荷兰驴">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f1a\u98de\u7684\u8377\u5170\u9a74&quot;,&quot;id&quot;:&quot;c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&fr=frs" target="_blank">会飞的荷...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-23        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5705066411,&quot;author_name&quot;:&quot;\u571f\u8c461551383768&quot;,&quot;author_nickname&quot;:&quot;\u571f\u8c46\u59d0\u10da&quot;,&quot;author_portrait&quot;:&quot;0914e59c9fe8b18631353531333833373638e76e&quot;,&quot;first_post_id&quot;:119783027832,&quot;reply_num&quot;:5,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}' >
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                 
                        <span class="threadlist_rep_num center_text"
                            title="回复">5</span>
                            </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5705066411" title="始祖家族，1~5季全集👇👇👇" target="_blank" class="j_th_tit ">始祖家族，1~5季全集👇👇👇</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 土豆姐ლ"
          data-field='{&quot;user_id&quot;:1860637705}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u571f\u8c461551383768&quot;,&quot;id&quot;:&quot;0914e59c9fe8b18631353531333833373638e76e&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%9C%9F%E8%B1%861551383768&ie=utf-8&id=0914e59c9fe8b18631353531333833373638e76e&fr=frs" target="_blank">土豆姐<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-9.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">5-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            始祖家族，1~5季全集👇👇👇 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm5705066411"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="24138" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=efe9623aa80f4bfb8c859656337f54c9/d24a432ac65c10383ea8c367be119313b17e895f.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=e8dedd48eb1190ef01fb92d7fe209f16/b03533fa828ba61ec538c58a4d34970a314e5944.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="98213" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=4f98d36d164c510fae91ea1850690914/ead2d186c9177f3eafd5f1a87ccf3bc79e3d5648.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=fd26de5877899e51788e3a1c729cdb33/b21bb051f8198618fea6e22146ed2e738ad4e6b6.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 骑驴看风景☜">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;J\u5c0f\u571f\u8c46\u5440&quot;,&quot;id&quot;:&quot;da2e4ae5b08fe59c9fe8b186e591802bcf&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=J%E5%B0%8F%E5%9C%9F%E8%B1%86%E5%91%80&ie=utf-8&id=da2e4ae5b08fe59c9fe8b186e591802bcf&fr=frs" target="_blank">骑驴看风...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            8-22        </span>
</div>
                </div>
                                </div>
    </div>
</li>










</ul>

<div class="thread_list_bottom clearfix">
        
<div id="frs_list_pager" class="pagination-default clearfix"><span class="pagination-current pagination-item ">1</span>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=50" class=" pagination-item " >2</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=100" class=" pagination-item " >3</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=150" class=" pagination-item " >4</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=200" class=" pagination-item " >5</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=250" class=" pagination-item " >6</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=300" class=" pagination-item " >7</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=350" class=" pagination-item " >8</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=400" class=" pagination-item " >9</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=450" class=" pagination-item " >10</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=50" class="next pagination-item " >下一页&gt;</a>
<a href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8&pn=7850" class="last pagination-item " >尾页</a>
</div>    <div class="th_footer_bright">
        <div class="th_footer_l">
                            共有主题数<span class="red_text">7900</span>个，贴子数
                <span class="red_text">442283</span>篇
                <a rel="noreferrer"  class="fans_name" href="/bawu2/platform/listMemberInfo?word=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8"
                   target="_blank">始祖党</a>数<span
                    class="red_text">73758</span>
                    </div>
    </div>
</div>
--></code><script>Bigpipe.register("frs-list/pagelet/thread_list", {"parent":"frs-list\/pagelet\/thread","scripts":["\/tb\/_\/verify_manager_phone_cba5a4d.js","\/tb\/_\/detect_manager_block_3e52a76.js","\/tb\/_\/block_user_7c0f0ff.js","\/tb\/_\/util_top_cookie_b437d61.js","\/tb\/_\/music_player_1dfd5c5.js","\/tb\/_\/util_picture_slide_9a62a0d.js","\/tb\/_\/util_media_init_de70972.js","\/tb\/_\/util_favorite_99b836c.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/util_picture_rotation_81f0b8d.js","\/tb\/_\/util_image_process_cc67662.js","\/tb\/_\/util_media_controller_0ed7ecf.js","\/tb\/_\/util_https_stat_a01778b.js","\/tb\/_\/scroll_event_7817c65.js","\/tb\/_\/game_code_thread_7141b4c.js","\/tb\/_\/game_thread_90bad35.js","\/tb\/_\/card_a7ea147.js","\/tb\/_\/single_icons_9d843f9.js","\/tb\/_\/umoney_query_e6ef23a.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/base_dialog_user_bar_ea71e42.js","\/tb\/_\/qianbao_cashier_dialog_5247354.js","\/tb\/_\/qianbao_purchase_tdou_81a2c40.js","\/tb\/_\/tdou_open_type_a72e1ed.js","\/tb\/_\/tdou_template_8d6b3f6.js","\/tb\/_\/tdou_builder_05101dd.js","\/tb\/_\/tdou_view_util_d282db0.js","\/tb\/_\/rsa_safe_299a966.js","\/tb\/_\/paykey_safe_payment_37d2c7b.js","\/tb\/_\/captcha_57d747c.js","\/tb\/_\/captcha_dialog_ceaacd2.js","\/tb\/_\/captcha_safe_payment_7f700b4.js","\/tb\/_\/mobile_safe_payment_5c23e71.js","\/tb\/_\/tbean_safe_3668241.js","\/tb\/_\/tbean_safe_ajax_5dbae2e.js","\/tb\/_\/tdou_data_747c462.js","\/tb\/_\/tdou_view_check_f11908d.js","\/tb\/_\/tdou_counter_cbe5c8a.js","\/tb\/_\/tdou_view_fec0b7b.js","\/tb\/_\/qianbao_purchase_member_efbbe6b.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/cashier_dialog_d52cf7c.js","\/tb\/_\/pay_member_c57f92d.js","\/tb\/_\/umoney_1379f71.js","\/tb\/_\/tdou_view_operation_bootstrap_7f5fd6b.js","\/tb\/_\/tdou_view_cashier_6afe462.js","\/tb\/_\/tdou_view_auto_redirect_c5d928c.js","\/tb\/_\/tdou_view_pay_ff7307f.js","\/tb\/_\/post_marry_d80a1ea.js","\/tb\/_\/interaction_197c48e.js","\/tb\/_\/member_api_c29c369.js","\/tb\/_\/month_icon_63870d4.js","\/tb\/_\/user_head_00b2e11.js","\/tb\/_\/user_visit_card_4e87a0b.js","\/tb\/_\/util_pop_video_0bb4bc1.js","\/tb\/_\/audio_player_0e5ab66.js","\/tb\/_\/voice_3a5eb8b.js","\/tb\/_\/thread_list_4584608.js","\/tb\/_\/member_api_c29c369.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/messenger_c93e9bb.js","\/tb\/_\/loader_12d7714.js","\/tb\/_\/tpl_ext_c01a6ba.js","\/tb\/_\/util_pager_9cf1330.js"],"styles":["\/tb\/_\/verify_manager_phone_7d1435e.css","\/tb\/_\/block_user_1e8ac98.css","\/tb\/_\/music_player_526eb38.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/game_code_thread_c9a2228.css","\/tb\/_\/game_thread_d41d8cd.css","\/tb\/_\/card_e028cbd.css","\/tb\/_\/single_icons_3112de2.css","\/tb\/_\/umoney_query_b5c3dca.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/base_dialog_user_bar_da68a26.css","\/tb\/_\/qianbao_cashier_dialog_c1e313a.css","\/tb\/_\/qianbao_purchase_tdou_4b31f54.css","\/tb\/_\/tdou_template_f7dd2ac.css","\/tb\/_\/paykey_safe_payment_8f2a8db.css","\/tb\/_\/captcha_8dce960.css","\/tb\/_\/captcha_safe_payment_d41d8cd.css","\/tb\/_\/mobile_safe_payment_8c5a3b9.css","\/tb\/_\/tbean_safe_3c779a3.css","\/tb\/_\/tbean_safe_ajax_d41d8cd.css","\/tb\/_\/qianbao_purchase_member_d190d50.css","\/tb\/_\/cashier_dialog_0390325.css","\/tb\/_\/pay_member_d41d8cd.css","\/tb\/_\/umoney_f12b09a.css","\/tb\/_\/post_marry_1ed5b11.css","\/tb\/_\/interaction_d4668aa.css","\/tb\/_\/month_icon_fbf7c06.css","\/tb\/_\/user_head_35f26e0.css","\/tb\/_\/user_visit_card_79e478c.css","\/tb\/_\/util_pop_video_3955ca6.css","\/tb\/_\/voice_fae8e00.css","\/tb\/_\/thread_list_13c3ce3.css","\/tb\/_\/thread_item_44be836.css","\/tb\/_\/thread_item_title_3b6344d.css","\/tb\/_\/frs_user_base_e6ee6b4.css","\/tb\/_\/util_pager_fd327a7.css","\/tb\/_\/thread_list_footer_99af8d2.css"]}).then(function(pagelet){    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':{"id":"5bdf3dc8486f2_1","name":"5bdf3dc8486f2_1","url_type":null,"url":null,"loc_code":"0001_3","pos_name":3,"goods_info":[{"adType":"3","id":"5bdf3dc8486f2_1","goods_style":1001}],"ext_info":"eyJwcm9kdWN0SWQiOjIsIl9jbGllbnRfdHlwZSI6MCwicGxhY2VfaWQiOiIwMDAxIiwibmV0X3R5cGUiOjAsImN1aWQiOiIiLCJiYWlkdWlkIjoiIiwiZnJlc2hUeXBlIjoiMiIsImZyZXNoQ291bnQiOiIiLCJzZWFyY2hfaWQiOjEwMDUzODk1OTUwMzAxNzA3ODcsInNlYXJjaF90aW1lIjoxNTQxMzU3MDAwLCJlbXB0eV9hZCI6MSwiZWlkX2xpc3QiOiIxOTg2MTAzIzE5ODYxMDIjNTAwMjM3MiM1MDAzNjg1IiwibmV0VHlwZSI6MCwicHJvZHVjdF9pZCI6MiwiZm9ydW1fZGlyIjoiXHU3NTM1XHU4OWM2XHU1MjY3IiwiZm9ydW1fc2Vjb25kX2RpciI6Ilx1N2Y4ZVx1NTI2NyIsImZvcnVtX2lkIjo3NzM5OTYzLCJzZWFyY2hJZDIiOjEwMDUzODk1OTUwMzAxNzA3ODcsInNpcCI6IjEyMS4zMi4xOTMuMTc3IiwiYWZkX3RyYW5zX2RhdGEiOnsic2hvd25fa2V5IjoiMl8yXyIsInRpdGxlX3NpZ24iOm51bGwsImJyYW5kX3NpZ24iOm51bGx9LCJmZWVkX2NvdW50Ijo1MCwicHJpY2Vzb3J0X3EiOjAsInJlcV9udW0iOjIsImRhX21lbnUxIjoiXHU3NTM1XHU4OWM2XHU1MjY3IiwiZGFfbWVudTIiOiJcdTdmOGVcdTUyNjciLCJkYV9tZW51MyI6NzczOTk2MywiZmxvb3IiOjMsInByZV9zaG93X2xvY2F0ZSI6MX0=","task_id":"5bdf3dc8486f2_1","client_type":"PC","page_name":"FRS","page_number":1,"task_name":"5bdf3dc8486f2_1","good_info":{"adType":"3","id":"5bdf3dc8486f2_1","goods_style":1001},"cpid":null,"imTimeSign":null,"tpl_name":null,"locator":"#thread_list .j_thread_list:not(.thread_top):eq(2)","loc_index":1,"first_screen":false,"load_type":"before"}    }]);
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':{"id":"5bdf3dc848728_3","name":"5bdf3dc848728_3","url_type":null,"url":null,"loc_code":"0001_15","pos_name":15,"goods_info":[{"adType":"3","id":"5bdf3dc848728_3","goods_style":1001}],"ext_info":"eyJwcm9kdWN0SWQiOjIsIl9jbGllbnRfdHlwZSI6MCwicGxhY2VfaWQiOiIwMDAxIiwibmV0X3R5cGUiOjAsImN1aWQiOiIiLCJiYWlkdWlkIjoiIiwiZnJlc2hUeXBlIjoiMiIsImZyZXNoQ291bnQiOiIiLCJzZWFyY2hfaWQiOjEwMDUzODk1OTUwMzAxNzA3ODcsInNlYXJjaF90aW1lIjoxNTQxMzU3MDAwLCJlbXB0eV9hZCI6MSwiZWlkX2xpc3QiOiIxOTg2MTAzIzE5ODYxMDIjNTAwMjM3MiM1MDAzNjg1IiwibmV0VHlwZSI6MCwicHJvZHVjdF9pZCI6MiwiZm9ydW1fZGlyIjoiXHU3NTM1XHU4OWM2XHU1MjY3IiwiZm9ydW1fc2Vjb25kX2RpciI6Ilx1N2Y4ZVx1NTI2NyIsImZvcnVtX2lkIjo3NzM5OTYzLCJzZWFyY2hJZDIiOjEwMDUzODk1OTUwMzAxNzA3ODcsInNpcCI6IjEyMS4zMi4xOTMuMTc3IiwiYWZkX3RyYW5zX2RhdGEiOnsic2hvd25fa2V5IjoiMl8yXyIsInRpdGxlX3NpZ24iOm51bGwsImJyYW5kX3NpZ24iOm51bGx9LCJmZWVkX2NvdW50Ijo1MCwicHJpY2Vzb3J0X3EiOjAsInJlcV9udW0iOjIsImRhX21lbnUxIjoiXHU3NTM1XHU4OWM2XHU1MjY3IiwiZGFfbWVudTIiOiJcdTdmOGVcdTUyNjciLCJkYV9tZW51MyI6NzczOTk2MywiZmxvb3IiOjE1LCJwcmVfc2hvd19sb2NhdGUiOjJ9","task_id":"5bdf3dc848728_3","client_type":"PC","page_name":"FRS","page_number":1,"task_name":"5bdf3dc848728_3","good_info":{"adType":"3","id":"5bdf3dc848728_3","goods_style":1001},"cpid":null,"imTimeSign":null,"tpl_name":null,"locator":"#thread_list .j_thread_list:not(.thread_top):eq(14)","loc_index":1,"first_screen":false,"load_type":"before"}    }]);
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.use('adsense-base/widget/tpl_ext', [{
        'type': 'POST',
    }]);
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.use('frs-list/widget/util_pager', [pagelet, true]);
    _.Module.use('frs-list/pagelet/thread_list', [], function (instance) {
        instance.init({
            pagelet: pagelet,
            ifCheck: null,
            videoAutoPlay: true        })
    });
});</script><code class="pagelet_html" id="pagelet_html_frs-list/pagelet/thread_footer" style="display:none;"><!--
<div id="forum_recommend" class="forum_recommend">
    <h3 class="pull_left">你可能感兴趣的吧...</h3>
    <span class="pull_right">
        <a rel="noreferrer"  class="btn all_attention" href="#" onclick="return false"><i class="icon-attention"></i>一键关注</a>
        <a rel="noreferrer"  class="btn exchange" href="#" onclick="return false" >下一页<i class="icon-next"></i></a>
    </span>

    <div id="slide_show" class="tbui_slideshow_container">
        <ul class="tbui_slideshow_list recommend_nav">
                                <li class="tbui_slideshow_slide list1">
                                                        <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=72216f4a4fc920dbd871ee66979fb824&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F8718367adab44aed17494530bb1c8701a08bfbdb.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0"
                                           target="_blank">吸血鬼日记</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0"
                                               target="_blank">703405</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="吸血鬼日记"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:1263743}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=originalfamily"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=a24a94b504e00b1c6e00b73059e28df6&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2Fd833c895d143ad4b9fafee9883025aafa50f06e0.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=originalfamily"
                                           target="_blank">originalfamily</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=originalfamily"
                                               target="_blank">4279</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="originalfamily"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:5155099}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%88%9D%E4%BB%A3%E5%90%B8%E8%A1%80%E9%AC%BC"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=e2bac2d30ed755fdecd7d090d198fe72&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F4610b912c8fcc3ce250f23179745d688d53f20c3.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%88%9D%E4%BB%A3%E5%90%B8%E8%A1%80%E9%AC%BC"
                                           target="_blank">初代吸血鬼</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%88%9D%E4%BB%A3%E5%90%B8%E8%A1%80%E9%AC%BC"
                                               target="_blank">242260</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="初代吸血鬼"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:7770943}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E9%AD%82%E4%B9%8B%E7%8C%8E%E6%89%8Bol"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=df31612156fb848b81e51140065cbb70&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F4e4a20a4462309f78dea8686730e0cf3d6cad698.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E9%AD%82%E4%B9%8B%E7%8C%8E%E6%89%8Bol"
                                           target="_blank">魂之猎手ol</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E9%AD%82%E4%B9%8B%E7%8C%8E%E6%89%8Bol"
                                               target="_blank">12039</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="魂之猎手ol"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:3155104}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                </li>
                                    <li class="tbui_slideshow_slide list2">
                                                        <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%BA%94%E5%AD%A3"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=c299bfaf9455da88ed6c02b703356184&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F279759ee3d6d55fb1346d0b26c224f4a21a4dda6.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%BA%94%E5%AD%A3"
                                           target="_blank">吸血鬼日记第五季</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0%E7%AC%AC%E4%BA%94%E5%AD%A3"
                                               target="_blank">36177</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="吸血鬼日记第五季"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:3196748}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E4%BA%94%E5%8E%9F"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=e3b4e70f5e3ba1b99fbd0a6968bf92f5&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F63d9f2d3572c11df408eb48b622762d0f703c23f.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E4%BA%94%E5%8E%9F"
                                           target="_blank">五原</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E4%BA%94%E5%8E%9F"
                                               target="_blank">19929</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="五原"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:358300}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%BC%80%E8%BD%A6%E6%97%85%E8%A1%8C"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=bdac8dbd0b6a21d2f9c6b83e28e79693&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F908fa0ec08fa513d24b274fa3f6d55fbb2fbd9fd.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%BC%80%E8%BD%A6%E6%97%85%E8%A1%8C"
                                           target="_blank">开车旅行</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%BC%80%E8%BD%A6%E6%97%85%E8%A1%8C"
                                               target="_blank">49308</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="开车旅行"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:8481090}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E4%B8%9C%E5%8C%BA%E5%A5%B3%E5%B7%AB"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=d24bfd7307e99aca43a7bdc508898eed&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F0ff41bd5ad6eddc49b578a343bdbb6fd53663348.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E4%B8%9C%E5%8C%BA%E5%A5%B3%E5%B7%AB"
                                           target="_blank">东区女巫</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E4%B8%9C%E5%8C%BA%E5%A5%B3%E5%B7%AB"
                                               target="_blank">12622</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="东区女巫"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:4911136}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                </li>
                                    <li class="tbui_slideshow_slide list3">
                                                        <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%A5%B3%E7%BA%B8"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=4663bdce88e3013b5f468f914d5eedb1&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2Fd31b0ef41bd5ad6ededa809783cb39dbb6fd3caf.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%A5%B3%E7%BA%B8"
                                           target="_blank">女纸</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%A5%B3%E7%BA%B8"
                                               target="_blank">32240</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="女纸"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:1626184}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E7%BE%8E%E5%89%A7%E5%BE%B7%E5%8F%A4%E6%8B%89"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=9ff92de79ff07ebf1ea32207647b887a&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F7e3e6709c93d70cfc28b5b56fadcd100baa12b7c.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E7%BE%8E%E5%89%A7%E5%BE%B7%E5%8F%A4%E6%8B%89"
                                           target="_blank">美剧德古拉</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E7%BE%8E%E5%89%A7%E5%BE%B7%E5%8F%A4%E6%8B%89"
                                               target="_blank">19504</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="美剧德古拉"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:3101654}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0kc"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=f42ca0cd17f3e303231dad726769fd7e&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F2934349b033b5bb57cecb56737d3d539b600bc74.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0kc"
                                           target="_blank">吸血鬼日记kc</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0kc"
                                               target="_blank">6870</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="吸血鬼日记kc"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:5221231}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%B0%91%E7%8B%BC"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=818e649ddca325b3792121c89294b5d5&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F42a98226cffc1e17bc3173824b90f603728de9f3.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%B0%91%E7%8B%BC"
                                           target="_blank">少狼</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%B0%91%E7%8B%BC"
                                               target="_blank">51772</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="少狼"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:2844087}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                </li>
                                    <li class="tbui_slideshow_slide list4">
                                                        <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E9%A3%8E%E4%B8%AD%E7%9A%84%E5%A5%B3%E7%8E%8B"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=33a57fdd5cc89ee8d84b515026f591e3&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F86d6277f9e2f0708bc1e9cd4e824b899a801f2cf.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E9%A3%8E%E4%B8%AD%E7%9A%84%E5%A5%B3%E7%8E%8B"
                                           target="_blank">风中的女王</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E9%A3%8E%E4%B8%AD%E7%9A%84%E5%A5%B3%E7%8E%8B"
                                               target="_blank">51690</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="风中的女王"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:2054714}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=josephmorgan"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=c923bd883500719e040e8e049704a30c&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F562c11dfa9ec8a137de2681ff503918fa1ecc050.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=josephmorgan"
                                           target="_blank">josephmorgan</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=josephmorgan"
                                               target="_blank">150413</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="josephmorgan"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:2004660}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F%E7%AC%AC%E4%B8%80%E5%AD%A3"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=f84713ba639bc9a23b27a8f82292e762&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F4b90f603738da977148c6af2b151f8198718e34c.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F%E7%AC%AC%E4%B8%80%E5%AD%A3"
                                           target="_blank">始祖家族第一季</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F%E7%AC%AC%E4%B8%80%E5%AD%A3"
                                               target="_blank">704</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="始祖家族第一季"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:5679480}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=kalijah"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=b5341a7bb6d8474c5acdf413b9611763&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F30adcbef76094b36eb4202dba1cc7cd98d109d37.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=kalijah"
                                           target="_blank">kalijah</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=kalijah"
                                               target="_blank">1192</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="kalijah"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:4567806}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                </li>
                                    <li class="tbui_slideshow_slide list5">
                                                        <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0%E7%AC%AC%E5%85%AD%E5%AD%A3"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=316aa374600553323a4895a19c4a6d95&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2Fcc11728b4710b912304a0d75c1fdfc03934522b6.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0%E7%AC%AC%E5%85%AD%E5%AD%A3"
                                           target="_blank">吸血鬼日记第六季</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E6%97%A5%E8%AE%B0%E7%AC%AC%E5%85%AD%E5%AD%A3"
                                               target="_blank">7690</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="吸血鬼日记第六季"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:2378968}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E5%A7%8B%E7%A5%96"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=664e75be05f51bfb70cdd630bb8442bc&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2Fb151f8198618367a62da1e392f738bd4b21ce587.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E5%A7%8B%E7%A5%96"
                                           target="_blank">吸血鬼始祖</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E5%90%B8%E8%A1%80%E9%AC%BC%E5%A7%8B%E7%A5%96"
                                               target="_blank">780</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="吸血鬼始祖"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:7753351}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=%E6%8B%AF%E6%95%91%E5%B8%8C%E6%9C%9B"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=ee63fc3c3bf14881d3cfc1d065d69023&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F86d6277f9e2f0708b79867f7e824b899a801f2ac.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=%E6%8B%AF%E6%95%91%E5%B8%8C%E6%9C%9B"
                                           target="_blank">拯救希望</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=%E6%8B%AF%E6%95%91%E5%B8%8C%E6%9C%9B"
                                               target="_blank">850</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="拯救希望"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:4173847}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                            <div class="recommend_item media_horizontal clearfix">
                                    <a rel="noreferrer"  class="media_left"
                                       href="//tieba.baidu.com/f?kw=klabekah"
                                       target="_blank">
                                        <img src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b65_65&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=8673e78688e9d16865a217e025bcce17&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F2fdda3cc7cd98d106b2b372c233fb80e7bec902b.jpg"/>
                                    </a>

                                    <div class="media_right text_overflow">
                                        <a rel="noreferrer"  class="name"
                                           href="//tieba.baidu.com/f?kw=klabekah"
                                           target="_blank">klabekah</a>

                                        <p><i class="icon_rcommend_num"></i>
                                            <a rel="noreferrer"  class="post_num"
                                               href="//tieba.baidu.com/f?kw=klabekah"
                                               target="_blank">263</a>
                                        </p>
                                        <a rel="noreferrer"  href="#" onclick="return false"
                                           class="btn-attention recommend_flow j_recommend_flow_click"
                                           title="klabekah"
                                           is_clicked="0"
                                           data-fid='{&quot;fid&quot;:8431567}'                                           data-tbs='{&quot;tbs&quot;:&quot;3b22fb4e08ce68ee1541357000&quot;}' >关注</a>
                                    </div>
                                </div>
                                                </li>
                        </ul>
    </div>
</div>

--></code><script>Bigpipe.register("frs-list/pagelet/thread_footer", {"parent":"frs-list\/pagelet\/thread","scripts":["\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/slide_show_d52e648.js","\/tb\/_\/forum_recommend_3d8be67.js"],"styles":["\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/slide_show_aad29db.css","\/tb\/_\/forum_recommend_5460e01.css"]}).then(function(pagelet){    _.Module.use('frs-list/widget/forum_recommend');
});</script><code class="pagelet_html" id="pagelet_html_encourage-tbguess/pagelet/sidebar" style="display:none;"><!--<div class="guess-sidebar-container">
    <div class="guess-sidebar">
        <ul class="title">
            <li class="football active">
                <span>足球竞猜</span>
            </li>
            <li class="more pull-right">
                <a href="/f?kw=竞技体育&ie=utf-8">更多>></a>
            </li>
        </ul>
        <ul class="body">
            <li class="football">
                <ul class="list">
                                            <li class="item guess-195" data-data="{&quot;id&quot;:195,&quot;type&quot;:1}">
                            <div class="intro">猜球赢海信大奖</div>
                            <div class="guess-main clearfix">
                                <div class="flag home"
                                     data-mine=""
                                     data-role="home">
                                    <a href="/f?ie=utf-8&kw=葡萄牙" class="flag">
                                        <img src="http://tb1.bdstatic.com/tb/cms/ngmis/file_1467565757444.png"/>
                                    </a>
                                    <a class="name" href="/f?ie=utf-8&kw=葡萄牙">
                                        葡萄牙                                    </a>

                                    <div class="percentage">
                                                                                <div class="value" title="145669">34%</div>
                                        <div class="bar"><span style="width: 34%"></span></div>
                                    </div>
                                    <div class="action">
                                        <div class="guess-btn sidebar-support">主赢</div>
                                    </div>
                                </div>
                                <div class="action away"
                                     data-mine=""
                                     data-role="away">
                                    <a href="/f?ie=utf-8&kw=威尔士足球" class="flag">
                                        <img src="http://tb1.bdstatic.com/tb/cms/ngmis/file_1467565783163.png"/>
                                    </a>
                                    <a class="name" href="/f?ie=utf-8&kw=威尔士足球">
                                        威尔士                                    </a>

                                    <div class="percentage">
                                                                                <div class="value" title="143578">33%</div>
                                        <div class="bar"><span style="width: 33%"></span></div>
                                    </div>
                                    <div class="action">
                                        <div class="guess-btn sidebar-support">客赢</div>
                                    </div>
                                </div>
                                <div class="draw body"
                                     data-mine=""
                                     data-role="draw">
                                    <div class="base">
                                        <div class="j-count-down count-down">1467831600</div>
                                        <div>欧洲杯</div>
                                    </div>
                                    <div class="vs">VS</div>
                                                                            <div class="percentage">
                                                                                        <div class="value" title="143605">33%</div>
                                            <div class="bar"><span style="width: 33%"></span></div>
                                        </div>
                                        <div class="action">
                                            <div class="guess-btn sidebar-support">平局</div>
                                        </div>
                                                                    </div>
                            </div>
                            <div class="guess-footer">
                                <div class="action">换一场</div>
                                <div class="body">
                                    <span>助攻总额: </span><i
                                        class="guess-icon bean-12"></i><span
                                        class="value margin-left">43W</span>
                                </div>
                            </div>
                        </li>
                                    </ul>
            </li>
        </ul>
    </div>
</div>
--></code><script>Bigpipe.register("encourage-tbguess/pagelet/sidebar", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":["\/tb\/_\/rsa_safe_299a966.js","\/tb\/_\/paykey_safe_payment_37d2c7b.js","\/tb\/_\/captcha_57d747c.js","\/tb\/_\/captcha_dialog_ceaacd2.js","\/tb\/_\/captcha_safe_payment_7f700b4.js","\/tb\/_\/mobile_safe_payment_5c23e71.js","\/tb\/_\/tbean_safe_3668241.js","\/tb\/_\/tbean_safe_ajax_5dbae2e.js","\/tb\/_\/user_api_10e048c.js","\/tb\/_\/icons_da74e35.js","\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/base_user_data_7bf9fa5.js","\/tb\/_\/mixin_b5f95cd.js","\/tb\/_\/bean_a6c16b5.js","\/tb\/_\/guess_f82c751.js","\/tb\/_\/sidebar_8446bb9.js"],"styles":["\/tb\/_\/paykey_safe_payment_8f2a8db.css","\/tb\/_\/captcha_8dce960.css","\/tb\/_\/captcha_safe_payment_d41d8cd.css","\/tb\/_\/mobile_safe_payment_8c5a3b9.css","\/tb\/_\/tbean_safe_3c779a3.css","\/tb\/_\/tbean_safe_ajax_d41d8cd.css","\/tb\/_\/icons_4bd55ce.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/base_user_data_f665ab7.css","\/tb\/_\/mixin_bd9244b.css","\/tb\/_\/bean_d41d8cd.css","\/tb\/_\/guess_3c31a66.css","\/tb\/_\/sidebar_2541a8b.css"]}).then(function(pagelet){    _.Module.getInstance('encourage-tbguess/widget/mixin', function (mixin) {
        mixin.bindData({"mineGuessInfo":{"count":0,"bean":0,"scores":{"total":0,"money":0,"other":0}},"homeForum":"\u7ade\u6280\u4f53\u80b2","mineAwardMap":[]});
    });
    _.Module.use('encourage-tbguess/widget/sidebar');
});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/forum_info" style="display:none;"><!--<div class="aside_region forum_info j_forum_info" id="">
    <h4 class="region_header clearfix">
        本吧信息        <span class="pull_right j_op"><a rel="noreferrer"  target="_blank" href="/bawu2/platform/detailsInfo?word=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&amp;ie=utf-8">查看详情&gt;&gt;</a>
 </span>
    </h4>
    <div class="region_cnt clearfix">
        


    <ul class="manager_groups aside_media_horizontal clearfix">
                                <li class="media_vertical ">
                                <a rel="noreferrer"  class="media_top manager_media" href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&amp;id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&amp;fr=frs"
                   target="_blank" title="会飞的荷兰驴">
                    <img src="https://gss0.bdstatic.com/6LZ1dD3d1sgCo2Kml5_Y_D3/sys/portrait/item/c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8" alt="">
                                            <span class="media_caption">吧主</span>
                                    </a>

                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/home/main/?un=%E4%BC%9A%E9%A3%9E%E7%9A%84%E8%8D%B7%E5%85%B0%E9%A9%B4&ie=utf-8&amp;id=c6e1e4bc9ae9a39ee79a84e88db7e585b0e9a9b4cfc8&amp;fr=frs" target="_blank"
                       title="会飞的荷兰驴">会飞的荷兰驴</a>
                                    </div>
            </li>
            </ul>
<div id="tbManagerCandidatesNum" style="display:none">
    </div>


<p class="forum_info_desc">
    <span>会员：</span>
    <a rel="noreferrer"  id="member_name_link" href="/bawu2/platform/listMemberInfo?word=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8"
       target="_blank">始祖党</a>
        </p>
<p class="forum_info_desc">
    <span>目录：</span>
            <a rel="noreferrer"  href="/f/fdir?fd=%E7%94%B5%E8%A7%86%E5%89%A7&ie=utf-8&amp;sd=%E7%BE%8E%E5%89%A7&ie=utf-8"
           target="_blank">美剧</a>
    </p>

<div class="apply_groups">
            <span id="tbManagerApply"></span>
                <ins>|</ins>
        <span id="tbManagerAssistApply"><a rel="noreferrer"  class="frs_apply_assist j_btn_apply_assist"
                                           href="/bawu2/platform/listCandidateInfo?word=%E5%A7%8B%E7%A5%96%E5%AE%B6%E6%97%8F&ie=utf-8">申请小吧主</a></span>
    </div>


    </div>
    <div class="region_footer"></div>
</div>
--></code><script>Bigpipe.register("frs-aside/pagelet/forum_info", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":["\/tb\/_\/login_dialog_21db6a0.js","\/tb\/_\/word_limit_47b28de.js","\/tb\/_\/forbidden_ea6d3fd.js","\/tb\/_\/frs-aside\/forum_info_24abb90.js"],"styles":["\/tb\/_\/aside_region_6df4cfc.css","\/tb\/_\/login_dialog_cc7c082.css","\/tb\/_\/word_limit_3c5481d.css","\/tb\/_\/forbidden_752e552.css","\/tb\/_\/frs-aside\/forum_info_415639b.css"]}).then(function(pagelet){    _.Module.use('frs-aside/widget/forum_info', [
        1,
        0,
        PageData.forum,
        {
            is_block: 0,
            block_reason: '',
            opgroup: '',
            days_tofree:0,
        }
    ]);
});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/zyq" style="display:none;"><!--<div class="aside_region zyq_mod_friend j_zyq_mod_friend" id="">
    <h4 class="region_header clearfix">
        友情贴吧        <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
            <ul class="aside_media_horizontal clearfix">
                    <li class="media_vetical ">
                <a rel="noreferrer"  class="media_top" href="/f?kw=初代吸血鬼&frs=yqtb" target="_blank" title="初代吸血鬼">
                <img src="http://imgsrc.baidu.com/forum/wh%3D60%2C60%3B/sign=5e6b761549086e066afd374d32244dc4/4610b912c8fcc3ce250f23179745d688d53f20c3.jpg" alt=""></a>
                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/f?kw=初代吸血鬼&frs=yqtb" target="_blank" class="j_mod_item" title="初代吸血鬼">初代吸血鬼</a>
                </div>
            </li>
            </ul>
    </div>
    <div class="region_footer"></div>
</div>
--></code><script>Bigpipe.register("frs-aside/pagelet/zyq", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":["\/tb\/_\/frs-aside\/zyq_3a18750.js","\/tb\/_\/frs-aside\/friend_b2f77b0.js"],"styles":["\/tb\/_\/aside_region_6df4cfc.css"]}).then(function(pagelet){    _.Module.use('frs-aside/widget/zyq');
});</script><code class="pagelet_html" id="pagelet_html_frs-aside/pagelet/search_back" style="display:none;"><!----></code><script>Bigpipe.register("frs-aside/pagelet/search_back", {"parent":"frs-aside\/pagelet\/normal_aside","scripts":[],"styles":[]}).then(function(pagelet){});</script><code class="pagelet_html" id="pagelet_html_live/pagelet/live_thread" style="display:none;"><!----></code><script>Bigpipe.register("live/pagelet/live_thread", {"parent":"live\/pagelet\/live","scripts":[],"styles":[]}).then(function(pagelet){});</script><script>Bigpipe.end();</script></body></html>

"""


网页 = 网页.replace('"最后回复时间">\n', '"最后回复时间">') #替换   , 1) 次数 1
网页 = 网页.replace('center_text"\n', 'center_text"') #替换   , 1) 次数 1

栏目内容列表=[]
帖子链接列表=[]

for 每栏 in 网页.split("j_threadlist_li_left"):

    if '"最后回复时间">' in 每栏 and '"回复"'in 每栏:
        内容字典 = {}
        for 每行 in 每栏.split("\n"):
            if '"最后回复时间">' in 每行 and "title=" in 每行 and "threadlist_reply_date" in 每行:

                规则 = '.{1,}最后回复时间">'
                最后回复时间 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                规则 = '<.{0,}'
                最后回复时间 = re.sub(规则, '', 最后回复时间)  # 替换   ,count=0,re.S|re.I
                最后回复时间 = 最后回复时间.strip()  # 默认则是去除空格

                内容字典["最后回复时间"] = 最后回复时间

                print("最后回复时间", 最后回复时间)

            if '"回复"' in 每行 and "title=" in 每行 and "threadlist_rep_num" in 每行:
                规则 = '.{1,}回复">'
                回复数 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                规则 = '<.{0,}'
                回复数 = re.sub(规则, '', 回复数)  # 替换   ,count=0,re.S|re.I
                回复数 = 回复数.strip()  # 默认则是去除空格
                内容字典["回复数"]= int(回复数)

                print("回复数", 回复数)

            if 'href=' in 每行 and "title=" in 每行 and "noreferrer" in 每行 and "_blank" in 每行 and "j_th_tit" in 每行:
                规则 = '.{1,}href="'
                帖子链接 = re.sub(规则, '', 每行)  # 替换   ,count=0,re.S|re.I
                规则 = '".{0,}'
                帖子链接 = re.sub(规则, '', 帖子链接)  # 替换   ,count=0,re.S|re.I
                帖子链接 = 帖子链接.strip()  # 默认则是去除空格

                帖子链接 = 'http://tieba.baidu.com{}'.format(帖子链接)  # '代入 '{}'

                内容字典["帖子链接"] = 帖子链接
                print("帖子链接", 帖子链接)

        栏目内容列表.append(内容字典)  # 列表追加

for 内容字典 in 栏目内容列表:

    if ':' in 内容字典["最后回复时间"] and 内容字典["回复数"] >1:
        帖子链接列表.append(内容字典["帖子链接"])  # 列表追加

for 帖子链接 in 帖子链接列表:
    print("帖子链接二:", 帖子链接)



















