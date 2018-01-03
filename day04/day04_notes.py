# coding=utf-8

string="你好"
print "string is ",type(string)
print string

ustring=u"你好"
print "ustring is ",type(ustring)
print ustring


gbk_string=ustring.encode("gbk")
print "gbk_string is ",type(gbk_string)
print gbk_string   # ????????????????

another_string=gbk_string.decode("gbk")
print "another_string is:",type(another_string)
print another_string