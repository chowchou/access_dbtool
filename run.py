# test = "SELECT id,起点埋深,终点埋深 from %s where 起点点号 in (select 起点点号 from %s WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）')" %(a,b)
a = 'FSL'
b = 'FSP'
test = 'SELECT id,起点埋深,终点埋深 from '+str(a)+ ' where 起点点号 in (select 起点点号 from ' + str(b) + " WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）')"
print(test)