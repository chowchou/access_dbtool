import re
import time

import pypyodbc as pypyodbc
from PyQt5.QtCore import QThread, pyqtSignal


class Check(QThread):
    _signal = pyqtSignal(dict)

    def __init__(self,data,types):
        super(Check, self).__init__()
        self.data = data
        self.types = types
        self.types_list = ['FS','GD','JK','LD','RS','SS','TR','TX','WS','YS','ZS']
    def work_runs(self,flag,mes,id='None'):
        # flag 0 = 开始检测 1 = 流程全部检测结束 2 = PASS 3 = NG
        res = {'flag':flag,'mes':mes,'id':id}
        self._signal.emit(res)

    def check_tools(self,res,table):
        self.result = res
        model = self.result[0]
        for i in range(len(self.result)):
            id = i + 1
            if self.result[i] == model:
                res = True
            else:
                mes = table + '-- ID = ' + str(id)
                self.work_runs('3','[ NG ]字段一致性检测错误',mes)
                res = False
        return res
    def check_first(self,a,b):
        try:
            test = 'SELECT 建设日期,管线权属单位,所在位置,工程编号,工程类别,勘测单位,测量时间,管线范畴,更新状态 from ' + str(a)
            self.curser.execute(test)
            result = self.curser.fetchall()
            print(result)
            x = self.check_tools(result,str(a))
            test = 'SELECT 建设日期,管线权属单位,所在位置,工程编号,工程类别,勘测单位,测量时间,管点范畴,更新状态,获取时机 from ' + str(b)
            self.curser.execute(test)
            result = self.curser.fetchall()
            print(result)
            y = self.check_tools(result,str(b))
            if x and y:
                n = True
                return n
            else:
                n = False
                return n
        except Exception as e:
            print(e)
            self.work_runs('3', '数据库错误', str(e))
    def texture(self,a):
        #a = L
        # sqla = a
        try:
            test = 'SELECT id from ' + str(a) + " where [材质]='' or [材质] is NULL"
            print(test)
            #"SELECT id from FSL where [材质]='' or [材质] is NULL "
            self.curser.execute(test)
            result = self.curser.fetchall()
            self.texture_num = 0
            if result:
                list = []
                for i in range(len(result)):
                    list.append(result[i][0])
                list = [str(i) for i in list]
                ab = ','.join(list)
                test = 'select id,电缆条数,光缆条数,管线使用状况,线型 from '+ str(a) + ' where id in (%s)' % ab
                # sql = 'select id,电缆条数,光缆条数,管线使用状况,线型 from FSL where id in (%s)' % a
                self.curser.execute(test)
                result = self.curser.fetchall()
                for i in range(len(result)):
                    id = result[i][0]
                    dl = result[i][1]
                    gl = result[i][2]
                    stu = result[i][3]
                    types = result[i][4]
                    if dl and gl:
                        # print('电缆光缆存在数据', 'id=', id)
                        self.texture_num += 1
                        mes = 'FSL -- ID = ' + str(id)
                        self.work_runs('3', '[ NG ]电缆光缆存在数据', mes)
                    # else:
                    #     self.work_runs('2', '[ PASS ]电缆光缆无异常')
                    if stu != '空管' and types != '预埋管线':
                        self.texture_num += 1
                        mes = 'FSL -- ID = ' + str(id)
                        self.work_runs('3', '[ NG ]管线使用状况、线型错误', mes)
                    # else:
                    #     self.work_runs('2', '[ PASS ]管线使用状况、线型错误无异常')
                        # print('管线使用状况、线型错误', 'id=', id)
            else:
                self.work_runs('0', '没有为空的材质字段')
            if self.texture_num == 0:
                self.work_runs('2', '[ PASS ]材质检测无异常')
            texture = True
            return texture
        except Exception as e:
            print(e)
            self.work_runs('3', '数据库错误', str(e))

    def error_comm(self,a):
        # a = 'FSL'
        try:
            test = 'SELECT 管径 from ' + str(a) + ' WHERE 管径 IS NOT NULL'
            self.curser.execute(test)
            result = self.curser.fetchall()
            # print(result, '管径')
            num = 0
            for i in range(len(result)):
                a = result[i][0]
                res = re.findall("[^0-9X]", a)
                print(res)
                if res:
                    mes = 'FSL -- ID = ' + str(i + 1)
                    self.work_runs('3', '[ NG ]非法字符错误', mes)
                    num += 1
            if num == 0:
                self.error_flag = True
            else:
                self.error_flag = False
            return self.error_flag
        except Exception as e:
            # print(e)
            self.work_runs('3', '数据库错误', str(e))

    def numofgk(self,a):
        try:
            sql = "select id,总孔数,已用孔数 from " + str(a) + " where id in (SELECT id from " + str(a) + " where 埋设方式 = '管块')"
            self.curser.execute(sql)
            result = self.curser.fetchall()
            # print(result)
            if result:
                num = 0
                for i in range(len(result)):
                    a = result[i][1]
                    b = result[i][2]
                    id = result[i][0]
                    if a < b:
                        num += 1
                        mes = 'FSL -- ID = ' + str(id)
                        self.work_runs('3', '[ NG ]管块孔数错误', mes)
                if num == 0:
                    self.work_runs('2', '[ PASS ]管块孔数正常')
            else:
                self.work_runs('0', '没有找到管块')
            flag = True
            return flag
        except Exception as e:
            print(e)
            self.work_runs('3', '数据库错误',str(e))
    def depth_gauge(self,a,b):
        #a = L b =P
        # "SELECT id,起点埋深,终点埋深 from FSL where 起点点号 in (select 起点点号 from FSP WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）')"
        # SELECT id,起点埋深,终点埋深 from '+ str(a) + ' where 起点点号 in (select 起点点号 from '+ str(b) + " WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）')
        try:
            test = 'select 起点点号 from '+ str(b) + " WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）'"
            self.curser.execute(test)
            result = self.curser.fetchall()
            print(result, '起点点号')
            if not result:
                self.work_runs('0', '没有找到附属物')
                flag = True
                return flag

            test = 'SELECT 起点点号,起点埋深 from '+ str(a) + ' where 起点点号 in (select 起点点号 from '+ str(b) + " WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）')"
            self.curser.execute(test)
            result = self.curser.fetchall()
            print(result,'起点埋深')
            test = 'SELECT 终点点号,终点埋深 from ' + str(a) + ' where 终点点号 in (select 起点点号 from ' + str(
                b) + " WHERE 附属物 = '阀门井' or 附属物 = '阀门' or 附属物 = '水井（井）')"
            self.curser.execute(test)
            result1 = self.curser.fetchall()
            print(result1,'终点埋深')
            test_list = []
            error_list = []
            for i in range(len(result)):
                a = result[i][0]
                c = result[i][1]
                print(i)
                for i in range(len(result1)):
                    b = result1[i][0]
                    d = result1[i][1]
                    if a == b:
                        print('find')
                        if c == d:
                            print(a,'正常')
                        else:
                            print(a,'不正常')
                            error_list.append(a)
                        sss = 1
                        break
                    else:
                        sss = 0
                        print('no find',a)
                if not sss:
                    test_list.append(a)
            print('起点埋深没有找到：',test_list)
            self.work_runs('3', '[ NG ]终点埋深没有找到', str(test_list))
            test_list1 = []
            error_list2 = []
            for i in range(len(result1)):
                a = result1[i][0]
                c = result1[i][1]
                print(i)
                for i in range(len(result)):
                    b = result[i][0]
                    d = result[i][1]
                    if a == b:
                        print('find',a,b)
                        if c == d:
                            print(a, '正常')
                        else:
                            print(a, '不正常')
                            error_list2.append(a)
                        sss = 1
                        break
                    else:
                        sss = 0
                        print('no find', a,b)
                if not sss:
                    test_list1.append(a)
            print('终点埋深没有找到：', test_list1)
            self.work_runs('3', '[ NG ]起点埋深没有找到', str(test_list1))
            list3 = error_list + error_list2
            list3.sort()
            # print('异常', set(list3))
            self.work_runs('3', '[ NG ]附属物深度错误', str(set(list3)))

            # if result:
            #     num = 0
            #     for i in range(len(result)):
            #         a = result[i][1]
            #         b = result[i][2]
            #         id = result[i][0]
            #         if a != b:
            #             num += 1
            #             mes = 'FSL -- ID = ' + str(id)
            #             self.work_runs('3', '[ NG ]附属物深度错误', mes)
            #     if num == 0:
            #         self.work_runs('2', '[ PASS ]附属物深度正常')
            # else:
            #     self.work_runs('0', '没有找到附属物')
            flag = True
            return flag

        except Exception as e:
            print(e)
            self.work_runs('3', '数据库错误', str(e))

    def tyeps_check(self):
        for i in range(11):
            names = 'type_'+str(i)
            type_name = self.types.get(names)
            if type_name:
                t_name_a = self.types_list[i]+'L'
                t_name_b = self.types_list[i] + 'P'
                self.run_all(t_name_a,t_name_b)
    # def test(self):
    #     try:
    #         a = 'FFFF'
    #         test = 'SELECT 管径 from ' + str(a) + ' WHERE 管径 IS NOT NULL'
    #         self.curser.execute(test)
    #         result = self.curser.fetchall()
    #         print(result, '管径')
    #         num = 0
    #         for i in range(len(result)):
    #             a = result[i][0]
    #             res = re.findall("[^0-9X]", a)
    #             print(res)
    #             if res:
    #                 mes = 'FSL -- ID = ' + str(i + 1)
    #                 self.work_runs('3', '[ NG ]非法字符错误', mes)
    #                 num += 1
    #         if num == 0:
    #             self.error_flag = True
    #         else:
    #             self.error_flag = False
    #         return self.error_flag
    #     except Exception as e:
    #         print(e)
    #         self.work_runs('3', '数据库错误', e)

    def run_all(self,name_a,name_b):
        self.work_runs('4', '字段一致性检测开始',name_a)
        if self.data.get('box_1'):
            self.work_runs('0','字段一致性检测开始')
            res = self.check_first(name_a,name_b)
            if res:
                self.work_runs('2','[ PASS ]字段一致性检测通过')
            self.work_runs('0', '字段一致性检测结束')

        if self.data.get('box_2'):
            self.work_runs('0', '材质检测开始')
            res = self.texture(name_a)
            if res:
                self.work_runs('0', '材质检测结束')

        if self.data.get('box_3'):
            self.work_runs('0', '非法字符检测开始')
            res = self.error_comm(name_a)
            if res:
                self.work_runs('2', '[ PASS ]非法字符检测无异常')
            self.work_runs('0', '非法字符检测结束')

        if self.data.get('box_4'):
            self.work_runs('0', '管块孔数检测开始')
            res = self.numofgk(name_a)
            if res:
                # self.work_runs('2', '[ PASS ]非法字符检测无异常')
                self.work_runs('0', '管块孔数检测结束')

        if self.data.get('box_5'):
            self.work_runs('0', '附属物深度检测开始')
            res = self.depth_gauge(name_a,name_b)
            if res:
                # self.work_runs('2', '[ PASS ]非法字符检测无异常')
                self.work_runs('0', '附属物深度检测结束')
        self.work_runs('1','所有检测结束')
        return

    def run(self):
        url = self.data.get('url')
        print(url)
        # self.run_all()
        strD = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=%s'%url
        db = pypyodbc.win_connect_mdb(strD)
        self.curser = db.cursor()
        # self.test()
        self.tyeps_check()
        self.curser.close()