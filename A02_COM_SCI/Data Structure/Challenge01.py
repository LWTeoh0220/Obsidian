# 记录所有已存在的账户
userAccounts = {}
# 记录所有被封锁的账户
lockedAccounts = set()
# 记录登入时的错误次数
failAccRecord = {} 


# 确认登入状态
def checkLogIn(acc, ps):
    if acc in lockedAccounts:
        return "此账户已被封锁"

    if acc not in userAccounts:
        return "此账户不存在"
    
    if userAccounts[acc] == ps:
        failAccRecord[acc] = 0
        return "~ 登入成功 ~"
    
    else:
        count = failAccRecord.get(acc,0) + 1
        failAccRecord[acc] = count

        if count >= 3:
            lockedAccounts.add(acc)
            return "密码错误\n此账户已被锁定"
        return "密码错误"
        

# 确认密码字数 & 输入userAccounts（ 这边没有加入其他限制——顺带一提，这些不是ai写的，写注解是是为了方便未来回看）
def checkSignUp(acc,ps):
        if len(ps) > 6:
            if acc in userAccounts:
                return "此账户已存在"
            else:
                userAccounts[acc] = ps
                return "注册成功"
        else:
            return "密码字数不足（需大于6位）"
            






# 主程式 。。。。。。
while True:
    detect = input("请选择操作选项（a 注册, b 登入，c 退出）？").lower()

    if detect not in ["a","b","c"]:
        print("请输入正确选项 ~~ ")
        continue

    if detect == "c":
        break


    if detect == "b":
        while True:
            acc = input("请输入账户： ")
            ps = input("请输入密码：")
            oput = checkLogIn(acc,ps)
            print(oput)

            if ("成功" in oput) or ("锁定" in oput):
                break


    if detect == "a":
        acc = input("请创建账户： ")
        ps = input("请设定密码： ")
        print(checkSignUp(acc,ps))
    
    
    



