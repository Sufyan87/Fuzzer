from re import L
import aiohttp
import asyncio
import sys
import ast
u = sys.argv[1]
name = sys.argv[2]
urls = open(name , "r")
stats = sys.argv[3]
choice = 0
list_403 = []
if stats !="all": 
    x = stats
    stats = sys.argv[4:]
    stats.append(x)
    choice = 1 # When user want specific status codes
else:
    e = sys.argv[4:]
    choice = 2  #
list = urls.readlines()
file = open("headers.txt")
head = file.readlines() 
async def main():
    async with aiohttp.ClientSession() as session:
        
        for i in range(len(list)):
            fc =list[i].rstrip("\n")
            full_url = (u + "/" + fc)
            async with session.get(full_url) as response: 
                if choice == 1:
                    if str(response.status) in stats:
                        print(i,"Status code:", response.status, "     ", full_url)
                        if str(response.status) == "403":
                            list_403.append(full_url)

                if choice == 2: ## To eliminate specific code. 
                    if str(response.status) not in e:
                        print("Status code:", response.status, "     ", full_url)
                        if str(response.status) == "403":
                            list_403.append(full_url)
async def bypass():
    async with aiohttp.ClientSession() as session:
        for k in range(len(list_403)):
            forbidden_url =list_403[k]
        #print(forbidden_url)
            for n in range(len(head)):
                hs =head[n].rstrip("\n")
                H = ast.literal_eval(hs)


            
            #print(type(H))
            #print(H)
                async with session.get(forbidden_url,headers=H) as response:
                    #print(response.status,H)
                    if str(response.status) == "200":
                        print("HEADER:", hs ,"URL:",forbidden_url)                
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
#print(list_403)
print("Now 403_Forbidden urls are seperated do you want to try bypass them?")
print("Enter 1 to bypass , To exit press any key" )
check_403 = input("enter:" )
if str(check_403) == "1":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bypass())
else:
    exit()



