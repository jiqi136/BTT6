# -*- coding:utf-8



import re
from lxml import etree,html #解析与定位网页

内容 = """
E:\python3an\an\python.exe E:/PY学习文件/BTT影视剧/发贴推广/维护代理ip.py
{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/277.11 (KHTML, like Gecko) Chrome/54.0.963.56 Safari/535.11'}
self.提取ip网址列表 ['https://www.kuaidaili.com/free/inha/1', 'https://www.kuaidaili.com/free/inha/2', 'https://www.kuaidaili.com/free/inha/3', 'https://www.kuaidaili.com/free/inha/4', 'https://www.kuaidaili.com/free/inha/5']
E:/PY学习文件/BTT影视剧/发贴推广/维护代理ip.py:319: RuntimeWarning: coroutine '类一一维护代理IP.模具一一异步打开网页' was never awaited
  self.模具一一异步打开网页(url)
帖子内容为空 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=device-width,initial-scale=1.0, maximum-scale=1.0,minimum-scale=1.0,user-scalable=no" />
<title>国内高匿免费HTTP代理IP - 快代理</title>

<meta name="keywords" content="高匿代理,国内代理,代理服务器,免费代理服务器,代理ip,ip代理,高匿代理ip,免费代理,免费代理ip" />
<meta name="description" content="快代理专业为您提供国内高匿免费HTTP代理服务器。" />

<meta content="index,follow" name="robots"/>
<meta content="index,follow" name="GOOGLEBOT"/>
<meta content="快代理"  name="Author"/>
<meta name="renderer" content="webkit" />
<meta name="baidu_union_verify" content="c087a423b52225f404d4c97e59e53464">
<meta name="google-site-verification" content="Pd8y4Id4xJSxMvj-OwUhaZaK7COpr-8LcANUG30jxW8" />
<link rel="shortcut icon" href="https://img.kuaidaili.com/img/favicon.ico?v=3" type="image/x-icon">


<link rel="stylesheet" href="https://img.kuaidaili.com/css/all.css?v=50" media="screen" />

<style>
    .tag_area2 { margin:10px 0 0px 0; text-align: left; }
    .tag_area2 .label { background-color:#c1c1bf;text-decoration:none; font-size:13px; padding:3px 5px 3px 5px;}
    .tag_area2 .label.active, .tag_area2 .label.active:hover { background-color:#468847; }
    .tag_area2 .label:hover { background-color:#aaa; }
    tbody a { color:#777; }
    tbody a:hover { text-decoration:none; }
</style>



<meta name="renderer" content="webkit">
<meta name="baidu-site-verification" content="AO3Q6dKj9R" />
<meta name="baidu-site-verification" content="1flUdvqxyo" />
<meta name="sogou_site_verification" content="9ELczs5cQc"/>
<meta name="360-site-verification" content="feeadcad97dd7093f9abb1ee5285f031" />
<meta baidu-gxt-verify-token="0fd36d429c039b254364ec1f35f82358">
</head>

<body>
<div class="body">
<!--notify-->
<div id="top_notify"></div>


<!--start header-->

    <!--PC header-->
    <div id="navigationBar" class="topnav topnav-has" style="z-index: 1000;">
        <div class="navigation-inner">
            <div class="logo">
                <h1>
                    <a href="/" class="logo-img">
                        <img class="logo-lit" src="https://img.kuaidaili.com/img/kdl-logo.png" alt="">
                    </a>
                </h1>
            </div>
            <div class="categories" id="nav-con">
                <ul class="menu">
                    <li id="menu_free" class="presentation">
                        <h2><a href="/free/">免费代理</a></h2>
                    </li>
                    <li id="menu_pricing" class="presentation">
                        <h2><a href="/pricing/">购买代理</a></h2>
                    </li>
                    <li id="menu_dps" class="presentation has-menu">
                        <h2><a href="/dps/">私密代理</a></h2>
                    </li>
                    <li id="menu_kps" class="presentation">
                        <h2><a href="/kps/">独享代理</a></h2></h2>
                    </li>
                    <li id="menu_ops" class="presentation">
                        <h2><a href="/ops/">开放代理</a></h2>
                    </li>
                    <li id="menu_fetch" class="presentation has-menu">
                        <h2><a href="/fetch/">代理提取</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="/fetch/">提取开放代理</a></li>
                                <li><a href="/dps/fetch/">提取私密代理</a></li>
                                <li><a href="/kps/fetch/">提取独享代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_apidoc" class="presentation has-menu">
                        <h2><a href="/apidoc/">API接口</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="/apidoc/">开放代理API</a></li>
                                <li><a href="/dps/apidoc/">私密代理API</a></li>
                                <li><a href="/kps/apidoc/">独享代理API</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_help" class="presentation has-menu">
                        <h2><a href="https://help.kuaidaili.com" target="_blank">帮助中心</a></h2>
                    </li>
                </ul>
            </div>
            <div class="operation">
                <span class="unlogin">
                    <a href="/login/" class="qc-btn link-dl"><span>登录</span></a>
                    <span class="stick">|</span>
                    <a href="/regist/" class="qc-btn link-dl"><span>注册</span></a>
                </span>
                <a href="/usercenter/" class="qc-btn link-name welcome-link"><span class="welcome"></span></a>
                <a href="/usercenter/" class="qc-btn link-mc"><span>会员中心</span></a><span id="noti"></span>
            </div>
        </div>
    </div>

    <!--mobile header-->
    <div id="navigationMobileBar" class="topnav-m topnav-m-has" style="z-index: 101;">
        <div class="navigation-inner" id="navDefault" style="transition: left 0s ease-in-out; transform: translateZ(0px); position: absolute; width: 100%; left: 0px;">
            <div class="navigation-bar m-nav-1" id="navigation-bar">
                <div class="area-left">
                    <div class="logo">
                        <h1>
                            <a href="/" class="logo-img">
                                <img class="logo-lit" src="https://img.kuaidaili.com/img/kdl-logo.png" alt="">
                                <img class="logo-dark" src="https://img.kuaidaili.com/img/kdl-logo.png" alt="">
                            </a>
                        </h1>
                    </div>
                </div>
                <div class="area-right">
                    <a href="javascript:;" class="nav-mobile-button m-more">
                        <span class="button-img"></span>
                    </a>
                    <a href="javascript:;" class="nav-mobile-button m-close">
                        <span class="button-img"></span>
                    </a>
                </div>
            </div>
            <div class="categories-mobile" id="navDefaultSub" style="opacity: 0; transition: opacity 0.4s ease-in-out; transform: translateZ(0px); display: none;">
                <ul id="m_top_menu" class="menu">
                    <li class="presentation nav-right"><h2><a href="/free/">免费代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/pricing/">购买代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/dps/">私密代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/kps/">独享代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/ops/">开放代理</a></h2></li>
                    <li class="presentation nav-down">
                        <h2><a href="javascript:void(0);">代理提取</a></h2>
                        <div class="nav-down-menu" style="display: none;">
                            <ul class="nav-down-menu-detail">
                                <li><a class="title" href="/fetch/">提取开放代理</a></li>
                                <li><a class="title" href="/dps/fetch/">提取私密代理</a></li>
                                <li><a class="title" href="/kps/fetch/">提取独享代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="presentation nav-down">
                        <h2><a href="javascript:void(0);">API接口</a></h2>
                        <div class="nav-down-menu" style="display: none;">
                            <ul class="nav-down-menu-detail">
                                <li><a class="title" href="/apidoc/">开放代理API</a></li>
                                <li><a class="title" href="/dps/apidoc/">私密代理API</a></li>
                                <li><a class="title" href="/kps/apidoc/">独享代理API</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="presentation nav-right"><h2><a href="https://help.kuaidaili.com" target="_blank">帮助中心</a></h2></li>
                </ul>
                <ul class="op">
                    <li><a href="/usercenter/" class="op-btn btn-style-2">会员中心</a></li>
                </ul>
                <div class="sign-in">
                    <a href="/usercenter/"class="sign-in-links welcome-link"><span class="welcome"></span></a>
                    <span class="unlogin">
                        <a id="m_login_btn" href="/login/" class="sign-in-links">登录</a>
                        <span class="stick">|</span>
                        <a id="m_opt_btn" href="/regist/" class="sign-in-links">注册</a>
                    </span>
                </div>
                <div class="contact">
                    <a href="tel:4000580638" class="ct-num">
                        <i class="icon"></i>
                        <span>400-058-0638</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

<!--end header-->


<div id="content">



<div class="con-pt"></div>
<div class="con-body">
<div>
    <div class="tag_area2" >
        <a id="tag_inha" class="label" href="/free/inha/">国内高匿代理</a> 
        <a id="tag_intr" class="label" href="/free/intr/">国内普通代理</a> 

        <span class="buy"><a href="/pricing/">购买更多代理>></a></span>
    </div>

    <div id="list" style="margin-top:15px;">
        <table class="table table-bordered table-striped">
          <thead>
              <tr>
                <th>IP</th>
                <th>PORT</th>
                <th>匿名度</th>
                <th>类型</th>
                <th>位置</th>
                <th>响应速度</th>
                <th>最后验证时间</th>
              </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td data-title="IP">218.64.148.150</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">江西省萍乡市  电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2018-09-23 03:30:54</td>
                </tr>
                
                <tr>
                    <td data-title="IP">220.248.125.82</td>
                    <td data-title="PORT">8118</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">上海市上海市  联通</td>
                    <td data-title="响应速度">0.8秒</td>
                    <td data-title="最后验证时间">2018-09-23 02:30:59</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.232.194.188</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">0.5秒</td>
                    <td data-title="最后验证时间">2018-09-23 01:30:47</td>
                </tr>
                
                <tr>
                    <td data-title="IP">27.208.85.137</td>
                    <td data-title="PORT">8060</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">山东省威海市  联通</td>
                    <td data-title="响应速度">0.5秒</td>
                    <td data-title="最后验证时间">2018-09-23 00:30:49</td>
                </tr>
                
                <tr>
                    <td data-title="IP">222.33.192.238</td>
                    <td data-title="PORT">8118</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 辽宁省 阜新市 铁通</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2018-09-22 23:30:51</td>
                </tr>
                
                <tr>
                    <td data-title="IP">39.135.11.169</td>
                    <td data-title="PORT">80</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">贵州省  移动</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2018-09-22 22:30:53</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.69.70.182</td>
                    <td data-title="PORT">8118</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 北京市 北京市 鹏博士</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2018-09-22 21:30:52</td>
                </tr>
                
                <tr>
                    <td data-title="IP">117.90.252.228</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2018-09-22 20:30:55</td>
                </tr>
                
                <tr>
                    <td data-title="IP">118.178.227.171</td>
                    <td data-title="PORT">80</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 浙江省 杭州市 阿里云</td>
                    <td data-title="响应速度">1.0秒</td>
                    <td data-title="最后验证时间">2018-09-22 19:30:59</td>
                </tr>
                
                <tr>
                    <td data-title="IP">117.87.176.198</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">江苏省徐州市  电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2018-09-22 18:31:01</td>
                </tr>
                
                <tr>
                    <td data-title="IP">39.135.9.166</td>
                    <td data-title="PORT">8080</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">贵州省遵义市  移动</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2018-09-22 17:30:57</td>
                </tr>
                
                <tr>
                    <td data-title="IP">183.129.244.17</td>
                    <td data-title="PORT">21213</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">浙江省杭州市  电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2018-09-22 16:30:59</td>
                </tr>
                
                <tr>
                    <td data-title="IP">183.129.242.126</td>
                    <td data-title="PORT">1080</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">浙江省杭州市  电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2018-09-22 15:30:47</td>
                </tr>
                
                <tr>
                    <td data-title="IP">112.232.130.108</td>
                    <td data-title="PORT">31414</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">山东省济南市  联通</td>
                    <td data-title="响应速度">0.5秒</td>
                    <td data-title="最后验证时间">2018-09-22 14:30:51</td>
                </tr>
                
                <tr>
                    <td data-title="IP">39.135.9.229</td>
                    <td data-title="PORT">8080</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">贵州省遵义市  移动</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2018-09-22 13:30:50</td>
                </tr>
                
            </tbody>
        </table>
        <p>注：表中响应速度是中国测速服务器的测试数据，仅供参考。响应速度根据你机器所在的地理位置不同而有差异。</p>

        <div id="listnav">
        <ul><li>第</li><li><a href="/free/inha/1/">1</a></li><li><a href="/free/inha/2/">2</a></li><li><a href="/free/inha/3/" class="active">3</a></li><li><a href="/free/inha/4/">4</a></li><li><a href="/free/inha/5/">5</a></li><li><a href="/free/inha/6/">6</a></li><li><a href="/free/inha/7/">7</a></li><li>...</li><li><a href="/free/inha/2476/">2476</a></li><li><a href="/free/inha/2477/">2477</a></li><li>页</li></ul>
        </div>

        <div class="btn center be-f"><a id="tobuy" href="/pricing/" target="_blank">购买更多代理</a></div>
    </div>
</div>
</div>

</div>


<div class="footer">
    <div class="con-body clearfix">
        <div class="footer-left">
            <a href="/" class="logo-link"><img height="35" src="/img/footer-logo.png"/></a>
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a><span>|</span></li>
            <li><a href="/contract/" target="_blank">服务条款</a><span>|</span></li>
            <li><a href="/law/" target="_blank">法律声明</a><span>|</span></li>
            <li><a href="https://img.kuaidaili.com/sitemap.xml">网站地图</a><span>|</span></li>
            <li><a href="https://help.kuaidaili.com/dev/api/" target="_blank">开发者指南</a><span>|</span></li>
            <li><a href="/changelog/">更新日志</a></li>
        </ul>
        <p class="foot-owner">© 2013-2018 积善科技（北京）有限公司<br/>
            <a style="margin-left:0px" href="http://www.miitbeian.gov.cn/publish/query/indexFirst.action" target="_blank">京ICP备16054786号</a>
            <span style="margin-left:6px">增值电信经营许可证 京B2-20181007</span>
            <a style="margin-left:5px" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802027137"><img src="https://img.kuaidaili.com/img/jgwab.png" style="height:18px;vertical-align:sub;" />京公网安备 11010802027137号</a>
        </p>
        </div>
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
          
            <a id='cxwz' class="safe03" href='https://credit.szfw.org/CX20180118037820350186.html' target='_blank'></a>
          
            
        </div>
    </div>
</div>
<div class="m-footer">
    <div class="con-body">
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a></li>
            <li><a href="https://help.kuaidaili.com/contract/" target="_blank">服务条款</a></li>
            <li><a href="https://help.kuaidaili.com/law/" target="_blank">法律声明</a></li>
            <li><a href="/sitemap.xml">网站地图</a></li>
            <li><a href="https://help.kuaidaili.com" target="_blank">帮助中心</a></li>
            <li><a href="/changelog/">更新日志</a></li>
        </ul>
        <p class="foot-owner">©2013-2018&nbsp; 积善科技（北京）有限公司</p>
        <a class="foot-owner" href="http://www.miitbeian.gov.cn/publish/query/indexFirst.action">京ICP备16054786号</a>
        <span class="foot-owner" style="margin-left:5px">增值电信经营许可证 京B2-20181007</span>
        <a class="foot-owner" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802027137"><img src="https://img.kuaidaili.com/img/jgwab.png" style="height:18px;vertical-align:sub;" />京公网安备 11010802027137号</a>
      
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
            <a id='cxwz' class="safe03" href='https://credit.szfw.org/CX20180118037820350186.html' target='_blank'></a>
            
        </div>
      
    </div>
</div>
<div id="mNavMask" style="position: fixed; top: 0px; left: 0px; bottom: 0; right: 0; width: 100%; z-index: 100; height: 100%; display: none; background: rgba(0, 0, 0, 0.74902);"></div>
<ul class="onMShow">
    <li>
        <a class="online-chat" href="javascript:void(0);"><br>
            <span class="bt3"></span>
            <div class="two">客服QQ: 800849628<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="tel:4000580638"><br>
            <span class="bt2"></span>
            <div class="two">客服电话：400-058-0638<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="/support/"><br>
            <span class="bt1"></span>
            <div>提交工单</div>
        </a>
    </li>
</ul>
<a href="javascript:void(0);" id="top_btn" class="label btt" style="display:none;"><span class="btn-top"></span></a>

</div>


<script type="text/javascript" src="https://img.kuaidaili.com/js/all.js?v=18"></script>

<script type="text/javascript">
$("#tag_inha").addClass("active")
$(document).ready(function() {
});
</script>

<script type="text/javascript">
var chat_url = "https://static.meiqia.com/dist/standalone.html?_=t&eid=72194";
$(document).ready(function() {
    init_chat();
});
</script>
<script type="text/javascript">
var menu = "menu_free";
if(menu) $('#'+menu).addClass('active');
var ucm = "";
if(ucm){
    $('#ucm_'+ucm).addClass('active');
    $('#ucm_'+ucm+' a i').addClass('icon-white');
}
</script>

<script type="text/javascript">
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?7ed65b1cc4b810e9fd37959c9bb51b31";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://img.kuaidaili.com/ga/ga.js','ga');
ga('create', 'UA-76097251-1', 'auto');
ga('send', 'pageview');

(function(){document.getElementById('cxwz').oncontextmenu = function(){return false;}})();
</script>

<!--[if lt IE 9]><link rel="stylesheet" href="https://img.kuaidaili.com/css/ie.css?v=9" media="screen" /><![endif]-->
</body>
</html>

IP列表数 0
端口列表数 0
代理类型列表 0
任务列表数 2
测试代理,异常
正常代理IP数 1
正常代理IP HTTP://110.188.0.86:60442
保存至文本
宽带连接进行时.....
�������ӵ� �������...
������֤�û���������...
����������ע�����ļ����...
������ ������ӡ�
��������ɡ�
换ip再连接完成

进程已结束,退出代码0

 """
