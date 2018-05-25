window.onload=function(){
    var a=document.querySelectorAll('A');
    for(var i=0;i<a.length;i++){
        var str=a[i].href;
        if(str.search(/wgewj/g)>0 ){
            a[i].parentNode.style.display='none';
        }
    }
    var img=document.querySelectorAll('img');
    for(var i=0;i<img.length;i++){
        var str=img[i].src;
        if(str.search(/heygugu/g)>0){
            img[i].parentNode.style.display='none';
        }
    }
    var iframe=document.querySelectorAll('iframe');
    for(var i=0;i<iframe.length;i++){
        var str=iframe[i].src;
        if(str.search(/heygugu/g)>0){
            iframe[i].parentNode.style.display='none';
        }
    }
    var div=document.querySelectorAll("div");
    for(var i=0;i<div.length;i++){
        var str=div[i].align;
        if(str){
            div[i].style.display='none';
        }
    }
    var di=document.querySelectorAll("ifeam");
    for(var i=0;i<di.length;i++){
        di[i].style.display='none'
    }
    document.querySelector("ifeam").style.display='none';
}
document.querySelectorAll("DIV[id*='BAIDU']")




window.onload=function(){
    var iframe=document.querySelectorAll('iframe');
    for(var i=0;i<iframe.length;i++){
        var str=iframe[i].src;
        if(str.search(/wo-x/g)>0){
            iframe[i].parentNode.style.display='none';
        }
    }
    document.querySelector(".ad_single_content").style.display='none';
}



window.onload=function(){
    var a=document.querySelectorAll('A');
    for(var i=0;i<a.length;i++){
            a[i].setAttribute('target','');
    }
    var div=document.createElement('div');
    div.style.opacity='0.6';
    div.style.border='solid 2px';
    div.style.position='fixed';
    div.style.bottom='20px';
    div.style.right='20px';
    div.style.width='40px';
    div.style.height='40px';
    var text=document.createTextNode('返回');
    var nowA=document.createElement('A');
    nowA.style.color='red';
    nowA.style.fontWeight='bold';
    nowA.href='javascript:history.back(-1)';
    nowA.appendChild(text);
    div.appendChild(nowA);
    document.querySelector('body').appendChild(div);
    document.querySelector("#prompt-box").style.display='none';
}




    window.onload=function(){
        var iframe=document.querySelectorAll('iframe');
        for(var i=0;i<iframe.length;i++){
            var str=iframe[i].src;
            if(str.search(/yuyue/g)>0||str.search(/88shu/g)>0||str.search(/dlads/g)>0){
                iframe[i].parentNode.style.display='none';
            }
        }
        var img=document.querySelectorAll('img');
        for(var i=0;i<img.length;i++){
            var str=img[i].src;
            if(str.search(/sysapr/g)>0){
                img[i].parentNode.style.display='none';
            }
        }
        var a=document.querySelectorAll('A');
        for(var i=0;i<a.length;i++){
            var str=a[i].href;
            if(str.search(/oe10/g)>0 ){
                a[i].parentNode.style.display='none';
            }
        }
    }



















    var aNodes=document.getElementsByTagName('a');
    for(var i=0;i<aNodes.length;i++){
        var aNode=aNodes[i];
        var str=aNode.href;
        var id=aNode.id;
        if(str.indexOf('m.uerzyr.cn')>-1||str.indexOf('m.wgewj.cn')>-1){
            aNode.parentNode.style.display='none';
        }
    }

    window.onload=function(){
        var iframe=document.querySelectorAll('iframe');
        for(var i=0;i<iframe.length;i++){
            var str=iframe[i].src;
            if(str.indexOf('yuyue')>-1||str.indexOf('88shu')>-1||str.indexOf('dlads')>-1){
                iframe[i].parentNode.style.display='none';
            }
        }
        var img=document.querySelectorAll('img');
        for(var i=0;i<img.length;i++){
            var str=img[i].src;
            if(str.indexOf('sysapr')>-1){
                img[i].parentNode.style.display='none';
            }
        }
        var a=document.querySelectorAll('A');
        for(var i=0;i<a.length;i++){
            var str=a[i].href;
            if(str.indexOf('oe10')>-1 ){
                a[i].parentNode.style.display='none';
            }
        }
    }


















//DIV[@class="mlist scroll"]/preceding-sibling::DIV[@class='header'][contains(string(),'无需播放器，在线播放')]/following-sibling::DIV[2]

window.onload=function(){
    var a=document.querySelectorAll('A');
    for(var i=0;i<a.length;i++){
        var str=a[i].href;
        if(str.search(/uri6/g)>0 ||str.search(/nmtouzi/g)>0||str.search(/apple/g)>0||str.search(/es6china/g)>0||str.search(/langjiyisheng/g)>0){
            a[i].style.display='none';
        }
        if(a[i].style.position=='fixed'){
            var id=a[i].nextSibling.id;
            var style=document.querySelectorAll('style');
            for(var x=0;x<style.length;x++){
                if(style[x].innerText.search('/'+id+'/g')){
                    style[x].innerText='';
                }
            }
            var style=document.createElement('style');
            var text=document.createTextNode('DIV[id*=\''+id+'\']{display:none}');
            style.appendChild(text);
            document.querySelector('head').appendChild(style);
       }
    }
    document.querySelector("#slide").style.display='none';
}































window.onload=function(){
    var iframe=document.querySelectorAll('iframe');
    for(var i=0;i<iframe.length;i++){
        var str=iframe[i].src;
        if(str.search(/wo-x/g)>0){
            iframe[i].parentNode.style.display='none';
        }
    }
    var divall=document.querySelectorAll("body>div");
    var cl=divall[divall.length-1].getAttribute('class');
    var style=document.querySelectorAll('style');
            for(var x=0;x<style.length;x++){
                if(style[x].innerText.search('/'+cl+'/g')){
                    style[x].innerText='';
                }
            }
    var style=document.createElement('style');
    var text=document.createTextNode('.'+cl+'{display:none}');
    style.appendChild(text);
    document.querySelector('head').appendChild(style);
}
















var div=document.querySelectorAll("div");
for(var i=0;i<div.length;i++){
    console.log(div[i].style.position);
    // if(div[i].style.position=='relative'){
    //     div[i].style.display='none';
    // }
}

















window.onload=function(){
    var a=document.querySelectorAll('A');
    for(var i=0;i<a.length;i++){
        var str=a[i].href;
        if(str.search(/ermao/g)>0||str.search(/xcsszx/g)>0||str.search(/uri6/g)>0||str.search(/lnk0/g)>0 ){
            a[i].parentNode.style.display='none';
        }
       if(a[i].style.position=='fixed'){
            var id=a[i].nextSibling.id;
            var style=document.querySelectorAll('style');
            for(var x=0;x<style.length;x++){
                if(style[x].innerText.search('/'+id+'/g')){
                    style[x].innerText='';
                }
            }
            var style=document.createElement('style');
            var text=document.createTextNode('DIV[id*=\''+id+'\']{display:none}');
            style.appendChild(text);
            document.querySelector('head').appendChild(style);
       }
    }
}

