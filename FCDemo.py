import pymysql
import itertools

def findDoubletons():
    print("======")
    print("Frequent doubletons found:")
    print("======")
    #itertools.combinations(p,r)从p中找出所有长度为r的排列情况… 有顺序
    doubletonCandidates = list(itertools.combinations(allSingletonTags,2))
    #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
    for(index,candidate) in enumerate(doubletonCandidates):
        tag1 = candidate[0]
        tag2 = candidate[1]
        cursor.execute("select count(fpt1.project_id) from\
        fc_project_tags fpt1 inner join fc_project_tags fpt2\
        on fpt1.project_id = fpt2.project_id where\
        fpt1.tag_name = %s and fpt2.tag_name = %s",(tag1,tag2))
        count = cursor.fetchone()[0]
        if count>minsupport:
            print(tag1,tag2,"[",count,"]")
            cursor.execute("insert into fc_project_tag_pairs\
            (tag1,tag2,num_projs) values(%s,%s,%s)",(tag1,tag2,count))
            doubletonSet.add(candidate)
            allDoubletonTags.add(tag1)
            allDoubletonTags.add(tag2)

def findTriplentons():
    print("======")
    print("Frequent tripletons found:")
    print("======")
    tripletonCandidates = list(itertools.combinations(allDoubletonTags,3))
    tripletonCandidatesSorted = []
    for tc in tripletonCandidates:
        tripletonCandidatesSorted.append(sorted(tc))
    for index,candidate in enumerate(tripletonCandidatesSorted):
        doubletonsInsideTripleton = list(itertools.combinations(candidate,2))
        tripletonCajdidateRejected = 0
        for index ,doubleton in enumerate(doubletonsInsideTripleton):
            if doubleton not in doubletonSet:
                tripletonCajdidateRejected = 1
                break
            if tripletonCajdidateRejected ==0:
                cursor.execute("select count(fpt1.project_id)\
                from fc_project_tags fpt1 inner join fc_project_tags fpt2\
                on fpt1.project_id = fpt2.project_id inner join\
                fc_project_tags fpt3 on fpt2.project_id = fpt3.project_id\
                where (fpt1.tag_name=%s and fpt2.tag_name=%s and\
                fpt3.tag_name = %s)",(candidate[0],candidate[1],candidate[2]))
                count = cursor.fetchone()[0]
                if count > minsupport :
                    print(candidate[0],",",candidate[1],",",candidate[2], ",","[", count, "]")
                    cursor.execute("insert into fc_project_tag_triples\
                    (tag1,tag2,tag3,num_projs) values (%s,%s,%s,%s)",(candidate[0],candidate[1],candidate[2],count))
                break




MINSUPPORTPCT = 5
doubletonSet =set()
allDoubletonTags = set()
db = pymysql.connect(host='localhost',
                     db='test',
                     user='root',
                     passwd='123456',
                     port=3306,
                     charset='utf8')
cursor = db.cursor()
quarryBaskets = "select count(distinct project_id) from fc_project_tags;"
cursor.execute(quarryBaskets)
#篮子的数量
baskets = cursor.fetchone()[0]
#满足最小支持度的篮子的数量
minsupport = baskets * MINSUPPORTPCT/100
print("Minnum support count:",minsupport)
cursor.execute("select distinct tag_name from fc_project_tags group by 1 \
having count(project_id)>= %s order by tag_name",minsupport)
#符合最小支持度的标签
singletons = cursor.fetchall()
allSingletonTags = []
for singleton in singletons:
    allSingletonTags.append(singleton[0])
#下面使用频繁的一项集创建候选二元组  findDoubletons()
findDoubletons()
findTriplentons()