def 整理内页内容(内容):
    帖子内容html = etree.HTML(内容)  #
    #print(内容)
    规则 = '//*[@id="list"]/table/tbody/tr[*]/td[1]/text()'
    #规则 = str(规则).replace("/tbody", "")
    IP列表 = 帖子内容html.xpath(规则)
    print(IP列表)


    规则 = '//*[@id="list"]/table/tbody/tr[*]/td[2]/text()'
    #规则 = str(规则).replace("/tbody", "")
    端口列表 = 帖子内容html.xpath(规则)
    print(端口列表)


    规则 = '//*[@id="list"]/table/tbody/tr[*]/td[4]/text()'
    #规则 = str(规则).replace("/tbody", "")
    代理类型列表 = 帖子内容html.xpath(规则)
    print(代理类型列表)


    代理类型IP端口列表=[]
    print('IP列表数',len(IP列表))
    print('端口列表数', len(端口列表))
    print('代理类型列表', len(代理类型列表))
    if len(IP列表)!=len(端口列表) and len(IP列表)!=len(代理类型列表):
        print('ip端口数据组不匹配，结束程序')
        等待用户输入 = input("\n按下 enter 确认键后继续")
    for 代理类型,IP,端口 in zip(代理类型列表,IP列表, 端口列表):
        IP端口 = "{}://{}:{}".format(代理类型,IP,端口)#'代入 '{}'

        代理类型IP端口列表.append(IP端口)



    for IP端口 in 代理类型IP端口列表:
        print(IP端口)


def 读取文本():
    try:  # 调用异常处理，应对易发生错误的位置
        文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'r', encoding='UTF-8')
        文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
    except UnicodeDecodeError as 异常原因:  # 异常处理
        print(异常原因)
        文本 = open(r"E:\PY学习文件\BTT影视剧\py快捷方式\代理IP.txt", 'r', encoding='gbk')
        文本内容列表 = 文本.readlines()  # read() #全部读取   readlines每一行
    else:  # 必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
        文本.close()
    print('文本内容列表\n',文本内容列表)

    for 行内容 in 文本内容列表:
        if '正常' in 行内容:
            行内容 =行内容.replace("//", "")  # 替换   , 1) 次数 1
            文本列表 = 行内容.split(":")
            类型=文本列表[0]
            IP = 文本列表[1]
            端口 = 文本列表[2]
            print(类型, IP,端口)

        else:
            pass




代理类型列表 = ['http']*100
print(代理类型列表)



