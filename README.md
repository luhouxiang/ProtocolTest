# ProtocolTest
使用dgango1.8.18+jquery1.11.3
# 目的：完成一个网页版的测试工具的功能
类似于postman,只是postman不能修改，有一些测试数据需要拿前面的测试结果作为参数。
另外，postman需要用户安装，对于新同事而言还需要教会其使用方法，参数设定等。
网页版省却以上事务，直接发网址，即可立即使用，进行验证工作。
# 构想
测试的协议采用http+json，其它协议暂不支持。  
通过下拉菜单选择get或是post  
当为post时，需要显示填写body数据的edit框，然后发送，发送完后获取数据。  
发送的过程就是把数据给到后台，后台根据post或是get进行数据转发到测试服务器，然后将结果显示出来。  
