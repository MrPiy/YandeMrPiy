var allt=$("#sk-body>.sk-bangumi")
var m=new Array()
for(var i=0;i<allt.length;i++){
	if(i<7){
		var name=$(allt[i]).find(".row").attr("id")
		var one=$(allt[i]).find(".an-info-group")
		m[name]=new Array()
		for(var t=0;t<one.length;t++){
			m[name][$(one[t]).find("a").text()]="https://mikanani.me"+$(one[t]).find("a").attr("href")
		}
	}
}
console.log(m)
console.log(JSON.stringify(m))
