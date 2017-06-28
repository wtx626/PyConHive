# Hive客户端
 &emsp;&emsp;HiveServer2为客户端在远程执行hive查询提供了接口，通过Thrift RPC来实现，还提供了多用户并发和认证功能。
目前使用python的用户可以通过pyhs2这个模块来连接HiveServer2，实现查询和取回结果的操作。
## 可通过以下方式来安装pyhs2：
<pre><code>easy_install pyhs2</code></pre>
## 如果安装不成功，可以尝试先安装以下的组件：
<pre><code>yum install cyrus-sasl-plain
yum install cyrus-sasl-devel</code></pre>